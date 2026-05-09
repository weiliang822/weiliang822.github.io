---
permalink: /
title: "Qingzhuo Wang"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

## About Me

I am a first-year M.S. student in Computer Science and Technology at [Tongji University](https://www.tongji.edu.cn), supervised by Associate Professor [Wen Shen](https://tongji.teacher.360eol.com/teacherBasic/preview?teacherId=30173) and Professor [Zhihua Wei](https://tongji.teacher.360eol.com/teacherBasic/preview?teacherType=&teacherId=13253). I received my B.Eng. in Computer Science and Technology from Tongji University in 2025.

My research interests lie in **LLM post-training**, **knowledge distillation**, and **agentic reinforcement learning**.

---

## Publications

### First-Author

- **A Unified Approach to Interpreting Knowledge Distillation for Large Language Models via Interactions**  
  **Qingzhuo Wang**\*, Ruiyang Qin\*, Zhenxin Qin, Wen Shen, Zhihua Wei  
  *ICML 2026*   &nbsp; [\[URL\]](https://icml.cc/virtual/2026/poster/65719)  
  <small>TL;DR: We interpret KD from a game-theoretic interaction perspective, revealing that the essence of distillation is the sparsification of interactions — student models selectively inherit salient simple interactions from teachers while compressing complex ones. We further propose the CIP loss to explicitly enforce this sparsification.</small>

- **Multilingual Safety Alignment via Self-Distillation**  
  Ruiyang Qin\*, **Qingzhuo Wang**\*, Dongrui Liu, Qiang Li, Zhihua Wei, Wen Shen  
  *arXiv 2026* &nbsp; [\[URL\]](https://arxiv.org/abs/2605.02971)  
  <small>TL;DR: We propose an on-policy self-distillation method that transfers the model's own safety capabilities from high-resource languages to low-resource ones, eliminating the dependency on high-quality human-annotated safety data while improving both in-distribution and out-of-distribution multilingual safety.</small>

- **TME-PSR: Time-aware, Multi-interest, and Explanation Personalization for Sequential Recommendation**  
  **Qingzhuo Wang**, Leilei Wen, Juntao Chen, Kunyu Peng, Ruiyang Qin, Zhihua Wei, Wen Shen  
  *arXiv 2026* &nbsp; [\[URL\]](https://arxiv.org/abs/2604.09439)  
  <small>TL;DR: A unified framework that simultaneously introduces time-aware personalization, multi-interest modeling, and explanation personalization into sequential recommendation, addressing the lack of comprehensive personalization in existing methods.</small>

### Co-Author

- **Evaluating and Explaining Prompt Sensitivity of LLMs Using Interactions**  
  Ruiyang Qin, **Qingzhuo Wang**, Tian Wang, Zhihua Wei, Wen Shen  
  *ICML 2026* &nbsp; [\[URL\]](https://icml.cc/virtual/2026/poster/65089)  
  <small>TL;DR: We introduce game-theoretic interactions as a fine-grained tool to analyze prompt sensitivity, proposing the IPS metric and revealing that even when outputs stay the same, most internal interactions are unstable — and that factors like SFT and scale reduce sensitivity by stabilizing low-order interactions.</small>

- **Mitigating Action-Relation Hallucinations in LVLMs via Relation-aware Visual Enhancement**  
  Zhenxin Qin, Qiang Li, **Qingzhuo Wang**, Ruiyang Qin, Zhihua Wei, Wen Shen  
  *ACL 2026*  
  <small>TL;DR: We define the Action-Relation Sensitivity (ARS) score to locate attention heads sensitive to action-relation changes, and propose Relation-aware Visual Enhancement (RVE), a training-free method that enhances attention to action-relevant image regions to mitigate action-relation hallucinations.</small>

- **Understanding and Defending VLM Jailbreaks via Jailbreak-Related Representation Shift**  
  Zhihua Wei, Qiang Li, Jian Ruan, Zhenxin Qin, Leilei Wen, Ruiyang Qin, **Qingzhuo Wang**, Dongrui Liu, Wen Shen  
  *arXiv 2026* &nbsp; [\[URL\]](https://arxiv.org/abs/2603.17372)  
  <small>TL;DR: We show that VLMs recognize harmful intent but enter a distinct jailbreak state rather than refusing, driven by a jailbreak-related representation shift induced by visual inputs. We propose JRS-Rem, a training-free defense that removes this shift at inference time.</small>

---

## Internships

**WeQuant** &mdash; Quant Researcher &nbsp; *Mar. 2025 &ndash; Oct. 2025*

- Independently led the full lifecycle of a low-frequency A-share Alpha strategy, covering data ingestion/cleaning, label construction, factor engineering, model training & prediction, and order-generation backtesting.
- Built multi-source factors (high-frequency aggregation, low-frequency price-volume, Wind, fundamentals, and risk-style), performed missing/lagged data repair, future-data auditing, correlation & volatility screening, and improved model stability via sample weighting, clip-scale, and early stopping. Backtest **rankIC 0.16**, Exceeding expectations **0.019%**.
- Built a reusable live-trading framework; the strategy ran continuously from Jun. to Oct. 2025. Live performance: **cumulative return 26.5%, cumulative excess 6.1%, max drawdown 6.6%, Sharpe 3.7, IR 1.07**.

**Bilibili** &mdash; Algorithm Engineer &nbsp; *Jul. 2024 &ndash; Dec. 2024*

- Designed and launched a redirect recall strategy targeting users who had wishlisted or saved items, significantly improving post-engagement conversion: **Orders +33.13%, GMV +113.14%, GPM +112.94%**.
- Trained product image and title embeddings via CNCLIP and integrated Faiss for online similarity filtering to reduce repetitive product exposure in feeds; maintained business metrics while improving diversity: avg. 4th-level category exposure **4.92 &rarr; 4.96**, IP exposure **5.80 &rarr; 5.85**.
- Applied isotonic regression with Bayesian smoothing for ranking model calibration, improving **COPC 0.91 &rarr; 1.01** and driving **Orders +5%, GMV +13%, GPM +13%**.
