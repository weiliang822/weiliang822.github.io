---
title: "Evaluating and Explaining Prompt Sensitivity of LLMs Using Interactions"
collection: publications
category: co-author
permalink: /publication/2026-07-21-prompt-sensitivity
excerpt: 'Interaction-based Prompt Sensitivity (IPS) reveals changes in LLM inference patterns that output-level metrics miss. Across 50 models, supervised fine-tuning, larger scale, dense architectures, and few-shot learning primarily stabilize low-order interactions.'
date: 2026-07-21
venue: 'ICML 2026'
paperurl: 'https://icml.cc/virtual/2026/poster/65089'
citation: 'Ruiyang Qin, Qingzhuo Wang, Tian Wang, Zhihua Wei, Wen Shen. (2026). &quot;Evaluating and Explaining Prompt Sensitivity of LLMs Using Interactions.&quot; <i>ICML 2026</i>.'
---

We analyze prompt sensitivity by decomposing an LLM's output score into game-theoretic interactions among input variables. In the evaluated settings, **60-80% of salient interactions remain unstable even when the final prediction is unchanged**. We introduce **Interaction-based Prompt Sensitivity (IPS)** to measure these changes beyond output-level consistency.

An evaluation of **50 open-source LLMs across six model families** identifies four factors associated with reduced sensitivity: supervised fine-tuning, larger model scale, dense architectures, and few-shot learning. These factors share a common pattern: they primarily stabilize **low-order interactions**, while high-order interactions remain more sensitive to prompt changes.
