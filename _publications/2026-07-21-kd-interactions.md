---
title: "A Unified Approach to Interpreting Knowledge Distillation for Large Language Models via Interactions"
collection: publications
category: first-author
permalink: /publication/2026-07-21-kd-interactions
excerpt: 'We interpret knowledge distillation from a game-theoretic interaction perspective, revealing that the essence of distillation is the sparsification of interactions, and propose the CIP loss to explicitly enforce this mechanism.'
date: 2026-07-21
venue: 'ICML 2026'
citation: 'Qingzhuo Wang*, Ruiyang Qin*, Zhenxin Qin, Wen Shen, Zhihua Wei. (2026). &quot;A Unified Approach to Interpreting Knowledge Distillation for Large Language Models via Interactions.&quot; <i>ICML 2026</i>.'
---

Despite the widespread success of knowledge distillation (KD) for compressing LLMs, the underlying mechanism of *why* KD works remains unclear. This paper proposes a unified framework based on game-theoretic interactions to interpret the distillation process. By decomposing the LLM's output into a sum of interactions—each representing a nonlinear relationship among a set of input words—we reveal that **the essence of distillation lies in the sparsification of interactions**: student models retain far fewer salient interactions while suppressing most others to near-zero effects. Crucially, we find that student models preferentially inherit simple interactions (involving few input variables) from the teacher, while complex interactions are largely compressed. We further show that the performance variance across KD methods arises from their ability to handle complex interactions—methods that achieve higher sparsity in complex interactions while preserving the most salient ones yield better performance. Motivated by these insights, we propose **Complex Interaction Penalty (CIP)**, a plug-and-play loss term that explicitly enforces sparsity of complex interactions during distillation. Extensive experiments demonstrate that CIP consistently improves diverse KD methods on both in-domain and out-of-distribution benchmarks across multiple LLM families.
