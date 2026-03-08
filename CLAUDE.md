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
**Org:** `organvm-ii-poiesis` | **Repo:** `chthon-oneiros`

### Edges
- *No inter-repo edges declared in seed.yaml*

### Siblings in Art
`core-engine`, `performance-sdk`, `example-generative-music`, `metasystem-master`, `example-choreographic-interface`, `showcase-portfolio`, `archive-past-works`, `case-studies-methodology`, `learning-resources`, `example-generative-visual`, `example-interactive-installation`, `example-ai-collaboration`, `docs`, `a-mavs-olevm`, `a-i-council--coliseum` ... and 14 more

### Governance
- Consumes Theory (I) concepts, produces artifacts for Commerce (III).

*Last synced: 2026-03-08T20:11:34Z*

## Session Review Protocol

At the end of each session that produces or modifies files:
1. Run `organvm session review --latest` to get a session summary
2. Check for unimplemented plans: `organvm session plans --project .`
3. Export significant sessions: `organvm session export <id> --slug <slug>`
4. Run `organvm prompts distill --dry-run` to detect uncovered operational patterns

Transcripts are on-demand (never committed):
- `organvm session transcript <id>` — conversation summary
- `organvm session transcript <id> --unabridged` — full audit trail
- `organvm session prompts <id>` — human prompts only


## Active Directives

| Scope | Phase | Name | Description |
|-------|-------|------|-------------|
| system | any | prompting-standards | Prompting Standards |
| system | any | research-standards-bibliography | APPENDIX: Research Standards Bibliography |
| system | any | research-standards | METADOC: Architectural Typology & Research Standards |
| system | any | sop-ecosystem | METADOC: SOP Ecosystem — Taxonomy, Inventory & Coverage |
| system | foundation | agent-seeding-and-workforce-planning | agent-seeding-and-workforce-planning |
| system | any | autopoietic-systems-diagnostics | SOP: Autopoietic Systems Diagnostics (The Mirror of Eternity) |
| system | any | cicd-resilience-and-recovery | SOP: CI/CD Pipeline Resilience & Recovery |
| system | any | cross-agent-handoff | SOP: Cross-Agent Session Handoff |
| system | any | document-audit-feature-extraction | SOP: Document Audit & Feature Extraction |
| system | any | essay-publishing-and-distribution | SOP: Essay Publishing & Distribution |
| system | any | market-gap-analysis | SOP: Full-Breath Market-Gap Analysis & Defensive Parrying |
| system | foundation | ontological-renaming | ontological-renaming |
| system | any | pitch-deck-rollout | SOP: Pitch Deck Generation & Rollout |
| system | any | promotion-and-state-transitions | SOP: Promotion & State Transitions |
| system | foundation | readme-and-documentation | readme-and-documentation |
| system | any | repo-onboarding-and-habitat-creation | SOP: Repo Onboarding & Habitat Creation |
| system | any | research-to-implementation-pipeline | SOP: Research-to-Implementation Pipeline (The Gold Path) |
| system | any | security-and-accessibility-audit | SOP: Security & Accessibility Audit |
| system | any | session-self-critique | session-self-critique |
| system | any | source-evaluation-and-bibliography | SOP: Source Evaluation & Annotated Bibliography (The Refinery) |
| system | any | stranger-test-protocol | SOP: Stranger Test Protocol |
| system | any | strategic-foresight-and-futures | SOP: Strategic Foresight & Futures (The Telescope) |
| system | any | typological-hermeneutic-analysis | SOP: Typological & Hermeneutic Analysis (The Archaeology) |

Linked skills: cross-agent-handoff, evaluation-to-growth, planning-and-roadmapping, repo-onboarding-and-habitat-creation, structural-integrity-audit


**Prompting (Anthropic)**: context 200K tokens, format: XML tags, thinking: extended thinking (budget_tokens)

<!-- ORGANVM:AUTO:END -->


## ⚡ Conductor OS Integration
This repository is a managed component of the ORGANVM meta-workspace.
- **Orchestration:** Use `conductor patch` for system status and work queue.
- **Lifecycle:** Follow the `FRAME -> SHAPE -> BUILD -> PROVE` workflow.
- **Governance:** Promotions are managed via `conductor wip promote`.
- **Intelligence:** Conductor MCP tools are available for routing and mission synthesis.
