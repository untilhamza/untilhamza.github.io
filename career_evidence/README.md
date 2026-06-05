# Career Evidence Bank

This folder is the working source of truth for updating Hamza's personal site, portfolio, and resumes.

The public site files are polished outputs. The files here are the detailed input layer: role history, project scope, dates, metrics, technical decisions, evidence links, and candidate-ready bullet material.

## How To Use This Folder

Before editing the site or resume:

1. Read `index.yml` to see the role/project map.
2. Open the relevant file in `roles/`.
3. If updating a resume, review `resume_ai_extractions/` for notes on what automated systems preserved or missed.
4. Use claims marked `Verified` or backed by local repo/report evidence directly.
5. Treat `Needs confirmation` as draft material. Confirm it with Hamza or stronger evidence before publishing.
6. If a new role, project, or achievement appears, create a new file from `_TEMPLATE.md`.

## Evidence Levels

- `Verified` - supported by a local repo, existing resume, contribution report, public link, or explicit user statement.
- `Strong draft` - likely true based on existing materials but should be checked before prominent use.
- `Needs confirmation` - useful candidate language that requires Hamza's review before publishing.

## Files

- `index.yml` - machine-readable map of roles/projects and where to find source material.
- `_TEMPLATE.md` - template for adding future roles/projects.
- `linkedin/` - LinkedIn-specific profile, About, experience, skills, and Featured section drafts.
- `resume_ai_extractions/` - diagnostic notes on how AI/ATS/platform parsers interpret generated resumes.
- `roles/quest-platform.md` - Quest safari quotation platform work.
- `roles/quest-pdf-service.md` - Quest PDF generation service work.
- `roles/xai-human-data.md` - xAI Human Data / AI Tutor software engineering contract work.
- `roles/hovernotes.md` - HoverNotes founder work.
- `roles/jonjabird.md` - JonjaBird founder/operator and business automation work.
- `roles/uganda-community-korea.md` - Uganda community leadership, governance values, diaspora partnership, and sports diplomacy work.
- `roles/bebridge-slid.md` - Bebridge/Slid work split by growth period.
- `roles/gogymi-textutor.md` - GoGymi/TexTutor freelance platform work.

## Public Artifact Targets

Use this evidence to update:

- Homepage: `_pages/about.md`
- CV page data: `_data/cv.yml`
- Project pages: `_projects/`
- Resume markdown: `2025-10-22-hamza-kyamanywa-resume.md` and tailored variants
- Generated PDFs under `assets/pdf/` when needed

## Writing Rules

- Keep resume bullets outcome-first: action, system, scale, result.
- Keep site copy human and readable; do not overload the homepage with every metric.
- Avoid duplicate or conflicting dates across files.
- Do not publish private client details, credentials, internal URLs, or unreleased financial data unless Hamza explicitly approves.
