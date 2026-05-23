#!/usr/bin/env python3
"""Parse Obsidian vault wikilinks and generate a color-coded knowledge graph."""

import os
import re
from pathlib import Path

import matplotlib.pyplot as plt
import networkx as nx

VAULT_DIR = Path(__file__).parent.parent / "obsidian-vault"
OUTPUT_PATH = Path(__file__).parent.parent / "docs" / "knowledge-graph.png"

NODE_COLORS = {
    "subsystem": "#4A90D9",
    "decision": "#E67E22",
    "physics": "#27AE60",
    "component": "#8E44AD",
    "request": "#E74C3C",
    "reference": "#95A5A6",
}

NODE_TYPE_ALIASES = {
    "requirement": "request",
}


def parse_vault(vault_dir: Path) -> tuple[list[str], list[tuple[str, str, str]]]:
    """Parse all markdown files in the vault. Returns nodes and edges."""
    nodes: list[str] = []
    edges: list[tuple[str, str, str]] = []
    file_map: dict[str, Path] = {}

    for md_file in vault_dir.rglob("*.md"):
        if md_file.name == "Dashboard.md":
            continue
        if md_file.parent.name == "templates":
            continue

        name = md_file.stem
        nodes.append(name)
        file_map[name] = md_file

        content = md_file.read_text(encoding="utf-8")

        # Extract node type from frontmatter
        node_type = "unknown"
        fm_match = re.match(r"^---\s*\n(.*?)\n---", content, re.DOTALL)
        if fm_match:
            for line in fm_match.group(1).splitlines():
                line = line.strip()
                if line.startswith("type:"):
                    raw = line.split(":", 1)[1].strip()
                    node_type = NODE_TYPE_ALIASES.get(raw, raw)

        # Extract wikilinks
        for link in re.findall(r"\[\[([^\]|]+)(?:\|[^\]]+)?\]\]", content):
            link_clean = link.strip()
            if link_clean and link_clean != name:
                edges.append((name, link_clean, node_type))

    return nodes, edges


def build_graph(
    nodes: list[str], edges: list[tuple[str, str, str]]
) -> nx.DiGraph:
    """Build a directed graph from parsed nodes and edges."""
    G = nx.DiGraph()
    for node in nodes:
        G.add_node(node)
    for src, dst, _ in edges:
        if src in G and dst in G:
            G.add_edge(src, dst)
    return G


def get_node_colors(G: nx.DiGraph, file_map: dict[str, Path]) -> list[str]:
    """Determine node colors based on frontmatter type."""
    colors = []
    for node in G.nodes():
        md_file = file_map.get(node)
        node_type = "unknown"
        if md_file and md_file.exists():
            content = md_file.read_text(encoding="utf-8")
            fm_match = re.match(r"^---\s*\n(.*?)\n---", content, re.DOTALL)
            if fm_match:
                for line in fm_match.group(1).splitlines():
                    line = line.strip()
                    if line.startswith("type:"):
                        raw = line.split(":", 1)[1].strip()
                        node_type = NODE_TYPE_ALIASES.get(raw, raw)
        colors.append(NODE_COLORS.get(node_type, "#CCCCCC"))
    return colors


def draw_graph(G: nx.DiGraph, colors: list[str], output_path: Path) -> None:
    """Draw and save the knowledge graph."""
    fig, ax = plt.subplots(1, 1, figsize=(20, 14))

    pos = nx.spring_layout(G, k=2.5, iterations=50, seed=42)

    nx.draw_networkx_nodes(
        G, pos, ax=ax, node_color=colors, node_size=800, alpha=0.9, edgecolors="#333333"
    )
    nx.draw_networkx_edges(
        G, pos, ax=ax, edge_color="#AAAAAA", arrows=True, arrowsize=12, width=0.8
    )
    nx.draw_networkx_labels(
        G, pos, ax=ax, font_size=6, font_family="sans-serif"
    )

    from matplotlib.lines import Line2D
    legend_handles = []
    for ntype, color in NODE_COLORS.items():
        legend_handles.append(Line2D([0], [0], marker="o", color="w",
                                      markerfacecolor=color, markersize=10, label=ntype))
    ax.legend(handles=legend_handles, loc="upper left", fontsize=8, framealpha=0.9)

    ax.set_title("QOSMIC Knowledge Graph", fontsize=16, fontweight="bold", pad=20)
    ax.axis("off")
    fig.tight_layout()
    fig.savefig(output_path, dpi=150, bbox_inches="tight", facecolor="white")
    print(f"Graph saved to {output_path}")


def main() -> None:
    nodes, edges = parse_vault(VAULT_DIR)
    print(f"Parsed {len(nodes)} nodes and {len(edges)} edges from vault")

    G = build_graph(nodes, edges)
    print(f"Graph: {G.number_of_nodes()} nodes, {G.number_of_edges()} edges")

    # Rebuild file_map for color lookup
    file_map: dict[str, Path] = {}
    for md_file in VAULT_DIR.rglob("*.md"):
        if md_file.name != "Dashboard.md" and md_file.parent.name != "templates":
            file_map[md_file.stem] = md_file

    colors = get_node_colors(G, file_map)
    draw_graph(G, colors, OUTPUT_PATH)


if __name__ == "__main__":
    main()
