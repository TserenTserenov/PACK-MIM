---
id: MIM.FM.011
name: Policy Treated as Resource
kind: FM (Failure Mode)
status: active
created: 2026-05-13
related:
  - MIM.M.015
  - MIM.FM.010
tags: [failure-mode, toc, policy-constraint, resource-constraint, misclassification]
s2r_families: [F6]
source: WP-313 Ф1 (TOC research, Schragenheim, Tendon TameFlow)
---

# MIM.FM.011 — Policy Treated as Resource

> Лечение системного ограничения (правило, политика, согласование) как ресурсного (нехватка людей, времени, инструментов).

## Summary

В knowledge work большинство bottleneck — policy constraints (правила, процессы, необходимость согласования), а не resource constraints (люди, время, деньги). Если классифицировать policy constraint как resource — применяется неправильный метод: добавляют ресурсы вместо того, чтобы менять правила. Результат: Elevation не даёт эффекта, bottleneck не устраняется.

## Как проявляется

- Нанимают людей, но скорость не растёт (constraint = процесс согласования, не люди)
- Покупают инструменты, но throughput не меняется (constraint = политика приоритизации)
- Bottleneck «перемещается» после каждой попытки Elevation (moving Herbie)
- Высокий utilization, но cycle time не падает (защитная мощность отсутствует, не constraint)
- >3 handover'а на единицу работы (process-mining сигнатура policy constraint)

## Диагностика (5 маркеров Policy Constraint)

1. **Перемещается**: bottleneck мигрировал между этапами 2+ раза
2. **Elevation не дала эффекта**: уже пробовали добавить ресурс — результата нет
3. **Текстовые маркеры**: «у нас принято», «требует согласования с», «всегда так делали», «SOP требует»
4. **Handover count >3** на единицу работы
5. **Cycle time variance высокая** (а не просто длинная), среднее непредсказуемо

## Диагностика (4 маркера Resource Constraint)

1. Bottleneck **стабилен** на одном этапе (не мигрирует)
2. Очередь **монотонно растёт** на конкретном этапе
3. **Один специалист/инструмент** в каждом handover
4. Utilization >85% **и** растущая очередь (а не только высокий utilization)

## Как устранить

- **Resource constraint** → Five Focusing Steps (Exploit → Subordinate → Elevate)
- **Policy constraint** → Evaporating Cloud (MIM.M.015): найти конфликтующие допущения, изменить правило

## Связи

- [MIM.M.015](../03-methods/MIM.M.015-evaporating-cloud.md) — EC — основной инструмент для policy constraints
- [MIM.FM.010](MIM.FM.010-elevate-before-subordinate.md) — часто возникают вместе: неверная классификация ведёт к Elevation без Subordinate

---

*Pack: MIM | Kind: FM | Source: WP-313 TOC research 2026-05-13*
