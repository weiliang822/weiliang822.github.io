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
  <small>TL;DR: We identify interaction sparsification as a common pattern across knowledge distillation methods. Complex Interaction Penalty (CIP) explicitly promotes sparsity in complex interactions and improves distillation performance.</small>

- **Multilingual Safety Alignment via Self-Distillation**  
  Ruiyang Qin\*, **Qingzhuo Wang**\*, Dongrui Liu, Qiang Li, Zhihua Wei, Wen Shen  
  *NeurIPS 2026* &nbsp; [\[URL\]](https://arxiv.org/abs/2605.02971)  
  <small>TL;DR: Multilingual Self-Distillation (MSD) transfers safety from high-resource to low-resource languages using multilingual queries without external response data. It supports on-policy and off-policy training, with Dual-Perspective Safety Weighting (DPSW) emphasizing safety-critical tokens.</small>

- **TME-PSR: Time-aware, Multi-interest, and Explanation Personalization for Sequential Recommendation**  
  **Qingzhuo Wang**, Leilei Wen, Juntao Chen, Kunyu Peng, Ruiyang Qin, Zhihua Wei, Wen Shen  
  *arXiv 2026* &nbsp; [\[URL\]](https://arxiv.org/abs/2604.09439)  
  <small>TL;DR: TME-PSR jointly models individual temporal rhythms, fine-grained interests, and personalized alignment between recommendations and explanations. It improves recommendation accuracy and explanation quality with lower computational cost on the evaluated datasets.</small>

### Co-Author

- **Bridging the Gap Between Harmfulness Belief and Refusal Behavior for Safety Alignment**  
  Lu Zhang, Chen Feng, **Qingzhuo Wang**, Wen Shen, Zhihua Wei  
  *NeurIPS 2026* &nbsp; [\[Details\]](/publication/2026-09-25-bridging-harmfulness-refusal)  
  <small>TL;DR: Bridging Harmfulness and Refusal (BHR) trains a LoRA adapter to carry harmfulness information from the instruction to the response-start position. Belief and belief-gated refusal losses improve jailbreak robustness while limiting over-refusal and preserving general capabilities.</small>

- **Evaluating and Explaining Prompt Sensitivity of LLMs Using Interactions**  
  Ruiyang Qin, **Qingzhuo Wang**, Tian Wang, Zhihua Wei, Wen Shen  
  *ICML 2026* &nbsp; [\[URL\]](https://icml.cc/virtual/2026/poster/65089)  
  <small>TL;DR: Interaction-based Prompt Sensitivity (IPS) reveals changes in LLM inference patterns that output-level metrics miss. Across 50 models, supervised fine-tuning, larger scale, dense architectures, and few-shot learning primarily stabilize low-order interactions.</small>

- **Mitigating Action-Relation Hallucinations in LVLMs via Relation-aware Visual Enhancement**  
  Zhenxin Qin, Qiang Li, **Qingzhuo Wang**, Ruiyang Qin, Zhihua Wei, Wen Shen  
  *ACL 2026* &nbsp; [\[URL\]](https://arxiv.org/abs/2605.11808)  
  <small>TL;DR: Action-Relation Sensitivity (ARS) identifies attention heads that localize action-relevant image regions. Relation-aware Visual Enhancement (RVE) boosts attention to these regions without additional training, reducing action-relation hallucinations with negligible inference overhead.</small>

- **Understanding and Defending VLM Jailbreaks via Jailbreak-Related Representation Shift**  
  Zhihua Wei, Qiang Li, Jian Ruan, Zhenxin Qin, Leilei Wen, Ruiyang Qin, **Qingzhuo Wang**, Dongrui Liu, Wen Shen  
  *NeurIPS 2026* &nbsp; [\[URL\]](https://arxiv.org/abs/2603.17372)  
  <small>TL;DR: For explicitly harmful inputs, VLMs can distinguish harmfulness yet shift into a distinct jailbreak state when images are added. JRS-Rem removes the jailbreak-related component of this representation shift at inference time to improve safety.</small>

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
