# Project Documents


the navigation is not working
also, can't you directly import the main.md from other sections to make a long document? it has to involve completely changing the page?

This repository is structured for writing a formal project report in Markdown with a PDF-like academic format (cover page, repeated header style, menu/table of contents, and sectioned content).

## Directory Structure

```text
project-documents/
├── assets/
│   ├── images/                 # Figures and screenshots used in report
│   └── logo/                   # University/course logos for cover/header
├── docs/
│   └── report/
│       ├── main.md             # Cover page + table of contents
│       ├── output/             # Generated PDF output
│       └── sections/           # Main content split by section
├── scripts/
│   ├── build-report.ps1        # Build Markdown to PDF (PowerShell)
│   └── build-report.sh         # Build Markdown to PDF (Bash)
├── styles/
│   └── report.css              # A4/page styling and print rules
└── templates/
    └── report-template.md      # Reusable report skeleton
```

## Where To Edit

- Keep `docs/report/main.md` minimal (cover + TOC).
- Write section content in `docs/report/sections/*.md`.
- Put project figures in `assets/images/`.
- Put logos in `assets/logo/`.
- Adjust print/page look in `styles/report.css`.

## Build PDF (Page-like Output)

Build scripts use `pandoc` + `weasyprint`.
They automatically combine `main.md` with all files in `docs/report/sections/` (sorted by filename).

Run with PowerShell:

```powershell
powershell -ExecutionPolicy Bypass -File scripts/build-report.ps1
```

Run with Bash:

```bash
bash scripts/build-report.sh
```

Optional custom input/output (Bash):

```bash
bash scripts/build-report.sh docs/report/main.md docs/report/output/report.pdf
```

Output:

- `docs/report/output/report.pdf`

## Notes

- Pure Markdown does not enforce page layout by itself; page behavior comes from the PDF renderer and CSS.
- `docs/report/main.md` already includes a cover style and menu structure inspired by your reference pages.
