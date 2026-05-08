---
title: "Evaluating and Explaining Prompt Sensitivity of LLMs Using Interactions"
collection: publications
category: co-author
permalink: /publication/2026-07-21-prompt-sensitivity
excerpt: 'We introduce game-theoretic interactions to fine-grainedly analyze prompt sensitivity of LLMs, proposing the IPS metric and uncovering that factors like SFT and scale reduce sensitivity by stabilizing low-order interactions.'
date: 2026-07-21
venue: 'ICML 2026'
paperurl: 'https://icml.cc/virtual/2026/poster/65089'
citation: 'Ruiyang Qin, Qingzhuo Wang, Tian Wang, Zhihua Wei, Wen Shen. (2026). &quot;Evaluating and Explaining Prompt Sensitivity of LLMs Using Interactions.&quot; <i>ICML 2026</i>.'
---

LLMs are often undermined by prompt sensitivity—semantically irrelevant changes in prompts can cause dramatic performance fluctuations. Previous studies only evaluate sensitivity by comparing final outputs, failing to explain the internal reasons. This paper introduces game-theoretic interactions as a fine-grained analytical tool: by decomposing the LLM's output into a set of AND interactions among input variables, we can identify which interactions are stable and which are unstable across prompt variations. Strikingly, we find that even when the LLM's final output remains the same, 60–80% of salient interactions are still unstable—a form of latent instability invisible to traditional output-level metrics. Building on this, we propose the **Interaction-based Prompt Sensitivity (IPS)** metric to quantify prompt sensitivity at the interaction level, and apply it to evaluate 50 open-source LLMs across 6 model families. We uncover four factors that reduce prompt sensitivity—supervised fine-tuning, increased model scale, dense architectures, and few-shot learning—and reveal a common underlying mechanism: all four primarily stabilize **low-order interactions** (involving few input variables), while high-order interactions remain sensitive.
