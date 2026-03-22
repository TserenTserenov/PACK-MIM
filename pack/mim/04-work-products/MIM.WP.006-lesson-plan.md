---
id: MIM.WP.006
name: Lesson Plan (План занятия)
status: active
summary: "Дизайн одного учебного события: цели, методы, активности, тайминг, оценка — готовый к реализации."
created: 2026-02-19
last_updated: 2026-02-19
related:
  produced_by:
    - MIM.M.010  # Backwards Design (Stage 3: Plan Learning Experiences)
  consumed_by:
    - MIM.M.006  # Scaffolding (реализация плана)
    - MIM.M.007  # PBL (план включает проблему)
    - MIM.M.008  # Case Method (план включает кейс)
    - MIM.M.009  # Experiential Learning (план включает цикл Колба)
  represents:
    - MIM.D.019  # Содержание ≠ Методика (план объединяет оба)
  enables_role:
    - MIM.R.002  # Instructor (реализует план)
    - MIM.R.001  # Facilitator (реализует план)
origin: EDU.WP.003
s2r_families: [F5]
updated: 2026-03-22
---

# [MIM.WP.006] Lesson Plan (План занятия)

---

## Definition

**Lesson Plan** — детальный дизайн одного учебного события (занятия, сессии, модуля): цели, выбранные методы, последовательность активностей, тайминг, материалы и способ оценки. Это «чертёж» для преподавателя — артефакт, по которому можно провести занятие.

Lesson Plan is NOT:
- Программа курса (план = одно событие, программа = серия событий)
- Список слайдов (слайды — материал, план — дизайн)
- Расписание (расписание = когда, план = что и как)

---

## Purpose

| Function | Description |
|----------|-------------|
| **Alignment** | Гарантирует, что активности ведут к целям обучения (не к «покрытию материала») |
| **Баланс теория/практика** | Явно выделяет время на практику — предотвращает MIM.FM.007 |
| **Воспроизводимость** | Другой преподаватель может провести занятие по плану |
| **Тайминг** | Предотвращает «не хватило времени на практику» |

---

## Produced By

| Method | Notes |
|--------|-------|
| [MIM.M.010](../03-methods/MIM.M.010-backwards-design.md) | Stage 3: Plan Learning Experiences |
| ADDIE Phase 2-3 (Design + Development) | [MIM.FORM.002](../02-domain-entities/formalizations/MIM.FORM.002-addie-model.md) |

---

## Consumed By

| Consumer | How Used |
|----------|----------|
| [MIM.R.002](../02-domain-entities/02A-roles.md) | Instructor проводит занятие по плану |
| [MIM.R.001](../02-domain-entities/02A-roles.md) | Facilitator использует для структурирования дискуссии |
| [MIM.R.007](../02-domain-entities/02A-roles.md) | Navigator адаптирует план под индивидуального ученика |

---

## Existence Criteria (MANDATORY)

**How to verify this work product exists:**

- [ ] Указаны цели занятия (связаны с целями из MIM.WP.004)
- [ ] Выбраны методы обучения (из MIM.M.006-005) с обоснованием для аудитории
- [ ] Определена последовательность активностей с таймингом
- [ ] Доля практики ≥30% от общего времени (prevention of MIM.FM.007)
- [ ] Определён способ проверки достижения целей (связь с MIM.WP.005)

**If all criteria are met, the work product exists. If any criterion fails, it does not.**

---

## Structure

| Field | Type | Required? | Constraints |
|-------|------|-----------|-------------|
| Цели занятия | List | Yes | Из MIM.WP.004, глаголы Блума |
| Целевая аудитория | Reference | Yes | Возрастная группа (MIM.FORM.003) |
| Методы | List | Yes | MIM.M.* с обоснованием |
| Активности | Sequence | Yes | Теория / практика / рефлексия с таймингом |
| Материалы | List | No | Что подготовить заранее |
| Оценка | Reference | Yes | Ссылка на MIM.WP.005 или встроенная проверка |
| Длительность | Duration | Yes | Соответствует возрастной группе |

---

## Related Failure Modes

Common failures when this WP is absent or malformed:
- [MIM.FM.007](../05-failure-modes/MIM.FM.007-content-without-practice.md) — план без практических блоков
- [MIM.FM.004](../05-failure-modes/MIM.FM.004-lecture-equals-learning.md) — план = «прочитать лекцию 90 мин»

---

*Pack ID: MIM | SPF.SPEC.001 compliant*
