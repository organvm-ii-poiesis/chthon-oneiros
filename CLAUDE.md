# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Is

CHTHON-ONEIROS is a psychological horror theory corpus and narrative engine — the "Underworld-dream" of the ORGANVM system (Organ II / Art). It treats horror as epistemology, not genre decoration. All content explores the unconscious as compositional engine through surrealism, found footage, digital paranoia, and reality failure.

Part of the **Artistic Triforce**: Polarity II (The Subconscious), inverse of KRYPTO-VELAMEN (Polarity I / The Conscious), historicized by Polarity III (The Temporal).

## Commands

```bash
# Update corpus statistics in CATALOG.md (word counts, file counts)
./tools/update_stats.sh

# Lint a file for Giallo color vocabulary violations
python3 ./tools/giallo_check.py <file_path>

# Run substrate metabolism (adds Unicode decay to production/beta files)
./tools/metabolize.sh

# Generate a semantic satiation exhibit
python3 ./tools/satiation.py <seed_word> [count]
```

## Architecture

### The Three Director Dials

Every piece of content is calibrated on three 0-100 axes. These are not tags — they are structural parameters that determine voice, vocabulary, and narrative logic:

- **$ARGENTO_GEL** — Chromatic aggression, ritual staging, operatic violence. High values = neon color, Giallo mystery structure, aggressive scoring.
- **$LYNCH_DRIFT** — Mundane-to-cosmic dread, dream logic, identity dissolution. High values = pauses, silence, the hum, suburban uncanny.
- **$KON_SPIRAL** — Mediation collapse, recursion, screen-as-predator. High values = screens within screens, identity merging, paranoid editing.

### The Core Loop (4-Stage Spiral)

All narrative fragments follow: **Mundane Anchor** (stable reality) → **Epistemic Drift** (one anomaly, investigation) → **The Peak** (reality failure) → **Unresolved Stop** (hard cut, no resolution). Defined in `bible/core_loop.md`.

### The Six Rings (Geography)

Ring 0 (Surface Internet) → Ring 1 (Digital Bleed) → Ring 2 (City of Gels) → Ring 3 (Deep Drift) → Ring 4 (Sediment) → Ring 5 (Fossil Bed). Defined in `bible/geography.md`.

### Research Framework

New research follows the **18-Step Protocol** in `research/framework_v2.md`: Ingestion (1-3) → Analysis (4-7) → Synthesis (8-13) → Framework Generation (14-18). Directors are organized into numbered clusters (1-14 for Stream A, 21-25 for Stream B / Chthonic Genealogy).

## Key Governance Files

- `bible/physics.md` — Immutable laws of the world (7 Epistemological Laws). Read before any contribution.
- `bible/core_loop.md` — The 4-Stage Spiral narrative architecture.
- `docs/CATALOG.md` — Single source of truth for corpus statistics. Must be updated when files change.
- `drafts/TEMPLATE.md` — Fragment template with dial metadata, technique checklists, and 7-point production self-check.
- `prompts/director_persona.md` — System prompt for the Director creative engine (dial-modulated voice).
- `.config/ai-agents/seed.yaml` — Automation contract defining agent triggers and inter-repo subscriptions.

## Content Rules

- **Giallo Law**: Use evocative color vocabulary, not plain colors. The linter enforces: red→CRIMSON, blue→INDIGO, green→EMERALD, yellow→SODIUM, purple→VIOLET, white→BLINDING, black→INK, orange→VERMILION.
- **Root hygiene**: Keep root clean. New theory → `docs/theory/`. New production → `production/beta/`. New research → `research/`.
- **Catalog truth**: Every new file must be reflected in `docs/CATALOG.md`. Run `./tools/update_stats.sh` after changes.
- **No safe content**: If it feels safe to publish, it's not ready. The audience must not be sure whether what they're encountering is real.
- **Never explain the horror**: Describe the thing itself. Do not tell the reader why something is scary.
- **Unresolved endings only**: No happy endings. No clear explanations. The mystery remains active.

## File Organization

- `bible/` — World laws, bestiary, geography, artifacts (authoritative, rarely changes)
- `research/` — Director deep-dives and thematic cluster reports (cluster_NN_*.md, world-NN-*.md)
- `production/alpha/` — Test fragments and dial calibration pieces
- `production/beta/` — Full episodes (Season 2: episodes 01-08)
- `release/week_NN/` — Canonical campaign drops and echoes (Season 1: weeks 01-24)
- `museum/` — The Anti-Archive: unrecorded artifacts, satiation exhibits, audits
- `docs/theory/` — Theoretical foundations (Artistic Triforce, GRINDER concepts)
- `docs/integration/` — Cross-repository synthesis (Triforce audits, Deep Time)
- `strategy/` — Release calendars, museum operations, leaderboard mechanics
- `tools/` — Automation scripts and the LingFrame sentiment lexicon
- `data/` — Research index and weight logs (JSON)

## ORGANVM Context

Organ II (Art) under `organvm-ii-poiesis`. Consumes theory from Organ I (`organvm-i-theoria`) and provides subconscious material to Polarity III (Narratological Lenses / LingFrame).

**Registry:** [`registry-v2.json`](https://github.com/meta-organvm/organvm-corpvs-testamentvm/blob/main/registry-v2.json)

<!-- ORGANVM:AUTO:START -->
## System Context (auto-generated — do not edit)

**Organ:** ORGAN-II (Art) | **Tier:** standard | **Status:** LOCAL
**Org:** `unknown` | **Repo:** `chthon-oneiros`

### Edges
- *No inter-repo edges declared in seed.yaml*

### Siblings in Art
`core-engine`, `performance-sdk`, `example-generative-music`, `metasystem-master`, `example-choreographic-interface`, `showcase-portfolio`, `archive-past-works`, `case-studies-methodology`, `learning-resources`, `example-generative-visual`, `example-interactive-installation`, `example-ai-collaboration`, `docs`, `a-mavs-olevm`, `a-i-council--coliseum` ... and 14 more

### Governance
- Consumes Theory (I) concepts, produces artifacts for Commerce (III).

*Last synced: 2026-02-24T12:41:28Z*
<!-- ORGANVM:AUTO:END -->
