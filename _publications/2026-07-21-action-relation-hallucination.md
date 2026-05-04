---
title: "Mitigating Action-Relation Hallucinations in LVLMs via Relation-aware Visual Enhancement"
collection: publications
category: conferences
permalink: /publication/2026-07-21-action-relation-hallucination
excerpt: 'We propose a relation-aware visual enhancement method to mitigate action-relation hallucinations in large vision-language models.'
date: 2026-07-21
venue: 'ACL 2026'
citation: 'Zhenxin Qin, Qiang Li, Qingzhuo Wang, Ruiyang Qin, Zhihua Wei, Wen Shen. (2026). &quot;Mitigating Action-Relation Hallucinations in LVLMs via Relation-aware Visual Enhancement.&quot; <i>ACL 2026</i>.'
---

Large vision-language models (LVLMs) frequently hallucinate incorrect action-relations—generating descriptions where entities perform wrong actions or have fabricated spatial/temporal relationships. This paper identifies action-relation hallucination as a distinct and underexplored failure mode, and proposes a Relation-aware Visual Enhancement (RaVE) framework to address it. RaVE enhances the visual grounding of relational concepts by introducing relation-focused visual features and a training strategy that explicitly aligns visual representations with action-relation semantics. The framework incorporates a relation-aware attention mechanism that directs the model to attend to relevant visual regions when generating relational descriptions, and a contrastive learning objective that sharpens the distinction between correct and hallucinated relations. Experiments on multiple benchmarks show that RaVE significantly reduces action-relation hallucinations while preserving general visual understanding capabilities.
