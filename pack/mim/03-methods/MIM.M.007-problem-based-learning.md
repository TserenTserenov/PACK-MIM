---
id: MIM.M.007
name: Problem-Based Learning (PBL)
origin: EDU.M.002
status: draft
s2r_families: [F5]
summary: >
  Learning through investigating and solving real or realistic ill-structured
  problems before receiving theory, driving self-directed knowledge acquisition.
sota: current
created: 2026-02-19
updated: 2026-03-22
related:
  produces:
    - MIM.WP.005  # Solution + reflection on learning process
  uses:
    - MIM.D.016  # Teaching ≠ Facilitation
    - MIM.D.018  # Knowledge ≠ Skill
  fails_with:
    - MIM.FM.007  # Problem too structured (no genuine inquiry)
    - MIM.FM.008  # Absent facilitation (learners flounder)
  requires_role:
    - MIM.R.001  # Наставник (ex-Facilitator)
---

## Definition

Problem-Based Learning (PBL) is an instructional method in which learners
encounter an ill-structured, real-world problem before receiving formal
instruction on the topic. Through investigation, learners identify their
own knowledge gaps, acquire necessary knowledge through self-directed
study, apply it to the problem, and reflect on the learning process.

PBL was developed by Howard Barrows at McMaster University Medical School
in the 1960s and formalized in Barrows (1986).

## Purpose

Develop problem-solving ability, self-directed learning skills, and deep
understanding by making the problem — not the lecture — the starting point
of learning. PBL integrates knowledge acquisition with application,
producing transferable competence rather than inert knowledge.

## Inputs

| Input | Description |
|-------|-------------|
| Ill-structured problem | A realistic problem without a single correct solution; requires investigation |
| Resource materials | Books, articles, databases, experts available for self-directed study |
| Facilitator guidance | A facilitator who guides the inquiry process without providing answers |

## Outputs

| Output | Description |
|--------|-------------|
| Solution | A reasoned, evidence-based response to the problem |
| Reflection on learning process | Explicit identification of what was learned, how, and what remains unknown |
| Identified knowledge gaps | List of what learners discovered they needed to learn |

## Roles Involved

- **Наставник (MIM.R.001):** Guides the inquiry process, asks probing
  questions, ensures productive group dynamics. Does NOT provide answers
  or lecture.

## Forces

_(Optional, WP-448 Ф10) What competing pressures does this method balance._

| Force | Tension |
|-------|---------|
| Genuine inquiry ↔ facilitator guidance | The facilitator must guide without lecturing (MIM.D.016) — too little guidance and learners flounder (MIM.FM.008), too much and the problem collapses into a worksheet (MIM.FM.007) |
| Self-directed discovery ↔ cognitive load for novices | Problem-first learning drives learners to find their own knowledge gaps, but for novices without schemas this same open-endedness overloads working memory (Sweller) — hence the recommended pairing with scaffolding (MIM.M.006) |
| Real-world realism ↔ learnability | An ill-structured problem must be realistic enough to demand genuine investigation, but structured enough that a knowledge gap is actually discoverable within the available resource materials |

## Related Methods

- MIM.M.006 (Scaffolding) — facilitator guidance in PBL is a form of
  scaffolding that fades as learners develop self-direction.
- MIM.M.008 (Case Method) — both use real-world situations; PBL is
  problem-first and self-directed, Case Method is analysis-centered with
  more instructor direction.
- MIM.M.009 (Experiential Learning) — PBL can serve as the "concrete
  experience" phase in Kolb's cycle.

## Key Distinctions

- **MIM.D.016 Teaching ≠ Facilitation.** In PBL the educator is a
  facilitator, not a teacher in the traditional sense. The facilitator
  does not transmit knowledge; they guide the learner's own inquiry
  process. Confusing these roles destroys PBL.
- **MIM.D.018 Knowledge ≠ Skill.** PBL targets both: knowledge is
  acquired in service of solving the problem (not for its own sake), and
  the problem-solving process itself builds skill. Assessing only
  knowledge misses half the outcome.

## Bias-Annotation

_(Optional, WP-448 Ф10) What systematic distortion does a practitioner risk when applying this method._

| Bias | Direction of distortion |
|------|--------------------------|
| Facilitator drifts toward teaching | Under time pressure or when learners struggle, the facilitator's attention shifts from asking probing questions toward supplying answers directly — the role quietly slides from facilitation (MIM.D.016) into lecturing (MIM.FM.009), even when the facilitator believes they are still guiding |
| Solution quality overweighted, reflection underweighted | Because the "Solution" output is concrete and gradeable, evaluators tend to over-focus on it while the "Reflection on learning process" output — equally required — gets treated as an afterthought, undermining the self-directed-learning half of PBL's purpose |

## Failure Modes

| ID | Failure Mode | Description |
|----|-------------|-------------|
| MIM.FM.007 | Problem too structured | The problem has a clear single answer and predetermined steps — no genuine inquiry occurs, PBL degrades to a worksheet |
| MIM.FM.008 | Absent facilitation | Facilitator is absent or passive; learners flounder without direction, frustration replaces learning |
| MIM.FM.009 | Theory-first contamination | Instructor lectures before presenting the problem, eliminating the knowledge-gap discovery that drives PBL |

## SoTA Status

**Status:** current
**Evidence strength:** Moderate-to-Strong (context-dependent)

**Basis:**
- Barrows, H.S. (1986). "A taxonomy of problem-based learning methods."
  *Medical Education*, 20(6), 481-486.
- Hmelo-Silver, C.E. (2004). "Problem-based learning: What and how do
  students learn?" *Educational Psychology Review*, 16(3), 235-266.
- Strobel & van Barneveld (2009). Meta-analysis: PBL superior for
  long-term retention and skill application; direct instruction superior
  for short-term factual recall.
- Hattie (2023): PBL d=0.35 (moderate) — but this average masks strong
  context-dependence: effective for applied domains, weaker for
  foundational knowledge.

**Notes:** PBL is most effective for adults and professionals (medicine,
engineering, law, business). It requires careful problem design and skilled
facilitation. Effectiveness is well-documented in medical education and
increasingly in engineering and management education.

**CLT consideration:** PBL can overload working memory for novices who
lack schemas to organize information (Sweller, 2006). Solution: combine
PBL with scaffolding (MIM.M.006) and worked examples for beginners.

**Three-Level placement (MIM.FORM.004):** Level 2 (Domain Method) —
effective for applied disciplines, must incorporate Level 1 meta-principles
(retrieval practice, feedback, spaced repetition).
