---
title: "A Unified Approach to Interpreting Knowledge Distillation for Large Language Models via Interactions"
collection: publications
category: conferences
permalink: /publication/2026-07-21-kd-interactions
excerpt: 'We propose a unified interaction-based framework to interpret knowledge distillation for LLMs, decomposing various KD loss functions into interpretable Shapley interaction components.'
date: 2026-07-21
venue: 'ICML 2026'
citation: 'Qingzhuo Wang*, Ruiyang Qin*, Zhenxin Qin, Wen Shen, Zhihua Wei. (2026). &quot;A Unified Approach to Interpreting Knowledge Distillation for Large Language Models via Interactions.&quot; <i>ICML 2026</i>.'
---

Knowledge distillation (KD) has become a key technique for compressing large language models, yet the mechanisms underlying different KD objectives remain poorly understood. In this work, we propose a unified interaction-based framework that leverages multivariate Shapley interactions to decompose and interpret various KD loss functions—including KLD, RKL, JSD, and TVD—into interpretable interaction components across different orders. Our theoretical analysis reveals how each KD objective transfers knowledge at different interaction levels, explaining why certain methods excel at capturing low-order (simple) versus high-order (complex) token interactions. Extensive experiments on LLM distillation tasks validate our framework, providing actionable insights for selecting and designing KD objectives tailored to specific downstream requirements.
