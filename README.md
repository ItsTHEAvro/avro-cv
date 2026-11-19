# CV / Resume Generator

Personal CV system: facts live in `data/`, layouts in `templates/`, one folder per job in `applications/`.

## New application

1. Create `applications/YYYY-MM_company-role/` and add `job_description.txt`.
2. Ask your agent: "Follow AGENTS.md and generate a CV for applications/<folder>."
3. Review `notes.md` (selected items, gaps) and the PDF in `build/`.

## Updating info

Edit `data/*.yaml` first; every future CV picks it up. Open questions: `data/TODO.md`.

## Building manually

From an application folder: `latexmk -pdf -outdir=../../build/<folder> cv.tex`
(or Ctrl+Alt+B in VS Code with LaTeX Workshop).
