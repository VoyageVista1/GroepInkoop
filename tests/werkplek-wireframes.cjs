// Integratietest: wireframes binnen de VoyageVista-werkplek (statische site).
const { chromium } = require('playwright');
const base = process.argv[2];
const shots = process.argv[3];
let fails = 0, passes = 0;
const ok = (c, m) => { if (c) passes++; else { fails++; console.log('FAIL', m); } };
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1440, height: 900 } });
  const errors = [];
  p.on('pageerror', e => errors.push('pageerror: ' + e.message));
  p.on('console', m => { if (m.type() === 'error' && !/server\.arcgisonline|ERR_|net::/.test(m.text())) errors.push(m.text()); });
  const bad = [];
  p.on('response', r => { if (r.status() >= 400 && r.url().startsWith(base)) bad.push(r.status() + ' ' + r.url()); });
  await p.goto(base + '/');
  await p.click('[data-a="enterDemo"]'); await p.waitForTimeout(400);
  ok(await p.isVisible('#nav'), 'werkplek geopend');
  // bestaande app werkt nog
  for (const r of ['start', 'dash', 'kansen', 'rps', 'levs', 'cts', 'salesdash', 'cat']) {
    await p.evaluate(h => location.hash = h, r); await p.waitForTimeout(150);
    const h1 = await p.textContent('#view h1').catch(() => '');
    ok(h1 && !/niet worden geladen/.test(await p.textContent('#view')), 'bestaande route ' + r + ' (' + (h1 || '').trim() + ')');
  }
  // wireframes in de zijbalk
  await p.evaluate(() => location.hash = 'dash'); await p.waitForTimeout(200);
  const navText = await p.textContent('#nav');
  for (const t of ['Nieuw · Productkansen', 'Nieuw · Reisproducten', 'Nieuw · Contracten', 'Nieuw · Leveranciers', 'Nieuw · Testflows user stories'])
    ok(navText.includes(t), 'zijbalk bevat ' + t);
  // klik in zijbalk: Nieuw · Contracten
  const groupOpen = async (label) => { const t = p.locator('.nav-trigger', { hasText: label }); if ((await t.getAttribute('aria-expanded')) !== 'true') await t.click(); await p.waitForTimeout(150); };
  await groupOpen('Inkoop');
  await p.click('#nav a[href="#wf.CT01"]'); await p.waitForTimeout(600);
  ok((await p.evaluate(() => location.hash)) === '#wf.CT01', 'route wf.CT01');
  ok(await p.getAttribute('#nav a[href="#wf.CT01"]', 'aria-current') === 'page', 'Nieuw · Contracten actief in zijbalk');
  const f = p.frameLocator('#wf-frame');
  ok((await f.locator('h1').textContent()) === 'Contractenoverzicht', 'iframe toont CT01');
  ok(await f.locator('.side').isHidden(), 'iframe zonder eigen zijbalk');
  const hgt = await p.$eval('#wf-frame', e => e.offsetHeight); ok(hgt > 700, 'iframe-hoogte past zich aan (' + hgt + ')');
  const crumb = await p.textContent('#view .crumb'); ok(/Productontwikkeling & Inkoop/.test(crumb) && /Inkoop/.test(crumb) && /Nieuw · Contracten/.test(crumb) && /CT01/.test(crumb), 'kruimelpad: ' + crumb.replace(/\s+/g, ' '));
  // flow C2 binnen de app
  await f.locator('tr[data-go=CT05]').click(); await p.waitForTimeout(300);
  ok((await p.evaluate(() => location.hash)) === '#wf.CT05', 'hash volgt iframe (CT05)');
  for (const c of await f.locator('.checks input').all()) await c.check();
  await f.getByRole('button', { name: 'Goedkeuren', exact: true }).click(); await p.waitForTimeout(400);
  ok((await f.locator('h1').textContent()) === 'Contractdetails', 'goedkeuren → CT02');
  ok((await p.textContent('#toasts')).includes('goedgekeurd'), 'melding verschijnt in werkplek-toast');
  // module wisselen in iframe → zijbalk volgt
  await f.locator('.det a[href="#/LV02"]').click(); await p.waitForTimeout(300);
  ok((await p.evaluate(() => location.hash)) === '#wf.LV02', 'hash LV02');
  ok(await p.getAttribute('#nav a[href="#wf.LV01"]', 'aria-current') === 'page', 'zijbalk volgt naar Nieuw · Leveranciers');
  // herladen op diepe link
  await p.reload(); await p.waitForTimeout(800);
  if (await p.isVisible('[data-a="enterDemo"]')) { await p.click('[data-a="enterDemo"]'); await p.waitForTimeout(400); await p.evaluate(() => location.hash = 'wf.LV02'); await p.waitForTimeout(600); }
  ok((await p.frameLocator('#wf-frame').locator('h1').textContent()) === 'Leverancierdetails', 'diepe link wf.LV02 werkt na herladen');
  // productontwikkeling
  await p.evaluate(() => location.hash = 'dash'); await p.waitForTimeout(200);
  await groupOpen('Productontwikkeling');
  await p.click('#nav a[href="#wf.PK01"]'); await p.waitForTimeout(500);
  ok((await p.frameLocator('#wf-frame').locator('h1').textContent()) === 'Productkansenoverzicht', 'Nieuw · Productkansen → PK01');
  await p.click('#nav a[href="#wf.flows"]'); await p.waitForTimeout(500);
  ok((await p.frameLocator('#wf-frame').locator('h1').textContent()) === 'Testflows user stories', 'Testflows in werkplek');
  if (shots) {
    await p.evaluate(() => location.hash = 'wf.CT05'); await p.waitForTimeout(700);
    await p.screenshot({ path: shots + '/app-CT05.png' });
    await p.evaluate(() => location.hash = 'wf.PK01'); await p.waitForTimeout(700);
    await p.screenshot({ path: shots + '/app-PK01.png' });
  }
  ok(bad.length === 0, 'geen 404: ' + bad.join(', '));
  ok(errors.length === 0, 'geen JS-fouten: ' + errors.join(' | '));
  console.log(`\n${passes} geslaagd, ${fails} mislukt`);
  await b.close(); process.exit(fails ? 1 : 0);
})();
