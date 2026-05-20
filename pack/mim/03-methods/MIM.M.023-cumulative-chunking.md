---
id: MIM.M.023
name: "Cumulative Chunking for Large Re-engineering"
kind: M (Method)
status: active
created: 2026-05-20
trust: hypothesis
revision_criterion: "Метод применить на реальном миграционном проекте (например, миграция legacy LMS на новую архитектуру) и сравнить с традиционным chunking (изолированные суб-проекты): даёт ли cumulative-вариант больше generalisation и меньше temporary interfaces."
related:
  see_also: [MIM.SOTA.001, MIM.D.026]
tags: [method, boro, re-engineering]
s2r_families: [F5]
---

# MIM.M.023 — Cumulative Chunking for Large Re-engineering

> Метод, извлечённый из BORO Methodology (Partridge, 1996+). Статус: **hypothesis** — требует эмпирической валидации в контексте применения.

---

# DP.M.095: Cumulative chunking — кумулятивный chunking больших проектов

## Обещание

Re-engineering или миграция большой системы выполняется как последовательность chunk-проектов, где **каждый последующий chunk включает scope всех предыдущих**. Каждый chunk компактифицируется через generalisation; широкий накопленный scope усиливает обнаружение общих паттернов без роста размера sub-project.

## Алгоритм

1. **Разбить** существующую систему на N chunks (по dependencies, по модулям, по информационным потокам — см. DP.M.010 wp-lifecycle для критериев).
2. **Запланировать порядок:** static data → transactions, независимые → зависимые.
3. **Chunk #1:** re-engineer изолированно, реализовать, ввести в продуктив. Подключить через temporary interface к остальной системе.
4. **Chunk #2:** scope = patterns(chunk #1) ∪ chunk #2. **Не** изолировать. Re-engineer объединённый scope — ищет generalisation между #1 и #2.
5. **Chunk #N:** scope = ∪(chunk #1..N). К моменту последнего chunk scope = вся система.
6. Каждый chunk, кроме финального, — **прототип** для следующего: документация ephemeral (см. DP.M.NNN ephemeral docs), модель ожидает refactor.

## Когда применять

- Система слишком велика для single-project re-engineering (man-years).
- Generalisation обещает значительный compaction (если паттерны в chunks похожи).
- Бизнес требует tangible progress между chunks (нельзя ждать до конца).

## Когда не применять

- Маленькая система — одно re-engineering эффективнее.
- Chunks не пересекаются по паттернам — нет повода объединять scope.
- Traditional environment без generalisation — кумулятивность только раздувает sub-projects.

## Шаги

| # | Что делает менеджер | Артефакт |
|---|---------------------|----------|
| 1 | Определить chunks по interface complexity + pattern similarity | chunk-карта |
| 2 | Установить порядок (static→transaction, independent→dependent) | sequence-plan |
| 3 | Re-engineer chunk #1 изолированно | business model #1 |
| 4 | На chunk #N — взять business model #1..N-1 как входной scope, добавить #N | business model #1..N |
| 5 | После каждого chunk — feedback в следующий (что generalised не так) | lessons-log |
| 6 | На последнем chunk — финализировать ВСЮ документацию | full docs |

## Связи

- [DP.M.010 WP Lifecycle](DP.M.010-wp-lifecycle.md) — chunks как РП с зависимостями
- [DP.SOTA.001 DDD Strategic](../06-sota/DP.SOTA.001-ddd-strategic.md) — bounded contexts как естественные chunks
- [DP.FM.014 Legacy Port Jump](../05-failure-modes/DP.FM.014-legacy-port-jump.md) — антипод: прыжок в новый дизайн без понимания legacy

## Пример из платформы

Миграция Aist бота: chunk #1 = consent + identity, chunk #2 = #1 + activity emitter, chunk #3 = #1+#2 + rewards. Каждый следующий выполняется на широком scope, выявляются shared patterns (например, RLS-изоляция между всеми тремя).
