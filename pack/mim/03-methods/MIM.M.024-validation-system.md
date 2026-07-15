---
id: MIM.M.024
name: "Validation System — Operational Model Verification"
kind: M (Method)
status: active
created: 2026-05-20
trust: hypothesis
revision_criterion: "Применить метод на следующем доменном моделировании (например, при разработке нового Pack для domain X): построить validation system, наполнить representative sample, прогнать запросы/отчёты. Сравнить число обнаруженных ошибок модели с baseline (моделирование без validation system)."
related:
  see_also: [MIM.SOTA.001, MIM.D.026]
tags: [method, boro, re-engineering]
s2r_families: [F5]
---

# MIM.M.024 — Validation System — Operational Model Verification

> Метод, извлечённый из BORO Methodology (Partridge, 1996+). Статус: **hypothesis** — требует эмпирической валидации в контексте применения.

---

# MIM.M.024: Validation System — операционная проверка модели до реализации

## Обещание

Бизнес-модель (или доменная Pack-модель) переводится в рабочую БД, наполняется **представительной выборкой operational objects** из существующей системы, и проверяется через reports/queries **до** того, как ресурсы будут потрачены на production-реализацию. Inaccurate patterns обнаруживаются и фиксируются на дешёвой стадии.

## Принцип

Object-schema-визуализация модели **недостаточна** для контроля её корректности. Требуется операционный «touch-and-feel»: запросы, отчёты, обход данных. Только живая работа с данными выявляет, что модель неточно отражает реальность.

## Алгоритм

1. **Построить** validation DB по структуре модели (не обязательно production-tech; PC-database / SQLite достаточно).
2. **Мигрировать** representative sample operational data из существующей системы. Для маленьких файлов — всё. Для больших — sample.
3. **Загрузить** новые operational items, обнаруженные в моделировании (например, новые conceptual patterns).
4. **Построить** набор reports + ad-hoc queries, покрывающих ключевые сценарии использования.
5. **Прогнать** запросы, показать пользователям/экспертам. Зафиксировать всё, что «не работает».
6. **Итерировать** модель до устранения расхождений. Только после этого — production-build.

## Когда применять

- Domain modelling нового Pack'а или major-rework существующего.
- Перед запуском полноценного re-engineering project (фиксирует accuracy ДО затрат на build).
- При сомнении в корректности паттерна — быстрая проверка через operational sample.

## Когда не применять

- Trivial-модель (1-2 entity, очевидная семантика).
- Domain без существующей системы для миграции данных (тогда → mock-генерация).

## Шаги (для нашей платформы)

| # | Что | Артефакт |
|---|-----|----------|
| 1 | Поднять SQLite/Postgres-instance с предлагаемой схемой Pack | validation.db |
| 2 | Мигрировать sample (≥10% или 100 строк, что больше) из production / legacy системы | populated DB |
| 3 | Написать 5-10 типовых запросов / reports под expected usage | queries.sql |
| 4 | Run + review с экспертом домена | review-log.md |
| 5 | Зафиксировать расхождения, обновить Pack-сущности | updated Pack |
| 6 | Повторить, пока расхождения не уйдут | converged validation |

## Связи

- [DP.M.005 ArchGate](DP.M.005-archgate.md) — validation system как один из gate-чеклистов для domain-моделей
- [DP.M.012 Machine Check Postcondition](DP.M.012-machine-check-postcondition.md) — родственный паттерн (validation на postcondition-уровне; этот метод — на model-уровне)
- [DP.D.001 Объект ≠ Модель](../01-domain-contract/01B-distinctions.md) — validation system проверяет ровно это соответствие

## Пример из платформы

Перед merge нового Pack-домена (например, PACK-MIM) — построить SQLite-instance, загрузить семпл реальных учебных событий, прогнать query «выдать ступень мастерства по пользователю N». Если запрос даёт неправдоподобный ответ — Pack-модель имеет дефект, исправить ДО внедрения в production calculation.
