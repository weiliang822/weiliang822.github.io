---
title: "Mitigating Action-Relation Hallucinations in LVLMs via Relation-aware Visual Enhancement"
collection: publications
category: conferences
permalink: /publication/2026-07-21-action-relation-hallucination
excerpt: 'We define the ARS score to locate action-relation-sensitive attention heads, and propose RVE, a training-free method that enhances attention to action-relevant image regions to mitigate action-relation hallucinations in LVLMs.'
date: 2026-07-21
venue: 'ACL 2026'
citation: 'Zhenxin Qin, Qiang Li, Qingzhuo Wang, Ruiyang Qin, Zhihua Wei, Wen Shen. (2026). &quot;Mitigating Action-Relation Hallucinations in LVLMs via Relation-aware Visual Enhancement.&quot; <i>ACL 2026</i>.'
---

Large vision-language models (LVLMs) suffer from action-relation hallucinations—incorrectly describing interactions between objects (e.g., "riding" vs. "pushing" a bicycle). Unlike object hallucinations that have been widely studied, action-relation hallucinations involve complex inter-object interactions and remain underexplored. We observe that the primary cause is the insufficient attention allocated to visual information: image tokens receive disproportionately low attention (10–100x less) compared to text tokens. To address this, we define the **Action-Relation Sensitivity (ARS)** score to quantify how sensitive each attention head is to action-relation changes, revealing that middle layers are most sensitive. We then propose **Relation-aware Visual Enhancement (RVE)**, a training-free method that enhances middle layers' attention toward action-relevant image regions identified by high-ARS heads, while constructing a denoising mask from low-ARS heads to suppress background noise. Extensive experiments demonstrate that RVE effectively mitigates action-relation hallucinations with negligible additional inference cost, while generalizing to spatial-relation and object hallucinations.
