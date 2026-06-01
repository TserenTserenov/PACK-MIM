---
id: MIM.M.032
name: Competency Questions как Definition of Done
type: method
domain: MIM
status: draft
valid_from: 2026-05-27
source_session: peer-сессия 19 (use-ontology-engineering-in-packs, Тема 1)
pack_refs:
  - source: SPF.SPEC.002 (commit bad069b)
---

# MIM.M.032: Competency Questions как Definition of Done для Pack/онтологии

## Контекст

Pack / онтологию / доменную модель проверяют структурно — frontmatter, схема, синтаксис линтером. Это не отвечает на вопрос: «делает ли Pack то, для чего создан?» Competency Questions (CQ, 3-5 вопросов) закрывают этот gap как функциональная приёмка.

## Алгоритм

1. **Формализация CQ.** Автор Pack/онтологии формулирует 3-5 вопросов уровня «может ли система ответить на Q?» — конкретных, проверяемых на содержании Pack.
2. **Хранение.** CQ помещаются в раздел шаблона Pack (`00-pack-manifest.md` или отдельный `competency-questions.md`).
3. **Tier-gating.**
   - **Soft-gate** (warning) для legacy-Pack'ов — позволяет существующим Pack'ам мигрировать.
   - **Required** для новых Pack'ов — без CQ Pack не считается готовым.
4. **Reviewer-checkbox.** При DoD-review reviewer отмечает: каждый CQ имеет ответ в текущем содержании Pack'а. Не автолинтер — semantic answer требует человека.

## Граница применимости

- CQ — ручная DoD, **не** автолинтер. Ставить как разделы шаблона + reviewer-checkbox, **не** как CI-gate.
- Дешевле full OntoClean-аудита (требует онтолога-эксперта).
- Применимо к доменным моделям, knowledge graphs, BC в DDD, doc-as-code системам — везде, где «pass syntax checks» ≠ «fit for purpose».

## Источник

Peer-сессия 19 «use-ontology-engineering-in-packs» (2026-05-27), Тема 1. Зафиксировано в SPF.SPEC.002 (commit bad069b).
