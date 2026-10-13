---
layout: page
title: JonjaBird
description: An end-to-end agentic AI mailroom connecting physical post, private correspondence, and families abroad
img:
importance: 3
category: work
---

### Why I Built It

My work as president of the Ugandans in South Korea Association (USKA) led me to build [JonjaBird](https://jonjabird.com). Foreign inmates in Korea have no internet access, while their families abroad face language barriers and unfamiliar postal systems when trying to stay in touch. I built an end-to-end agentic AI system to run the mailroom connecting them.

### The End-to-End System

Paper is the inmate’s interface. Families use a digital portal. Between them, the mailroom agent, Hermes, coordinates the work across scanned mail, application tools, browser automation, and postal fulfillment.

1. **Incoming mail:** the agent checks the virtual-office mailbox and imports scanned letters and envelopes into the portal, with duplicate-safe intake.
2. **Understanding and routing:** multimodal processing reads the scans. The agent identifies the author and intended reader, matches known people, sorts mixed envelopes, separates private passages, and submits a structured review. The application validates the result before delivering letters to verified readers or inviting new recipients.
3. **Requests inside letters:** the agent extracts and handles service requests, researches answers where appropriate, records decisions, and leaves exceptions requiring my judgment for review.
4. **Outgoing correspondence:** families compose letters, include documents, review print packets, and pay through the portal. The agent takes the funded job, checks the recipient and postal address, downloads the recorded documents, and works through Korea Post’s website to submit them for printing and mailing.
5. **Tracking and follow-through:** scheduled jobs bring carrier events back into the portal, update delivery status, and notify the sender. Queue monitors pick up new work and surface held or overdue items.

### What I Built and Own

- **The agent and its operating environment:** tool access, task-specific skills, persistent operational knowledge, scheduled work, and recovery procedures. Hermes records lessons as skills that can be reviewed and versioned.
- **The operations API and CLI:** authenticated tools for intake, review, recipient matching, request decisions, outgoing jobs, and tracking. The agent operates through the same application rules as staff, with recorded actions.
- **The multimodal mail pipeline:** scan reading, structured review, sender/recipient resolution, mixed-envelope sorting, and separation of family-facing and private material.
- **The physical fulfillment integration:** Korea Post browser automation, generated print documents, recipient/address checks, posting records, and delivery tracking.
- **The full product around the agents:** member accounts, private correspondence and document libraries, a letter composer, packet previews, checkout, staff workflows, and the underlying service model.

### Agent Evaluation

I built **JonjaBird Bench** to test whether a model can run a complete fictional mailroom shift using the real agent skills and tools. It covers mailbox intake, letter review, and an outgoing postal workflow against a mock post office. The grader scores task outcomes and records cost and time, so model choices and skill changes can be checked against repeatable evidence.

The application remains the system of record for identities, per-letter access, payment confirmation, and postal evidence. Uncertain or restricted operations can be held for review, and a model’s claim of completion does not mark a letter paid, posted, or delivered.

### Stack

Hermes Agent, multimodal LLMs, browser automation, Next.js, React, TypeScript, PostgreSQL, Python, WeasyPrint, Stripe, Cloudflare R2, and Vercel. The earlier incoming-review pipeline used Eve; Hermes now owns the central mailroom workflow.

[Visit JonjaBird](https://jonjabird.com)
