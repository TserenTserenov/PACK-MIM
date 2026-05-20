---
id: MIM.M.025
name: "Migration Translation Model — Formal Traceability"
kind: M (Method)
status: active
created: 2026-05-20
trust: hypothesis
revision_criterion: "На следующей миграции (например, перенос domain X из legacy в новую архитектуру) построить translation model с явными tuples. Сравнить число «потерянных в трансляции» паттернов с baseline-миграцией без формальных tuples."
related:
  see_also: [MIM.SOTA.001, MIM.D.026]
tags: [method, boro, re-engineering]
s2r_families: [F5]
---

# MIM.M.025 — Migration Translation Model — Formal Traceability

> Метод, извлечённый из BORO Methodology (Partridge, 1996+). Статус: **hypothesis** — требует эмпирической валидации в контексте применения.

---

# DP.M.097: Migration Translation Model — формальная трассируемость от business model к implemented system

## Обещание

Перевод бизнес-модели (или доменной Pack-модели) в реализацию формализован через **explicit translation tuples**: каждый объект бизнес-модели связан с объектом implementation model через явную тройку (business_object, translation_rule, system_object). Traceability возможна в обе стороны. Незаавторизованные изменения в реализации обнаруживаются автоматически.

## Принцип

Без формальной translation model системные аналитики / разработчики имеют тенденцию **«править» доменную модель** при реализации, не возвращая правки в источник. Бизнес-модель деградирует, реализация дрейфует от домена.

Формальный translation layer:
- делает translation видимым (артефакт, а не «в голове разработчика»);
- позволяет автоматическую проверку соответствия;
- запрещает unilateral модификации (только через обратный канал к domain modeller).

## Структура translation tuple

```
(business_object, translation_rule_id, system_object)
```

Где:
- **business_object** — сущность из domain-модели (Pack-entity, или класс бизнес-объектов)
- **translation_rule_id** — ссылка на правило трансляции (как именно)
- **system_object** — сущность из implementation (БД-таблица, Python-class, MCP-инструмент)

Расширения:
- Для operational data — extra layer `(existing_system_entity → translation_rule → business_object → translation_rule → target_system_entity)`.

## Алгоритм

1. **Зафиксировать** domain-модель (Pack-сущности frozen for migration).
2. **Зафиксировать** target system model (БД-схема, API-контракты).
3. **Построить** translation tuples: для каждой Pack-сущности — какой system-object её реализует.
4. **Записать** translation rules (например, «country.iso_code → countries.iso2», «events PascalCase → tables snake_case»).
5. **Автоматизировать** проверку: при изменении одной из моделей — diff на tuples. Изменения в реализации без соответствующего изменения в Pack → flag.
6. **Применить** к operational migration: tuples переиспользуются для миграции живых данных.

## Когда применять

- Migration project domain → implementation (например, перенос новой Pack-сущности в БД).
- Multi-implementation domain (одна доменная модель → разные стеки/представления).
- При высоком риске drift между Pack и кодом.

## Когда не применять

- Trivial 1-to-1 mapping (overkill).
- Domain в активной разработке — translation rules будут переписываться каждый день.

## Связи

- [DP.SOTA.012 Multi-Representation Architecture](../06-sota/DP.SOTA.012-multi-representation-architecture.md) — translation model как формализация multi-representation
- [DP.D.067 Card ≠ Append-only Event](../01-domain-contract/DP.D.067-card-vs-event.md) — translation tuples могут быть и card-формой, и event-stream-формой
- [DP.FM.014 Legacy Port Jump](../05-failure-modes/DP.FM.014-legacy-port-jump.md) — translation model заставляет понять legacy ДО прыжка в новый дизайн
- [DP.FM.030 Compliance Matrix Narrative Drift](../05-failure-modes/DP.FM.030-compliance-matrix-narrative-drift.md) — родственный паттерн drift, который ловит translation-tuples-проверка

## Пример из платформы

Миграция rewards-домена: Pack `DP.ECON.001 Points Engine` → Neon `rewards` БД. Translation tuples:
```
(POINTS_EVENT type='accrue', accrue-rule, rewards.points_events.amount > 0)
(POINTS_EVENT type='burn', burn-rule, rewards.points_events.amount < 0 + redemption_id)
```
Если в коде появится `type='refund'` без обновления Pack — translation-проверка укажет на drift.
