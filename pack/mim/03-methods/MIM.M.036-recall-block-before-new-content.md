---
id: MIM.M.036
name: "Recall Block Before New Content"
status: active
s2r_families: [F5]
summary: >
  Design pattern for AI-generated learning guides: insert a 2-3 concept recall
  block at the start of new content, auto-populated from previous session
  metadata. Activates spaced retrieval practice without manual annotation.
sota: current
created: 2026-07-07
updated: 2026-07-07
source: "WP-149 personal guide daily render cycle"
related:
  uses:
    - MIM.M.011  # Retrieval Practice — cognitive mechanism
    - MIM.M.012  # Spaced Repetition — scheduling principle
  synergy_with:
    - MIM.M.011
    - MIM.M.012
---

## Definition

Recall Block Before New Content — педагогический design pattern: перед
началом нового учебного материала предъявить 2-3 вопроса/задания на
активное припоминание понятий из предыдущих сессий.

В AI-генерируемых руководствах блок собирается автоматически из метаданных
предыдущих рендеров (какие понятия изучались вчера/позавчера) — ручная
разметка не требуется.

## Purpose

Запустить механизм spaced retrieval practice (MIM.M.011 + MIM.M.012) в
начале каждой сессии без дополнительных усилий автора курса или участника.

## Distinction from MIM.M.011 Implementation Patterns

MIM.M.011 описывает «low-stakes quiz в начале занятия» как один из паттернов.
MIM.M.036 уточняет три дополнительных инварианта:

1. **Контент:** только понятия из предыдущего материала (retrieval cues ←
   previous render metadata), не новый материал.
2. **Позиционирование:** ДО нового контента (не «в начале» как заголовок
   секции — до первого нового концепта сессии).
3. **Автогенерация:** в AI-driven системах — из machine-readable метаданных,
   не ручная разметка.

## Inputs

| Input | Description |
|-------|-------------|
| Метаданные предыдущих рендеров | Список понятий из последних N сессий |
| Правило выборки | Сколько понятий, насколько «старых» (1 день / 3 дня / неделя) |
| Шаблон вопроса | Формат rappel-вопроса («Что такое X?», «Чем X отличается от Y?») |

## Outputs

| Output | Description |
|--------|-------------|
| Recall block | 2-3 вопроса на припоминание в начале руководства/урока |
| Спейсинг сигнал | Понятие «получило повторение» → обновляется в метаданных |

## Evidence Strength

**Strong (inherited from MIM.M.011 + MIM.M.012).** Эффект тестирования
(d=0.50) и эффект интервального повторения (d≥0.46) — два из наиболее
воспроизводимых результатов когнитивной науки.

## When to Apply

- AI-generated daily/weekly learning guides с циклическим рендером
- Системы с machine-readable метаданными предыдущих сессий
- Любой последовательный курс с кумулятивным контентом

## Failure Modes

| Failure Mode | Description |
|-------------|-------------|
| Recall слишком давний | Понятия из 3+ недель назад без промежуточного повторения → failure to recall, демотивация |
| Recall = preview нового | Вставлен не предыдущий материал, а анонс нового → нет retrieval cue, только подсказка |
| Нет feedback | Вопрос задан, правильный ответ не показан после → закрепляет ошибки (MIM.FM.FM.001) |
