---
title: "Understanding and Defending VLM Jailbreaks via Jailbreak-Related Representation Shift"
collection: publications
category: manuscripts
permalink: /publication/2026-03-21-vlm-jailbreak
excerpt: 'We investigate the mechanism of VLM jailbreaks through representation shift analysis and propose a defense method based on detecting and correcting jailbreak-related representation shifts.'
date: 2026-03-21
venue: 'arXiv 2026'
paperurl: 'https://arxiv.org/abs/2603.17372'
citation: 'Zhihua Wei, Qiang Li, Jian Ruan, Zhenxin Qin, Leilei Wen, Ruiyang Qin, Qingzhuo Wang, Dongrui Liu, Wen Shen. (2026). &quot;Understanding and Defending VLM Jailbreaks via Jailbreak-Related Representation Shift.&quot; <i>arXiv 2026</i>.'
---

Vision-language models (VLMs) are vulnerable to jailbreak attacks that exploit visual inputs to bypass safety alignment. This paper provides a mechanistic understanding of VLM jailbreaks by analyzing jailbreak-related representation shifts—systematic changes in the model's internal representations induced by adversarial visual inputs. We discover that successful jailbreaks cause predictable shifts in the representation space that move the model's hidden states away from safety-aligned regions toward unsafe generation patterns. Based on this insight, we propose a defense framework that detects jailbreak attempts by monitoring representation shifts in real time and corrects them by steering representations back toward safe regions. Our approach operates without modifying model weights and can be applied as a plug-in defense module. Extensive experiments across multiple VLMs and jailbreak methods demonstrate that our defense significantly reduces attack success rates while maintaining model utility on benign inputs.
