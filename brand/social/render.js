// Render The IE Hub social images from template.html with Playwright (Chromium).
//   node brand/social/render.js                 -> the brand set and the example post into brand/social/out/
//   node brand/social/render.js posts.json      -> one image per entry: {"name","format","theme","eyebrow","headline","sub"}
// Formats: og 1200x630, x-header 1500x500, linkedin-cover 4200x700, square 1080x1080, portrait 1080x1350.
const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

const HERE = __dirname;
const SIZES = { og: [1200, 630], 'x-header': [1500, 500], 'linkedin-cover': [4200, 700], square: [1080, 1080], portrait: [1080, 1350] };
const DEFAULT = [];
for (const theme of ['dark', 'light']) {
  for (const format of Object.keys(SIZES)) DEFAULT.push({ name: `brand-${format}-${theme}`, format, theme });
}
const example = { eyebrow: 'open course · draft, open for review', headline: 'Charting Process Behavior',
  sub: 'Chart a process over time, separate routine variation from signals, and judge whether it can meet its specifications.' };
for (const format of ['og', 'square', 'portrait']) DEFAULT.push({ name: `post-example-${format}-dark`, format, theme: 'dark', ...example });

const jobs = process.argv[2] ? JSON.parse(fs.readFileSync(process.argv[2], 'utf8')) : DEFAULT;
(async () => {
  const browser = await chromium.launch();
  fs.mkdirSync(path.join(HERE, 'out'), { recursive: true });
  for (const j of jobs) {
    const [w, h] = SIZES[j.format];
    const page = await browser.newPage({ viewport: { width: w, height: h } });
    const params = new URLSearchParams(Object.entries(j).filter(([k]) => k !== 'name'));
    await page.goto('file://' + path.join(HERE, 'template.html') + '?' + params);
    await page.evaluate(() => document.fonts.ready);
    await page.screenshot({ path: path.join(HERE, 'out', j.name + '.png'), clip: { x: 0, y: 0, width: w, height: h } });
    await page.close();
    console.log('wrote', j.name + '.png', `${w}x${h}`);
  }
  await browser.close();
})();
