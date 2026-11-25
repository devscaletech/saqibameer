// Prints reports/.build/*.html to PDF. Run after: python reports/make_pdfs.py
const { chromium } = require('playwright');
const path = require('path');
const jobs = require(path.join(__dirname, '.build', 'jobs.json'));
(async () => {
  const b = await chromium.launch(); const p = await b.newPage();
  for (const j of jobs) {
    await p.goto('file://' + j.html, { waitUntil: 'load' });
    await p.pdf({ path: j.pdf, format: 'A4', printBackground: true, displayHeaderFooter: true,
      headerTemplate: '<span></span>', footerTemplate: j.footer, preferCSSPageSize: true });
    console.log('wrote', path.basename(j.pdf));
  }
  await b.close();
})();
