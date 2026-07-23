---
id: MIM.M.011
name: Retrieval Practice
origin: EDU.M.006
status: active
s2r_families: [F5]
summary: >
  Strengthening memory and understanding by actively recalling information
  rather than passively re-reading. One of the most evidence-based methods
  in cognitive science (d=0.50).
sota: current
created: 2026-02-19
updated: 2026-03-22
related:
  produces:
    - MIM.WP.005  # Assessment rubric can double as retrieval practice
  uses:
    - MIM.D.023  # Prior knowledge level determines retrieval difficulty
    - MIM.D.018  # Tests knowledge AND skill retention
  fails_with:
    - MIM.FM.004  # Retrieval practice is the antidote to "lecture = learning"
    - MIM.FM.007  # Content without practice — retrieval is active practice
  synergy_with:
    - MIM.M.012  # Spaced Repetition — retrieval + spacing = maximum effect
---

## Definition

Retrieval Practice — метод обучения, при котором ученик активно
извлекает информацию из памяти (вспоминает), а не пассивно перечитывает
или переслушивает материал. Каждый акт успешного припоминания укрепляет
связи в памяти сильнее, чем повторное чтение того же материала.

Известен также как "testing effect" (эффект тестирования): тестирование
само по себе является обучением, а не только его измерением.

## Purpose

Перевести знания из пассивного «узнавания» (recognition) в активное
«припоминание» (recall), что обеспечивает значительно более прочное
и переносимое обучение.

## Inputs

| Input | Description |
|-------|-------------|
| Изученный материал | Содержание, которое ученик ранее встречал |
| Retrieval cues | Вопросы, подсказки, задания, требующие припоминания |
| Обратная связь | Правильный ответ после попытки припоминания |

## Outputs

| Output | Description |
|--------|-------------|
| Укреплённая память | Более прочное и долговременное запоминание |
| Выявленные пробелы | Области, где ученик не может вспомнить = зоны для повторного изучения |
| Метакогнитивная калибровка | Ученик точнее оценивает, что знает и чего не знает |

## Evidence Strength

**Strong.** Один из наиболее воспроизводимых эффектов в когнитивной науке.

| Источник | Результат |
|----------|-----------|
| Roediger & Karpicke (2006) | Testing effect: retrieval > re-reading для долговременного запоминания |
| Dunlosky et al. (2013) | Rated "high utility" — одна из 2 стратегий из 10 с высшей оценкой |
| Effect size | d = 0.50 (мета-анализ, Adesope et al., 2017) |
| Rowland (2014) | Мета-анализ 159 исследований: устойчивый эффект |

## Roles Involved

- **Докладчик (MIM.R.002):** Проектирует retrieval-задания, обеспечивает
  обратную связь.
- **Instructional Designer (MIM.R.008):** Встраивает retrieval practice
  в структуру курса (quiz, flashcards, practice tests).

## Key Distinctions

- **MIM.D.023 Стиль обучения ≠ Уровень знаний.** Сложность retrieval
  заданий должна учитывать уровень предварительных знаний, а не
  «стиль обучения».
- **MIM.D.017 Формативное ≠ Суммативное.** Retrieval practice — это
  формативное оценивание: цель не в оценке, а в укреплении знаний.

## Forces

_(Optional, WP-448 Ф10) Какие конкурирующие давления удерживает метод._

| Force | Tension |
|-------|---------|
| Трудность припоминания ↔ успешность попытки | Retrieval работает сильнее, когда припоминание требует усилия (desirable difficulty), но слишком лёгкое задание скатывается в узнавание (FM.002), а слишком трудное без опоры на предзнание даёт только фрустрацию без выигрыша для памяти |
| Формативная цель ↔ ощущение оценивания | Метод по замыслу формативный — не про оценку, а про укрепление знаний (MIM.D.017) — но любая форма теста (quiz, practice test) естественно ощущается учеником как оценивание, что может сместить его поведение от честного припоминания к угадыванию ответа, который «зачтут» |
| Фактическое припоминание ↔ уровень применения | Реализовать retrieval факта (Level 1 Bloom) технически проще, чем сконструировать задание на припоминание применения/анализа — отсюда системный риск скатиться к FM.003, даже когда цель курса выше уровня фактов |

## Synergy with Spaced Repetition

Retrieval Practice + Spaced Repetition (MIM.M.012) = максимальный эффект.
Извлечение из памяти через увеличивающиеся интервалы — «золотой стандарт»
запоминания в когнитивной науке.

## Implementation Patterns

| Паттерн | Описание | Когда использовать |
|---------|----------|--------------------|
| Low-stakes quiz | Короткий тест без оценки в начале занятия | Каждое занятие |
| Think-pair-share | Вспомни → обсуди с соседом → расскажи группе | Лекции, семинары |
| Flashcards | Карточки с вопросом и ответом (Anki, Quizlet) | Самостоятельное обучение |
| Brain dump | Написать всё, что помнишь по теме, за 5 мин | Начало занятия |
| Practice test | Полный тест без оценки, с обратной связью | Перед суммативным экзаменом |

## Bias-Annotation

_(Optional, WP-448 Ф10) Какое систематическое искажение грозит практикующему._

| Bias | Direction of distortion |
|------|--------------------------|
| Узнавание маскируется под припоминание | Внимание проектировщика заданий незаметно съезжает к формату multiple-choice (узнавание правильного варианта среди предложенных) вместо открытого припоминания — задание выглядит как retrieval practice, но не создаёт нужного эффекта (FM.002 назван прямо в самом методе) |
| Метрика лёгкости замера подменяет метрику эффекта | Фактические вопросы (Level 1 Bloom) проще составить и проверить автоматически, чем задания на применение/анализ — практика системно смещается к тому, что легче измерить, а не к тому, что даёт максимальный эффект (Synergy с MIM.M.012 требует именно вдумчивого, не только частого, припоминания) |

## Failure Modes

| ID | Failure Mode | Description |
|----|-------------|-------------|
| FM.001 | Без обратной связи | Retrieval без feedback может закреплять ошибки |
| FM.002 | Слишком лёгкий retrieval | Узнавание (recognition) вместо припоминания (recall) — не даёт эффекта |
| FM.003 | Только фактическое | Retrieval только фактов (Level 1 Bloom) без retrieval на уровне применения/анализа |

## SoTA Status

**Status:** current

**Basis:**
- Roediger, H.L. & Karpicke, J.D. (2006). "Test-Enhanced Learning."
  *Psychological Science*, 17(3), 249-255.
- Dunlosky, J. et al. (2013). "Improving Students' Learning With Effective
  Learning Techniques." *Psychological Science in the Public Interest*, 14(1).
- Adesope, O. et al. (2017). Meta-analysis: d = 0.50 across 272 studies.

**Notes:** Retrieval practice — один из двух методов с рейтингом "high utility"
по Dunlosky et al. (2013), наряду со Spaced Repetition.

**Revision criterion:** Если появятся данные, что активное припоминание
не превосходит пассивное перечитывание для долговременного запоминания.

---

*Pack ID: MIM | SPF.SPEC.001 compliant*
