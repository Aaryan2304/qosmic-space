# RAG Pipeline Test Results

## Test Date
2025-05-19

## Configuration
- Embedding model: sentence-transformers/all-MiniLM-L6-v2 (384-dim, local CPU)
- LLM: OpenRouter openrouter/free (auto-routes across free models)
- Vector store: ChromaDB (local, embedded)
- Chunks indexed: 128 from 22 notes

## Test Queries and Results

### Query 1: "Why does our FSM need 400 Hz bandwidth?"
**Retrieved chunks:**
1. LEO Satellite Orbital Mechanics (physics) — dist=0.274
2. Piezoelectric vs Voice-Coil FSM Actuator (decision) — dist=0.719
3. REQ-002 Pointing Accuracy (requirement) — dist=0.727

**Answer:** The LLM correctly identified that the retrieved context does not contain the full explanation for the 400 Hz requirement. It noted the relationship to pointing accuracy and actuator selection but could not provide the specific rationale.

**Citations:** [[Piezoelectric vs Voice-Coil FSM Actuator]], [[REQ-002 Pointing Accuracy]]

**Assessment:** The retrieval did not surface the FSM 400 Hz Bandwidth Requirement note directly. This is a limitation of the small embedding model matching on wikilink text rather than semantic content. The LLM handled the missing information gracefully by saying it couldn't find the answer in the context.

### Query 2: "What are the trade-offs between RC and SCT telescopes?"
**Retrieved chunks:**
1. Coma Aberration (physics) — dist=0.889
2. Telescope Assembly (subsystem) — dist=1.043
3. Why Ritchey-Chretien over Schmidt-Cassegrain (decision) — dist=1.073

**Answer:** The LLM extracted specific trade-offs from the context:
- Cost: RC ~2x more expensive than SCT
- Field of view: RC coma-free ~30+ arcmin vs SCT limited to ~15 arcmin
- 1550 nm performance: RC excellent (all-reflective) vs SCT good (chromatic effects)
- Alignment sensitivity: RC higher vs SCT lower

**Citations:** [[Why Ritchey-Chretien over Schmidt-Cassegrain]], [[Coma Aberration]]

**Assessment:** Good quality answer with specific numbers and correct citations.

### Query 3: "What components are in the pointing and tracking system?"
**Retrieved chunks:**
1. Thorlabs PIA13 Actuator (component) — dist=0.472
2. REQ-002 Pointing Accuracy (requirement) — dist=0.688
3. Telescope Assembly (subsystem) — dist=0.759

**Answer:** The LLM identified the Thorlabs PIA13 Actuator as a component of the pointing and tracking system.

**Citations:** [[Thorlabs PIA13 Actuator]]

**Assessment:** The answer is correct but thin — it only mentioned one component. The retrieved chunks included references to Control Software and Telescope Assembly as dependencies, but the LLM focused on the most directly relevant component.

## Known Limitations
1. **Retrieval quality:** The all-MiniLM-L6-v2 model (384-dim) produces high distance scores (0.27-1.07) indicating weak semantic matches. Upgrading to text-embedding-3-small (1536-dim) would improve retrieval quality.
2. **Wikilink matching:** Chunks containing wikilink text (e.g., "[[FSM 400 Hz Bandwidth Requirement]]") can match on keywords rather than semantic content, leading to suboptimal retrieval.
3. **LLM non-determinism:** The openrouter/free endpoint routes to different models, producing variable response quality. Retry logic (2 attempts) handles empty responses.
4. **Citation accuracy:** The LLM sometimes returns section headers instead of note titles as citations. Improved prompt engineering partially addresses this.

## Bugs Fixed During Testing
1. `delete_collection` failing when collection doesn't exist — fixed with `list_collections()` check
2. `message.content` being None for some LLM responses — fixed with None check and retry logic
3. Citation format inconsistency — improved with explicit prompt instructions and examples
