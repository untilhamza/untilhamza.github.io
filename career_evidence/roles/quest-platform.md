# Quest Safari Quotation Platform

## Metadata

- Evidence status: Verified local repo and user-stated CTO/co-founder role and 3-person team leadership, exact dates need confirmation
- Public name: Quest Safari Quotation Platform
- Organization/client: Quest
- Public URL: https://questheaven.com
- Role/title: CTO and Co-founder
- Period: 2026 - Present needs confirmation
- Location: Needs confirmation
- Source repo: `private-local-workspace/quest/quest-web-app`
- Repo remote: `https://github.com/questdev-canine/quest-web-app.git`
- Existing public artifacts: Not yet integrated into site/resume

## One-Line Positioning

Co-founded and leads technology for Quest (https://questheaven.com), a production Next.js platform that helps Uganda-based tour operators create accurate safari quotations, manage itinerary data, deliver branded quotes, and run operator-facing quote workflows.

## Context

Quest is a web application for Uganda-based tour operators. The platform supports Quest/admin operations, operator dashboards, company onboarding, document verification, content libraries, travel requests, itinerary building, quote generation, quote email delivery, PDF previews/exports, tourist tracking, billing, and analytics.

## Ownership

- Platform application development across Next.js App Router, TypeScript, Tailwind CSS, shadcn/ui, PostgreSQL/Supabase, Drizzle ORM, NextAuth v5, and Resend.
- Admin panel systems for managing platform data such as destinations, activities, hotels/lodges, transport, companies, users, settings, categories, and geography.
- Operator dashboard workflows for travel requests, itinerary creation, quote generation, quote email delivery, PDF preview/export, content libraries, analytics, billing, and tourist tracking.
- Product and architecture decisions around company-scoped content, trial/subscription gating, quote output monetization, Stripe billing, exchange rates, PDF infrastructure, and release workflow.
- Leadership of a 3-person engineering/product team.
- Deployment workflow and branch promotion process for shared QA, personal QA branches, and production releases.

## Major Workstreams

### Platform Architecture

- Problem: Tour operators need fast, accurate, structured safari quotation workflows.
- What Hamza built: Next.js 16 App Router application with typed database access, role-based surfaces, company onboarding, operator dashboards, content libraries, quote workflows, analytics, and billing surfaces.
- Technologies: Next.js 16, React 19, TypeScript, Tailwind CSS 4, shadcn/ui, Drizzle ORM, PostgreSQL/Supabase.
- Result: Production platform foundation for Quest's quotation operations and SaaS launch path.
- Evidence: `quest-web-app/README.md`, `package.json`, `src/app`, `src/db`, `docs/progress/hamza/CURRENT.md`.

### Authentication And Roles

- Problem: Quest requires separate access patterns for internal admins, tour operators, and future partner users.
- What Hamza built: Role-aware app structure using NextAuth v5 and protected app/admin surfaces.
- Technologies: NextAuth v5, PostgreSQL, Drizzle ORM, middleware/server routes.
- Result: Admin and operator workflows can be separated cleanly.
- Evidence: `quest-web-app/README.md` role table and project structure.

### Quote Operations

- Problem: Operators need to convert travel requests into itineraries and quotes.
- What Hamza built: Operator dashboard architecture for requests, tourists, itineraries, pricing, quote generation, PDF preview/export, and quote email delivery.
- Technologies: Next.js App Router, server actions/API routes, database models.
- Result: Workflow support for quote creation and management.
- Evidence: `quest-web-app/README.md`; `src/app/app/quotes`; `src/app/app/requests`; `src/app/app/tourists`; `docs/progress/hamza/CURRENT.md`.

### Product Strategy, Monetization, And Billing

- Problem: Quest needs a launch model that gives operators enough freedom to build quotes while monetizing professional outputs.
- What Hamza built: Free + Pro pricing strategy and Stripe implementation plan where company-level subscriptions, full-access trials, checkout/webhook sync, billing settings, plan badges, and feature gates unlock clean PDFs, quote emails, and advanced branding.
- Technologies: Stripe, PostHog, Next.js route handlers/server actions, Drizzle, company subscription fields.
- Result: SaaS monetization architecture adapted from HoverNotes patterns while preserving Quest-specific company ownership and trial logic.
- Evidence: `docs/reference/stripe-pricing-subscriptions.md`; `docs/progress/hamza/CURRENT.md`; `src/app/pricing`; `src/app/app/settings/billing`; `src/app/api/stripe/webhook`.

### Quote PDF And Email Delivery

- Problem: Safari operators need professional, branded quote documents and a way to send them to travelers from the platform.
- What Hamza built: Quote PDF integration with preview/edit flows, page settings, R2-backed assets, quote email composer with Resend, merge tags, branded sender domains, logo controls, and PDF attachments.
- Technologies: PDF service integration, Cloudflare R2, Resend, Next.js server actions, typed PDF data transforms.
- Result: Operators can compose branded quote emails and deliver generated quote PDFs through Quest workflows.
- Evidence: `docs/progress/hamza/CURRENT.md`; `docs/progress/pdf-generation-plan.md`; `src/lib/pdf/transform-quote-to-pdf.ts`; `src/lib/email/*`; `quote-email-actions.ts`.

### Data Management

- Problem: Safari quote accuracy depends on structured destination, activity, hotel, room-rate, transport, company, and user data.
- What Hamza built: Admin and operator content-management areas plus seed/import/update scripts for domain data, including destination/activity/accommodation/transport content, images, themes, vehicles, staff, reviews, and company-specific settings.
- Technologies: Drizzle ORM, PostgreSQL, TypeScript scripts.
- Result: Maintainable data foundation for the platform and a path toward company-scoped content libraries on top of Quest defaults.
- Evidence: `quest-web-app/package.json` scripts; `README.md` admin panel list; `src/app/app/content-library`; `src/app/admin`; `docs/progress/hamza/CURRENT.md`.

### Exchange Rates And Quote Economics

- Problem: Uganda tour operators quote travelers in USD while many operating costs are in UGX.
- What Hamza built: USD/UGX exchange-rate settings, live/manual rate refresh, daily cron behavior, and transport fuel cost conversion into quote pricing.
- Technologies: Next.js, Drizzle/PostgreSQL, Open Exchange Rates needs confirmation, cron routes.
- Result: Quotes can show more accurate local-cost-to-client-price calculations for transport and fuel.
- Evidence: `docs/reference/exchange-rates.md`; `docs/progress/hamza/CURRENT.md`; `src/app/api/cron/update-exchange-rates`.

### Release And Deployment Workflow

- Problem: Quest needs a reliable shared QA and production release process.
- What Hamza built: Vercel-oriented deployment scripts and documented branch promotion workflow using `test`, release branches, and production promotion.
- Technologies: Vercel, shell scripts, Git workflow.
- Result: Clear handoff path for feature QA and production releases.
- Evidence: `quest-web-app/README.md` deployment and branch promotion sections.

## Technical Stack

- Frontend: Next.js 16, React 19, TypeScript, Tailwind CSS 4, shadcn/ui, Radix UI, dnd-kit, TipTap.
- Backend: Next.js App Router, API routes, server-side logic.
- Data: PostgreSQL, Supabase, Drizzle ORM, migrations and seed scripts.
- Auth: NextAuth v5, Google OAuth.
- Email/analytics/payments: Resend, PostHog, Stripe.
- Storage/media: Cloudflare R2, image upload/crop workflows, PDF preview screenshots.
- Deployment: Vercel, documented branch promotion workflow.

## Resume Bullet Bank

- Co-founded Quest and leads technology as CTO, leading a 3-person engineering/product team building a Next.js 16 safari quotation platform for Uganda-based tour operators.
- Built operator workflows for travel requests, tourists, itinerary planning, quote generation, PDF preview/export, quote email delivery, billing, analytics, and content libraries.
- Designed role-aware platform surfaces for Quest admins and tour operators using NextAuth v5, PostgreSQL/Supabase, and Drizzle ORM.
- Implemented structured data workflows for destinations, activities, hotels, room rates, transport, companies, and users to improve quote accuracy and operational maintainability.
- Designed Quest's Free + Pro launch model with company-level Stripe subscriptions, full-access trials, billing settings, plan badges, and output-level feature gates for clean PDFs/email/branding.
- Built quote PDF and email delivery workflows with R2-backed assets, Resend, branded sender domains, merge tags, page settings, preview regeneration, and PDF service integration.
- Established Vercel-based deployment and branch promotion workflow across feature branches, personal QA branches, shared QA, release branches, and production.

## Site/Portfolio Angles

- Useful as a portfolio case study for domain-specific B2B SaaS in travel/tourism.
- Strong angle: full-stack product engineering for a real operational platform, not a generic demo.
- Strong angle: data-heavy quote generation workflows with admin and operator surfaces.

## Proof Links And Evidence

- Local repo: `private-local-workspace/quest/quest-web-app`
- Repo README describes product, stack, user roles, admin panel, operator dashboard, and deployment workflow.

## Needs Confirmation

- Exact start month and whether to use `2026 - Present` or a specific month.
- Exact public role title: user stated CTO and co-founder.
- Launch status, customer/user scale, and any measurable business outcomes.
- Which features Hamza personally built versus inherited.
