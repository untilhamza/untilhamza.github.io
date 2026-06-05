# GoGymi / TexTutor

## Metadata

- Evidence status: Verified from contribution reports, final public wording needs review
- Public name: TexTutor
- Organization/client: GoGymi
- Role/title: Senior Full Stack Engineer / freelance technical lead
- Period: Jan 2025 - Sep 2025
- Location: Remote, Switzerland
- Source repos: Needs confirmation
- Existing public artifacts: `_pages/about.md`, `_data/cv.yml`, `project_contributions/`

## One-Line Positioning

Delivered a full-stack AI-powered EdTech SaaS platform for Swiss teachers and students, spanning architecture, authentication, billing, multilingual UX, collaboration, and AI grammar correction.

## Context

TexTutor is described in existing site/resume materials as an AI-powered educational platform for Swiss teachers and students. Contribution reports describe Hamza as the primary/full-stack contributor across frontend, backend, billing, DevOps, authentication, and AI integrations.

## Ownership

- Full-stack platform architecture.
- Next.js/React frontend for teacher and student dashboards.
- Database schema and migration management.
- Authentication, email verification, and password reset flows.
- Stripe subscriptions, trials, billing dashboard, and webhook flows.
- Multilingual user interface and billing emails.
- AI grammar correction and feedback workflows.
- Rich text/collaboration workflows using Lexical and LiveBlocks.
- Deployment and local development infrastructure.

## Major Workstreams

### Architecture And Infrastructure

- Problem: TexTutor needed a complete product foundation.
- What Hamza built: Next.js 15, React 19, PostgreSQL, Drizzle ORM, Supabase, TypeScript platform architecture.
- Technologies: Next.js, React, TypeScript, PostgreSQL, Drizzle ORM, Supabase, Docker.
- Result: Production/pre-launch platform foundation.
- Evidence: `project_contributions/TEXTUTOR_HAMZA_CONTRIBUTIONS.md`, `project_contributions/HAMZA_CONTRIBUTIONS2.md`.

### Authentication And Security

- Problem: Teachers/students needed secure onboarding and account management.
- What Hamza built: Authentication system with email verification, password reset, protected routes, sessions, and role-aware access.
- Technologies: JWT/session handling, bcrypt, email verification flows.
- Result: Complete user-management foundation.
- Evidence: Contribution reports.

### Billing And Subscription System

- Problem: GoGymi needed monetization with subscriptions, trials, usage tracking, and localized billing communication.
- What Hamza built: Stripe webhook integration, subscription lifecycle management, free trial logic, usage/credit tracking, billing UI, and multilingual billing emails.
- Technologies: Stripe, webhooks, Resend/email templates, TypeScript.
- Result: Complete billing and subscription system.
- Evidence: Contribution reports mention 15+ commits and specific billing work.

### AI Grammar Correction

- Problem: The product needed AI-powered language correction and educational feedback.
- What Hamza built: Grammar correction workflows with formatting preservation, rule/preset management, multilingual support, credit validation, and feedback UI.
- Technologies: AI providers need confirmation, Python integration, Next.js frontend.
- Result: Core AI product workflow for educational writing support.
- Evidence: Contribution reports.

### Rich Text And Collaboration

- Problem: Teachers/students needed assignment creation, feedback, commenting, and collaborative editing.
- What Hamza built: Lexical editor integration, LiveBlocks collaboration, comments/threading, share flows, notifications, and PDF export workflows.
- Technologies: Lexical, LiveBlocks, React, PDF export.
- Result: Collaborative assignment and feedback experience.
- Evidence: Contribution reports.

### Internationalization

- Problem: Swiss/European education workflows needed multilingual support.
- What Hamza built: i18n support across English, German, French, Spanish, and Italian, including billing emails.
- Technologies: i18n message files, localized email templates.
- Result: Multi-language product and communication layer.
- Evidence: Contribution reports and existing resume.

## Metrics And Outcomes

- 554-555 commits:
  - Status: Verified from contribution reports.
  - Evidence: `project_contributions/TEXTUTOR_HAMZA_CONTRIBUTIONS.md`, `project_contributions/HAMZA_CONTRIBUTIONS2.md`.
  - Public wording: "Delivered 550+ commits across frontend, backend, billing, authentication, AI workflows, and deployment."
- 5 languages:
  - Status: Verified from contribution reports/resume.
  - Public wording: "Built multilingual product and billing workflows across EN/DE/ES/FR/IT."
- 43,000+ lines added:
  - Status: Strong draft from contribution report.
  - Public wording: Use only if Hamza wants commit-volume emphasis.

## Technical Stack

- Frontend: Next.js 15, React 19, TypeScript, Tailwind CSS, Radix UI, Lexical.
- Backend/data: PostgreSQL, Drizzle ORM, Supabase, server actions/API routes.
- Billing: Stripe, webhooks, subscriptions, free trials.
- Collaboration: LiveBlocks, comments, notifications.
- Email/i18n: Resend, multilingual templates, EN/DE/ES/FR/IT.
- AI: Grammar correction providers and Python integration need confirmation.
- DevOps: Docker, CI/CD needs confirmation.

## Resume Bullet Bank

- Delivered TexTutor, an AI-powered EdTech SaaS platform for Swiss teachers and students, across full-stack architecture, dashboards, authentication, billing, AI correction, and deployment workflows.
- Built complete Stripe subscription infrastructure with webhooks, trials, usage tracking, billing dashboards, and multilingual billing emails.
- Implemented multilingual product flows across English, German, French, Spanish, and Italian for user-facing UI and transactional communication.
- Integrated AI grammar correction workflows with formatting preservation, preset/rule management, usage validation, and educational feedback loops.
- Built rich assignment and feedback experiences with Lexical, LiveBlocks collaboration, comments, notifications, sharing, and PDF export.

## Site/Portfolio Angles

- Strong freelance/client delivery story.
- Good proof of end-to-end SaaS execution outside Slid/HoverNotes.
- Strong for roles needing product engineering, billing, i18n, AI features, and client ownership.

## Proof Links And Evidence

- `project_contributions/TEXTUTOR_HAMZA_CONTRIBUTIONS.md`
- `project_contributions/HAMZA_CONTRIBUTIONS2.md`
- `_data/cv.yml`
- `_pages/about.md`

## Needs Confirmation

- Whether public name should be `TexTutor`, `TextUtor`, or another spelling.
- Exact launch status.
- Source repo path and whether it can be referenced.
- Which AI providers were used.
- Public-safe wording for commit count and line count.
