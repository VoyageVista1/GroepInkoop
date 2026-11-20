// Navigatiecontrole voor prototype/wireframes.html
const { chromium } = require('playwright');
const path = require('path');
const file = 'file://' + path.resolve(process.argv[2]);
const out = process.argv[3];
let fails = 0, passes = 0;
const ok = (c, m) => { if (c) passes++; else { fails++; console.log('FAIL', m); } };

(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1280, height: 860 } });
  const errors = [];
  p.on('pageerror', e => errors.push(e.message));
  p.on('console', m => { if (m.type() === 'error') errors.push(m.text()); });
  await p.goto(file + '#/DA01');
  const ids = await p.evaluate(() => ORDER.slice());
  ok(ids.length === 71, 'aantal schermen = 71 (' + ids.length + ')');

  // 1. Elk scherm rendert, en elke link/knop wijst naar een bestaand scherm
  let links = 0;
  for (const id of ids) {
    await p.goto(file + '#/' + id); await p.waitForTimeout(20);
    const h1 = await p.textContent('h1');
    ok(h1 && !/niet gevonden/i.test(h1), id + ' rendert (' + h1 + ')');
    const targets = await p.$$eval('#view [data-go], #view a[href^="#/"]', els => els.map(e => e.dataset.go || e.getAttribute('href').slice(2)));
    for (const t of targets) {
      links++;
      const valid = await p.evaluate(t => !!SCREENS[t] || ['back', '#print', '#addrule', 'flows', 'index'].includes(t), t);
      ok(valid, id + ' → ' + t + ' bestaat');
    }
    const cur = await p.$eval('#nav [aria-current=page]', a => a.dataset.m).catch(() => null);
    ok(cur === id.slice(0, 2), id + ' actieve navigatie ' + cur);
  }
  // 2. Bereikbaarheid: elk scherm heeft minstens één inkomende link
  const incoming = await p.evaluate(() => { const inc = {}; ORDER.forEach(i => inc[i] = 0);
    ORDER.forEach(i => { const d = SCREENS[i]; const t = [];
      (d.btns || []).forEach(b => t.push(b[1])); (d.demo || []).forEach(b => t.push(b[1])); if (d.newTo) t.push(d.newTo);
      [].concat(d.rowTo || []).forEach(x => t.push(x)); (d.kpis || []).forEach(k => k[2] && t.push(k[2]));
      (d.det || []).forEach(x => x[2] && t.push(x[2])); (d.tl || []).forEach(x => Array.isArray(x) && t.push(x[1]));
      t.forEach(x => { if (inc[x] !== undefined && x !== i) inc[x]++; }); });
    MODS.forEach(m => inc[m[3]]++); return inc; });
  for (const [id, n] of Object.entries(incoming)) ok(n > 0, id + ' heeft inkomende link');

  // helpers
  const go = async id => { await p.goto(file + '#/' + id); await p.waitForTimeout(30); };
  const click = async label => { await p.getByRole('button', { name: label, exact: true }).first().click(); await p.waitForTimeout(40); };
  const at = async (id, m) => { const h = await p.evaluate(() => location.hash); ok(h === '#/' + id, m + ' → verwacht ' + id + ', kreeg ' + h); };
  const fill = async (label, v) => { const f = p.locator(`.f[data-label="${label}"]`).locator('input,select,textarea'); const tag = await f.evaluate(e => e.tagName);
    if (tag === 'SELECT') { const opts = await f.locator('option').allTextContents(); await f.selectOption({ label: v === '*' ? opts[1] : v }); } else await f.fill(v); };

  // ---- Contractflows ----
  await go('CT01'); await click('+ Nieuw'); await at('CT03', 'C1 nieuw contract');
  await click('Concept opslaan'); ok(await p.isVisible('#ferr'), 'C1 leeg opslaan geweigerd'); await at('CT03', 'C1 blijft op formulier');
  ok(await p.locator('.f.bad').count() >= 5, 'C1 verplichte velden gemarkeerd');
  await fill('Leverancier', '*'); await fill('Inkoper', '*'); await fill('Begindatum', '2027-01-01'); await fill('Einddatum', '2026-12-31'); await fill('Inkoopprijs', '118');
  await click('Concept opslaan'); ok((await p.textContent('#view')).includes('einddatum moet na de begindatum'), 'C1 einddatum vóór begindatum geweigerd');
  await fill('Einddatum', '2027-12-31'); await click('Annuleren'); ok(await p.isVisible('.modal'), 'C1 annuleren met wijzigingen vraagt bevestiging');
  await p.click('.modal [data-no]'); await click('Concept opslaan'); await at('CT02', 'C1 opgeslagen → details');
  await click('Voorwaarden'); await at('CT04', 'C1 voorwaarden'); await fill('Voorwaarden', 'Annulering tot 30 dagen kosteloos'); await fill('Dagen voor vertrek', '30'); await fill('Kostenpercentage', '0');
  await click('Opslaan'); await at('CT02', 'C1 voorwaarden opgeslagen');

  await go('CT01'); await p.click('tr[data-go=CT05]'); await at('CT05', 'C2 rij CON-031 → beoordeling');
  await click('Terugsturen'); ok((await p.textContent('#reasonm')).includes('verplicht'), 'C2 terugsturen zonder reden geweigerd');
  await click('Goedkeuren'); ok(await p.isVisible('#ferr'), 'C2 goedkeuren zonder controlepunten geweigerd');
  for (const c of await p.$$('.checks input')) await c.check();
  await click('Goedkeuren'); await at('CT02', 'C2 goedgekeurd → details');
  await go('CT05'); await p.fill('#reason', 'Annuleringsregel ontbreekt'); await click('Terugsturen'); await at('CT06', 'C2 terugsturen → CT06');
  await p.fill('#reason', 'Document ontbreekt'); await click('Terugsturen'); await at('CT03', 'C2 terug naar inkoper');

  await go('CT01'); await p.click('a.kpi[href="#/CT08"]'); await at('CT08', 'C3 KPI loopt af');
  await click('Verlenging bekijken'); await at('CT07', 'C3 verlengen');
  await fill('Begindatum', '2027-01-01'); await fill('Einddatum', '2027-12-31'); await fill('Inkoopprijs', '121');
  await click('Verlengingsconcept maken'); await at('CT02', 'C3 verlengingsconcept'); await click('Ter goedkeuring'); await at('CT05', 'C3 ter goedkeuring');

  await go('ON02'); await click('Afsluiten'); await at('ON05', 'C4 afsluiten');
  await click('Akkoord'); ok((await p.textContent('#ferr')).includes('vervolgactie open'), 'C4 akkoord geblokkeerd door open vervolgactie');
  await p.click('#ferr a'); await at('ON06', 'C4 naar vervolgactie');
  await fill('Omschrijving', 'Prijsvoorstel afronden'); await fill('Verantwoordelijke', '*'); await fill('Deadline', '2026-11-05'); await fill('Status', 'Afgerond');
  await click('Taak opslaan'); await at('ON02', 'C4 taak opgeslagen'); await click('Afsluiten'); await click('Akkoord'); await at('CT03', 'C4 akkoord → contractformulier');

  await go('CT02'); await click('Bezetting'); await at('CT12', 'C5 bezetting'); await click('Lage bezetting melden'); await at('CT13', 'C5 melden');
  await fill('Omschrijving', 'Bezetting 60%'); await fill('Verantwoordelijke', '*'); await fill('Deadline', '2026-11-30'); await click('Melding registreren'); await at('PL02', 'C5 taak voor Sales');
  await go('CT02'); await click('Archiveren'); await at('CT11', 'C5 archiveren'); await click('Archiveren'); await at('CT11', 'C5 archiveren zonder reden geweigerd');
  await p.fill('#reason', 'Contract vervangen'); await click('Archiveren'); await at('CT01', 'C5 gearchiveerd');
  await go('CT03'); await p.click('.demo a[href="#/CT10"]'); await at('CT10', 'C uitzondering opslaan mislukt'); await click('Opnieuw opslaan'); await at('CT03', 'C herstel');
  await go('CT03'); await p.click('.demo a[href="#/CT09"]'); await at('CT09', 'C uitzondering geen rechten'); await click('Contract bekijken'); await at('CT02', 'C geen rechten → bekijken');

  // ---- Product- en leveranciersflows ----
  await go('PK01'); await click('+ Nieuw'); await at('PK03', 'P1'); await fill('Naam', 'Wandelen Madeira'); await fill('Bestemming', '*'); await fill('Onderzoeksinformatie', 'Vraag naar actieve reizen');
  await click('Opslaan als concept'); await at('PK02', 'P1 opgeslagen'); await click('Ter beoordeling'); await at('PK04', 'P1 beoordelen');
  for (const c of await p.$$('.checks input')) await c.check(); await click('Kansrijk'); await at('RP03', 'P1 kansrijk → reisproduct');
  await fill('Naam', 'Rondreis Japan'); await fill('Bestemming', 'Japan'); await fill('Reisduur (dagen)', '14'); await click('Concept opslaan'); await at('RP07', 'P2 opgeslagen');
  await click('Route opbouwen'); await at('RD01', 'P2 route'); await click('+ Nieuw'); await at('RD03', 'P2 onderdeel');
  await fill('Type', 'Accommodatie'); await fill('Startdag', '10'); await fill('Aantal dagen', '2'); await fill('Volgorde', '6'); await click('Opslaan'); await at('RD01', 'P2 onderdeel opgeslagen');
  await click('Route controleren'); await at('RD04', 'P2 routecontrole'); await click('Concept bewaren'); await at('RP02', 'P2 terug naar product');
  await click('Publicatie controleren'); await at('RP04', 'P2 publicatiecontrole'); for (const c of await p.$$('.checks input')) await c.check();
  await click('Goedkeuren'); await at('RP10', 'P2 goedgekeurd'); await click('Nu publiceren'); await at('CA02', 'P2 gepubliceerd in catalogus');
  await go('RP04'); await p.fill('#reason', 'Verblijf dag 10–11 ontbreekt'); await click('Terugsturen'); await at('RP05', 'P3 teruggestuurd'); await click('Bewerken'); await at('RP03', 'P3 bewerken');
  await go('LV01'); await click('+ Nieuw'); await at('LV03', 'P4'); await click('Registreren'); ok(await p.isVisible('#ferr'), 'P4 leeg registreren geweigerd');
  await fill('Naam', 'Sakura Hotels'); await fill('Type', 'Hotel'); await fill('Plaats', 'Tokio'); await fill('E-mail', 'fout-adres'); await click('Registreren');
  ok((await p.textContent('#view')).includes('geen geldig e-mailadres'), 'P4 ongeldig e-mail');
  await fill('E-mail', 'info@sakura.example'); await click('Registreren'); ok(await p.isVisible('#fwarn'), 'P4 waarschuwing dubbele leverancier'); await at('LV03', 'P4 blijft staan bij dubbel');
  await click('Registreren'); await at('LV02', 'P4 bewust doorgaan → details');
  await click('Contactmoment'); await at('LV05', 'P4 contactmoment'); await fill('Medewerker', '*'); await fill('Bezoekdatum', '2026-11-05'); await fill('Gespreksonderwerp', 'Tarieven 2027');
  await click('Opslaan'); await at('LV07', 'P4 historie');
  await go('LV02'); await click('Aanbiedingen'); await at('AB01', 'P5'); await click('Vergelijken'); await at('AB05', 'P5 vergelijken');
  await click('Selecteren'); ok(await p.isVisible('#pickerr'), 'P5 selecteren zonder keuze geweigerd'); await p.check('input[name=pick][value="0"]'); await click('Selecteren'); await at('AB02', 'P5 geselecteerd');
  await click('Koppelen'); await at('AB04', 'P5 koppelen'); await fill('Reisproduct', '*'); await fill('Reisonderdeel', '*'); await fill('Aanbod', '*'); await click('Koppelen'); await at('RD02', 'P5 gekoppeld');
  await go('CA01'); await p.click('tr[data-go=CA02]'); await at('CA02', 'P6'); await click('Feedback geven'); await at('CA05', 'P6 feedback');
  await fill('Onderwerp', 'Reisduur klopt niet'); await fill('Omschrijving', 'Folder zegt 9 dagen'); await click('Feedback verzenden'); await at('CA06', 'P6 verzonden');
  await go('PK01'); await p.fill('#q', 'zzz'); ok(await p.isVisible('#none'), 'P lege zoekopdracht toont melding'); await p.click('#none a'); await at('PK05', 'P lege resultaten scherm');
  await go('RP03'); await p.click('.demo a[href="#/RP06"]'); await at('RP06', 'P versieconflict'); await click('Nieuwe versie laden'); await at('RP03', 'P versieconflict herstel');
  await go('RP02'); await p.click('.demo a[href="#/RP09"]'); await at('RP09', 'P geen rechten');
  await go('RD04'); await click('Ontbrekend verblijf bekijken'); await at('RD06', 'P ontbrekend verblijf'); await click('Onderdeel toevoegen'); await at('RD03', 'P herstel verblijf');

  // ---- Flowpagina en index ----
  await go('flows'); const flowLinks = await p.$$eval('#view a[href^="#/"]', a => a.map(x => x.getAttribute('href').slice(2)));
  ok(flowLinks.length > 40, 'flowpagina heeft stappen (' + flowLinks.length + ')');
  await go('index'); ok((await p.$$('#view .idx li')).length === 71, 'index toont 71 schermen');
  // Mobiel
  await p.setViewportSize({ width: 390, height: 800 }); await go('CT02');
  const sw = await p.evaluate(() => document.documentElement.scrollWidth); ok(sw <= 392, 'mobiel geen horizontale scroll (' + sw + ')');
  await p.click('#menuBtn'); ok(await p.isVisible('#nav'), 'mobiel menu opent');
  if (out) { await p.setViewportSize({ width: 1280, height: 860 }); for (const id of ['DA01', 'CT05', 'LV03']) { await go(id); await p.screenshot({ path: `${out}/${id}.png`, fullPage: true }); } }

  ok(errors.length === 0, 'geen JS-fouten: ' + errors.join(' | '));
  console.log(`\n${passes} geslaagd, ${fails} mislukt · ${links} links gecontroleerd`);
  await b.close(); process.exit(fails ? 1 : 0);
})();
