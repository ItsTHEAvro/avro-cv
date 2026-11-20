# CV Generation Instructions (for AI agents)

## Repo layout

- `data/` SINGLE SOURCE OF TRUTH: all facts about me (YAML)
- `sources/` raw material (LinkedIn exports, old CVs, syllabus). Read only when asked to update data/.
- `templates/` LaTeX layouts: cv/, cv-picture/, resume/. Never edit these.
- `applications/` one folder per job: job_description.txt, cv.tex, .sty, notes.md, cv.pdf

## Hard rules

1. Use ONLY facts from `data/`. Never invent metrics, dates, skills, employers, or links.
2. Items with `show: false` are never printed.
3. Skills marked `cert_only` / `cert_only_items` may appear in a skills list but must never be described as project or work experience.
4. Certifications with `part_of` are not listed when their parent is listed.
5. Never claim cryptography or steganography CTF skills.
6. Rewording bullets to match the job's language is fine; changing facts is not.
7. If the job wants something not in data/, list it under "Gaps" in notes.md. Do not fill it in.
8. Obey any `note` field on an entry; notes are instructions (e.g. "only for teaching roles", "never print rating").

## Generating a CV

1. Read `applications/<slug>/job_description.txt` (or the circular image/PDF in the folder).
2. Map requirements to tags (vocabulary below) and pick the matching `summaries` entry.
3. Select entries by tag match first, then `priority` (high > medium > low). Within an entry, pick the bullets whose tags match; use `note: one-line version` bullets when space is tight.
4. Choose a template:
   - `resume`: 1 page, industry jobs and internships
   - `cv`: 2 pages max, academic, research, scholarships
   - `cv-picture`: only when a photo is expected (common for Bangladeshi employers)
5. Copy the template's `.sty` into the application folder and write `cv.tex` there.
   - Command argument ORDER differs between templates (e.g. `\resumeProject` vs `\cvProject`); read the `% #1, #2...` comments in the template.
   - Escape LaTeX special characters: & % $ # \_ { } ~ ^
   - Photo path: `../../data/assets/photo.png`
   - In the COPIED .sty (never in templates/), uncomment the portfolio
     `\contactItem` block at the end of the header command and set it to
     `https://avro.bd` / `avro.bd` with the `\faGlobe` icon.
   - If the CV runs over its page limit, margins in the COPIED .sty may be reduced
     to 0.6in before cutting content.
6. Compile from the application folder: `latexmk -pdf cv.tex`, then `latexmk -c` to remove
   auxiliary files. The PDF stays next to cv.tex as `cv.pdf` and is committed.
   Fix errors and respect the page limit.
7. Write `notes.md`: template chosen, entries included, entries omitted, job keywords covered, and Gaps.

## Academic and Bangladeshi circulars

- Check the eligibility rules (SSC/HSC/degree grade floors) against `data/education.yaml`
  and `data/transcript.yaml`, and record the result in notes.md.
- Include SSC and HSC entries when the circular sets grade requirements for them.
- Never print individual course grades unless asked (see the note in transcript.yaml).

## Tag vocabulary

ml, xai, llm, data, cv (computer vision), iot, swe, web, cybersec, networking,
research, cp (competitive programming), leadership, teaching, office

## Updating data

When I share new info, update the right file in `data/`, keep the existing schema, and add new open questions to `data/TODO.md`.