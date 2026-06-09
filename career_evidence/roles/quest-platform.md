# Quest Travel Planning Platform

## Metadata

- Evidence status: Verified local repo and user-stated CTO/co-founder role, 3-person team leadership, Kampala/Uganda setup, and remote-from-Seoul work location; exact dates need confirmation
- Public name: Quest Travel Planning Platform
- Organization/client: Quest, Kampala, Uganda
- Public URL: https://questheaven.com
- Role/title: CTO and Co-founder
- Period: 2026 - Present needs confirmation
- Location: Remote, Kampala (Uganda)
- Source repo: `private-local-workspace/quest/quest-web-app`
- Repo remote: `https://github.com/questdev-canine/quest-web-app.git`
- Existing public artifacts: Not yet integrated into site/resume

## One-Line Positioning

Co-founded and leads technology for Quest (https://questheaven.com), a Kampala, Uganda-based travel planning platform for tour and travel companies. Quest helps operators prepare trips from shared and company-specific destination data, plan itineraries, price trips accurately, and turn those plans into quotes, documents, emails, and marketing materials while Hamza works remotely from Seoul.

## Context

Quest is a Kampala, Uganda-based web application for tour and travel companies in Uganda and East Africa. The platform supports Quest/admin operations, operator dashboards, company onboarding, destination and activity databases, accommodation/transport data, travel requests, itinerary building, quote generation, automated travel document generation, marketing content, quote email delivery, PDF previews/exports, tourist tracking, billing, and analytics.

User clarification on 2026-06-06: describe Quest as travel planning software, not just safari quotation software or PDF infrastructure. The quote/PDF/email layer is an important output surface, but the larger product is the operational system around destination data, trip preparation, itineraries, accurate pricing, documents, and marketing materials for tour/travel companies.

## Ownership

- Platform application development across Next.js App Router, TypeScript, Tailwind CSS, shadcn/ui, PostgreSQL/Supabase, Drizzle ORM, NextAuth v5, and Resend.
- Admin panel systems for managing the travel data layer: destinations, activities, hotels/lodges, room rates, transport, companies, users, settings, categories, geography, and reusable content.
- Operator dashboard workflows for travel requests, itinerary creation, pricing, quote generation, travel documentation, marketing materials, quote email delivery, PDF preview/export, content libraries, analytics, billing, and tourist tracking.
- Product and architecture decisions around company-scoped content, destination data, trial/subscription gating, output monetization, Stripe billing, exchange rates, document infrastructure, and release workflow.
- Leadership of a 3-person engineering/product team.
- Deployment workflow and branch promotion process for shared QA, personal QA branches, and production releases.

## Major Workstreams

### Platform Architecture

- Problem: Tour and travel companies need structured software for preparing trips, reusing destination data, building itineraries, pricing travel plans accurately, and turning those plans into customer-facing materials.
- What Hamza built: Next.js 16 App Router application with typed database access, role-based surfaces, company onboarding, operator dashboards, destination/activity/accommodation/transport data, itinerary workflows, quote/document/marketing workflows, analytics, and billing surfaces.
- Technologies: Next.js 16, React 19, TypeScript, Tailwind CSS 4, shadcn/ui, Drizzle ORM, PostgreSQL/Supabase.
- Result: Production platform foundation for Quest's travel planning operations, destination-data workflows, operator content layer, customer-facing outputs, and SaaS launch path.
- Evidence: `quest-web-app/README.md`, `package.json`, `src/app`, `src/db`, `docs/progress/hamza/CURRENT.md`.

### Authentication And Roles

- Problem: Quest requires separate access patterns for internal admins, tour operators, and future partner users.
- What Hamza built: Role-aware app structure using NextAuth v5 and protected app/admin surfaces.
- Technologies: NextAuth v5, PostgreSQL, Drizzle ORM, middleware/server routes.
- Result: Admin and operator workflows can be separated cleanly.
- Evidence: `quest-web-app/README.md` role table and project structure.

### Travel Planning And Quote Workflows

- Problem: Operators need to convert travel requests into concrete trip plans, itineraries, accurate prices, documents, and customer-facing quote/marketing materials.
- What Hamza built: Operator dashboard architecture for requests, tourists, itinerary planning, destination selection, accommodation/activity/transport selection, pricing, quote generation, PDF preview/export, quote email delivery, and reusable travel content.
- Technologies: Next.js App Router, server actions/API routes, database models.
- Result: Workflow support for quote creation and management.
- Evidence: `quest-web-app/README.md`; `src/app/app/quotes`; `src/app/app/requests`; `src/app/app/tourists`; `docs/progress/hamza/CURRENT.md`.

### Product Strategy, Monetization, And Billing

- Problem: Quest needs a launch model that gives operators enough freedom to build quotes while monetizing professional outputs.
- What Hamza built: Free + Pro pricing strategy and Stripe implementation plan where company-level subscriptions, full-access trials, checkout/webhook sync, billing settings, plan badges, and feature gates unlock clean PDFs, quote emails, and advanced branding.
- Technologies: Stripe, PostHog, Next.js route handlers/server actions, Drizzle, company subscription fields.
- Result: SaaS monetization architecture adapted from HoverNotes patterns while preserving Quest-specific company ownership and trial logic.
- Evidence: `docs/reference/stripe-pricing-subscriptions.md`; `docs/progress/hamza/CURRENT.md`; `src/app/pricing`; `src/app/app/settings/billing`; `src/app/api/stripe/webhook`.

### Travel Documentation And Email Delivery

- Problem: Travel companies need professional, branded trip documents and a way to send travel plans, quotes, and related materials to travelers from the platform.
- What Hamza built: Travel document and quote PDF integration with preview/edit flows, page settings, R2-backed assets, quote email composer with Resend, merge tags, branded sender domains, logo controls, and PDF attachments.
- Technologies: PDF service integration, Cloudflare R2, Resend, Next.js server actions, typed PDF data transforms.
- Result: Operators can compose branded quote emails and deliver generated quote PDFs through Quest workflows.
- Evidence: `docs/progress/hamza/CURRENT.md`; `docs/progress/pdf-generation-plan.md`; `src/lib/pdf/transform-quote-to-pdf.ts`; `src/lib/email/*`; `quote-email-actions.ts`.

### Destination Data And Content Management

- Problem: Travel planning quality depends on structured destination, activity, hotel/lodge, room-rate, transport, geography, company, and content data across Uganda and East Africa.
- What Hamza built: Admin and operator content-management areas plus seed/import/update scripts for travel-domain data, including destination/activity/accommodation/transport content, entry fees, room rates, vehicle data, images, themes, vehicles, staff, reviews, and company-specific settings.
- Technologies: Drizzle ORM, PostgreSQL, TypeScript scripts.
- Result: Maintainable travel-data foundation for the platform and a path toward company-scoped planning, itinerary, and marketing content on top of Quest defaults.
- Evidence: `quest-web-app/package.json` scripts; `README.md` admin panel list; `src/db/schema/destinations.ts`; `src/db/schema/activities.ts`; `src/db/schema/hotels.ts`; `src/db/schema/transport.ts`; `src/app/app/content-library`; `src/app/admin`; `docs/progress/hamza/CURRENT.md`.

### Pricing And Quote Economics

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

- Co-founded Quest and leads technology as CTO, leading a 3-person engineering/product team building a Next.js 16 travel planning platform for tour and travel companies in Uganda.
- Built operator workflows that turn travel requests and destination data into itineraries, accurate pricing, branded quotes, trip documents, quote emails, reusable content, and marketing materials.
- Designed role-aware platform surfaces for Quest admins and tour operators using NextAuth v5, PostgreSQL/Supabase, and Drizzle ORM.
- Implemented structured data workflows for destinations, activities, hotels/lodges, room rates, transport, geography, companies, travelers, and users to improve trip planning, pricing accuracy, and operational maintainability.
- Designed Quest's Free + Pro launch model with company-level Stripe subscriptions, full-access trials, billing settings, plan badges, and output-level feature gates for clean PDFs/email/branding.
- Built travel document, quote PDF, and email delivery workflows with R2-backed assets, Resend, branded sender domains, merge tags, page settings, preview regeneration, and PDF service integration.
- Established Vercel-based deployment and branch promotion workflow across feature branches, personal QA branches, shared QA, release branches, and production.

## Site/Portfolio Angles

- Useful as a portfolio case study for domain-specific B2B SaaS in travel/tourism.
- Strong angle: full-stack product engineering for a real operational platform, not a generic demo.
- Strong angle: data-heavy travel planning workflows with destination databases, itinerary generation, pricing, documents, and admin/operator surfaces.

## Proof Links And Evidence

- Local repo: `private-local-workspace/quest/quest-web-app`
- Repo README describes product, stack, user roles, admin panel, operator dashboard, and deployment workflow.

## Needs Confirmation

- Exact start month and whether to use `2026 - Present` or a specific month.
- Exact public role title: user stated CTO and co-founder.
- Location phrasing confirmed by user on 2026-06-06: Quest is set up in Kampala, Uganda, and Hamza works on it remotely from Seoul.
- Launch status, customer/user scale, and any measurable business outcomes.
- Which features Hamza personally built versus inherited.
