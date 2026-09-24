---
title: "Understanding and Defending VLM Jailbreaks via Jailbreak-Related Representation Shift"
collection: publications
category: co-author
permalink: /publication/2026-03-21-vlm-jailbreak
excerpt: 'For explicitly harmful inputs, VLMs can distinguish harmfulness yet shift into a distinct jailbreak state when images are added. JRS-Rem removes the jailbreak-related component of this representation shift at inference time to improve safety.'
date: 2026-03-21
venue: 'NeurIPS 2026'
paperurl: 'https://arxiv.org/abs/2603.17372'
citation: 'Zhihua Wei, Qiang Li, Jian Ruan, Zhenxin Qin, Leilei Wen, Ruiyang Qin, Qingzhuo Wang, Dongrui Liu, Wen Shen. (2026). &quot;Understanding and Defending VLM Jailbreaks via Jailbreak-Related Representation Shift.&quot; <i>NeurIPS 2026</i>.'
---

Using explicitly harmful multimodal inputs, we find that VLM representations distinguish harmful from benign requests, while jailbreak and refusal samples form separable internal states. These observations suggest that harmfulness recognition alone does not reliably trigger refusal. We define the **jailbreak-related representation shift** as the component of the image-induced shift along an identified jailbreak direction.

**Jailbreak-Related Shift Removal (JRS-Rem)** removes this component at inference time without additional model training. Experiments across three VLMs and seven safety datasets cover explicitly harmful inputs, implicitly harmful inputs, and adversarial attacks. The results show improved safety while preserving performance on benign tasks.
