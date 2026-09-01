`report.md` in the repository root lists pages on the sibling sites that this playbook does not link yet.

For each entry, add a markdown link in the ONE place it belongs, following the conventions already in `content/docs/`:

- handson notes → the **Hands-On Labs** list of the matching competency page
- sols problems → **Field Cases**
- checklists → **Checklists**
- automations `case-studies/` → **Automation Case Studies**; any other automations page → **Reference Library**, under `**Automation Playbook**`
- architectures → **Reference Library**, under `**Architecture Field Notes**`
- templates → **Reference Library**, under `**Templates**`
- pipelines → **Reference Library**, under `**Pipeline Field Guide**`
- a new catalogue section (Toolian, Framework Thinking, another checklist section) → `content/docs/references/_index.md`

Rules:

- Use the page's own `<title>` as the link text, minus the site-name suffix.
- Pick the competency by subject. If nothing fits well, add it to `content/docs/references/_index.md` rather than forcing it onto a competency page.
- Do not restructure existing content, do not add new sections or commentary, and do not touch anything the report did not mention.
- Then run `hugo --quiet` and fix any build error before finishing.
