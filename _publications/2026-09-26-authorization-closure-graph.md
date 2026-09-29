---
title: "Authorization Closure Graph: Minimal Repair for LLM Agents with Evolving User Instructions"
collection: publications
category: first-author
permalink: /publication/2026-09-26-authorization-closure-graph
excerpt: 'Authorization Closure Graph (ACG) tracks authorization dependencies as user instructions evolve, preserving valid permissions and identifying the minimal evidence or authority needed to proceed. Across three LLMs and two tasks, it improves action safety and task success.'
date: 2026-09-26
venue: 'arXiv 2026'
paperurl: 'https://arxiv.org/abs/2609.32428'
citation: 'Qingzhuo Wang, CaiYi Wang, Jinglu Meng, Ruiyang Qin, Kunyu Peng, Zhihua Wei, Wen Shen. (2026). &quot;Authorization Closure Graph: Minimal Repair for LLM Agents with Evolving User Instructions.&quot; <i>arXiv 2026</i>.'
---

**Qingzhuo Wang**, CaiYi Wang, Jinglu Meng, Ruiyang Qin, Kunyu Peng, Zhihua Wei, Wen Shen

**Authorization Closure Graph (ACG)** represents user authorization and its dependencies as an evolving, versioned state for tool-using LLM agents. When instructions change, ACG invalidates affected permissions while retaining unaffected authorization. It then computes a minimal repair identifying the missing evidence or authority required for execution, reducing stale-authority errors and unnecessary authorization requests.

Evaluations across three LLMs and two tasks show improved action safety and task success rates.

[Code](https://github.com/weiliang822/ACG)
