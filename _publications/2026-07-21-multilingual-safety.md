---
title: "Multilingual Safety Alignment via Self-Distillation"
collection: publications
category: first-author
permalink: /publication/2026-07-21-multilingual-safety
excerpt: 'Multilingual Self-Distillation (MSD) transfers safety from high-resource to low-resource languages using multilingual queries without external response data. It supports on-policy and off-policy training, with Dual-Perspective Safety Weighting (DPSW) emphasizing safety-critical tokens.'
date: 2026-06-01
venue: 'NeurIPS 2026'
paperurl: 'https://arxiv.org/abs/2605.02971'
citation: 'Ruiyang Qin*, Qingzhuo Wang*, Dongrui Liu, Qiang Li, Zhihua Wei, Wen Shen. (2026). &quot;Multilingual Safety Alignment via Self-Distillation.&quot; <i>NeurIPS 2026</i>.'
---

**Multilingual Self-Distillation (MSD)** transfers an LLM's existing safety capabilities from high-resource languages to low-resource languages. It uses multilingual queries without requiring external response data in any language. The framework supports both **on-policy and off-policy self-distillation**, using student-sampled and teacher-sampled responses, respectively.

We introduce **Dual-Perspective Safety Weighting (DPSW)** to adapt the distillation objective at the token level. DPSW uses teacher and student confidence to increase the weights of safety-critical tokens and reduce those of non-critical tokens. Experiments on multilingual jailbreak and utility benchmarks show improved safety, including transfer to unseen languages and more challenging datasets, while preserving general capabilities.
