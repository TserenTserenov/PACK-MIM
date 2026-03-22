---
id: MIM.WP.004
name: Learning Requirements (ТЗ на обучение)
status: active
summary: "Документ с профилем аудитории, целями обучения по Блуму и gap-анализом — вход для проектирования программы."
created: 2026-02-19
last_updated: 2026-02-19
related:
  produced_by:
    - MIM.M.010  # Backwards Design (Stage 1: Identify Desired Results)
  consumed_by:
    - MIM.M.006  # Scaffolding (для калибровки ZPD)
    - MIM.M.007  # PBL (для выбора проблемы)
    - MIM.M.008  # Case Method (для подбора кейсов)
  represents:
    - MIM.D.019  # Содержание ≠ Методика (разделяет что от как)
    - MIM.D.015  # Педагогика ≠ Андрагогика (профиль аудитории)
  enables_role:
    - MIM.R.008  # Instructional Designer (основной потребитель)
origin: EDU.WP.001
s2r_families: [F5]
updated: 2026-03-22
---

# [MIM.WP.004] Learning Requirements (ТЗ на обучение)

---

## Definition

**Learning Requirements** — документ, фиксирующий входные данные для проектирования обучения: кого учим (профиль аудитории), зачем (цели обучения), откуда стартуем (текущий уровень) и в каких ограничениях (время, бюджет, формат).

Learning Requirements is NOT:
- Учебный план (это следующий шаг, MIM.WP.006)
- Список тем для лекций (это содержание, не требования)
- Маркетинговое описание курса

---

## Purpose

| Function | Description |
|----------|-------------|
| **Фокусировка** | Определяет, что именно должно измениться в результате обучения (цели по Блуму) |
| **Сегментация** | Описывает аудиторию с достаточной детализацией для выбора методов |
| **Ограничения** | Фиксирует рамки: время, бюджет, формат, инфраструктура |
| **Валидация** | Даёт критерии для оценки: цели достигнуты или нет |

---

## Produced By

| Method | Notes |
|--------|-------|
| [MIM.M.010](../03-methods/MIM.M.010-backwards-design.md) | Stage 1: Identify Desired Results |
| ADDIE Phase 1 (Analysis) | [MIM.FORM.002](../02-domain-entities/formalizations/MIM.FORM.002-addie-model.md) |

---

## Consumed By

| Consumer | How Used |
|----------|----------|
| [MIM.R.008](../02-domain-entities/02A-roles.md) | Instructional Designer использует как вход для проектирования |
| [MIM.M.006](../03-methods/MIM.M.006-scaffolding.md) | Для определения ZPD и калибровки поддержки |
| [MIM.M.007](../03-methods/MIM.M.007-problem-based-learning.md) | Для подбора проблемы под уровень аудитории |

---

## Existence Criteria (MANDATORY)

**How to verify this work product exists:**

- [ ] Описан профиль аудитории: возрастная группа (MIM.FORM.003), профессиональный опыт, текущий уровень
- [ ] Сформулированы цели обучения через глаголы таксономии Блума (MIM.FORM.001): «ученик сможет [глагол] [объект]»
- [ ] Проведён gap-анализ: текущий уровень vs целевой уровень
- [ ] Зафиксированы ограничения: время, бюджет, формат, размер группы
- [ ] Указаны критерии успеха: как измерить достижение целей

**If all criteria are met, the work product exists. If any criterion fails, it does not.**

---

## Structure

| Field | Type | Required? | Constraints |
|-------|------|-----------|-------------|
| Профиль аудитории | Structured | Yes | Возрастная группа, опыт, мотивация |
| Цели обучения | List | Yes | Глагол Блума + объект, уровень 1-6 |
| Gap-анализ | Table | Yes | Текущий уровень → целевой уровень |
| Ограничения | Structured | Yes | Время, бюджет, формат |
| Критерии успеха | Checklist | Yes | Наблюдаемые, измеримые |

---

## Related Failure Modes

Common failures when this WP is absent or malformed:
- [MIM.FM.005](../05-failure-modes/MIM.FM.005-one-size-fits-all.md) — без профиля аудитории один метод для всех
- [MIM.FM.008](../05-failure-modes/MIM.FM.008-ignoring-prior-experience.md) — без gap-анализа опыт игнорируется

---

*Pack ID: MIM | SPF.SPEC.001 compliant*
