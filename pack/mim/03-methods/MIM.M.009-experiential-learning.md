---
id: MIM.M.009
name: Experiential Learning Cycle
origin: EDU.M.004
status: draft
s2r_families: [F5]
summary: >
  Kolb's four-stage cycle — concrete experience, reflective observation,
  abstract conceptualization, active experimentation — structuring learning
  through doing with deliberate reflection.
sota: current
created: 2026-02-19
updated: 2026-03-22
related:
  produces:
    - MIM.WP.007  # Experiential learning journal, conceptual models, action plans
  uses:
    - MIM.D.021  # Teaching ≠ Informing
  fails_with:
    - MIM.FM.013  # Experience without reflection
    - MIM.FM.014  # Cycle truncated (skipping stages)
  requires_role:
    - MIM.R.001  # Наставник (ex-Facilitator)
    - MIM.R.006  # Mentor
---

## Definition

Experiential Learning is an instructional method based on Kolb's (1984)
four-stage learning cycle:

1. **Concrete Experience (CE):** The learner engages in a direct experience
   or activity.
2. **Reflective Observation (RO):** The learner reflects on the experience
   from multiple perspectives.
3. **Abstract Conceptualization (AC):** The learner forms generalizations,
   principles, or theories from the reflection.
4. **Active Experimentation (AE):** The learner tests the new concepts in
   new situations, generating the next concrete experience.

The cycle is iterative: each round deepens understanding. Learning occurs
through the transformation of experience, not merely its accumulation.

## Purpose

Structure learning-by-doing so that experience is converted into
transferable knowledge and tested principles. Without the full cycle,
experience remains anecdotal and does not generalize. The method ensures
that action and reflection are both present and connected.

## Inputs

| Input | Description |
|-------|-------------|
| Experience opportunity | A situation where the learner can act, observe, and receive feedback |
| Reflection framework | Structured questions or prompts guiding reflective observation |
| Conceptual models | Theories or frameworks available for the abstract conceptualization stage |

## Outputs

| Output | Description |
|--------|-------------|
| Experiential learning journal | Written record of experiences, reflections, and emerging principles |
| Conceptual models | Generalizations and theories the learner has constructed from experience |
| Action plans | Plans for active experimentation to test new concepts |

## Roles Involved

- **Наставник (MIM.R.001):** Designs the experience, provides reflection
  prompts, guides conceptualization, and creates conditions for
  experimentation.
- **Mentor (MIM.R.006):** Supports longer-term experiential learning
  cycles, helps the learner connect experiences across time, and provides
  perspective from their own experience.

## Forces

_(Optional, WP-448 Ф10) What competing pressures does this method balance._

| Force | Tension |
|-------|---------|
| Full four-stage cycle ↔ time and momentum | Each stage (CE→RO→AC→AE) adds value, but running all four fully takes time — truncating under schedule pressure is exactly what produces partial learning (MIM.FM.014) |
| Concrete experience ↔ abstract conceptualization | Grounding in a specific experience keeps the concept alive and applicable, but the method also demands generalization beyond that one experience — theory introduced without the prior experience stays inert (MIM.FM.015), while experience without conceptualization stays anecdotal |
| Iterative depth ↔ linear closure | The cycle is meant to repeat and deepen understanding across rounds, which pulls against the natural desire to treat one pass through CE-RO-AC-AE as "done" |

## Related Methods

- MIM.M.006 (Scaffolding) — scaffolding can be applied within any stage
  of the experiential cycle, especially during abstract conceptualization.
- MIM.M.007 (Problem-Based Learning) — PBL can serve as the concrete
  experience that initiates the cycle.
- MIM.M.008 (Case Method) — case analysis is a form of reflective
  observation on vicarious experience.

## Key Distinctions

- **MIM.D.021 Teaching ≠ Informing.** Experiential learning is teaching
  through structured experience and reflection. Informing (transmitting
  facts) skips the experience and reflection stages entirely. A lecture
  about riding a bicycle is informing; riding, falling, reflecting, and
  riding again is experiential learning. The distinction determines
  whether the full cycle is activated.

## Bias-Annotation

_(Optional, WP-448 Ф10) What systematic distortion does a practitioner risk when applying this method._

| Bias | Direction of distortion |
|------|--------------------------|
| Reflection stage quietly dropped under time pressure | Concrete Experience is visible and easy to schedule (an activity happened), so attention and time default to it, while Reflective Observation — invisible, harder to verify happened at all — is the stage most often silently skipped, directly producing MIM.FM.013 |
| Reflection journal treated as compliance artifact | Once a "reflection framework" exists as a required output, learners can drift toward filling it out to satisfy the requirement rather than genuinely engaging Reflective Observation — the artifact gets produced while the actual cognitive work it is meant to evidence does not happen |

## Failure Modes

| ID | Failure Mode | Description |
|----|-------------|-------------|
| MIM.FM.013 | Experience without reflection | Learners go through activities but skip reflective observation; experience does not convert to learning |
| MIM.FM.014 | Cycle truncated | One or more stages are skipped (commonly: reflection or experimentation); learning remains partial |
| MIM.FM.015 | Conceptualization without grounding | Abstract theories are introduced without prior concrete experience; concepts remain inert and disconnected |

## SoTA Status

**Status:** current
**Evidence strength:** Moderate (widely used, but effect sizes variable)

**Basis:**
- Kolb, D.A. (1984). *Experiential Learning: Experience as the Source
  of Learning and Development.* Prentice-Hall.
- Jarvis, P. (2006). *Towards a Comprehensive Theory of Human Learning.*
  Routledge.
- Moon, J.A. (2004). *A Handbook of Reflective and Experiential Learning.*
  Evidence for reflection as learning mechanism.

**Notes:** Experiential learning is effective across all age groups, with
particular strength for adults who bring prior experience to the cycle.
The model is widely applied in professional education, outdoor education,
service learning, and workplace training. Critics note the model's
linearity; Jarvis (2006) offers a more nuanced multi-path model.

**Enhancement with Level 1 meta-principles (MIM.FORM.004):** Embed
retrieval practice (MIM.M.011) in the Reflective Observation stage and
spaced repetition (MIM.M.012) between cycles for maximum effect.

**Three-Level placement:** Level 2 (Domain Method) — particularly
effective for interpersonal skills, leadership, and professional practice.
