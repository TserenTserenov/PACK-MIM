---
id: MIM.M.027
name: "Compacting in Object Modelling"
kind: M (Method)
status: active
created: 2026-05-20
trust: hypothesis
revision_criterion: "Опровергнуть на современных микросервисных архитектурах (где scope = количество сервисов, а compacting не наблюдается из-за bounded-context boundaries). Альтернатива: ограничить применимость domain-кором, не cross-context интеграцией."
related:
  see_also: [MIM.SOTA.001, MIM.D.026]
tags: [method, boro, re-engineering]
s2r_families: [F5]
---

# MIM.M.027 — Compacting in Object Modelling

> Метод, извлечённый из BORO Methodology (Partridge, 1996+). Статус: **hypothesis** — требует эмпирической валидации в контексте применения.

---

# MIM.M.027: Compacting in Object Modelling

## Аннотация

**Compacting** — эмпирически наблюдаемое свойство объектно-ориентированного моделирования: с ростом scope re-engineering'а модель не растёт по сложности, а наоборот, **уплотняется** — несколько паттернов обобщаются в один, более общий. Это противоположно поведению entity-моделирования, где сложность растёт сверх-линейно: каждый новый паттерн должен быть согласован со всеми существующими (harmonisation cost).

## Сравнительная характеристика

| Параметр | Entity Modelling | Object Modelling |
|----------|------------------|------------------|
| Размер при росте scope | Растёт сверх-линейно | Растёт sub-линейно, может локально уменьшаться |
| Стоимость нового паттерна | Harmonisation со всеми существующими | Возможность обобщения существующих |
| Re-use | Низкий (паттерны привязаны к контексту) | Высокий (объекты general → multi-context) |
| Эффект scope | Сложность ↑ | Compacting ↑ |

## Авторская модель (hypothesis)

Partridge утверждает, что compacting — следствие *более точных* и *более явных* паттернов в object paradigm:
- Greater **explicitness** — паттерн виден целиком, нет implicit отношений через attribute-сравнения.
- Increased **accuracy** — модель отражает структуру предметной области без искажений от технологии хранения.
- → как следствие — **higher re-usability**.

Аналогия с manufacturing engineering: повышение точности изготовления → возможность взаимозаменяемых частей → re-use (Prologue §4.1).

## Эмпирическая база

- Investment management system re-development (1987–1990) — securities back-office, ранее requiring multiple custom modules, после re-engineering обработала «new financial instruments and situations that no-one had thought of when the system was built» (Preface First Edition, «The benefits»).
- Shell Downstream Data Model (ISO 15926 family) — продолжение BORO-практики в process industry.

## Ограничения / возражения

- Не подтверждено на современных микросервисных архитектурах (где compacting блокируется bounded-context границами — каждый context имеет свой Ubiquitous Language).
- Утверждение «scope ↑ → simpler model» работает в пределах одной онтологической парадигмы; **между** парадигмами compacting не масштабируется (DDD Context Map).
- Trust = hypothesis: эмпирика 1990-х на одной отрасли (финансы) + одном консалтинговом контексте (BORO Solutions). Современная пере-валидация отсутствует.

## Когда учитывать

- При оценке альтернатив архитектурных подходов (ArchGate) — добавить вопрос: «Как ведёт себя модель с ростом scope?»
- При планировании bounded contexts — compacting работает **внутри** контекста, не между.
- При выборе между entity-first и object-first моделированием в early-stage проекте.

## Связи

- **MIM.M.026** Re-engineering via Reverse + Forward — compacting проявляется именно на Forward-стадии.
- **DP.D.063** Business Modelling ≠ System Modelling — compacting — свойство business model'и, не system model'и.
- **DP.SOTA.001** DDD Strategic — bounded contexts ограничивают зону compacting.
- **DP.SOTA.011** Coupling Model — coupling описывает связи, compacting описывает размер; ортогональные оси.
- **DP.SOTA.007** AI Ontology Engineering — если применять LLM как ontology engineer, compacting станет наблюдаемой метрикой quality.
