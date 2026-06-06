# HoverNotes

## Metadata

- Evidence status: Repo-backed working draft; user-confirmed revenue/install metrics and U.S. company setup as of 2026-06-05/06
- Public name: HoverNotes
- Organization/client: HoverNotes, U.S. company
- Role/title: Technical Founder and CEO
- Period: Jul 2025 - Present
- Location: U.S. company; operated remotely from Seoul, South Korea
- Source repos:
  - `private-local-workspace/hovernotes/hover-notes-web-app`
  - Remote: `https://github.com/HoverNotes/hover-notes-web-app.git`
  - Related repos inferred from docs, paths need confirmation: `hover-notes-extension`, `hover-notes-llm-api`
- Existing public artifacts: `_pages/about.md`, `_data/cv.yml`, `2025-10-25-hamza-kyamanywa-openai-resume.md`

## One-Line Positioning

Founded and built HoverNotes, a U.S. company and privacy-first AI video note-taking product operated remotely from Seoul, with around 20K Chrome/Edge installs and over $10K/month revenue as of June 5, 2026, turning online videos into structured notes through a browser extension, a Next.js web app, local-first Obsidian workflows, and multimodal AI note generation.

## Context

HoverNotes is a U.S.-based privacy-first video learning platform that Hamza operates remotely from Seoul. The product spans a Chrome/Edge browser extension, a Next.js web app, local file/vault integrations, payment and subscription systems, analytics, SEO/content infrastructure, and an AI backend integration for transcript, screenshot, and multimodal note generation.

The local web app repo is currently a production Next.js app (`hover-notes`, version `1.17.17` in `package.json`) with active changelog entries through June 2026.

## Ownership

- Product strategy, architecture, implementation, and go-to-market.
- Chrome Extension for video detection/integration.
- Next.js web app for user and product workflows.
- Python FastAPI AI backend for note generation.
- AI pipelines using OpenAI GPT-4/Whisper, LangChain/LangGraph, and multilingual generation.
- Privacy-first local workflows and Obsidian integration.
- Pricing, payments, billing reliability, and region-specific monetization.
- SEO, content architecture, i18n/localization, and growth analytics.
- Production operations, debugging, telemetry, release/change management, and customer-facing stability work.

## Major Workstreams

### Product And Business

- Problem: Learners need usable notes from video learning without losing ownership of their personal knowledge base.
- What Hamza built: Privacy-first AI video note-taking SaaS from concept to production product, including the web app, extension-facing workflows, pricing, payments, analytics, and growth loops.
- Technologies: Next.js, React, TypeScript, Drizzle/PostgreSQL, Stripe, Razorpay, PostHog, Vercel Analytics, Vercel Workflows.
- Result: User confirmed on 2026-06-05 that HoverNotes is over $10K/month revenue, not pure MRR because annual subscriptions are included, with around 20K installs across Chrome and Edge. Internal product analysis shows a 20-minute free tier with about 40% conversion among users who hit the paywall, 1,629 engaged AI Notes users, and 141,548 AI Notes minutes in one 30-day analysis window.
- Evidence: User statement on 2026-06-05 for revenue/install metrics; `docs/product-research/2026-04-06-ai-notes-funnel-analysis.md` for funnel/product analytics. Confirm exact wording and precision before publishing beyond this draft.

### AI Note Generation

- Problem: Video content needs to become structured, useful study notes across languages.
- What Hamza built: Extension/web-app AI Notes flow that records learning sessions, streams status into a Lexical editor, gates legacy versus modern backend pipelines by extension version, and supports transcript-only, screenshot-aware, and multimodal note generation paths.
- Technologies: Lexical, Zustand, TypeScript, PostHog telemetry, backend AI APIs, Whisper/Groq transcription needs confirmation, OpenAI/GPT-4 needs confirmation, LangGraph/LangChain needs confirmation.
- Result: Production AI Notes workflow with active state UI, language selection, Mermaid preference, capture recovery, warning/error telemetry, async v10_1 job polling, and AI-generated editor blocks.
- Evidence: `CHANGELOG.md` entries for PRs #541-#589 especially AI Notes v10_1 async jobs, audio-only mode, Mermaid preference, capture recovery, diagnostics, telemetry, and UI improvements; `components/lexical-editor/plugins/AINotesPlugin/index.tsx`; `components/lexical-editor/nodes/TranscriptionNode.tsx`; `lib/ai-notes-request.ts`; `lib/ai-notes-pipeline.ts`.

### Multimodal Screenshots Pipeline

- Problem: Backend-side video frame extraction is slower, more expensive, and less visually faithful than using captured frames from the browser.
- What Hamza built: Cross-repo v10 AI Notes plan where the extension captures scene-change screenshots, the web app deduplicates/ranks/downsized screenshots, and the backend receives transcript plus selected segment images for multimodal generation and critique.
- Technologies: Browser capture, image deduplication, dHash, MediaPipe similarity needs confirmation, screenshot quality scoring, backend v10 payload contracts.
- Result: Flag-gated pipeline intended to reduce latency/cost and improve visual grounding by sending only high-value screenshots.
- Evidence: `docs/projects/ai-notes-audio-screenshots.md`; `components/lexical-editor/utils/imageDedup.ts`; `components/lexical-editor/utils/aiCaptureImageResolver.ts`; `lib/ai-notes-request.ts`; tests in `lib/__tests__/ai-notes-request.test.ts` and `components/lexical-editor/utils/aiCaptureImageResolver.test.ts`.

### Universal Video Compatibility

- Problem: Learners use many video platforms, not only YouTube.
- What Hamza built: Extension-facing editor and product flows designed for videos across YouTube, Udemy, Coursera, Bilibili, and other learning platforms; app copy and analytics explicitly track platform-specific behavior and drop-off.
- Technologies: Chrome/Edge extension APIs needs confirmation, iframe postMessage API, browser media workflows, TypeScript, React.
- Result: Broader platform compatibility and targeted fixes for platform-specific UX such as YouTube ad pause/resume handling, ad muting/speed restoration, and extension version nudges.
- Evidence: `HOVERNOTES_ARCHITECTURE.md`; `CHANGELOG.md` YouTube ad pause/silence/speed entries; `docs/product-research/2026-04-06-ai-notes-funnel-analysis.md` domain analysis; `lib/extension-store-versions.ts`; `lib/extension-store-urls.ts`.

### Privacy And Obsidian Integration

- Problem: Users want notes in their own local knowledge systems.
- What Hamza built: Local-first editor flow with direct Obsidian vault saving, file-management UX, local screenshot insertion, note history, auto-save/destructive-save guardrails, and vault reconnect/recovery logic.
- Technologies: File System Access API needs confirmation, iframe postMessage bridge, Lexical editor, Markdown export, local screenshot handling.
- Result: User-owned notes and images stored in local vault workflows rather than permanent cloud storage by default.
- Evidence: `HOVERNOTES_ARCHITECTURE.md`; `docs/FILE-MANAGEMENT-ARCHITECTURE.md`; `CHANGELOG.md` entries for note history, save recovery, destructive save guard, screenshot capture, and vault feedback tracking.

### Monetization And Billing Infrastructure

- Problem: A global SaaS needs payments that match regional buyer behavior and can handle recurring access reliably.
- What Hamza built: Multi-region pricing and payment system covering Stripe for global card payments, WeChat Pay/Alipay one-time passes for China, Razorpay/UPI for India, subscription status APIs, webhook handling, and Vercel Workflow-based recurring billing where Razorpay lacks native cross-border subscriptions.
- Technologies: Stripe, Razorpay, Vercel Workflows, Drizzle/PostgreSQL, R2/invoice storage needs confirmation.
- Result: Production pricing tiers for Global, East Asia, India, and China; region-specific payment options; retry/cancel flows; subscription access cleanup on terminal Stripe statuses; Razorpay workflow health/debug docs.
- Evidence: `docs/PRICING-TIERS.md`; `app/pricing/pricing-data.ts`; `lib/geo/countries-pricing-data.ts`; `app/api/checkout/route.ts`; `app/api/stripe/webhook/route.ts`; `app/api/razorpay/*`; `app/workflows/razorpay-recurring-billing.ts`; `docs/razorpay-recurring-billing-workflow.md`; `CHANGELOG.md` PRs #565-#566 and #593.

### Internationalization And Market Expansion

- Problem: Video learners are global, and the product needs localized UI, pricing, SEO, and content.
- What Hamza built: Locale system, translated UI copy across 10 supported locales, blog translation workflow, language selectors for public and extension experiences, region-specific Chinese homepage/pricing copy, and AI Notes language shortcuts.
- Technologies: Next.js App Router i18n routes, JSON locale files, translation import/export scripts, database-backed blog translations needs confirmation.
- Result: Supported locales include Korean, Chinese, Japanese, Italian, Portuguese, Russian, German, Spanish, Vietnamese, and French; public and extension copy kept aligned across locales.
- Evidence: `lib/i18n/locales/*.json`; `docs/TRANSLATION-WORKFLOW.md`; `app/[lang]/`; `CHANGELOG.md` PRs #583-#586 and #584 Chinese marketing copy.

### SEO, Content, And Discoverability

- Problem: A new product needs search visibility, canonical hygiene, structured data, localized content, and crawl control across production/staging.
- What Hamza built: Dynamic metadata/canonical helpers, sitemap/robots handling, schema markup for blog collection/articles/breadcrumbs/videos, multilingual hreflang-style metadata needs confirmation, and SEO documentation/audits.
- Technologies: Next.js metadata API, JSON-LD, MDX/blog system, robots/sitemap routes.
- Result: Canonical domain consistency for `hovernotes.io`, crawler controls for staging, schema-rich blog content, localized marketing/blog pages.
- Evidence: `lib/seo/metadata-helpers.ts`; `app/robots.ts`; `app/sitemap.ts`; `docs/SEO-SCHEMA-MARKUP.md`; `SEO-AUDIT-CURRENT-STATE.md`; `CHANGELOG.md` Chinese SEO copy and language selector entries.

### Production Reliability And Observability

- Problem: AI video capture is failure-prone across browsers, devices, store versions, ad states, network paths, and backend pipelines.
- What Hamza built: Telemetry and recovery systems for AI Notes sessions, extension diagnostics, media payload sizes, warning correlation, active-session heartbeat, fallback upload paths, old-extension routing, and customer-facing error states.
- Technologies: PostHog, browser/extension diagnostics, structured event payloads, tests, Vercel logs/workflows.
- Result: Better ability to detect active sessions, debug weak machines, correlate warning chunks to sessions, route older extensions to compatible backends, and avoid stuck editor states.
- Evidence: `CHANGELOG.md` PRs #556-#579 and #593; `docs/vercel-workflows-guide.md`; `lib/__tests__/ai-notes-request.test.ts`; `lib/__tests__/extension-store-versions.test.ts`.

## Technical Stack

- Frontend: Next.js 15, React 19, TypeScript, Tailwind CSS, Radix UI, Lexical editor, Zustand.
- Browser/extension: Chrome/Edge extension integration, iframe postMessage bridge, video capture workflows. Exact extension repo/path needs confirmation.
- Backend/API: Next.js route handlers, Drizzle ORM, PostgreSQL/Supabase, NextAuth.js, Python FastAPI AI backend needs confirmation.
- AI: OpenAI/GPT-4, Whisper/Groq transcription, LangChain, LangGraph, multimodal screenshot pipelines. Backend provider details need confirmation before final public wording.
- Payments/monetization: Stripe, Razorpay, Vercel Workflows, regional pricing, one-time passes, subscription webhooks.
- Analytics/ops: PostHog, Vercel Analytics, Vercel Speed Insights, internal product analysis scripts/docs.
- Growth/content: MDX/blog system, JSON-LD schema, sitemap/robots, locale JSON files, translation scripts.
- Integrations: Obsidian vault workflows, YouTube/Udemy/Coursera/Bilibili and other video platforms.

## Resume Bullet Bank

- Founded HoverNotes, a privacy-first AI video note-taking SaaS, growing it to over $10K/month revenue and around 20K Chrome/Edge installs while owning product strategy, architecture, implementation, and go-to-market.
- Built the production Next.js/React web app for the extension editor, subscriptions, pricing, localization, SEO, analytics, and local-first note-taking workflows.
- Architected AI Notes flows that coordinate browser capture, editor state, backend routing, asynchronous job polling, telemetry, and recovery across legacy and modern AI pipelines.
- Designed a multimodal video-in, notes-out pipeline that captures and deduplicates key frames client-side before sending selected visual context to the backend for AI note generation.
- Built local-first Obsidian vault workflows, including file save/reconnect paths, screenshot handling, note history, and guardrails against destructive auto-save behavior.
- Implemented region-aware monetization across Stripe for global card payments, WeChat Pay/Alipay one-time passes for China, and Razorpay/UPI for India, including Vercel Workflow-based recurring billing and webhook/subscription access controls.
- Used product analytics to diagnose AI Notes activation and paywall behavior, including a 30-day analysis showing about 40% conversion among users who reached the 20-minute paywall. Confirm before public use.
- Built multilingual product and content infrastructure across 10 supported locales, including localized UI copy, translated blog workflows, and market-specific Chinese SEO/pricing copy.
- Improved search visibility with canonical metadata, sitemap/robots handling, schema.org JSON-LD for blog/articles/breadcrumbs/videos, and localized marketing content.
- Added production observability for AI Notes sessions, media payloads, extension diagnostics, warning correlation, and active-session heartbeat tracking to debug cross-browser/device failures.
- Maintained release discipline through internal changelog/versioning, focused PRs, tests around AI Notes contracts and extension-version gates, and production incident docs.

## Site/Portfolio Angles

- Founder story: technical depth plus product and customer ownership.
- AI product case study: local-first AI, browser extension, video processing, and knowledge management.
- Strong for roles needing 0-to-1 ownership, AI systems architecture, or founder empathy.
- Monetization case study: region-aware pricing, Stripe/Razorpay/China payment methods, billing reliability, and paywall analytics.
- Growth case study: SEO/i18n/blog infrastructure plus measurable funnel analysis.
- Reliability case study: turning messy browser video capture into observable, recoverable product infrastructure.

## Proof Links And Evidence

- `_pages/about.md`
- `_data/cv.yml`
- `2025-10-25-hamza-kyamanywa-openai-resume.md`
- `private-local-workspace/hovernotes/hover-notes-web-app/HOVERNOTES_ARCHITECTURE.md`
- `private-local-workspace/hovernotes/hover-notes-web-app/CHANGELOG.md`
- `private-local-workspace/hovernotes/hover-notes-web-app/package.json`
- `private-local-workspace/hovernotes/hover-notes-web-app/docs/projects/ai-notes-audio-screenshots.md`
- `private-local-workspace/hovernotes/hover-notes-web-app/docs/product-research/2026-04-06-ai-notes-funnel-analysis.md`
- `private-local-workspace/hovernotes/hover-notes-web-app/docs/PRICING-TIERS.md`
- `private-local-workspace/hovernotes/hover-notes-web-app/docs/razorpay-recurring-billing-workflow.md`
- `private-local-workspace/hovernotes/hover-notes-web-app/docs/SEO-SCHEMA-MARKUP.md`
- `private-local-workspace/hovernotes/hover-notes-web-app/docs/TRANSLATION-WORKFLOW.md`
- `private-local-workspace/hovernotes/hover-notes-web-app/lib/seo/metadata-helpers.ts`
- `private-local-workspace/hovernotes/hover-notes-web-app/lib/i18n/locales/`
- `private-local-workspace/hovernotes/hover-notes-web-app/app/workflows/razorpay-recurring-billing.ts`
- `private-local-workspace/hovernotes/hover-notes-web-app/components/lexical-editor/plugins/AINotesPlugin/index.tsx`
- `private-local-workspace/hovernotes/hover-notes-web-app/components/lexical-editor/nodes/TranscriptionNode.tsx`

## Needs Confirmation

- Current status of HoverNotes.
- Exact revenue wording and whether to publish publicly: over $10K/month revenue, not MRR because annual subscriptions are included.
- Exact Chrome/Edge install count and whether to round publicly as 20K+ installs.
- Exact job title to use publicly: `Technical Founder and CEO`, `Founder`, `Founder/Engineer`, or another framing.
- Location phrasing confirmed by user on 2026-06-06: officially a U.S. company; Hamza works on it remotely from Seoul.
- Extension repo path, backend repo path, and whether they can be named.
- Backend provider details: OpenAI/GPT-4, Whisper/Groq, LangChain, LangGraph, FastAPI.
- Whether internal funnel metrics can be used publicly, and at what precision.
- Whether period should still be `Present`.
