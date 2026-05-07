---
title: "Multilingual Safety Alignment via Self-Distillation"
collection: publications
category: first-author
permalink: /publication/2026-07-21-multilingual-safety
excerpt: 'We propose an on-policy self-distillation method for multilingual safety alignment, transferring the model''s own safety capabilities from high-resource to low-resource languages without reliance on human-annotated safety data.'
date: 2026-06-01
venue: 'arXiv 2026'
paperurl: 'https://arxiv.org/abs/2605.02971'
citation: 'Ruiyang Qin*, Qingzhuo Wang*, Dongrui Liu, Qiang Li, Zhihua Wei, Wen Shen. (2026). &quot;Multilingual Safety Alignment via Self-Distillation.&quot; <i>arXiv 2026</i>.'
---

Safety alignment of LLMs is predominantly conducted in English, leaving low-resource languages significantly under-aligned and vulnerable to harmful outputs. Traditional approaches rely heavily on high-quality human-annotated safety response data in each target language, which is expensive and hard to scale. This paper proposes an on-policy self-distillation method that transfers the model's own safety capabilities from high-resource languages to low-resource ones. By leveraging the model's existing safety knowledge in well-aligned languages as the distillation source, our approach eliminates the dependency on external multilingual safety data. Experiments across multiple models and diverse multilingual scenarios demonstrate significant improvements in both in-distribution and out-of-distribution language safety, while preserving the model's general reasoning capabilities.
