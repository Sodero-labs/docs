# Sodero Docs

The source of [docs.sodero.io](https://docs.sodero.io): one versioned manual per product, built with
[MkDocs Material](https://squidfunk.github.io/mkdocs-material/) and published with
[mike](https://github.com/jimporter/mike) to the `gh-pages` branch.

| Folder | Published at | Contents |
| :--- | :--- | :--- |
| `sodero-cloud/` | `/sodero-cloud/<version>/` | Sodero Cloud manual (`mkdocs.yml`, `docs/`) |
| `stellar-x/` | `/stellar-x/<version>/` | Stellar X manual (`mkdocs.yml`, `docs/`) |
| `shared/` | | Settings (`base.yml`) and theme (`theme/`) used by every manual |
| `home/` | `/` | Product home page, not-found page, CNAME, robots.txt, sitemap index, llms.txt |
| `tools/` | | Scripts that update the `gh-pages` branch |

Each product folder keeps its own versions: `/<product>/versions.json` lists them, `/<product>/latest/`
is the newest one and `/<product>/` opens it. The header of every page has a product menu and a
version menu for the product.

## Write and preview

```bash
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
.venv/bin/mkdocs serve -f sodero-cloud/mkdocs.yml    # or stellar-x/mkdocs.yml
```

The version menu stays hidden in this preview because it reads `versions.json` from the published site.

Write a page as `docs/<section>/<page>/index.md` with its images in `images/` next to it, and add it to
`nav` in the product's `mkdocs.yml` (and to the `llmstxt` sections). Settings shared by every
manual go to `shared/base.yml`; the header and page templates are in `shared/theme/`.

## Publish

Push a tag named `<product>/<version>`. The `publish site` workflow builds that product's manual
with mike, deploys it to `/<product>/<version>/`, points `/<product>/latest/` to it, and publishes
`home/` to the root.

```bash
git tag stellar-x/v2.0.1 && git push origin stellar-x/v2.0.1
git tag sodero-cloud/v1.0.1 && git push origin sodero-cloud/v1.0.1
```

Publish every change as a new version: raise the patch number and add an entry to the product's
`CHANGELOG.md`. To take a version off the site, delete it with mike:

```bash
mike delete --config-file stellar-x/mkdocs.yml --push v2.0.1
```

`home/404.html` sends the addresses of a removed version to the same page of the latest version.

### Addresses from before the product split

Before the split, the Stellar X manual was deployed at the root of `gh-pages` (`/v2.0.0/`, `/latest/`).
Those addresses now forward to `/stellar-x/`. `tools/migrate_pages.py` made that move once and is kept
for recovery. The tags `v1.0.0`, `v1.0.1` and `v2.0.0` are from that time and no longer trigger a build.
