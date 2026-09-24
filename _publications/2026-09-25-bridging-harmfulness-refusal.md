---
title: "Bridging the Gap Between Harmfulness Belief and Refusal Behavior for Safety Alignment"
collection: publications
category: co-author
permalink: /publication/2026-09-25-bridging-harmfulness-refusal
excerpt: 'Bridging Harmfulness and Refusal (BHR) trains a LoRA adapter to carry harmfulness information from the instruction to the response-start position. Belief and belief-gated refusal losses improve jailbreak robustness while limiting over-refusal and preserving general capabilities.'
date: 2026-09-25 00:00:00 +0800
venue: 'NeurIPS 2026'
citation: 'Lu Zhang, Chen Feng, Qingzhuo Wang, Wen Shen, Zhihua Wei. (2026). &quot;Bridging the Gap Between Harmfulness Belief and Refusal Behavior for Safety Alignment.&quot; <i>NeurIPS 2026</i>.'
---

**Lu Zhang, Chen Feng, Qingzhuo Wang, Wen Shen, Zhihua Wei**

Safety-aligned LLMs can recognize harmful requests internally yet still produce compliant responses. We find that harmfulness information is not reliably preserved between the final instruction token and the response-start token. **Bridging Harmfulness and Refusal (BHR)** trains a LoRA adapter to carry this information to the response-start representation, establishing an additional pathway to refusal.

A **belief loss** maintains accurate harmfulness judgments at the instruction position. A **belief-gated refusal loss** uses these judgments to regulate refusal learning and reduce over-refusal on benign inputs. Experiments across multiple LLMs and safety benchmarks show improved robustness to diverse jailbreak attacks while preserving general capabilities.
