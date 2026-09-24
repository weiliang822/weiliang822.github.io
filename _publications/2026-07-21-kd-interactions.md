---
title: "A Unified Approach to Interpreting Knowledge Distillation for Large Language Models via Interactions"
collection: publications
category: first-author
permalink: /publication/2026-07-21-kd-interactions
excerpt: 'We identify interaction sparsification as a common pattern across knowledge distillation methods. Complex Interaction Penalty (CIP) explicitly promotes sparsity in complex interactions and improves distillation performance.'
date: 2026-07-21
venue: 'ICML 2026'
paperurl: 'https://icml.cc/virtual/2026/poster/65719'
citation: 'Qingzhuo Wang*, Ruiyang Qin*, Zhenxin Qin, Wen Shen, Zhihua Wei. (2026). &quot;A Unified Approach to Interpreting Knowledge Distillation for Large Language Models via Interactions.&quot; <i>ICML 2026</i>.'
---

We use game-theoretic interactions to analyze how knowledge distillation (KD) changes the inference behavior of large language models. Decomposing output scores into interactions among input variables reveals a common pattern across the studied KD methods: **interaction sparsification**. Students retain fewer salient interactions, preferentially inherit simple teacher interactions, and suppress many complex interactions.

Differences in how KD methods handle complex interactions help explain their performance differences. Motivated by this analysis, we introduce **Complex Interaction Penalty (CIP)**, a plug-and-play loss that promotes sparsity in complex interactions during distillation. Experiments across multiple model families show improvements for diverse KD methods on both in-domain and out-of-distribution benchmarks.
