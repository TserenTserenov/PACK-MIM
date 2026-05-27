---
id: MIM.DISJOINT
version: 1.0.0
status: active
created: 2026-05-27
scope: pack-internal
count: 15
---

# Реестр disjointness: MIM

> Machine-readable registry of hard distinctions with disjoint classes.
> Source: `01B-distinctions.md` (MIM.D.001–MIM.D.025).
> Purpose: enable pack-lint [R5] to detect when a new entity claims membership in both classes of a distinction.

## Format

Each row defines a distinction whose two sides are **disjoint classes**:
- A new entity MUST NOT map to both `class_a` and `class_b` simultaneously
- The `test_boundary` column quotes the operational test from `01B-distinctions.md`
- The `rationale` column explains why this distinction is in the registry (risk of pack-internal confusion)

## Registry (top-15)

| # | Distinction ID | Class A | Class B | Test Boundary | Rationale |
|---|----------------|---------|---------|---------------|-----------|
| 1 | MIM.D.001 | Seminar | Practicum | «If you remove the speaker, the event is impossible → seminar. If you remove exercises, the event is meaningless → practicum.» | Most frequent confusion in MIM: expecting skill from a knowledge-format (MIM.FM.001) |
| 2 | MIM.D.002 | Practicum | Residency | «Result is thrown away after exercise → practicum. Result is presented to customer/colleagues → residency.» | Newcomers without base skills attempt residency → failure |
| 3 | MIM.D.003 | Residency | Internship | «Who chooses what to do? You → residency. Manager → internship.» | Resident waits for «assignments» instead of defining their masterpiece |
| 4 | MIM.D.004 | Review | Exam | «Qualification is measured at every meeting → review. Qualification is checked at the end → exam.» | Splitting «learn» / «be evaluated» kills raw feedback |
| 5 | MIM.D.005 | Format | Program | «What type of event is this? → format. What are we developing? → program.» | Identifying format with program destroys flexibility |
| 6 | MIM.D.007 | S2Principle | S1Bias | «You consciously check the rule before applying → principle (S2). You apply automatically → inductive bias (S1).» | Seminar without practicum leaves principle as «cabinet knowledge» |
| 7 | MIM.D.009 | WorkshopOrg | SchoolOrg | «Workshop = infinite becoming of mastery. School = finite program with diploma.» | Expecting diploma from workshop → misalignment |
| 8 | MIM.D.010 | Organization | Community | «MIM = organizational machine (employees, budget, SoTA-research). Community = union of like-minded people.» | Blurring funding/accountability boundaries |
| 9 | MIM.D.012 | Thinker | Creator | «Writing texts = thinking. Action = entering the world with responsibility for risks.» | AI agent promises are speech acts with real consequences |
| 10 | MIM.D.013 | AICriticRole | AIGeneratorRole | «Student generates, AI evaluates → deliberate practice. AI generates, human edits → risk of competence atrophy.» | Confusing roles leads to wrong didactic design |
| 11 | MIM.D.014 | WorkCulture | TitleCulture | «Result (masterpiece) is valued vs status (diploma) is valued.» | Qualification through doing vs qualification through exam |
| 12 | MIM.D.015 | Pedagogy | Andragogy | «Teaching children vs teaching adults. Motivation, role of experience, application.» | Applying child-teaching methods to adults |
| 13 | MIM.D.017 | FormativeAssessment | SummativeAssessment | «Assessment for improving the process vs fixing the result.» | Using summative tools during learning kills growth mindset |
| 14 | MIM.D.018 | Knowledge | Skill | «Declarative (explain) vs procedural (do). Bloom 1-2 vs 3-6.» | Testing knowledge when goal is skill (MIM.FM.006) |
| 15 | MIM.D.019 | Content | Methodology | «What to teach (Pack) vs how to teach (transferable across domains).» | Changing content when method should change, or vice versa |

## Machine-readable block (for pack-lint R5)

```yaml
disjoint_pairs:
  - distinction: MIM.D.001
    class_a: MIM.FMT.001
    class_b: MIM.FMT.002
  - distinction: MIM.D.002
    class_a: MIM.FMT.002
    class_b: MIM.FMT.003
  - distinction: MIM.D.003
    class_a: MIM.FMT.003
    class_b: Internship
  - distinction: MIM.D.004
    class_a: MIM.FMT.004
    class_b: Exam
  - distinction: MIM.D.005
    class_a: FMT
    class_b: PRG
  - distinction: MIM.D.007
    class_a: S2Principle
    class_b: S1Bias
  - distinction: MIM.D.009
    class_a: WorkshopOrg
    class_b: SchoolOrg
  - distinction: MIM.D.010
    class_a: Organization
    class_b: Community
  - distinction: MIM.D.012
    class_a: Thinker
    class_b: Creator
  - distinction: MIM.D.013
    class_a: AICriticRole
    class_b: AIGeneratorRole
  - distinction: MIM.D.014
    class_a: WorkCulture
    class_b: TitleCulture
  - distinction: MIM.D.015
    class_a: Pedagogy
    class_b: Andragogy
  - distinction: MIM.D.017
    class_a: FormativeAssessment
    class_b: SummativeAssessment
  - distinction: MIM.D.018
    class_a: Knowledge
    class_b: Skill
  - distinction: MIM.D.019
    class_a: Content
    class_b: Methodology
```

## Notes for KE (Knowledge Extractor)

When adding a new entity to this Pack:
1. Check if the entity's `type:` or `types:` in frontmatter maps to any `class_a` + `class_b` pair above
2. If both classes are claimed → reject or require explicit justification in `exceptions:`
3. If a new distinction is discovered during KE → propose adding it to this registry (top-15 may grow)

## Changelog

| Date | Version | Change |
|------|---------|--------|
| 2026-05-27 | 1.0.0 | Initial registry: 15 disjoint pairs from MIM.D.001–MIM.D.019. Created per peer-session 2026-05-27-19-use-ontology-engineering-in-packs. |
