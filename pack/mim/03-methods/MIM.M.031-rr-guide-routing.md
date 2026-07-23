---
id: MIM.M.031
name: Маршрутная таблица руководств программы РР
name_ru: Маршрутная таблица руководств программы РР
name_en: PR Program Guide Routing Table
title: Маршрутная таблица руководств программы РР (тип системы → дисциплина → руководство)
type: method
domain: mim
s2r_families: [F5, F6]
status: hypothesis
trust: hypothesis
revision_criterion: |
  Таблица — гипотеза, потому что:
  (а) все шесть index.md канонических руководств в `docs/docs/ru/professional/{firefighting,
  systems-thinking, methodology, systems-engineering, personality-engineering,
  systems-management}/` — стабы (только frontmatter с названием R1-R10, нет содержательного
  введения); реальный текст рассредоточен по подразделам каждого каталога;
  (б) каноническая модель MIM.M.030 даёт только три типа систем (personality/team/
  organization), но программа РР состоит из шести руководств, три из которых
  (рациональная работа, системное мышление, методология) являются базовыми/универсальными
  и не привязаны к одному типу систем — их роль определяется ступенью субъекта,
  а не типом изменяемой системы;
  (в) триггеры для каждого руководства составлены по названиям подразделов и общему
  скоупу программы РР (`docs/docs/ru/professional/index.md`), а не по эмпирике реальных
  запросов пилотов — после 10-20 реальных вызовов Менеджера оргразвития на разных
  типах запросов веса триггеров и распределение «универсальных» руководств между
  типами потребуют ревизии.

  Триггер пересмотра:
  - На 10 вызовах R31 > 30% запросов попадают в «универсальный» слой (не SI/SM/IL) →
    пересмотреть, является ли «универсальный» отдельным system_type или должен быть
    разнесён по существующим трём;
  - Появилось содержательное наполнение index.md руководств → пересоставить
    first_step_pointer'ы на основе явных вводных разделов;
  - Стабильно отказывают first_step_pointer'ы (раздел не открывается / содержит общий
    обзор без действия ≤30 мин) → заменить указатель.
mim_belonging_summary: |
  Маршрутная таблица — операционный артефакт роли DP.ROLE.063 Менеджер оргразвития,
  парный к классификатору MIM.M.030. Принадлежит PACK-MIM, потому что описывает связь
  между дисциплинами программы РР (домен МИМ) и типами систем-объектов изменения.
  Не относится к PACK-personal (не описывает состояние субъекта) и не относится к
  PACK-digital-platform (не описывает контракт/инфраструктуру, а только данные маршрутизации).
tags: [routing, org-development, rr-program, guide-selection, routing-table-name-pending-revision]
valid_from: 2026-05-31
schema_version: 1
wp: WP-377
related:
  used_by:
    - DP.SC.049     # Менеджер оргразвития — Шаг 3 маршрутизация
    - DP.ROLE.063   # Менеджер оргразвития (R31) — носитель роли
  uses:
    - MIM.M.030     # Классификатор типа системы — даёт system_type на входе
  see_also:
    - MIM.PRG.002   # Программа рабочего развития
---

# MIM.M.031 — Маршрутная таблица руководств программы РР

## Назначение

Маршрутная таблица для роли DP.ROLE.063 Менеджер оргразвития: на вход — результат классификатора MIM.M.030 (`system_type` ∈ {personality, team, organization}); на выход — конкретное руководство программы РР с указателем на раздел для первого шага ≤30 мин.

## Структура программы РР (источник: `docs/docs/ru/professional/index.md`)

Программа РР включает шесть канонических руководств, общее время ~480 ч:

| # | Руководство | Каталог | Часы | Источник | Слой |
|---|-------------|---------|------|----------|------|
| R1 | Рациональная работа (распожаризация) | `firefighting/` | 120 | П. Медведева, В. Агроскин, А. Лубенченко | базовый/универсальный |
| R5 | Системное мышление | `systems-thinking/` | 120 | А. Левенчук | универсальный |
| R7 | Методология | `methodology/` | 60 | А. Левенчук | универсальный |
| R8 | Системная инженерия | `systems-engineering/` | 60 | А. Левенчук | СИ (организация) |
| R9 | Инженерия личности (мастерства) | `personality-engineering/` | 60 | А. Левенчук | ИЛ (личность) |
| R10 | Системный менеджмент | `systems-management/` | 60 | А. Левенчук | СМ (команда) |

> **R2, R3, R4, R6** (моделирование коммуникации, рабочее моделирование, контрфактичность, системное моделирование) — поддерживающие, не входят в шесть канонических согласно `professional/index.md`.

---

## Маршрутная таблица

```yaml
# Слой 1: прямое соответствие system_type → дисциплина → руководство (три типа MIM.M.030)

- system_type: personality
  discipline: IL
  guide:
    title: "R9. Инженерия личности (мастерства)"
    path: docs/docs/ru/professional/personality-engineering/
    canonical_id: R9
    triggers:
      - "хочу изменить себя"
      - "прокрастинирую"
      - "хочу новые привычки"
      - "развитие мастерства"
      - "self-improvement"
      - "хочу преподавать / передавать опыт"
      - "построить свою практику обучения"
    first_step_pointer:
      section: introduction.md
      path: docs/docs/ru/professional/personality-engineering/introduction.md
      action_template: |
        Прочитать введение (~10 мин) → выбрать одну из практик каталога:
        teaching-practice / methodological-practice-how-to-teach / cultural-promotion-practice
        → завершить «examples-of-personal-engineering» как разогрев (15-20 мин).

- system_type: team
  discipline: SM
  guide:
    title: "R10. Системный менеджмент"
    path: docs/docs/ru/professional/systems-management/
    canonical_id: R10
    triggers:
      - "в команде хаос"
      - "роли не ясны"
      - "никто не отвечает"
      - "конфликты в команде"
      - "распределение ответственности"
      - "не понимают друг друга"
      - "тимлид без рычагов"
      - "руководство командой 3-10 человек"
    first_step_pointer:
      section: introduction.md
      path: docs/docs/ru/professional/systems-management/introduction.md
      action_template: |
        Прочитать введение (~10 мин) → перейти к «management-practices-and-manager-roles»
        (карта 7 практик менеджера) → выбрать практику-болевую точку (operational
        management / leadership / organizational-design) для второго шага (~20 мин).

- system_type: organization
  discipline: SI
  guide:
    title: "R8. Системная инженерия"
    path: docs/docs/ru/professional/systems-engineering/
    canonical_id: R8
    triggers:
      - "процессы разваливаются"
      - "масштабирование ломает"
      - "архитектура продукта"
      - "разделение инженерного труда"
      - "DevOps / CI-CD"
      - "evolutionary architecture"
      - "техдолг как системная проблема"
      - "10+ человек, есть структура"
    first_step_pointer:
      section: introduction.md
      path: docs/docs/ru/professional/systems-engineering/introduction.md
      action_template: |
        Прочитать введение (~10 мин) → если запрос про процесс работы — далее
        «engineering-process»; если про структуру системы — «evolutionary-architecture»;
        если про деление труда между инженерами — «arch-role-of-creator-engineer-and-the-
        division-of-engineering-labor» (~20 мин).

# Слой 2: базовые/универсальные руководства (любой system_type, выбираются по ступени
# субъекта или по характеру вторичного запроса)

- system_type: any   # ИСПОЛЬЗОВАТЬ КАК БАЗУ ПЕРЕД СПЕЦИАЛИЗИРОВАННЫМИ
  discipline: foundation_rational_work
  guide:
    title: "R1. Рациональная работа (распожаризация)"
    path: docs/docs/ru/professional/firefighting/
    canonical_id: R1
    triggers:
      - "рабочий хаос"
      - "постоянно тушу пожары"
      - "не справляюсь с входящим"
      - "выгорание"
      - "не вижу что важно"
      - "стиль работы хаотичный"
      - "хочу начать с базы"
    first_step_pointer:
      section: introduction.md
      path: docs/docs/ru/professional/firefighting/introduction.md
      action_template: |
        Прочитать «introduction.md» + «who-this-guide-is-not-for.md» (~10 мин) →
        выполнить «exercise-0.md» (стартовое упражнение ~15 мин) →
        запомнить «guide-to-productivity-factors.md» как чек-лист на неделю.
    when_to_use: |
      Первая дисциплина для любого нового субъекта программы РР независимо от system_type.
      Если ступень субъекта (cp.iwe из R28) < 3 — рекомендовать ДО специализированных
      руководств (СИ/СМ/ИЛ), потому что без распожаризации специализированные методы
      ложатся на горящий стиль и не приживаются.

- system_type: any
  discipline: foundation_systems_thinking
  guide:
    title: "R5. Системное мышление"
    path: docs/docs/ru/professional/systems-thinking/
    canonical_id: R5
    triggers:
      - "не вижу систему за частями"
      - "путаюсь в уровнях"
      - "интересы стейкхолдеров"
      - "что такое система"
      - "третье поколение системного подхода"
      - "хочу научиться различать"
    first_step_pointer:
      section: introduction.md
      path: docs/docs/ru/professional/systems-thinking/introduction.md
      action_template: |
        Прочитать «introduction.md» (~10 мин) → перейти к «our-version-of-systems-
        thinking-third-generation» (поколение 3, ~15 мин) → закрепить через
        «system-implementation-and-description» как первое различение реализация ≠
        описание.
    when_to_use: |
      Универсальный язык для всех трёх специализированных дисциплин (СИ/СМ/ИЛ).
      Рекомендовать параллельно с любой специализированной, если субъект на ступени
      cp.wld < 3 (мировоззрение). Самостоятельно — если запрос про различения / язык
      описания систем.

- system_type: any
  discipline: foundation_methodology
  guide:
    title: "R7. Методология"
    path: docs/docs/ru/professional/methodology/
    canonical_id: R7
    triggers:
      - "не знаю как выбирать метод"
      - "метод vs работа"
      - "разработка процессов"
      - "стратегия как теория"
      - "engineering processes"
      - "method as first-class object"
    first_step_pointer:
      section: introduction.md
      path: docs/docs/ru/professional/methodology/introduction.md
      action_template: |
        Прочитать «introduction.md» (~10 мин) → перейти к «method-as-a-first-class-
        object» (~15 мин) → закрепить через «methodology-as-a-fundamental-method-of-
        thinking».
    when_to_use: |
      Универсальный мета-уровень: выбор и развитие методов работы. Рекомендовать после
      того, как субъект освоил хотя бы одно из специализированных руководств (СИ/СМ/ИЛ)
      и сталкивается с задачей выбора между методами или их адаптации. Преждевременно
      на ступени cp.iwe < 3.
```

---

## Алгоритм маршрутизации

```python
def route(system_type: str, cp_iwe: int, request_text: str) -> dict:
    """
    Вход:
      system_type ∈ {personality, team, organization, ambiguous}
      cp_iwe — ступень субъекта по cp.iwe (от R28 Диагноста)
      request_text — исходный запрос (для триггер-matching на втором проходе)

    Выход:
      {primary_guide: ..., foundation_guide: ... | None, rationale: ...}
    """
    # Шаг A. Если ambiguous — не маршрутизировать (см. MIM.M.030 §margin < 3).
    if system_type == "ambiguous":
        return {"error": "needs_clarification"}

    # Шаг B. Специализированное руководство по типу.
    primary = {
        "personality": "R9 — Инженерия личности",
        "team":        "R10 — Системный менеджмент",
        "organization":"R8 — Системная инженерия",
    }[system_type]

    # Шаг C. Базовое руководство — если ступень низкая.
    foundation = None
    if cp_iwe < 3:
        foundation = "R1 — Рациональная работа (распожаризация)"
        # Сначала R1, потом primary — иначе primary ляжет на горящий стиль.

    # Шаг D. Если триггеры запроса прямо указывают на universal-дисциплину —
    # рекомендовать её как дополнение/замену.
    if matches_triggers(request_text, "R5"):
        foundation = "R5 — Системное мышление" if not foundation else foundation
    if matches_triggers(request_text, "R7") and cp_iwe >= 3:
        foundation = "R7 — Методология"

    return {
        "primary_guide": primary,
        "foundation_guide": foundation,
        "rationale": f"system_type={system_type}, cp.iwe={cp_iwe}",
    }
```

---

## Forces

_(Optional, WP-448 Ф10) Какие конкурирующие давления удерживает метод._

| Force | Tension |
|-------|---------|
| Специализация по system_type ↔ универсальные дисциплины поверх | Слой 1 маршрутизирует по типу системы (personality/team/organization), но Слой 2 явно накладывает базовые руководства (R1/R5/R7) поверх специализации по ступени субъекта — оба слоя должны сработать вместе, и Алгоритм маршрутизации явно кодирует их приоритет (Шаг C, Шаг D) |
| Стабильность маршрутной таблицы ↔ известная гипотетичность триггеров | Таблица уже используется в продакшене (DP.SC.049 Шаг 3), но `revision_criterion` прямо признаёт, что триггеры составлены по названиям подразделов, не по эмпирике реальных запросов — метод работает, зная о собственной непроверенности |
| R1 как обязательная база для низкой ступени ↔ мотивация субъекта на специализированную дисциплину | При `cp_iwe < 3` метод рекомендует сначала R1 (распожаризация), прежде чем специализированное руководство — но субъект, обратившийся с конкретной проблемой (например, «в команде хаос»), может хотеть сразу специализированное R10, а не базовое R1, которое кажется не относящимся к его запросу |

## Bias-Annotation _(tentative — trust: hypothesis, триггеры составлены по структуре программы, не по эмпирике реальных запросов)_

_(Optional, WP-448 Ф10) Какое систематическое искажение грозит практикующему._

| Bias | Direction of distortion |
|------|--------------------------|
| Triggers-matching воспринимается как надёжное измерение, а не как эвристика на непроверенных весах | Список триггеров-фраз для каждого руководства выглядит конкретным и исчерпывающим, но revision_criterion прямо признаёт: они составлены по общему скоупу программы, не по 10-20 реальным вызовам — практикующий, доверяющий точному совпадению фразы, рискует упустить, что распределение «универсальных» руководств между типами ещё не откалибровано |
| first_step_pointer считается рабочим без проверки актуальности index.md | Указатели ссылаются на конкретные разделы (`introduction.md`, `exercise-0.md`), но revision_criterion явно называет все шесть index.md «стабами» на момент написания — практикующий, слепо следующий action_template, может отправить субъекта на пустой или неполный раздел (см. FM.R4), не проверив её актуальность заранее |

## Failure modes

| ID | Условие | Поведение |
|----|---------|-----------|
| FM.R1 | `system_type == ambiguous` (margin < 3) | Не маршрутизировать. Возврат к MIM.M.030 §margin < 3 за уточнением. |
| FM.R2 | `cp.iwe` неизвестен (R28 не вызван) | Не маршрутизировать. Возврат к Шагу 2 DP.SC.049 §4. |
| FM.R3 | Запрос содержит сильные триггеры двух разных primary-руководств (например, личность + команда одновременно) | Рекомендовать оба, начать с того, что соответствует scores[dominant] из MIM.M.030. |
| FM.R4 | `first_step_pointer.path` не существует / раздел пустой | Откатиться на `path` каталога (`docs/.../<guide>/`) + интерактивный выбор подраздела с автором запроса. Лог в `learning.guide_routing_misses`. |

---

## Метрика и калибровка

Лог каждого вызова в `learning.guide_routing_decisions`:

```yaml
session_id: ...
subject_id: ...
input:
  system_type: personality | team | organization
  cp_iwe: 0..5
  request_text: "..."
output:
  primary_guide: R8 | R9 | R10
  foundation_guide: R1 | R5 | R7 | null
post_hoc_outcome: null | helpful | irrelevant | wrong_type
```

**Калибровка (период: 20 вызовов):**
- > 30% `wrong_type` или `irrelevant` → пересмотр триггеров (см. revision_criterion в frontmatter).
- > 20% случаев `FM.R4` (first_step_pointer не работает) → обновить указатели после содержательного наполнения index.md (внешняя зависимость: контент-канал `docs/docs/ru/professional/`).

---

## Связи

- **Используется в:** DP.SC.049 §4 (Менеджер оргразвития, Шаг 3 — маршрутизация).
- **Носитель:** DP.ROLE.063 (Менеджер оргразвития, R31).
- **Вход берёт от:** MIM.M.030 (Классификатор типа системы — даёт `system_type` + `scores` + `margin`).
- **Программа:** MIM.PRG.002 (Программа рабочего развития).
- **WP:** WP-377 (порождающий РП, Ф2.1).
- **Источник перечня руководств:** `docs/docs/ru/professional/index.md`.
