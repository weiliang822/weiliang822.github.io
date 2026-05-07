---
title: "Understanding and Defending VLM Jailbreaks via Jailbreak-Related Representation Shift"
collection: publications
category: co-author
permalink: /publication/2026-03-21-vlm-jailbreak
excerpt: 'We show that VLM jailbreaks are not perception failures but distinct internal states driven by image-induced representation shifts, and propose JRS-Rem to remove these shifts at inference time.'
date: 2026-03-21
venue: 'arXiv 2026'
paperurl: 'https://arxiv.org/abs/2603.17372'
citation: 'Zhihua Wei, Qiang Li, Jian Ruan, Zhenxin Qin, Leilei Wen, Ruiyang Qin, Qingzhuo Wang, Dongrui Liu, Wen Shen. (2026). &quot;Understanding and Defending VLM Jailbreaks via Jailbreak-Related Representation Shift.&quot; <i>arXiv 2026</i>.'
---

Vision-language models (VLMs) often exhibit weakened safety alignment when the visual modality is introduced—even adding a blank image can substantially increase jailbreak success rates. This paper challenges the prevailing "safety perception failure" hypothesis by analyzing VLM jailbreaks using explicitly harmful multimodal data. We observe that VLMs can clearly distinguish harmful from benign inputs in their representation space, and that jailbreak samples form a **distinct internal state** separable from both benign and refusal states. This suggests that jailbreaks do not arise from a failure to recognize harmful intent; instead, the visual modality shifts representations toward a specific jailbreak state where the model fails to trigger refusal despite recognizing the danger. We formalize this as the **jailbreak-related representation shift**—the component of the image-induced shift along a defined jailbreak direction. Based on this understanding, we propose **JRS-Rem** (Jailbreak-Related Shift Removal), a training-free defense that removes the jailbreak-related shift at inference time. Experiments across three VLMs and seven datasets show that JRS-Rem significantly enhances safety while preserving utility on benign tasks.
