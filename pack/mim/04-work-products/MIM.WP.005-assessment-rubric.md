---
id: MIM.WP.005
name: Assessment Rubric (Оценочная рубрика)
status: active
summary: "Инструмент оценивания с критериями и уровнями достижения — проверяет соответствие результатов целям обучения."
created: 2026-02-19
last_updated: 2026-02-19
related:
  produced_by:
    - MIM.M.010  # Backwards Design (Stage 2: Determine Assessment Evidence)
  consumed_by:
    - MIM.M.009  # Experiential Learning (оценка в фазе рефлексии)
  represents:
    - MIM.D.017  # Формативное ≠ Суммативное оценивание
    - MIM.D.018  # Знание ≠ Навык (рубрика проверяет навык, не только знание)
  enables_role:
    - MIM.R.002  # Instructor (использует для оценки)
    - MIM.R.008  # Instructional Designer (создаёт)
origin: EDU.WP.002
s2r_families: [F5]
updated: 2026-03-22
---

# [MIM.WP.005] Assessment Rubric (Оценочная рубрика)

---

## Definition

**Assessment Rubric** — структурированный инструмент оценивания, описывающий критерии оценки и уровни достижения для каждого критерия. Рубрика связывает цели обучения (MIM.WP.004) с наблюдаемыми результатами и обеспечивает объективность оценки.

Assessment Rubric is NOT:
- Тест с вариантами ответов (проверяет только запоминание, уровни 1-2)
- Субъективное впечатление преподавателя
- Анкета удовлетворённости (Kirkpatrick Level 1 ≠ Level 2)

---

## Purpose

| Function | Description |
|----------|-------------|
| **Валидация обучения** | Проверяет, достигнуты ли цели на нужном уровне Блума |
| **Объективность** | Одинаковые критерии для всех учеников — снижает субъективность |
| **Обратная связь** | Показывает ученику, где он и что улучшить (формативное применение) |
| **Согласованность** | Гарантирует, что оценка измеряет то, чему учили (alignment) |

---

## Produced By

| Method | Notes |
|--------|-------|
| [MIM.M.010](../03-methods/MIM.M.010-backwards-design.md) | Stage 2: Assessment before activities |

---

## Consumed By

| Consumer | How Used |
|----------|----------|
| [MIM.R.002](../02-domain-entities/02A-roles.md) | Instructor использует для оценки работ |
| [MIM.R.007](../02-domain-entities/02A-roles.md) | Navigator использует для диагностики пробелов |
| Ученик | Для самооценки и понимания ожиданий |

---

## Existence Criteria (MANDATORY)

**How to verify this work product exists:**

- [ ] Для каждой цели обучения (из MIM.WP.004) определён хотя бы один критерий оценки
- [ ] Каждый критерий имеет ≥3 уровней достижения (например: начинающий, развивающийся, продвинутый)
- [ ] Уровень оценки соответствует уровню цели по Блуму (цель на Apply → задание на Apply, не на Remember)
- [ ] Описания уровней наблюдаемы: что именно ученик делает на каждом уровне

**If all criteria are met, the work product exists. If any criterion fails, it does not.**

---

## Structure

| Field | Type | Required? | Constraints |
|-------|------|-----------|-------------|
| Цель обучения (из WP.001) | Reference | Yes | ID цели + формулировка |
| Критерий | String | Yes | Наблюдаемый аспект оценки |
| Уровни достижения | Table | Yes | ≥3 уровней с описанием |
| Тип оценивания | Enum | Yes | Формативное / Суммативное |
| Уровень Блума | Number (1-6) | Yes | Должен совпадать с целью |

---

## Related Failure Modes

Common failures:
- [MIM.FM.006](../05-failure-modes/MIM.FM.006-testing-knowledge-not-skills.md) — рубрика на уровнях 1-2 при целях на 3-6
- [MIM.FM.004](../05-failure-modes/MIM.FM.004-lecture-equals-learning.md) — отсутствие рубрики = нет проверки обучения

---

*Pack ID: MIM | SPF.SPEC.001 compliant*
