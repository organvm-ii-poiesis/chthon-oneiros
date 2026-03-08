# CHTHON-ONEIROS Implementation Plan: The System V1.0

**Objective:** Operationalize the "Shadow Instrument" thesis. Transform the repo from a collection of files into a "Living Nightmare Engine."

## Phase 1: The Substrate (Architectural Life)
**Goal:** Make the file structure feel "Biological" and "Digestive."

1.  **Dynamic "Digestive" Scripts:**
    *   Create `tools/metabolize.sh`: A script that "ages" files in the `production/` folder. It adds "glitch" artifacts (Unicode noise, Zalgo text) to older files, simulating digestion/decay over time.
    *   *Concept:* The deeper a file goes into the archive, the less human-readable it becomes.

2.  **The "Trapdoor" Link Structure:**
    *   Update `README.md` and `CATALOG.md` to include "Cyclical" links. (e.g., Clicking "Exit" takes you to "Ring 4").
    *   Use relative paths to create "Infinite Loops" in the directory navigation.

## Phase 2: The Entity Swarm (Agentic Haunt)
**Goal:** Deploy agents that "Act" rather than "Serve."

1.  **The "Director" Agent (Active):**
    *   Refine the `prompts/director_persona.md` into a scriptable tool that *intervenes* in user drafts.
    *   *Behavior:* If the user writes a "Safe" scene, the Director Agent automatically suggests a "Dial" increase.

2.  **The "Giallo" Linter:**
    *   Create a simple linter (`tools/giallo_check.py`) that scans text for "weak" color words (blue, red) and suggests "strong" replacements (INDIGO, CRIMSON, VERMILION). Enforces the aesthetic axis programmatically.

## Phase 3: The Curse (Physics Engine)
**Goal:** Enforce the "Conservation of Dread."

1.  **The "Dread Metric" Tracker:**
    *   Expand `data/weights/weight_log.json` to track "Entropy" per file.
    *   If a file hasn't been "Viewed" (touched) in X days, the "Curse" activates (it gets moved to `Ring 4: Sediment`).

2.  **The "Bible" Validator:**
    *   A script that checks new `production/` files against the `bible/bestiary.md`. Does the entity match the Class? If not, flag as "Epistemic Violation."

---

## Execution Order
1.  **Thesis:** Commit `docs/strategy/system_thesis_v1.md`.
2.  **Tooling:** Build the `metabolize.sh` script (The Digestion).
3.  **Agents:** Build the `giallo_check.py` (The Aesthetic Law).
4.  **Integration:** Link these tools to the `seed.yaml` configuration.
