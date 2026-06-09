# Bebridge Inc. / Slid

## Metadata

- Evidence status: Strong draft from existing resume/site/project pages
- Public name: Slid
- Organization/client: Bebridge Inc.
- Role/title progression: Full Stack Engineer (Level 2), Senior Software Engineer (Level 3), AI Engineer and Team Lead (Level 4)
- Public title preference for LinkedIn/resume: Lead AI Engineer. User noted on 2026-06-05 that principal-level AI engineering scope is accurate because he set direction and solved the hardest problems, but `Principal AI Engineer` should be treated as scope language unless confirmed as an official title. User clarified on 2026-06-06 that the `AI Engineer & Team Lead` resume label should be converted to `Lead AI Engineer`.
- Period: Jun 2022 - Jun 2025
- Location: Seoul, South Korea
- Source repos: Private/not currently linked
- Existing public artifacts: `_pages/about.md`, `_data/cv.yml`, `_projects/`, resume markdown files

## One-Line Positioning

Joined Bebridge as an early engineer and grew into a Lead AI Engineer, building cross-platform EdTech and AI features for Slid's 50K+ MAU learning platform.

## Context

Slid is an EdTech platform for learning from online videos. Existing site/resume materials position Hamza as an early engineer who helped scale product surfaces across web, Chrome Extension, desktop, mobile, and AI-powered learning features.

## Role Periods

### Full Stack Engineer (Level 2)

- Period: Jun 2022 - May 2023
- Focus: Web, extension, desktop, mobile foundations; real-time transcription; authentication; payments; performance.
- Recognition: Hero Award 2022; promoted to Level 3.

### Senior Software Engineer (Level 3) - R&D And AI Innovation

- Period: Jun 2023 - Dec 2023
- Focus: RAG, AI chat, semantic search, video summarization, export systems, performance, open source.
- Recognition: Hero Award 2023; promoted to Level 4.

### AI Engineer And Team Lead (Level 4)

- Period: Jan 2024 - Jun 2025
- Focus: AI product leadership, mobile app, auto-notes, server-side video processing, cost optimization, LangGraph agent systems.
- Scope: Principal-level AI engineering work, including setting technical direction and solving the hardest AI/product problems across video learning, mobile constraints, AI output quality, and production cost.

## Major Workstreams

### AI Auto Notes

- Problem: Learners needed automatic notes from video lectures.
- What Hamza built: LLM/Whisper-based automatic note generation from video.
- Technologies: LLM APIs, Whisper, Python/FastAPI, AWS, LangGraph.
- Result: Existing resume claims 12% video engagement lift and 25% overall retention boost.
- Evidence: Existing resume/CV and project pages. Metrics should be confirmed before heavy external use.

### Mobile AI Innovation

- Problem: Mobile platforms have constraints around video capture and processing.
- What Hamza built: React Native iOS/Android app features backed by server-side video processing using AWS Lambda and FFmpeg.
- Technologies: React Native, AWS Lambda, EventBridge, S3, FFmpeg, Python/FastAPI.
- Result: Existing resume claims 40% mobile retention increase.
- Evidence: Existing resume/CV.

### AI Chat And RAG

- Problem: Users needed to search and converse with their learning notes.
- What Hamza built: Conversational AI for notes using LangChain, Pinecone vector DB, semantic search, and streaming responses.
- Technologies: LangChain, Pinecone, embeddings, streaming UI.
- Result: Existing resume claims 25% session duration increase.
- Evidence: Existing resume/CV.

### Real-Time Transcription

- Problem: Users needed live transcription while learning from video.
- What Hamza built: WebRTC to Socket.io to speech-to-text pipeline.
- Technologies: WebRTC, Socket.io, Google Cloud Speech STT, Whisper/Groq provider evolution.
- Result: Existing resume claims 51% premium subscription increase and 90% transcription cost reduction.
- Evidence: Existing resume/CV and Stack Overflow impact mention.

### Cross-Platform Authentication

- Problem: Slid needed unified identity across web, Chrome Extension, React Native mobile, and Electron desktop.
- What Hamza built: Cross-platform authentication using AWS Cognito and custom storage/session patterns.
- Technologies: AWS Cognito, cookies/tokens, browser extension context, React Native, Electron.
- Result: Unified access and faster platform expansion.
- Evidence: Existing resume/CV and project pages.

### Payment And Pricing

- Problem: Slid needed international and Korean payment support with premium feature access.
- What Hamza built: Stripe and Payple multi-gateway integration with subscription and privilege control.
- Technologies: Stripe, Payple, backend payment APIs, webhooks.
- Result: Existing project pages claim 35% checkout improvement and 98%+ payment success.
- Evidence: `_projects/11_project.md`.

### Export Systems

- Problem: Users needed notes in multiple document/workspace formats.
- What Hamza built: Multi-format export to Word, PDF, Markdown, and Notion.
- Technologies: Document generation, Markdown/AST processing, Notion API.
- Result: Existing resume claims 96% accuracy and 75% support burden reduction.
- Evidence: Existing resume/CV.

## Technical Stack

- Frontend/mobile: React, React Native, Chrome Extension, Electron.
- Backend: Python, FastAPI, Node.js.
- AI: LLM APIs, Whisper, LangChain, LangGraph, Pinecone, embeddings.
- Realtime/media: WebRTC, Socket.io, FFmpeg.
- Cloud: AWS Lambda, EventBridge, S3, Cognito.
- Payments: Stripe, Payple, Apple In-App Purchase needs confirmation.

## Resume Bullet Bank

- Led AI transformation for Slid's 50K+ MAU EdTech platform, shipping LLM-powered auto-notes, AI chat, semantic search, and transcript correction systems.
- Built LLM/Whisper auto-notes from video lectures and helped drive measurable engagement and retention gains across learning workflows.
- Spearheaded React Native mobile AI features backed by server-side AWS Lambda and FFmpeg video processing to overcome mobile platform constraints.
- Designed LangGraph multi-agent transcript correction workflows with custom reasoning tools to improve AI-generated learning content quality.
- Built early RAG and conversational AI experiences for learning notes using LangChain, Pinecone, embeddings, and streaming responses.
- Pioneered real-time transcription pipeline using WebRTC, Socket.io, and cloud speech-to-text providers, then optimized provider strategy for major cost reductions.
- Built cross-platform authentication and payment systems across web, extension, mobile, and desktop, including AWS Cognito, Stripe, and Payple.

## Site/Portfolio Angles

- Strong anchor role: progression from early engineer to AI team lead.
- Good for showing repeated ownership across product, infrastructure, AI, mobile, and business metrics.
- Split into 2-4 portfolio projects if the site needs depth: Auto Notes, Mobile AI, RAG Chat, Payments/Auth.

## Proof Links And Evidence

- `_data/cv.yml`
- `_pages/about.md`
- `2025-10-25-hamza-kyamanywa-openai-resume.md`
- `_projects/10_project.md` through `_projects/15_project.md` contain detailed Slid-related project pages.

## Needs Confirmation

- Exact public-safe metrics and whether all can be published.
- Use `Lead AI Engineer` as the public title on homepage/resume/LinkedIn while keeping team-lead responsibilities in the description.
- Which project pages are too inflated, outdated, or need pruning.
