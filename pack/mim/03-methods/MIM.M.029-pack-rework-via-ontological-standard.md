---
id: MIM.M.029
title: Pack rework через онтологический стандарт
type: method
domain: mim
status: hypothesis
trust: hypothesis
revision_criterion: если 2-й случай применения (UFO/DOLCE/4D к другому Pack) даст менее 50% переносимого материала — пересмотреть как «частный метод BORO-rework»
tags: [pack-engineering, ontology, rework, governance]
valid_from: 2026-05-20
schema_version: 1
---

# MIM.M.029 — Pack rework через онтологический стандарт

## Описание

Rework существующего Pack-знания = применение канонического онтологического стандарта (BORO, UFO, DOLCE, 4D) к уже описанным сущностям. Не переписывание содержания, а formal grounding задним числом: существующие методы/различения/SOTA получают онтологическую базу через стандарт.

## Вход

- Pack с N ad-hoc сущностями (методы, различения без явной онтологической основы)
- Выбранный онтологический стандарт (BORO / UFO / DOLCE / 4D)

## Выход

- Cross-pack alignment: сущности нескольких связанных Pack получают согласованную онтологическую базу
- `trust: hypothesis` + `revision_criterion` на каждой переоформленной сущности
- SOTA-аннотация эволюции парадигм (опционально)

## Алгоритм

1. Выбрать стандарт — критерий: покрывает ли парадигмы, использованные в Pack (Substance/Entity/Object для BORO)?
2. Sweep existing entities — список ad-hoc формализаций
3. Map: каждой сущности — категория стандарта (Object/Type/Tuple/...)
4. Refactor in-place — frontmatter + body содержат категорию + revision_criterion
5. Cross-pack alignment — связанные Pack (personal, digital-platform) обновить синхронно
6. Add SOTA-annotation paradigm-history (если стандарт сам — эволюция)

## Критерий применимости

«Есть ли в Pack сущность, описанная ad-hoc, без явной онтологической базы?» Да → кандидат на rework. Особенно полезно при cross-pack drift, когда родственные Pack описывают одну онтологическую территорию через несовместимые понятия.

## Failure mode без метода

Ad-hoc Pack-сущности накапливают drift: один Pack использует «Object», другой «Сущность», третий «Концепт» — без формального соответствия. При cross-pack reasoning возникает confusion. Без онтологического стандарта rework сводится к переписыванию имён, не к grounding.

## Применимо к

- Mature Pack'и с ≥30 ad-hoc сущностями
- Cross-pack alignment (≥2 связанных Pack)
- Подготовка Pack к публикации (внешний reader нуждается в онтологической базе)

## Прецедент

WP-345 Ф-B (2026-05-20): BORO применён к PACK-MIM, PACK-personal, PACK-digital-platform. Артефакты: MIM.M.023-027 + MIM.D.026-031 + MIM.SOTA.001 + DP.SOTA.024-025 + PACK-personal BORO-derived FMs.

## Связи

- **MIM.SOTA.001** — paradigm history (Substance → Entity → Object) как пример SOTA-annotation
- **DP.M.094** (dual-signal-ritual-gate) — другой governance-method для Pack-quality
