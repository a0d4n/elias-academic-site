# Elias Kübler — academic website

Live site: https://a0d4n.github.io/elias-academic-site/

Built with the [Academic Pages](https://github.com/academicpages/academicpages.github.io) Jekyll template and hosted free on GitHub Pages. Every commit to `master` rebuilds and redeploys the site automatically in about a minute; progress is visible under the repository's **Actions** tab.

All edits can be made in the GitHub website: open a file, click the pencil icon, edit, then **Commit changes**.

## Where things live

| What | File |
|---|---|
| About text (homepage) | `index.md` |
| Sidebar: name, title, affiliation, links | `author:` block in `_config.yml` |
| Profile photo | `images/Elias.jpg` (replace the file, keep the name) |
| Research page | `_data/research.yml` |
| Political Opinions page | `_data/opinions.yml` |
| CV PDF | `files/Elias_Kuebler_CV.pdf` |
| Navigation bar | `_data/navigation.yml` |

## Common updates

**Add a paper.** Open `_data/research.yml`. Under `working_papers:`, `work_in_progress:` or `publications:`, replace `[]` with an entry; the file contains a commented example showing every field. To attach a PDF, upload it to `files/` (**Add file → Upload files**) and link it as `/files/name.pdf`. Empty sections are hidden automatically.

**Add a presentation.** Same file, under `presentations:` (fields: `title`, `event`, `location`, `date`).

**Add an opinion piece.** Open `_data/opinions.yml` and add an entry with `title`, `outlet`, `date` (YYYY-MM-DD) and `url`. Entries are sorted newest first automatically.

**Update the CV.** Upload the new PDF to `files/` with the name `Elias_Kuebler_CV.pdf`, replacing the old file. The download button on the CV page appears as soon as the file exists.

**Add Google Scholar, SSRN or ORCID to the sidebar.** Add a line to the `author:` block in `_config.yml`, e.g. `ssrn: "https://papers.ssrn.com/sol3/cf_dev/AbsByAuth.cfm?per_id=…"`. Supported keys: `googlescholar`, `ssrn`, `orcid`, `researchgate` (full URLs).

YAML is sensitive to indentation: use spaces, not tabs, and keep entries aligned like the examples. If a commit breaks the build, the Actions tab shows a red cross and the previous version of the site stays online.

## Safety check on every deploy

Before each deployment, `.github/scripts/check_site.py` verifies that the four navigation pages exist and that every internal link and file reference on the site resolves. If anything is broken, the deploy stops and the live site is left unchanged.

## Moving the site to Elias's own GitHub account

1. In this repository: **Settings → General → Danger Zone → Transfer ownership**, and enter Elias's GitHub username. He accepts the transfer by email.
2. Optionally rename the repository to `<his-username>.github.io` for a shorter address (https://&lt;his-username&gt;.github.io/).
3. In `_config.yml`, update the three hosting lines:
   - `url: "https://<his-username>.github.io"`
   - `baseurl: ""` if the repository is named `<his-username>.github.io`, otherwise `"/<repository-name>"`
   - `repository: "<his-username>/<repository-name>"`
4. In the new repository: **Settings → Pages → Source: GitHub Actions**.
5. Commit, wait for the Actions run to finish, and check the new address. Update the live-site link at the top of this README.

## Previewing locally (optional)

With Ruby installed: `bundle install`, then `bundle exec jekyll serve` and open http://localhost:4000/elias-academic-site/. Alternatively, `docker compose up` using the included `docker-compose.yaml`.
