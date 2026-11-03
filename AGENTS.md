# Personal Site Agent Notes

This repo is Hamza Kyamanywa's personal site, portfolio, and resume source.

Before updating `_pages/about.md`, `_data/cv.yml`, `_projects/`, resume markdown files, or generated resume PDFs, read `career_evidence/README.md` and the relevant files under `career_evidence/roles/`.

Use `career_evidence/` as the source of truth for role scope, project details, dates, metrics, technologies, and proof links. Do not invent metrics or claims. If a fact is useful but not yet verified, add it as `Needs confirmation` in the relevant evidence file before using it in public-facing copy.

Current public-facing artifacts:

- `_pages/about.md` - homepage biography and high-level positioning
- `_data/cv.yml` - Jekyll CV data rendered by the site
- `_projects/` - project detail pages
- `2025-10-22-hamza-kyamanywa-resume.md` - general resume source
- `2025-10-25-hamza-kyamanywa-openai-resume.md` - OpenAI-tailored resume source
- `project_contributions/` - older contribution reports, currently especially useful for TexTutor/GoGymi

When tailoring the site or resume for a role:

1. Identify the target audience and role.
2. Pull only relevant claims from `career_evidence/`.
3. Prefer concrete outcomes, scale, and ownership over broad summaries.
4. Preserve facts and dates consistently across the homepage, CV data, project pages, and resume sources.
5. Leave a short note in the relevant evidence file if you discover stronger proof or a better phrasing.

## Hosting (2026-11-04)

- `untilhamza.com` is the canonical host. The zone is in the Cloudflare account "Untilhamza@gmail.com's Account" (`9a74175b08039eed2e93d47f8e9b6001`); local `wrangler` is already logged in to it via OAuth (`wrangler whoami`). That token can deploy Workers and attach custom domains but cannot edit DNS records or zone settings, so use the dashboard for those.
- Interim setup: the `untilhamza-com` Worker (`edge/untilhamza-com/`) proxies the GitHub Pages build (`untilhamza.github.io`, `gh-pages` branch) under `untilhamza.com`, 308s `www.` and `http://` to `https://untilhamza.com`, and rewrites absolute github.io URLs. Deploy with `npx wrangler deploy --config edge/untilhamza-com/wrangler.jsonc`.
- `_config.yml` `url` is `https://untilhamza.com`, so canonicals point there; `_includes/head.html` JS-redirects visitors who land on `untilhamza.github.io`.
- Planned: an Astro site on Cloudflare Workers (like `hover-notes-web-site`) replaces the proxy on the same custom domain. Design directions: `design/personal-site-2026-11-04/`.
