# QOSMIC Knowledge Graph Schema

## Purpose

This document defines the schema for QOSMIC's organizational knowledge graph, stored as an Obsidian vault. Each node is a markdown file with YAML frontmatter for structured data and markdown body for human-readable content. Links between nodes use Obsidian's `[[wikilink]]` syntax.

---

## Node Types

### 1. Subsystem

Represents a major subsystem of the optical ground station.

**Frontmatter fields:**

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `type` | string | Yes | Must be `subsystem` |
| `name` | string | Yes | Display name of the subsystem |
| `description` | string | Yes | One-paragraph overview |
| `status` | string | Yes | `active` or `deprecated` |
| `parent` | wikilink | No | Parent subsystem, e.g., `[[Telescope Assembly]]` |

**Example:**

```markdown
---
type: subsystem
name: Pointing and Tracking System
description: Responsible for acquiring and maintaining optical link with LEO satellites.
status: active
parent: [[Telescope Assembly]]
---

# Pointing and Tracking System

The pointing and tracking system (PAT) is responsible for...
```

---

### 2. DesignDecision

Records a specific engineering decision with rationale, alternatives, and trade-offs.

**Frontmatter fields:**

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `type` | string | Yes | Must be `decision` |
| `title` | string | Yes | Concise decision statement |
| `status` | string | Yes | `proposed`, `accepted`, `superseded`, or `rejected` |
| `date` | string | Yes | Date in `YYYY-MM-DD` format |
| `author` | string | Yes | Name or identifier of decision author |
| `subsystem` | wikilink | Yes | Affected subsystem |
| `alternatives_considered` | list | Yes | List of alternatives evaluated |
| `tradeoffs` | string | Yes | Key trade-offs between alternatives |
| `physics_rationale` | string | Yes | Physics or engineering principles behind the decision |

**Required links:**
- `derives-from` -> at least one `[[Requirement]]`
- `justified-by` -> at least one `[[Physics Concept]]`
- `implemented-by` -> at least one `[[Component]]` (if applicable)

---

### 3. PhysicsConcept

A physics or engineering principle that underpins design decisions.

**Frontmatter fields:**

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `type` | string | Yes | Must be `physics` |
| `name` | string | Yes | Name of the concept |
| `domain` | string | Yes | One of: `optics`, `mechanics`, `atmospheric`, `quantum`, `orbital` |
| `description` | string | Yes | Explanation of the concept |
| `key_equations` | string | No | Relevant equations |

---

### 4. Component

A physical component, part, or assembly used in the ground station.

**Frontmatter fields:**

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `type` | string | Yes | Must be `component` |
| `name` | string | Yes | Component name |
| `vendor` | string | Yes | Manufacturer or supplier name |
| `part_number` | string | Yes | Vendor part number |
| `cost_inr` | number | Yes | Approximate cost in INR |
| `lead_time_weeks` | number | Yes | Typical lead time in weeks |
| `datasheet_url` | string | No | URL to component datasheet |
| `status` | string | Yes | `active` or `obsolete` |

---

### 5. Requirement

A system or subsystem requirement derived from customer needs, physics constraints, or internal goals.

**Frontmatter fields:**

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `type` | string | Yes | Must be `requirement` |
| `id` | string | Yes | Unique identifier, format `REQ-XXX` |
| `text` | string | Yes | Full requirement statement |
| `source` | string | Yes | One of: `customer`, `physics`, `regulatory`, `internal` |
| `priority` | string | Yes | `critical`, `high`, `medium`, or `low` |
| `verification_method` | string | Yes | One of: `test`, `analysis`, `inspection`, `demonstration` |

---

### 6. Reference

An external reference: academic paper, datasheet, standard, or internal document.

**Frontmatter fields:**

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `type` | string | Yes | Must be `reference` |
| `title` | string | Yes | Full title of the reference |
| `authors` | string | Yes | Author names |
| `year` | number | Yes | Publication year |
| `url` | string | No | URL to the reference |
| `doi` | string | No | DOI if available |
| `type` | string | Yes | One of: `paper`, `datasheet`, `standard`, `internal_doc` |

---

## Link Types

| Link Type | From -> To | Meaning |
|-----------|-----------|---------|
| `derives-from` | DesignDecision -> Requirement | Decision addresses this requirement |
| `implemented-by` | DesignDecision -> Component | Decision realized through this component |
| `justified-by` | DesignDecision -> PhysicsConcept | Physics basis for this decision |
| `depends-on` | Subsystem -> Subsystem | Functional dependency |
| `supersedes` | DesignDecision -> DesignDecision | Replaces an older decision |
| `tested-by` | Requirement -> Reference | Verification evidence |
| `references` | Any -> Reference | Cites an external reference |
| `uses-component` | Subsystem -> Component | Subsystem uses this component |
| `based-on` | PhysicsConcept -> Reference | Concept sourced from reference |

---

## Vault Directory Structure

```
obsidian-vault/
├── templates/
├── subsystems/
├── decisions/
├── physics/
├── components/
├── requirements/
├── references/
└── Dashboard.md
```

## Naming Conventions

- **Subsystem files**: `Subsystem Name.md`
- **Decision files**: Descriptive title
- **Requirement files**: `REQ-XXX Description.md`
- **Reference files**: Short title

## Status Workflows

### Design Decision Lifecycle
```
proposed -> accepted -> superseded
                  \-> rejected
```

### Subsystem Lifecycle
```
active -> deprecated
```
