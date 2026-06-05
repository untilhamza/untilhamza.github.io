# JonjaBird

## Metadata

- Evidence status: Verified local business workspace; public framing and metrics need confirmation
- Public name: JonjaBird
- Organization/client: JonjaBird / HOVERNOTES LLC product line needs confirmation
- Role/title: Founder, product operator, and automation engineer
- Period: Mar 2026 - Present needs confirmation
- Location: Seoul, South Korea
- Source workspace:
  - `private-local-workspace/inmate-letters-business`
- Existing public artifacts: Not yet integrated into site/resume
- Private/internal artifacts:
  - `business-docs/`
  - `client-accounts/`
  - `templates/`
  - `scripts/`

## One-Line Positioning

Founded and operationalized JonjaBird, a hybrid physical-digital mail and support service for foreign inmates in South Korea and their overseas sponsors, combining service design, pricing strategy, legal/privacy docs, client ledgers, and Python/WeasyPrint document automation.

## Context

JonjaBird serves a communication gap for non-Korean inmates in Korean correctional facilities. Inmates have no internet access and international families often cannot reliably manage Korean prison mail, printing, address formatting, translation, payments, or account visibility.

The current operating model is a manual MVP: inbound inmate letters are received and scanned, sponsors receive digital copies, sponsor replies are printed and mailed back through Korean post, and related charges/deposits are tracked through client account ledgers and generated PDFs. The workspace also contains the spec for a future sponsor/admin portal that would migrate the Excel ledger and PDF workflow into a Next.js + FastAPI system.

## Ownership

- Founder/operator for the service concept, launch plan, customer workflows, and operating docs.
- Business analysis across market sizing, competitor comparison, pricing, unit economics, legal/privacy posture, and service catalog design.
- Customer-facing materials: intro letters, service forms, terms, tone guide, multilingual one-pagers, receipts, deposit confirmations, account statements, and typed/translated client documents.
- Operations system for client account ledgers, receipt/deposit/statement numbering, credit balances, service charges, and auditability.
- Python PDF automation using WeasyPrint, openpyxl, shared font handling, and reusable script conventions.
- Future platform architecture/spec for sponsor portal, admin queue, deposits, ledgers, receipts/statements, payments, storage, and document-processing service boundaries.

## Major Workstreams

### Business And Service Design

- Problem: Foreign inmates in Korea need a reliable bridge to sponsors abroad, and sponsors need proof that letters, services, and funds are being handled transparently.
- What Hamza built: A full operating model for letter forwarding, AI research, typing/transcription, court-document translation, photo printing, money transfer support, credits, statements, and heavy printed-package pricing.
- Technologies/process: Business docs, pricing model, service catalog, changelog decision log, operational playbooks, customer-facing forms, and private client account trackers.
- Result: A real service system with clear workflows, pricing logic, grandfathering rules, package rules, and customer-facing documentation.
- Evidence: `business-docs/01-business-overview.md`, `03-pricing-model.md`, `05-operational-plan.md`, `10-onboarding-playbook.md`, `12-service-catalog.md`, `CHANGELOG.md`.

### Pricing, Unit Economics, And Trust Model

- Problem: Sponsors need transparent, itemized spending, while the business needs pricing that covers Korean postage, printing, handling, and operational risk.
- What Hamza built: Pricing revisions that moved the service away from commodity postage, bundled tracked express mail into core services, introduced a credit/balance model, separated money transfers from JonjaBird credits, and added a large printed-package rule for high-page-count packets.
- Technologies/process: Pricing model spreadsheet, markdown pricing model, change-log governance, customer-specific grandfathering, ledger/statement alignment.
- Result: Current pricing model documents per-service margins, market comparisons, order examples, overage rules, and the distinction between service credits and inmate-bank money transfers.
- Evidence: `business-docs/03-pricing-model.md`, `business-docs/CHANGELOG.md`, `business-docs/pricing-revenue-model.xlsx`.

### Document Automation And Audit Trail

- Problem: A sensitive mail/payment service needs clean proof of charges, deposits, balances, and account history without hand-making every PDF.
- What Hamza built: Python + WeasyPrint PDF templates for service receipts and credit deposit confirmations, plus a statement generator that reads `.xlsx` credit trackers and produces branded account statements.
- Technologies: Python, WeasyPrint, openpyxl, HTML/CSS PDF layouts, local font stack, file-path-safe script conventions.
- Result: Reusable generation workflow for service receipts (`JB-2026-XXXX`), deposit confirmations (`DEP-2026-XXXX`), and statements (`STMT-2026-XXXX`) with output folders, numbering rules, and PDF gotchas documented.
- Evidence: `scripts/README.md`, `templates/generate_receipt.py`, `templates/generate_deposit_confirmation.py`, `scripts/build_statement.py`, `client-accounts/receipts/`, `client-accounts/deposit-confirmations/`, `client-accounts/statements/`.

### Client Account Operations

- Problem: Sponsors and inmates need balances and service activity that reconcile with payments and PDF artifacts.
- What Hamza built: Client account trackers and a workflow that keeps deposits and charges as separate ledger rows, aligns balances with receipts/deposit confirmations, and produces statements from the same source data.
- Technologies/process: Excel `.xlsx` credit trackers, generated PDFs, sequential document numbering, manual deposit confirmation flow.
- Result: Private client account files exist for ABU Donzo, Giedrius Voronovic, and Jacek Polanski, with receipt outputs visible through June 2026.
- Evidence: `client-accounts/abu-donzo-credit-tracker.xlsx`, `client-accounts/giedrius-voronovic-credit-tracker.xlsx`, `client-accounts/jacek-polanski-credit-tracker.xlsx`, `client-accounts/receipts/`.

### AI-Assisted Prisoner Services

- Problem: Inmates lack internet access and often need research, typing, translation, or document prep that is difficult to request from prison.
- What Hamza built: Service definitions and one-off deliverables for AI research, handwritten-to-typed documents, legal/court document translation, address overlays, bilingual questionnaire translation, and prison-mail packages.
- Technologies: AI-assisted drafting/transcription/translation, Python PDF generation, bilingual formatting, Korean/English document workflows.
- Result: The workspace contains concrete generated client deliverables, including typed legal/court documents, Korean translations, research reports, and bilingual client materials.
- Evidence: `business-docs/12-service-catalog.md`, `client-accounts/abu-donzo/`, `client-accounts/typed-letters/`, `scripts/build_sam_research_js.py`, `scripts/build_sam_sexed_translation.py`, `scripts/generate_clemency_letter_abu_danzo.py`, `scripts/generate_clemency_letter_abu_danzo_korean.py`.

### Future Sponsor/Admin Platform Spec

- Problem: Manual operation works for seed clients but will not scale once sponsor submissions, deposits, scans, charges, and statements grow.
- What Hamza built: A living web app spec for sponsor signup, inmate profiles, letter/photo submission, pay-at-send, credit loading, manual deposit fallback, admin queue, scanned replies, ledgers, receipts/statements, and future OCR/translation/AI pipelines.
- Technologies planned: Next.js App Router, TypeScript, FastAPI, WeasyPrint, Postgres, Prisma, S3-compatible storage, Stripe, Wise/manual deposit fallback, Resend/Postmark, Vercel, Fly.io/Railway.
- Result: The spec preserves compatibility between today's `.xlsx` ledger/PDF scripts and the eventual DB-backed portal.
- Evidence: `business-docs/19-web-app-spec.md`, especially sections 3, 4, 5, 6, and 8.

## Metrics And Outcomes

- Generated service receipts:
  - Status: Verified local artifacts and script README numbering.
  - Evidence: `client-accounts/receipts/`, `scripts/README.md`.
  - Public wording: "Built an auditable receipt workflow with sequential service receipts through `JB-2026-0016`." Confirm whether to expose numbering publicly.
- Deposit confirmations:
  - Status: Verified workflow; artifact visibility varies by local folder state.
  - Evidence: `templates/generate_deposit_confirmation.py`, `scripts/README.md`, `client-accounts/deposit-confirmations/`.
  - Public wording: "Separated service receipts from credit deposit confirmations to make sponsor balances easier to audit."
- Client account system:
  - Status: Verified local files.
  - Evidence: `client-accounts/*-credit-tracker.xlsx`.
  - Public wording: "Maintained client credit ledgers that reconcile deposits, charges, balances, receipts, and statements."
- Pricing/unit economics:
  - Status: Verified docs; exact public metrics need approval.
  - Evidence: `business-docs/03-pricing-model.md`, `CHANGELOG.md`.
  - Public wording: "Designed pricing and unit economics for a specialized mail-and-document service with tracked Korean postal delivery."
- Customer/client count:
  - Status: Needs confirmation before public use.
  - Evidence: `client-accounts/` suggests multiple named clients, but names are private.
  - Public wording: "Supported early paying clients" only if Hamza confirms wording and privacy posture.

## Technical Stack

- Business/docs: Markdown, Excel `.xlsx`, generated PDFs, changelog-driven decision log.
- Automation: Python, WeasyPrint, openpyxl, HTML/CSS for PDF layouts.
- Document generation: A5 receipts/deposit confirmations, account statements, service forms, one-pagers, bilingual letters.
- AI/document work: AI-assisted research, transcription, translation, legal/court document prep.
- Payments/ledger: Manual deposit confirmation, Wise, Stripe planned/available via existing infrastructure, credit balances, money-transfer fee model.
- Future app: Next.js App Router, TypeScript, FastAPI, Postgres, Prisma, S3-compatible storage, Stripe Checkout, Resend/Postmark, Vercel, Fly.io/Railway.
- Operations: Korean post workflows, prison mail addressing, package restrictions, sponsor/inmate service agreements, privacy/data-retention rules.

## Resume Bullet Bank

- Founded JonjaBird, a hybrid physical-digital mail and support service helping foreign inmates in South Korea communicate with sponsors abroad through scanned letters, printed replies, payments, and document support.
- Designed the end-to-end operating system for inmate intake, sponsor onboarding, letter forwarding, service requests, credit balances, money transfers, statements, and customer-facing terms.
- Built Python/WeasyPrint automation for branded service receipts, credit deposit confirmations, and account statements, with sequential numbering and reusable output conventions.
- Created client credit-ledger workflows that separate deposits from service charges and reconcile balances against receipts, deposit confirmations, and generated statements.
- Developed pricing and unit-economics models for letter forwarding, AI research, transcription, translation, photo printing, money transfers, and large printed mail packages.
- Authored a future sponsor/admin portal spec mapping today's Excel/PDF workflow into a Next.js + FastAPI architecture with Stripe payments, admin queueing, Postgres ledgers, file storage, and WeasyPrint PDF endpoints.
- Produced AI-assisted research, transcription, translation, and bilingual document deliverables for real inmate support workflows under strict accuracy and privacy constraints.
- Established operational governance through a changelog, service catalog, tone guide, legal/privacy terms, onboarding playbook, and PDF generation README.

## Site/Portfolio Angles

- Founder/operator case study: turning a painful, real-world communication gap into a working service with docs, money flows, and artifacts.
- Product-systems case study: operational workflows first, then a future platform spec that cleanly maps manual state into software.
- Automation case study: using Python PDF generation and spreadsheets to make a sensitive manual service auditable before building a full app.
- AI-for-operations case study: practical AI research/transcription/translation for people with no internet access, framed carefully because some content is legal-adjacent.
- Strong for roles needing founder empathy, complex workflow design, compliance-aware product thinking, and boring-but-critical internal tools.

## Proof Links And Evidence

- `private-local-workspace/inmate-letters-business/business-docs/01-business-overview.md`
- `private-local-workspace/inmate-letters-business/business-docs/03-pricing-model.md`
- `private-local-workspace/inmate-letters-business/business-docs/05-operational-plan.md`
- `private-local-workspace/inmate-letters-business/business-docs/10-onboarding-playbook.md`
- `private-local-workspace/inmate-letters-business/business-docs/12-service-catalog.md`
- `private-local-workspace/inmate-letters-business/business-docs/16-terms-and-conditions.md`
- `private-local-workspace/inmate-letters-business/business-docs/17-style-and-tone-guide.md`
- `private-local-workspace/inmate-letters-business/business-docs/19-web-app-spec.md`
- `private-local-workspace/inmate-letters-business/business-docs/CHANGELOG.md`
- `private-local-workspace/inmate-letters-business/scripts/README.md`
- `private-local-workspace/inmate-letters-business/templates/generate_receipt.py`
- `private-local-workspace/inmate-letters-business/templates/generate_deposit_confirmation.py`
- `private-local-workspace/inmate-letters-business/scripts/build_statement.py`
- `private-local-workspace/inmate-letters-business/client-accounts/`

## Needs Confirmation

- Whether JonjaBird should be public on the site/resume at all, given privacy and legal-adjacent sensitivity.
- Public role title: `Founder`, `Founder/Operator`, `Product Founder`, `Founder and Automation Engineer`, or another framing.
- Period and whether to present it as active.
- Whether to name HOVERNOTES LLC as the operating entity.
- Which client count/revenue/payment metrics are safe to publish.
- Whether to mention "inmates," "incarcerated people," or a softer public phrase depending on audience.
- Whether to include client-facing legal/court-document work on a resume, or keep it as private evidence only.
- Whether to publish any pricing details or only describe pricing/unit-economics work generally.
