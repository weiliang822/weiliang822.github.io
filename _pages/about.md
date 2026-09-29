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

My research interests lie in **LLM post-training**, **Quantitative Research**, and **agentic reinforcement learning**.

---

## Selected Publications

### First-Author

- **AlphaDiverse: Post-Training Local Quantitative Research Agents for Diverse Exploration in Alpha Factor Mining** <small>(Work done during an internship at Shanghai Non-convex Intelligent Technology.)</small>  
  **Qingzhuo Wang**, Zikun Wei, Zhihua Wei, Wen Shen  
  *arXiv 2026* &nbsp; [\[URL\]](https://arxiv.org/abs/2609.29014)  
  <small>TL;DR: AlphaDiverse post-trains local Planner and Realizer agents with diverse research traces, supervised fine-tuning, and joint GRPO. Across four Chinese stock universes, it combines competitive prediction with broader exploration in alpha factor mining.</small>

- **Authorization Closure Graph: Minimal Repair for LLM Agents with Evolving User Instructions**  
  **Qingzhuo Wang**, CaiYi Wang, Jinglu Meng, Ruiyang Qin, Kunyu Peng, Zhihua Wei, Wen Shen  
  *arXiv 2026* &nbsp; [\[URL\]](https://arxiv.org/abs/2609.32428)  
  <small>TL;DR: Authorization Closure Graph (ACG) tracks authorization dependencies as user instructions evolve, preserving valid permissions and identifying the minimal evidence or authority needed to proceed. Across three LLMs and two tasks, it improves action safety and task success.</small>

- **A Unified Approach to Interpreting Knowledge Distillation for Large Language Models via Interactions**  
  **Qingzhuo Wang**\*, Ruiyang Qin\*, Zhenxin Qin, Wen Shen, Zhihua Wei  
  *ICML 2026*   &nbsp; [\[URL\]](https://icml.cc/virtual/2026/poster/65719)  
  <small>TL;DR: We identify interaction sparsification as a common pattern across knowledge distillation methods. Complex Interaction Penalty (CIP) explicitly promotes sparsity in complex interactions and improves distillation performance.</small>

- **Multilingual Safety Alignment via Self-Distillation**  
  Ruiyang Qin\*, **Qingzhuo Wang**\*, Dongrui Liu, Qiang Li, Zhihua Wei, Wen Shen  
  *NeurIPS 2026* &nbsp; [\[URL\]](https://arxiv.org/abs/2605.02971)  
  <small>TL;DR: Multilingual Self-Distillation (MSD) transfers safety from high-resource to low-resource languages using multilingual queries without external response data. It supports on-policy and off-policy training, with Dual-Perspective Safety Weighting (DPSW) emphasizing safety-critical tokens.</small>

### Co-Author

- **Bridging the Gap Between Harmfulness Belief and Refusal Behavior for Safety Alignment**  
  Lu Zhang, Chen Feng, **Qingzhuo Wang**, Wen Shen, Zhihua Wei  
  *NeurIPS 2026* &nbsp; [\[Details\]](/publication/2026-09-25-bridging-harmfulness-refusal)  
  <small>TL;DR: Bridging Harmfulness and Refusal (BHR) trains a LoRA adapter to carry harmfulness information from the instruction to the response-start position. Belief and belief-gated refusal losses improve jailbreak robustness while limiting over-refusal and preserving general capabilities.</small>

- **Evaluating and Explaining Prompt Sensitivity of LLMs Using Interactions**  
  Ruiyang Qin, **Qingzhuo Wang**, Tian Wang, Zhihua Wei, Wen Shen  
  *ICML 2026* &nbsp; [\[URL\]](https://icml.cc/virtual/2026/poster/65089)  
  <small>TL;DR: Interaction-based Prompt Sensitivity (IPS) reveals changes in LLM inference patterns that output-level metrics miss. Across 50 models, supervised fine-tuning, larger scale, dense architectures, and few-shot learning primarily stabilize low-order interactions.</small>

- **Understanding and Defending VLM Jailbreaks via Jailbreak-Related Representation Shift**  
  Zhihua Wei, Qiang Li, Jian Ruan, Zhenxin Qin, Leilei Wen, Ruiyang Qin, **Qingzhuo Wang**, Dongrui Liu, Wen Shen  
  *NeurIPS 2026* &nbsp; [\[URL\]](https://arxiv.org/abs/2603.17372)  
  <small>TL;DR: For explicitly harmful inputs, VLMs can distinguish harmfulness yet shift into a distinct jailbreak state when images are added. JRS-Rem removes the jailbreak-related component of this representation shift at inference time to improve safety.</small>

---

## Internships

**Shanghai Non-convex Intelligent Technology** &nbsp; *Jun. 2026 &ndash; Present*

Developed **AlphaDiverse**, a multi-agent framework for alpha factor mining. Collected diverse research trajectories and post-trained local research agents with supervised fine-tuning and joint reinforcement learning to improve predictive performance and exploration diversity.

**WeQuant** &mdash; Quant Researcher &nbsp; *Mar. 2025 &ndash; Oct. 2025*

Developed and deployed a low-frequency A-share alpha strategy, covering data preparation, factor research, predictive modeling, and backtesting. Built a reusable live-trading framework to support the strategy's operation.

**Bilibili** &mdash; Algorithm Engineer &nbsp; *Jul. 2024 &ndash; Dec. 2024*

Improved e-commerce recommendation through targeted retrieval, multimodal product representations, and ranking model calibration. Deployed strategies that increased conversion and recommendation diversity while reducing repetitive product exposure.
