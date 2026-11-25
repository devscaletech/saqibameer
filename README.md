# saqibameer.com

Personal website of **Saqib Ameer — AI Growth Leader, Dubai**.

Static HTML/CSS/JS (no framework, no build step needed to deploy).

```
site/            ← the website (deploy this folder)
  index.html, about.html, services.html, stack.html, work.html, insights.html, contact.html, 404.html
  assets/css/site.css   monochrome design system + animations
  assets/js/site.js     preloader, cursor, reveals, counters, marquees, parallax, stack interaction
  assets/img/           black & white photography
build.py         regenerates every page in site/ from shared header/footer + content
images.json      (optional) overrides which image goes where
```

## Edit content
Change text in `build.py`, then run `python build.py` and commit.

## Deploy on Cloudflare Pages
1. Cloudflare dashboard → Workers & Pages → Create → Pages → Connect to Git → pick `saqi097/saqibameer`.
2. Framework preset: **None**. Build command: *(leave empty)*. Build output directory: **`site`**.
3. Save and deploy, then add the custom domain `saqibameer.com` under the project's Custom domains tab.

Every push to `main` redeploys automatically.
