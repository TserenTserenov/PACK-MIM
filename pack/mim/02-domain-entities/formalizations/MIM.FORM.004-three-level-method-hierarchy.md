---
id: MIM.FORM.004
origin: EDU.FORM.004
name: Three-Level Method Hierarchy
status: active
s2r_families: [F5]
summary: "Трёхуровневая иерархия методов обучения: мета-принципы (когнитивная наука) → доменные методы (педагогические архитектуры) → контекстные техники (локальные приёмы)."
created: 2026-02-19
updated: 2026-03-22
related:
  - MIM.M.006  # Scaffolding — domain method
  - MIM.M.007  # PBL — domain method
  - MIM.M.011  # Retrieval Practice — meta-principle
  - MIM.M.012  # Spaced Repetition — meta-principle
  - MIM.D.019  # Содержание ≠ Методика
  - MIM.D.023  # Стиль обучения ≠ Уровень знаний
  - MIM.FORM.001  # Bloom's — used for calibrating all levels
---

# [MIM.FORM.004] Three-Level Method Hierarchy

## Definition

Трёхуровневая иерархия методов обучения — формализация, упорядочивающая
все методы по степени универсальности. Каждый уровень имеет свою область
применимости и evidence base.

## The Three Levels

```
Level 1: Meta-Principles (когнитивная наука)
    │    Работают ВСЕГДА, для ВСЕХ аудиторий
    │    Evidence: strong (мета-анализы, replicated)
    ↓
Level 2: Domain Methods (педагогические архитектуры)
    │    Работают для ОПРЕДЕЛЁННЫХ аудиторий/предметов
    │    Evidence: moderate-to-strong (контекстно-зависимые)
    ↓
Level 3: Context Techniques (локальные приёмы)
    │    Работают В КОНКРЕТНОЙ ситуации
    │    Evidence: local (experience-based, не generalized)
```

## Level 1: Meta-Principles

Основаны на когнитивной науке. Работают для всех возрастов, предметов,
форматов. Не зависят от контекста.

| Принцип | Суть | Effect Size | Источник |
|---------|------|-------------|----------|
| **Retrieval Practice** | Вспоминание > перечитывание | d=0.50 | Adesope et al. (2017) |
| **Spaced Repetition** | Распределение > концентрация | d=0.54 | Cepeda et al. (2006) |
| **Interleaving** | Чередование тем > блочное изучение | g=0.42 | Brunmair & Richter (2019) |
| **Feedback** | Обратная связь ускоряет обучение | d=0.70 | Hattie & Timperley (2007) |
| **Cognitive Load Management** | Не перегружать рабочую память | — | Sweller et al. (2019) CLT |
| **Desirable Difficulties** | Оптимальная трудность > комфорт | — | Bjork & Bjork (2011) |
| **Elaboration** | Связывание нового с известным | d=0.75 | Dunlosky et al. (2013) |

**Правило:** Мета-принципы применяются ВСЕГДА, независимо от предмета
или аудитории. Если метод обучения нарушает мета-принцип — метод ошибочен.

## Level 2: Domain Methods

Педагогические архитектуры, эффективные для определённых аудиторий
и предметных областей.

| Метод | Лучше всего для | Хуже всего для | Ссылка |
|-------|-----------------|----------------|--------|
| **Scaffolding** | Новички, сложные задачи | Эксперты (expertise reversal) | MIM.M.006 |
| **PBL** | Прикладные области (медицина, инженерия) | Абстрактные начальные знания | MIM.M.007 |
| **Case Method** | Менеджмент, право, бизнес | Точные науки (мало «кейсов») | MIM.M.008 |
| **Experiential Learning** | Навыки взаимодействия, лидерство | Формальные знания (математика) | MIM.M.009 |
| **Backwards Design** | Проектирование любых курсов | — (универсален, но сложнее для непрофессионалов) | MIM.M.010 |
| **Direct Instruction** | Новички, базовые навыки | Продвинутые (нужна автономия) | (общеизвестен) |

**Правило:** Доменные методы должны подчиняться мета-принципам Level 1.
Если PBL не включает retrieval practice и feedback — он неполон.

## Level 3: Context Techniques

Локальные приёмы, эффективные в конкретной ситуации. Не генерализуются.

| Техника | Контекст | Почему не Level 2 |
|---------|----------|-------------------|
| Think-Pair-Share | Лекция, 30+ человек | Зависит от размера группы и культуры |
| Jigsaw | Семинар, 10-25 человек | Зависит от делимости материала |
| Muddiest Point | Конец занятия | Формативный feedback, локальный формат |
| One-Minute Paper | Конец лекции | Локальный retrieval practice |
| Gallery Walk | Проектная работа | Зависит от физического пространства |

**Правило:** Context techniques — реализации мета-принципов и доменных
методов в конкретных условиях. Think-Pair-Share = retrieval practice
(Level 1) + facilitation (Level 2) в формате лекции для 30 человек (Level 3).

## Usage Rules

1. **Сверху вниз**: сначала проверь мета-принципы, затем выбери доменный
   метод, затем подбери контекстные техники
2. **Не путай уровни**: "retrieval practice не работает для моей аудитории"
   — ошибка (Level 1 работает всегда; возможно, неверно реализован на Level 3)
3. **Adaptation на Level 2-3**: адаптация под аудиторию происходит
   на уровнях 2 и 3, не на уровне 1
4. **Evidence соответствует уровню**: не требуй мета-анализов для Level 3
   техник; не принимай anecdotal evidence для Level 1

## Distinctions

| Часто путают | На самом деле |
|-------------|---------------|
| «Retrieval practice не подходит для детей» | Level 1 работает для всех; нужна адаптация формата (Level 3) |
| «PBL — лучший метод» | PBL — Level 2 (не для всех), должен включать Level 1 принципы |
| «Think-Pair-Share — метод обучения» | Think-Pair-Share — Level 3 техника, реализующая Level 1+2 |

## Parallel with ECO.D.007 (Human ↔ AI)

| Level | Человек | ИИ |
|-------|---------|----|
| Meta-principles | Spaced repetition, retrieval | Rehearsal, regularization |
| Domain methods | PBL, scaffolding | Curriculum learning, fine-tuning |
| Context techniques | Think-pair-share | Batch size tuning, prompt engineering |

## SoTA

- **Status**: `emerging` — иерархия как формализация новая (EDU Pack),
  но компоненты (каждый уровень) — established SoTA
- **Basis**: Dunlosky et al. (2013) evidence rankings; Hattie (2023)
  Visible Learning; Sweller et al. (2019) CLT; Merrill (2002)
  First Principles of Instruction
- **Revision criterion**: Если обнаружится, что мета-принципы контекстно-
  зависимы (т.е. Level 1 не универсален)

---

*Pack ID: MIM | SPF.SPEC.001 compliant*
