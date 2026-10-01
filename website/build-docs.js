// Zet de Markdown-documenten uit docs/ om naar HTML-pagina's in website/docs/.
// Gebruik: cd website && npm install && npm run build (de site zelf is ../index.html)
const fs = require('fs');
const path = require('path');
const { marked } = require('marked');

const ROOT = path.resolve(__dirname, '..');
const OUT = path.join(__dirname, 'docs');

// bron (t.o.v. repo) -> [uitvoerbestand, paginatitel, korte omschrijving]
const DOCS = {
  'docs/ontwerp/scope.md': ['scope.html', 'Scope', 'Probleem, eerste versie, buiten scope en open besluiten'],
  'docs/ontwerp/use-cases-klantenservice.md': ['use-cases-klantenservice.html', 'Use cases Klantenservice', 'Use-casebeschrijvingen en user flows UC-K01 t/m UC-K09'],
  'docs/ontwerp/erd.md': ['erd.html', 'ERD', 'ERD Inkoop en Klantenservice: entiteiten, relaties en aandachtspunten'],
  'docs/ontwerp/ux-eisen.md': ['ux-eisen.html', 'UX-eisen', 'Toetsbare UX-eisen per taak (concept)'],
  'docs/figma-board.md': ['figma-board.html', 'FigJam-board', 'Overzicht van het FigJam-board met use cases Inkoop'],
  'docs/interview-analyse.md': ['interview-analyse.html', 'Interviewanalyse', 'Bevindingen uit het interview met de opdrachtgever'],
  'docs/backlog/inkoop-product-backlog.md': ['inkoop-product-backlog.html', 'Product backlog Inkoop', 'User stories, Definition of Ready/Done en sprintdoelen'],
  'docs/productrisicoanalyse-teststrategie.md': ['productrisicoanalyse-teststrategie.html', 'Risicoanalyse & teststrategie', 'Productrisico’s, risicomatrix en testaanpak'],
};

// GitHub-compatibele slug, zodat bestaande #ankers in de documenten blijven werken
function slug(text, seen) {
  let s = text.toLowerCase().trim()
    .replace(/<[^>]+>/g, '')
    .replace(/[^\p{L}\p{N}\s_-]/gu, '')
    .replace(/\s/g, '-');
  const base = s; let n = seen[base] || 0;
  if (n) s = `${base}-${n}`;
  seen[base] = n + 1;
  return s;
}

// Schrijft een link uit een Markdown-bron om naar een doel dat vanuit website/docs/ werkt
function rewriteHref(href, srcRel) {
  if (/^(https?:|mailto:|#)/.test(href)) return href;
  const [file, hash] = href.split('#');
  const abs = path.normalize(path.join(path.dirname(srcRel), file));
  if (DOCS[abs]) return DOCS[abs][0] + (hash ? '#' + hash : '');
  if (!fs.existsSync(path.join(ROOT, abs))) throw new Error(`Link naar onbekend bestand: ${href} in ${srcRel}`);
  // Markdown zonder eigen webpagina: naar GitHub (alleen voor teamleden)
  if (abs.endsWith('.md')) return 'https://github.com/VoyageVista1/GroepInkoop/blob/HEAD/' + abs.split(path.sep).join('/') + (hash ? '#' + hash : '');
  return path.relative('website/docs', abs).split(path.sep).join('/') + (hash ? '#' + hash : '');
}

function page(title, desc, body, toc, mermaid) {
  const nav = Object.values(DOCS).map(([f, t]) =>
    `<a href="${f}"${t === title ? ' aria-current="page"' : ''}>${t}</a>`).join('');
  return `<!doctype html>
<html lang="nl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>${title} · VoyageVista Werkplek</title>
<meta name="description" content="${desc}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Playfair+Display:wght@600&display=swap" rel="stylesheet">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' rx='8' fill='%230b2536'/%3E%3Cpath d='M8 10l8 13 8-13' stroke='%23fb923c' stroke-width='3.2' fill='none' stroke-linecap='round' stroke-linejoin='round'/%3E%3C/svg%3E">
<link rel="stylesheet" href="doc.css">
${mermaid ? '<script id="mermaid-lib" src="https://cdn.jsdelivr.net/npm/mermaid@10.9.1/dist/mermaid.min.js"></script>\n<script>window.mermaid&&mermaid.initialize({startOnLoad:true,theme:matchMedia("(prefers-color-scheme: dark)").matches?"dark":"neutral"})</script>\n' : ''}<script>try{var t=localStorage.getItem("vv-theme");if(t)document.documentElement.setAttribute("data-theme",t)}catch(e){}</script>
</head>
<body>
<a class="skip" href="#inhoud">Naar de inhoud</a>
<header class="top">
  <div class="wrap top-in">
    <a class="brand" href="../../index.html"><span class="mark"><svg width="16" height="16" viewBox="0 0 24 24" aria-hidden="true"><path d="M5 6l7 12 7-12" stroke="#fb923c" stroke-width="3" fill="none" stroke-linecap="round" stroke-linejoin="round"/></svg></span>VoyageVista <span class="muted">Werkplek</span></a>
    <a class="back" href="../../index.html#documenten">← Terug naar de website</a>
  </div>
  <nav class="wrap tabs" aria-label="Documenten">${nav}</nav>
</header>
<div class="wrap layout">
  <aside class="toc" aria-label="Inhoud van dit document"><strong>Op deze pagina</strong>${toc}</aside>
  <main id="inhoud" class="doc">${body}</main>
</div>
<footer class="wrap foot">Gegenereerd uit de Markdown-bron in <code>docs/</code> · Team GroepInkoop · casus VoyageVista</footer>
</body>
</html>
`;
}

fs.mkdirSync(OUT, { recursive: true });
for (const [src, [out, title, desc]] of Object.entries(DOCS)) {
  const md = fs.readFileSync(path.join(ROOT, src), 'utf8');
  const seen = {}; const toc = [];
  const renderer = new marked.Renderer();
  renderer.heading = (text, level, raw) => {
    const id = slug(raw, seen);
    if (level === 2) toc.push(`<a href="#${id}">${text.replace(/<[^>]+>/g, '')}</a>`);
    return `<h${level} id="${id}">${text}</h${level}>\n`;
  };
  renderer.link = (href, t, text) => {
    const h = rewriteHref(href, src);
    const ext = /^https?:/.test(h) ? ' target="_blank" rel="noopener"' : '';
    return `<a href="${h}"${t ? ` title="${t}"` : ''}${ext}>${text}</a>`;
  };
  renderer.image = (href, t, text) =>
    `<img class="fig-img" src="${rewriteHref(href, src)}" alt="${text || t || ''}" loading="lazy">`;
  renderer.code = (code, lang) => lang === 'mermaid'
    ? `<div class="mermaid-wrap"><pre class="mermaid">${code.replace(/</g, '&lt;')}</pre></div>\n`
    : `<pre><code>${code.replace(/&/g, '&amp;').replace(/</g, '&lt;')}</code></pre>\n`;
  renderer.table = (header, body) =>
    `<div class="table"><table><thead>${header}</thead><tbody>${body}</tbody></table></div>\n`;
  const body = marked.parse(md, { renderer, gfm: true });
  fs.writeFileSync(path.join(OUT, out), page(title, desc, body, toc.join(''), /```mermaid/.test(md)));
  console.log('✓', src, '→', path.join('website/docs', out));
}
