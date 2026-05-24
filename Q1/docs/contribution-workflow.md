# QOSMIC Knowledge Graph — Contribution Workflow

## Purpose

This document defines how engineers contribute to the QOSMIC organizational knowledge graph without leaving their normal workflow. The goal is to make knowledge capture as frictionless as possible while maintaining quality through a lightweight review process.

---

## Adding a New Design Decision

### Step-by-step

1. **Create a new note** from the "Design Decision" template (available in the vault's templates folder)
2. **Fill in frontmatter**: title, subsystem, status=`proposed`, date, author
3. **Write the content**: Context, alternatives evaluated, decision, trade-offs table
4. **Link to related notes**: At least one Requirement (`derives-from`), one Physics Concept (`justified-by`), and optionally Components (`implemented-by`)
5. **Change status** from `proposed` to `reviewed` after peer review
6. **Change status** from `reviewed` to `canonical` after CTO approval

### Template shortcut

Using the Templater plugin, an engineer can press `Ctrl+Shift+N` (or a custom hotkey) to create a new Design Decision note from the template. The template pre-populates all required frontmatter fields and section headings.

---

## Conflict Resolution

When two engineers have different rationales for the same design decision:

1. **Both engineers create separate Design Decision notes**, each linking to the same Requirement but with different `justified-by` chains
2. **A third "Decision Record" note** is created that links to both via `supersedes` and explains the final choice
3. **Both original notes are kept** with status=`superseded` (not deleted) to preserve the reasoning history
4. **The Decision Record note** becomes the canonical reference

This approach preserves both viewpoints rather than overwriting one. Future engineers can read the superseded notes to understand why the rejected alternative was considered.

### Example

- Engineer A creates: "Use piezoelectric FSM actuator" (status=superseded)
- Engineer B creates: "Use voice-coil FSM actuator" (status=superseded)
- CTO creates: "FSM actuator selection record" (status=canonical, supersedes both)

---

## Obsolete Knowledge

Design decisions become obsolete when:
- A new decision supersedes them (linked via `supersedes`)
- The subsystem is deprecated
- The underlying physics or requirements change

**Policy**: Obsolete notes are NOT deleted. Their status is changed to `superseded` and they remain in the vault for historical context. A Dataview query on the Dashboard automatically filters out superseded notes from the default view.

---

## Status Workflow

```
proposed → reviewed → canonical
                      ↘ superseded (rejected alternative)
```

| Status | Meaning | Who can set |
|--------|---------|-------------|
| `proposed` | Initial draft, under review | Author |
| `reviewed` | Peer-reviewed, technically sound | Peer reviewer |
| `canonical` | Approved, current best practice | CTO |
| `superseded` | Replaced by newer decision | Author of superseding note |
| `rejected` | Evaluated but not adopted | CTO |

---

## Obsidian Plugin Proposal: "Knowledge Graph Review"

### Problem

Engineers need to:
- See which notes are pending review
- Validate that Design Decisions link to at least one Requirement
- Track the status of their contributions
- Find conflicting rationale quickly

### Solution

A custom Obsidian plugin called **"Knowledge Graph Review"** that adds:

1. **Status ribbon icon**: Shows a colored icon on each note based on its status (proposed=orange, reviewed=yellow, canonical=green, superseded=gray)

2. **Review panel**: A sidebar panel showing:
   - All notes with status=`proposed` (pending review)
   - All notes with status=`reviewed` (pending CTO approval)
   - Notes missing required links (e.g., Design Decision with no `derives-from` link)

3. **Quick actions**: Buttons to:
   - "Submit for review" (proposed → reviewed)
   - "Approve" (reviewed → canonical)
   - "Mark superseded" (canonical → superseded)

4. **Link validation**: On save, warns if a Design Decision note doesn't link to at least one Requirement

### Alternative (no custom plugin)

Using existing plugins:
- **Templater**: Template with status dropdown and pre-populated fields
- **Dataview**: Dashboard query showing all proposed/reviewed notes
- **QuickAdd**: One-click new decision creation with hotkey

This combination provides 80% of the custom plugin's functionality without writing any code.

---

## Automation with Templater + Dataview

### New Decision Hotkey

Using QuickAdd + Templater, configure a hotkey that:
1. Prompts for the decision title
2. Creates a new note from the Design Decision template
3. Pre-fills the date and author
4. Opens the note for editing

### Dashboard Queries

The Dashboard note includes Dataview queries:

```dataview
TABLE status, date, subsystem
FROM "decisions"
WHERE status = "proposed"
SORT date DESC
```

```dataview
TABLE status, date, subsystem
FROM "decisions"
WHERE status = "reviewed"
SORT date DESC
```

These queries automatically show all notes needing attention, updated in real-time as engineers change statuses.

---

## Review Cadence

| Activity | Frequency | Responsible |
|----------|-----------|-------------|
| Peer review of proposed decisions | Within 3 business days | Assigned peer reviewer |
| CTO approval of reviewed decisions | Within 5 business days | CTO |
| Vault-wide quality audit | Monthly | Founder's Office |
| Obsolete knowledge cleanup | Quarterly | Founder's Office |

---

## Key Principles

1. **Knowledge is never deleted** — superseded notes stay for historical context
2. **Minimum viable process** — review gates exist to catch errors, not to create bureaucracy
3. **Templates reduce friction** — engineers fill in structured fields, not blank pages
4. **Links over hierarchy** — the graph structure means there's no single "right place" for a note; what matters is that it's linked
5. **Status is explicit** — every note's frontmatter status tells you its trust level at a glance
