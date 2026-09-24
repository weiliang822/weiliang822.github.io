---
title: "Mitigating Action-Relation Hallucinations in LVLMs via Relation-aware Visual Enhancement"
collection: publications
category: co-author
permalink: /publication/2026-07-21-action-relation-hallucination
excerpt: 'Action-Relation Sensitivity (ARS) identifies attention heads that localize action-relevant image regions. Relation-aware Visual Enhancement (RVE) boosts attention to these regions without additional training, reducing action-relation hallucinations with negligible inference overhead.'
date: 2026-06-01
venue: 'ACL 2026'
paperurl: 'https://arxiv.org/abs/2605.11808'
citation: 'Zhenxin Qin, Qiang Li, Qingzhuo Wang, Ruiyang Qin, Zhihua Wei, Wen Shen. (2026). &quot;Mitigating Action-Relation Hallucinations in LVLMs via Relation-aware Visual Enhancement.&quot; <i>ACL 2026</i>.'
---

Action-relation hallucinations occur when large vision-language models incorrectly describe interactions between objects, such as confusing pushing a bicycle with riding it. Our analysis links these errors to insufficient attention to visual information. **Action-Relation Sensitivity (ARS)** measures how attention heads respond to action-relation changes, identifying heads that localize relevant image regions.

**Relation-aware Visual Enhancement (RVE)** increases attention to these regions in the middle layers without additional training. It combines an enhancement mask derived from sensitive heads with a denoising mask derived from insensitive heads to avoid amplifying background noise. Experiments show reduced action-relation hallucinations with negligible additional inference cost, with benefits extending to spatial-relation and object hallucinations.
