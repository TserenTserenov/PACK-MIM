---
id: MIM.M.013
type: method
name: "Spiral Curriculum (Спиральный учебный план)"
name_en: "Spiral Curriculum"
origin: EDU.M.008
s2r_families: [F5]
summary: "Метод организации учебного материала, при котором ключевые концепции повторно изучаются на возрастающей глубине (Bloom 0→5). 3 принципа Bruner: (1) тема посещается многократно, (2) сложность растёт с каждым посещением, (3) новое обучение явно связано со старым. Современные реализации: CPA (Singapore Math), Cosmic Education (Montessori), Mastery-based progression."
status: active
created: 2026-02-21
updated: 2026-03-22
related:
  - { id: "MIM.FORM.006", type: "uses", note: "TPM defines the depth scale (Bloom 0-5)" }
  - { id: "MIM.FORM.007", type: "implements", note: "PC generates programs using this method" }
  - { id: "MIM.M.006", type: "complements", note: "Scaffolding within each spiral turn" }
  - { id: "MIM.M.010", type: "uses", note: "Backwards Design for each spiral turn" }
  - { id: "MIM.M.011", type: "integrates", note: "Retrieval practice reinforces previous turns" }
  - { id: "MIM.M.012", type: "integrates", note: "Spaced repetition governs inter-turn intervals" }
  - { id: "MIM.D.024", type: "respects", note: "Near transfer within turns; far transfer only with explicit bridges" }
evidence:
  - "Bruner, J. (1960). The Process of Education — original spiral curriculum theory"
  - "Singapore Math CPA progression — international benchmark (MOE Syllabus 2025)"
  - "Montessori Cosmic Education (AMS, 2024) — 5-year longitudinal RCT: delayed benefits for mathematical problem-solving (Nature Scientific Reports, 2025)"
  - "P4C meta-analysis: g=0.59 (MDPI, 2025) — spiral questioning produces strong reasoning gains"
  - "Metacognition interventions: g=0.48 (Springer Metacognition and Learning, 2025)"
  - "BC K-12 Learning Progressions — proficiency continuum framework"
---

# MIM.M.013 — Spiral Curriculum (Спиральный учебный план)

## Определение

Метод организации учебной программы, при котором ключевые концепции (принципы мышления ZP + FPF) повторно изучаются через запланированные интервалы, каждый раз на возрастающей глубине (Bloom 0→5) и в новом контексте (доменная ротация).

## Три принципа Bruner (1960)

1. **Повторное посещение:** тема изучается многократно на протяжении всей программы
2. **Рост сложности:** каждое посещение — на более глубоком когнитивном уровне (Bloom)
3. **Связывание:** новое обучение ЯВНО связано со старым («Помнишь, как…? Теперь…»)

## Входы

| Вход | Описание | Источник |
|------|---------|---------|
| Целевой принцип | Какой принцип (ZP.*, FPF.*) | Профиль ученика / MIM.R.009 |
| Текущая глубина | Где ученик сейчас (0-5) | MIM.WP.007 |
| Целевая глубина | Куда идём на этом витке | Текущая + 1 |
| Контекст/домен | В каком домене будем изучать | Правило R6 из MIM.FORM.007 |
| Предшествующий опыт | Что ученик уже делал с этим принципом | Learning Progression Map |

## Выходы

| Выход | Описание |
|-------|---------|
| Учебная единица | Конкретное задание для одного витка (unit schema из MIM.FORM.007) |
| Bridge-фраза | Явная связь с предыдущим витком |
| Assessment | Критерии проверки (can-do утверждения для целевой глубины) |
| Updated Map | Обновлённая Learning Progression Map |

## Алгоритм применения

```
1. Определи текущую глубину ученика по принципу (MIM.WP.007)
2. Выбери принцип для текущего витка (стратегия: breadth-first или bottleneck-first)
3. Определи Bloom-цель для следующей глубины (depth+1)
4. Выбери домен (правило R6: не повторяй домен предыдущего витка!)
5. Сформулируй bridge: «Помнишь, как мы [предыдущий виток]? Теперь…»
6. Спроектируй задание (Backwards Design: цель → оценка → активность)
7. Встрой retrieval practice: повторение ключевых идей предыдущих витков
8. Проведи занятие
9. Оцени: может ли ученик выполнить can-do утверждения глубины?
10. Обнови Learning Progression Map
```

## Три паттерна спирали

### Паттерн 1: Bloom-спираль (основной)

Каждый виток целит в следующую глубину Bloom:
```
Глубина 1 → Remember: узнай принцип
Глубина 2 → Understand: объясни своими словами
Глубина 3 → Apply: примени к новой ситуации
Глубина 4 → Analyze: найди нарушение
Глубина 5 → Create: создай систему на принципе
```

### Паттерн 2: CPA-спираль (Singapore Math)

Каждый виток меняет модальность представления:
```
Виток A → Concrete: физические объекты, манипуляции руками
Виток B → Pictorial: схемы, диаграммы, визуальные модели
Виток C → Abstract: формулы, символы, формальные определения
```

### Паттерн 3: Cosmic-спираль (Montessori)

Каждый виток расширяет контекст:
```
Виток 1 → Я: как принцип работает в моей жизни
Виток 2 → Семья/класс: как принцип работает в группе
Виток 3 → Общество: как принцип работает в городе/стране
Виток 4 → Мир: как принцип работает в природе/науке
Виток 5 → Универсальное: как принцип работает ВЕЗДЕ
```

## Типичные ошибки

1. **Повторение без углубления.** Если виток 2 = та же глубина Bloom, что и виток 1, это не спираль — это повторение. Каждый виток ОБЯЗАН быть глубже.
2. **Отсутствие bridge.** Без явной фразы-связки ученик не видит преемственности. «Это новая тема» — антипаттерн. Правильно: «Помнишь, как мы…?»
3. **Один домен на все витки.** Если ZP.1 изучается только на примерах из математики, ученик не увидит его транс-дисциплинарность. Правило R6: сменяй домен.
4. **Пропуск retrieval practice.** Без активного припоминания предыдущих витков знание не интегрируется. Начало каждого занятия = 2-минутный recall предыдущего.

## Кому подходит

Подходит ВСЕМ возрастам и глубинам. Spiral Curriculum — мета-метод, совместимый с любым другим методом из PACK-MIM (scaffolding, PBL, case method внутри витка). Форма витка адаптируется под когнитивные ограничения ученика (MIM.FORM.006 → таблица форм).

---

*Последнее обновление: 2026-03-22*
