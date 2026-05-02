# Sanskrit Logic vs Neural Models: A Morphological Analysis

## 📌 Overview
This project compares a **rule-based symbolic system** with a **Large Language Model (LLM)** for identifying grammatical roles in Sanskrit.

Sanskrit allows flexible word order, so this study tests whether grammar can be determined using only **morphological suffixes (Vibhakti)** instead of position or meaning.

---

## 🎯 Research Question
Can a simple suffix-based system reliably identify grammatical roles in Sanskrit, and how does it compare to modern AI models under strict constraints?

---

## 🧠 Methodology

### 1. Dataset
- 100 manually annotated verses
- Each verse contains:
  - `text_split` (tokens)
  - `analysis` (true grammatical labels)

---

### 2. Symbolic Logic Engine
A rule-based parser using suffix detection:
- Assigns cases based on endings
- Handles ambiguity (e.g., neuter forms)
- Uses **no context or word order**

---

### 3. Scramble Experiment
- Word order of verses was randomized
- Created `scrambled_verses.json`

---

### 4. LLM Evaluation
- Tested using a controlled prompt
- Instructed to rely **only on morphology**

---

## 📊 Results

| Model | Natural Order | Scrambled Order |
|------|-------------|----------------|
| Symbolic Engine | ~88% | ~88% |
| LLM | High (~90%+) | Variable |

> The Δ (delta) in accuracy for the Symbolic Engine between natural and scrambled order was **0%**, demonstrating perfect structural consistency.

---

## 🔍 Key Findings

- The symbolic model is **order-independent**
- LLMs often:
  - use contextual knowledge
  - override explicit constraints
  - resolve ambiguity using meaning

> Even when constrained, LLMs incorporate latent knowledge beyond morphology.

---

## ⚖️ Interpretation

- **Symbolic systems**
  - deterministic
  - consistent
  - transparent

- **Neural models**
  - flexible
  - context-aware
  - rely on **probabilistic heuristics rather than strict constraint satisfaction**

---

## ⚠️ Limitations

- No Sandhi splitting
- Limited irregular forms
- Simplified verb handling
- Small dataset (100 verses)

---

## 🚀 Future Work

- Add Sandhi resolution
- Expand dataset
- Include syntactic (Karaka) analysis
- Develop a **hybrid neuro-symbolic system**

---
## Project Structure
sanskrit-logic-project/
├── data/
│ ├── raw/sanskrit_gold.json
│ └── processed/scrambled_verses.json
├── scripts/
│ ├── test.py
│ └── scramble.py
├── results/
│ └── comparison_table.csv
└── README.md

---

## 🧾 Conclusion

This project demonstrates that a symbolic system can achieve high accuracy (~88%) while remaining completely independent of word order.

In contrast, neural models, while powerful, may violate explicit constraints by relying on latent contextual knowledge.

---

## 👩‍💻 Author
**Khyati Chaurasia**  
**Project Type:** Computational Linguistics / Neuro-Symbolic AI Research

##This repository is currently private and will be made public upon acceptance of the research submission.
