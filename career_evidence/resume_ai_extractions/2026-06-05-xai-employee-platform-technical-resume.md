# xAI Employee Platform Resume Extraction - Technical Resume

## Metadata

- Evidence status: User-provided platform extraction snapshot
- Date observed: 2026-06-05
- Source resume: `site-repo/assets/pdf/2026-06-05-Hamza-Kyamanywa-Resume-Technical-Draft.pdf`
- Platform/context: xAI / TeachX employee platform resume parser
- Purpose: Track what AI/ATS-style systems extract from Hamza's resume so future resume edits can be tested against actual parser behavior.

## Extracted Work Experience

### Technical Founder & CEO

- Company: HoverNotes
- Location: Remote / Seoul
- Dates: Jul 2025 - Present
- Current: Yes
- Platform summary:
  - Founded AI video note-taking SaaS with $10K+/month revenue and 20K installs.
  - Built Chrome/Edge extension, Next.js app, Obsidian workflows, Stripe/Razorpay payments, and multimodal AI pipelines.

### CTO & Co-founder

- Company: Quest
- Location: Remote
- Dates extracted: Jan 2026 - Present
- Current: Yes
- Platform summary:
  - Led 3-person team building Next.js safari quotation platform and PDF infrastructure.
  - Implemented Stripe subscriptions, PostgreSQL/Supabase, Drizzle ORM, and Puppeteer PDF generation.
- Parser note:
  - Resume source says `2026 - Present`; the platform inferred `Jan 2026 - Present`.

### Software Engineering Specialist, Human Data / AI Tutor

- Company: xAI
- Location: Remote
- Dates: May 2026 - Present
- Current: Yes
- Platform summary:
  - Evaluated and reviewed AI-generated code for model training across Python, TypeScript, Java, Go, Rust, C/C++, databases, and security domains.

### Senior Full Stack Engineer / Freelance Technical Lead

- Company: GoGymi / TexTutor
- Location: Remote, Switzerland
- Dates: Jan 2025 - Sep 2025
- Platform summary:
  - Built AI EdTech SaaS with Next.js 15, React 19, Stripe subscriptions, multilingual support, AI grammar correction, and Lexical/LiveBlocks collaboration features.

### AI Engineer & Team Lead

- Company: Bebridge Inc. / Slid
- Location: Seoul, South Korea
- Dates: Jan 2024 - Jun 2025
- Platform summary:
  - Led LLM-powered auto-notes, AI chat, semantic search, and React Native mobile AI features.
  - Optimized costs with LangGraph, Whisper, AWS Lambda, and caching strategies.

### Senior Software Engineer / Full Stack Engineer

- Company: Bebridge Inc. / Slid
- Location: Seoul, South Korea
- Dates: Jun 2022 - Dec 2023
- Platform summary:
  - Built core systems including RAG/conversational AI with LangChain/Pinecone, real-time transcription, cross-platform auth/payments, and multi-format exports.
  - Promoted from L2 to L4.

## Extracted Education

### Korea University

- Degree: B.S. in Electrical and Electronics Engineering
- Location: Seoul, South Korea
- Dates: Mar 2019 - Feb 2023
- Platform summary:
  - GPA 4.02/4.5.
  - Magna Cum Laude.
  - Global Korea Scholarship and Ugandan Government Scholarship recipient.
  - Co-authored paper on interpretable music genre classification, Springer Nature.

## Extracted Skills

- OpenAI API
- Whisper
- LangChain
- LangGraph
- RAG
- vector search
- prompt engineering
- multimodal AI workflows
- Next.js
- React
- TypeScript
- React Native
- Tailwind CSS
- Lexical
- Chrome/Edge extensions
- Obsidian
- local-first workflows
- Python
- FastAPI
- Node.js
- Express
- PostgreSQL
- Supabase
- Drizzle ORM
- MongoDB
- Redis
- AWS Lambda
- S3
- EventBridge
- Docker
- Vercel
- Cloudflare R2
- Hetzner
- CI/CD
- PostHog
- Sentry
- Stripe
- Razorpay
- webhooks
- subscriptions
- trials
- pricing
- credits
- PDF/document generation
- Korean (TOPIK 5)
- English
- Luganda
- WebRTC
- Socket.io
- AWS Cognito
- Payple
- Pinecone
- embeddings
- FFmpeg
- Handlebars
- Puppeteer
- NextAuth v5
- LiveBlocks

## What The Parser Preserved Well

- Current focus on HoverNotes, Quest, and xAI was extracted correctly.
- HoverNotes scale was preserved as `$10K+/month revenue` and `20K installs`.
- Quest leadership was preserved as a `3-person team`.
- The technical stack came through strongly, especially AI/LLM, Next.js/React/TypeScript, payments, PDF generation, and infrastructure.
- Slid's 50K+ MAU context was preserved in the employer line.
- Promotion from L2 to L4 survived extraction.
- Education honors and scholarships survived extraction.

## What The Parser Simplified Or Lost

- HoverNotes regional payment nuance was collapsed into `Stripe/Razorpay payments`; WeChat Pay/Alipay and China/India/global segmentation did not appear in the summarized role text, though the skills list retained Stripe and Razorpay.
- Quest's safari-domain workflow depth was compressed to `quotation platform and PDF infrastructure`.
- xAI title was shortened to `Software Engineering Specialist, Human Data / AI Tutor`, dropping the full `Software Engineering (Expert)` wording.
- Open source/community details were mostly converted into skills, not experience.
- Ugandan Community Vice President role did not appear as a separate work/leadership entry.
- Quest dates were inferred as `Jan 2026 - Present` from a source that only said `2026 - Present`.

## Resume Implications

- If a platform parser is the target, explicit skills lists work: the parser extracted a broad and accurate technical skill set.
- If a specific regional payment story matters, phrase it directly in the role bullet rather than relying on the skills section.
- If community leadership matters, it likely needs its own clearly labeled section or role-like entry; otherwise parsers may ignore it.
- If exact Quest start month matters, add the month explicitly in the source resume to avoid parser inference.
- The technical resume successfully communicates an AI/full-stack/payments/PDF/platform profile to automated systems.

## Sensitive/Private Notes

- The platform account details and external work email from the user-provided screenshot should not be published on the public site or resume unless explicitly approved.
