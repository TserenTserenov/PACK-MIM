---
id: MIM.M.006
name: Scaffolding
origin: EDU.M.001
status: draft
s2r_families: [F5]
summary: >
  Gradually removing instructional support as the learner demonstrates
  increasing competence within the Zone of Proximal Development.
sota: current
created: 2026-02-19
updated: 2026-03-22
related:
  produces:
    - MIM.WP.004  # Progression evidence showing decreasing support needs
  uses:
    - MIM.D.022  # Adaptation ≠ Simplification
  fails_with:
    - MIM.FM.004  # Premature removal of support
    - MIM.FM.005  # Permanent scaffolding (support never removed)
  requires_role:
    - MIM.R.002  # Докладчик (ex-Instructor)
    - MIM.R.007  # Navigator
---

## Definition

Scaffolding is an instructional method in which the teacher provides
structured support to the learner performing a task that is beyond their
current independent capability but within reach with assistance (the Zone
of Proximal Development). As the learner gains competence, the support is
systematically reduced ("faded") until the learner can perform
independently.

The concept originates from Vygotsky's Zone of Proximal Development (ZPD)
and was formalized as "scaffolding" by Wood, Bruner & Ross (1976).

## Purpose

Enable the learner to accomplish tasks they cannot yet do alone, while
building the competence to eventually perform independently. Scaffolding
bridges the gap between current ability and target competency without
bypassing the learning process.

## Inputs

| Input | Description |
|-------|-------------|
| Learner's current level | Assessed baseline of what the learner can do independently |
| Target competency | The skill or understanding the learner should reach |
| Learning tasks | Sequenced tasks within the ZPD, calibrated to the learner |

## Outputs

| Output | Description |
|--------|-------------|
| Progression evidence | Observable data showing decreasing support needs over time |
| Independent performance | Learner demonstrates target competency without assistance |

## Roles Involved

- **Докладчик (MIM.R.002):** Designs the scaffolding sequence, calibrates
  task difficulty, decides when to fade support.
- **Navigator (MIM.R.007):** Provides one-on-one scaffolding in real time,
  adjusts support moment-by-moment based on learner responses.

## Related Methods

- MIM.M.009 (Experiential Learning) — scaffolding can structure the
  experience phase of Kolb's cycle.
- MIM.M.007 (Problem-Based Learning) — facilitator guidance in PBL is a
  form of scaffolding.

## Key Distinctions

- **MIM.D.022 Adaptation ≠ Simplification.** Scaffolding adapts support to
  the learner's level — it does NOT simplify the target task. The task
  remains at full complexity; what changes is the amount and type of
  assistance. Simplification removes complexity; scaffolding manages it.

## Failure Modes

| ID | Failure Mode | Description |
|----|-------------|-------------|
| MIM.FM.004 | Premature removal of support | Support is faded before the learner has sufficient competence, leading to failure and demotivation |
| MIM.FM.005 | Permanent scaffolding | Support is never removed; the learner becomes dependent and does not develop independent capability |
| MIM.FM.006 | Misidentified ZPD | Tasks are set outside the Zone of Proximal Development — too easy (no learning) or too hard (scaffolding insufficient) |

## SoTA Status

**Status:** current
**Evidence strength:** Strong

**Basis:**
- Wood, D., Bruner, J.S., & Ross, G. (1976). "The role of tutoring in
  problem solving." *Journal of Child Psychology and Psychiatry*, 17(2),
  89-100.
- Vygotsky, L.S. (1978). *Mind in Society: The Development of Higher
  Psychological Processes.*
- Hattie, J. (2023). *Visible Learning: The Sequel.* d=0.82 for
  scaffolding (one of the highest effect sizes).
- Sweller, J. (2024). Expertise Reversal Effect: scaffolding that helps
  novices can HINDER experts who already have schemas. Must calibrate
  support to prior knowledge level (MIM.D.023).

**Notes:** Scaffolding is effective across all age groups, with particular
strength for children and beginners. It is one of the most empirically
supported instructional methods in education research. **Caveat:** For
experts, excessive scaffolding creates extraneous cognitive load (CLT)
— the Expertise Reversal Effect (Sweller, 2024). Calibrate scaffolding
level to prior knowledge (MIM.D.023), not to learning style.

**Human ↔ AI parallel (ECO.D.007):** Scaffolding ↔ Curriculum Learning
in ML: both present progressively harder tasks as competence grows.
