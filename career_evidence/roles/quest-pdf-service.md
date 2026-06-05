# Quest PDF Service

## Metadata

- Evidence status: Verified local repo and user-stated CTO/co-founder role, dates need confirmation
- Public name: Quest PDF Service
- Organization/client: Quest
- Role/title: CTO and Co-founder / PDF infrastructure owner
- Period: 2026 - Present needs confirmation
- Location: Needs confirmation
- Source repo: `private-local-workspace/quest/quest-pdf-service`
- Existing public artifacts: Not yet integrated into site/resume

## One-Line Positioning

Led the PDF infrastructure for Quest, building a production microservice that turns quote JSON into branded, paginated A4 safari quote PDFs, previews, and stored outputs in Cloudflare R2.

## Context

Quest needs professional quote documents for safari operators and travelers. The web app sends structured quote data to this service, which renders branded templates, paginates content, generates PDFs in headless Chrome, and uploads the result to Cloudflare R2.

The PDF service is part of the broader Quest CTO/co-founder role and pairs with the web app's quote builder, page settings, preview/edit drawers, quote email workflow, R2 asset handling, and output-level monetization.

## Ownership

- Express/TypeScript service for PDF generation endpoints.
- Handlebars template architecture with modular page partials.
- Browser-based pre-pagination engine for A4 document layout.
- Puppeteer orchestration for PDF generation.
- Cloudflare R2 upload/delete storage integration.
- Per-page preview and screenshot-generation support.
- Signature background-removal endpoint for handwritten signatures.
- Docker/Hetzner deployment workflow.

## Major Workstreams

### Quote PDF Rendering

- Problem: Quest needs pixel-perfect safari quote documents from structured app data.
- What Hamza built: JSON-to-HTML-to-PDF pipeline using Handlebars templates and Puppeteer.
- Technologies: Node.js 20, TypeScript, Express, Handlebars, Puppeteer.
- Result: Quote data can be converted into branded PDFs via `/generate-pdf` and supporting preview flows.
- Evidence: `quest-pdf-service/README.md`, `src/server.ts`, `src/pdf-generator.ts`, `template/`.

### Pre-Pagination Engine

- Problem: Dynamic itinerary and pricing content can overflow fixed A4 pages.
- What Hamza built: In-browser pagination that measures rendered content, splits overflowing pages, adds continuation headers, and controls footers.
- Technologies: Puppeteer, browser DOM measurement, TypeScript.
- Result: More reliable document output for variable-length safari quotes.
- Evidence: `quest-pdf-service/README.md`, `src/paginator.ts`.

### Template System

- Problem: Quote PDFs need reusable pages and configurable order.
- What Hamza built: Modular Handlebars partials for cover, summary, itinerary, pricing, terms, vehicles, about, and back cover, with theme support.
- Technologies: Handlebars, CSS variables, TypeScript helpers.
- Result: Reusable branded document system with per-company customization.
- Evidence: `quest-pdf-service/README.md`, `src/template-engine.ts`, `template/partials`.

### Storage And Environments

- Problem: Generated PDFs need durable public storage with separate dev/prod targets.
- What Hamza built: Cloudflare R2 upload/delete integration with company folder structure and request-level storage target switching.
- Technologies: Cloudflare R2, S3-compatible SDK, Express.
- Result: Generated PDFs are stored and returned as public URLs, with dev/prod bucket separation.
- Evidence: `quest-pdf-service/README.md`, `src/r2.ts`.

### Signature Processing

- Problem: Operators may need clean handwritten signatures in quote PDFs.
- What Hamza built: `/process-signature` endpoint for signature background removal.
- Technologies: Node.js image processing pipeline. Exact library needs confirmation.
- Result: Better-looking branded PDFs with clean signature assets.
- Evidence: `quest-pdf-service/README.md`, `src/signature.ts`.

## Technical Stack

- Backend: Node.js 20, TypeScript, Express.
- Rendering: Puppeteer, Handlebars, browser DOM measurement.
- Storage: Cloudflare R2.
- Deployment: Docker, Hetzner.
- Templates: HTML/CSS, Handlebars partials, CSS variables.

## Resume Bullet Bank

- Built Quest's PDF generation microservice, converting quote JSON into branded A4 safari quote PDFs with Puppeteer, Handlebars, and TypeScript.
- Designed a pre-pagination engine that measures rendered content in headless Chrome, splits overflowing itinerary/pricing sections, and injects continuation headers and controlled footers.
- Implemented Cloudflare R2 upload/delete workflows with dev/prod storage targeting and company-scoped folder organization.
- Created modular quote templates with configurable page order, company theming, full-bleed covers, itinerary pages, pricing pages, terms, vehicles, about pages, back covers, and per-page previews.

## Site/Portfolio Angles

- Strong case study for document-generation infrastructure and layout engineering.
- Good complement to Quest platform entry: web app plus specialized PDF microservice.
- Useful for showing backend craft beyond standard CRUD apps.

## Proof Links And Evidence

- Local repo: `private-local-workspace/quest/quest-pdf-service`
- Repo README documents features, endpoints, architecture, storage, and deployment.

## Needs Confirmation

- Exact start/end period.
- Public role title: user stated CTO and co-founder.
- Whether generated PDFs are live in production and at what volume.
- Signature image-processing implementation details and any measurable quality/support outcomes.
