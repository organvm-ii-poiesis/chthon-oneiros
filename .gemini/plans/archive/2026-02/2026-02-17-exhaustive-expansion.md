# CHTHON-ONEIROS: Exhaustive Expansion Plan (Phase II)

**Objective:** Transmute the 300K-word research corpus into a production-ready narrative engine, establish the canonical "World Bible," and operationalize the competitive release strategy.

---

## Phase 1: Structural Architecture (The Bible)
**Goal:** Synthesize the 10 World Briefs and 3 Director Reports into a coherent, governing "Series Bible."

1.  **Create `bible/` Directory:**
    *   `bible/physics.md`: Define the "Laws of PHANTASMATA" (derived from *Philosophy of Fear* + *Temporal Work*). Rules of magic/reality.
    *   `bible/geography.md`: Map the "zones" of the world (e.g., The Digital Bleed, The Giallo City, The Dream Tunnels).
    *   `bible/bestiary.md`: Catalog of entities/threats derived from *Body Transgression* and *Asian Horror* research.
    *   `bible/artifacts.md`: Registry of cursed objects/media (from *Found Footage* and *ARG* research).

2.  **Define the "Core Loop":**
    *   Formalize how a "GRINDER" story begins, escalates, and ends based on the *Comparative Director Report*.

---

## Phase 2: Creative Synthesis (Production)
**Goal:** Prove the "Dial System" by producing the first generation of narrative assets.

1.  **Pilot Fragments (The "Alpha" Drop):**
    *   Generate 3 Narrative Fragments using `drafts/TEMPLATE.md` + `DIAL-WORKSHEET.md`:
        *   **Fragment A:** "Neon Dream" ($GIALLO lead). Focus on color/ritual.
        *   **Fragment B:** "Identity Dissolve" ($PSYCHO lead). Focus on screen-life/paranoia.
        *   **Fragment C:** "Raw Nerve" ($GRINDHOUSE lead). Focus on auditory/visceral horror.
    *   *Deliverable:* 3 polished Markdown files in `production/alpha/`.

2.  **Asset Generation for Strategy:**
    *   Draft 5 "Social/Viral Diegetic" text posts (mock tweets, forum logs) based on *World-02 (Digital Paranoia)*.

---

## Phase 3: Knowledge Management & Tooling
**Goal:** Make the corpus "computable" for AI agents and future RAG systems.

1.  **Structured Metadata Extraction:**
    *   Create `data/research_index.json`: A structured JSON file summarizing every research document with:
        *   `concepts`: List of key terms.
        *   `dial_alignments`: {Argento: X, Lynch: Y, Kon: Z}.
        *   `pull_quotes`: Best 3 quotes per file.
    *   *Why:* This allows future agents to "query" the research without re-reading 300K words every time.

2.  **The "Director" System Prompt:**
    *   Draft `prompts/director_persona.md`: A system prompt that takes Dial Settings as input and outputs a specific writing style (e.g., "Act as Argento with 80% intensity").

3.  **Update `seed.yaml`:**
    *   Add `production-executor` agent definition.

---

## Phase 4: Strategy & Release Planning
**Goal:** Operationalize the "Competitive Release" strategy found in the ChatGPT archives.

1.  **The Campaign Calendar:**
    *   Create `strategy/release_calendar_v1.md`.
    *   Map a 12-week "Season 1" release schedule.
    *   Define "Intervention Points" where GRINDER interacts with QUEER (the companion repo).

2.  **The "Leaderboard" Mechanic:**
    *   Draft a spec for the "Competitive Tension" system mentioned in *Release Strategy Enhancement.md*. How do we track "wins"? (e.g., Word count? Engagement? "Scariness" rating?).

---

## Execution Order

1.  **Architecture:** Build the `bible/` foundation so we know *where* we are.
2.  **Tooling:** Build the `data/` index so we can find things.
3.  **Production:** Write the `production/` fragments to test the bible.
4.  **Strategy:** Plan the `strategy/` release for the produced assets.
