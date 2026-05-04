---
title: "Multilingual Safety Alignment via Self-Distillation"
collection: publications
category: manuscripts
permalink: /publication/2026-07-21-multilingual-safety
excerpt: 'We propose a self-distillation framework for multilingual safety alignment, transferring safety capabilities from high-resource to low-resource languages without external data.'
date: 2026-07-21
venue: 'arXiv 2026'
citation: 'Ruiyang Qin*, Qingzhuo Wang*, Dongrui Liu, Qiang Li, Zhihua Wei, Wen Shen. (2026). &quot;Multilingual Safety Alignment via Self-Distillation.&quot; <i>arXiv 2026</i>.'
---

Safety alignment of large language models (LLMs) typically focuses on English, leaving other languages vulnerable to harmful outputs. This paper proposes a self-distillation framework for multilingual safety alignment that leverages the model's own safety capabilities in high-resource languages (e.g., English) to improve safety in low-resource languages—without requiring external multilingual safety data. Our method distills safety-aware representations from the dominant language into other languages through a carefully designed training objective that preserves the model's general multilingual capabilities while strengthening cross-lingual safety transfer. Experiments across multiple languages and safety benchmarks demonstrate that our approach significantly improves multilingual safety performance while maintaining helpfulness, outperforming existing multilingual alignment methods.
