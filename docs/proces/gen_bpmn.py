#!/usr/bin/env python3
"""Genereert het klantenserviceproces (BPMN 2.0) als SVG, HTML en .bpmn uit één model."""
from xml.sax.saxutils import escape as xesc
import os

OUT = os.path.dirname(os.path.abspath(__file__))
W = 3230
FONT = "'IBM Plex Sans', 'Segoe UI', Roboto, Arial, sans-serif"

# ---------------- Layout ----------------
TW, TH = 150, 62          # taak
GR = 25                   # halve diagonaal gateway
ER = 18                   # straal event
X0 = 20                   # linkerrand pools
POOL_BAND = 40            # verticale poolnaam
LANE_BAND = 170           # lane-naam
CX0 = X0 + POOL_BAND + LANE_BAND  # begin inhoud

TITLE_H = 52
POOL_K = (70, 222)        # Klant
POOL_V = (240, 868)       # VoyageVista
LANES = [                 # (id, naam, y0, y1, kleur)
    ('L_ks', 'Klantenservice\n(shop en contactcenter)', 240, 530, '#ece4fb'),
    ('L_sr', 'Senior\nklantenservice', 530, 640, '#e2d8f6'),
    ('L_at', 'After Travel', 640, 750, '#f2e3f7'),
    ('L_fi', 'Financiën &\nAdministratie', 750, 868, '#dde9f8'),
]
POOL_L = (886, 940)       # Leverancier (dichtgeklapt)
LEGEND_Y = 968
H = 1060

yK = 146
rU, rM, rL = 305, 395, 482
ySR, yAT, yFI = 585, 695, 809

# element: id -> dict(type, x, y, label, lane, extra)
E = {}
def el(i, t, x, y, label='', pool='V', lane=None, **kw):
    E[i] = dict(id=i, type=t, x=x, y=y, label=label, pool=pool, lane=lane, **kw)

# Klant
el('k_start', 'start', 270, yK, 'Klant heeft vraag\nof klacht', 'K')
el('k1', 'task', 400, yK, 'Neemt contact op\n(telefoon, e-mail,\nshop, social media)', 'K')
el('k2', 'task', 2210, yK, 'Ontvangt antwoord\nof voorstel', 'K')
el('k3', 'task', 2370, yK, 'Reageert op\nvoorstel (akkoord\nof bezwaar)', 'K')
el('k4', 'task', 2680, yK, 'Ontvangt\neindbesluit', 'K')
el('k5', 'task', 2860, yK, 'Vult zelf\nrekeningnummer in', 'K', badge=5)
el('k_end', 'end', 2990, yK, 'Klant\ngeholpen', 'K')

# Klantenservice
el('ms', 'msgstart', 400, rM, 'Contact\nontvangen', lane='L_ks')
el('m1', 'task', 530, rM, 'Klant zoeken\n(e-mail, telefoon,\nnaam)', lane='L_ks')
el('m2', 'task', 700, rM, 'Contactmoment\nvastleggen in\nklantdossier', lane='L_ks', badge=1)
el('gw1', 'gateway', 850, rM, 'Soort\ncontact?', lane='L_ks', below=True)
el('m3', 'task', 980, rU, 'Vraag beantwoorden\nof wijziging\nverwerken', lane='L_ks')
el('me1', 'msgend', 1120, rU, 'Vraag\nafgehandeld', lane='L_ks', lblright=True)
el('m4', 'task', 980, rM, 'Klacht registreren\n(urgentie\nautomatisch)', lane='L_ks', badge=2)
el('gw2', 'gateway', 1120, rM, 'Klant nu\nop reis?', lane='L_ks')
el('m5', 'task', 1260, rM, 'Hotel vragen om\noplossing ter\nplaatse', lane='L_ks', badge=3)
el('gm1', 'gateway', 1400, rM, '', lane='L_ks')
el('m6', 'task', 1530, rM, 'Klacht beoordelen\n(historie, zelf\ngekozen?)', lane='L_ks', badge=4)
el('gw3', 'gateway', 1670, rM, 'Klacht\ngegrond?', lane='L_ks', below=True)
el('m7', 'task', 1670, rU, 'Ongegrond\nverklaren met\nonderbouwing', lane='L_ks')
el('m8', 'task', 1810, rM, 'Compensatie-\nvoorstel volgens\nrichtlijn', lane='L_ks')
el('gm2', 'gateway', 2090, rM, '', lane='L_ks')
el('m10', 'task', 2210, rM, 'Klant informeren\nover besluit of\nvoorstel', lane='L_ks')
el('m11', 'receive', 2370, rM, 'Reactie klant\nverwerken', lane='L_ks')
el('gw4', 'gateway', 2500, rM, 'Klant\nakkoord?', lane='L_ks')
el('ds', 'datastore', 615, rL, 'Klantdossier\n(werkplek)', lane='L_ks')

# Senior
el('s1', 'task', 1810, ySR, 'Voorstel\ncontroleren\n(vier ogen)', lane='L_sr', badge=6)
el('gs', 'gateway', 1950, ySR, 'Goed-\ngekeurd?', lane='L_sr', below=True)
el('do', 'dataobject', 1650, ySR, 'Compensatie-\nrichtlijn\n(% van reissom)', lane='L_sr')

# After Travel
el('a1', 'task', 2500, yAT, 'Klacht opnieuw\nbeoordelen\n(maatwerk)', lane='L_at')
el('a2', 'task', 2680, yAT, 'Eindbesluit\nvastleggen en\ncommuniceren', lane='L_at')

# Financiën
el('f1', 'task', 2830, yFI, 'Compensatie\nuitbetalen (indien\nvan toepassing)', lane='L_fi')
el('f2', 'task', 2990, yFI, 'Klachtdossier\nafsluiten', lane='L_fi')
el('f_end', 'end', 3120, yFI, 'Klacht\nafgehandeld', lane='L_fi')

def bounds(e):
    t = e['type']
    if t in ('task', 'receive'):
        return e['x'] - TW / 2, e['y'] - TH / 2, TW, TH
    if t == 'gateway':
        return e['x'] - GR, e['y'] - GR, 2 * GR, 2 * GR
    if t in ('start', 'end', 'msgstart', 'msgend'):
        return e['x'] - ER, e['y'] - ER, 2 * ER, 2 * ER
    if t == 'datastore':
        return e['x'] - 24, e['y'] - 20, 48, 40
    if t == 'dataobject':
        return e['x'] - 16, e['y'] - 21, 32, 42

def P(i, side):
    e = E[i]; x, y, w, h = bounds(e)
    return {'l': (x, y + h / 2), 'r': (x + w, y + h / 2), 't': (x + w / 2, y), 'b': (x + w / 2, y + h)}[side]

def off(p, dx=0, dy=0):
    return (p[0] + dx, p[1] + dy)

# ---------------- Stromen ----------------
# (id, bron, doel, waypoints, label, labelpos)
SEQ = []
def seq(i, s, t, pts, label='', lp=None, anchor='start'):
    SEQ.append(dict(id='sf_' + i, s=s, t=t, pts=pts, label=label, lp=lp, anchor=anchor))

# Klant
seq('fk1', 'k_start', 'k1', [P('k_start', 'r'), P('k1', 'l')])
seq('fk2', 'k1', 'k2', [P('k1', 'r'), P('k2', 'l')])
seq('fk3', 'k2', 'k3', [P('k2', 'r'), P('k3', 'l')])
seq('fk4', 'k3', 'k4', [P('k3', 'r'), P('k4', 'l')])
seq('fk5', 'k4', 'k5', [P('k4', 'r'), P('k5', 'l')])
seq('fk6', 'k5', 'k_end', [P('k5', 'r'), P('k_end', 'l')])
# VoyageVista
seq('f1', 'ms', 'm1', [P('ms', 'r'), P('m1', 'l')])
seq('f2', 'm1', 'm2', [P('m1', 'r'), P('m2', 'l')])
seq('f3', 'm2', 'gw1', [P('m2', 'r'), P('gw1', 'l')])
seq('f4', 'gw1', 'm3', [P('gw1', 't'), (850, rU), P('m3', 'l')], 'Vraag of wijziging', (842, rU - 12), 'end')
seq('f5', 'm3', 'me1', [P('m3', 'r'), P('me1', 'l')])
seq('f6', 'gw1', 'm4', [P('gw1', 'r'), P('m4', 'l')], 'Klacht', (882, rM - 8))
seq('f7', 'm4', 'gw2', [P('m4', 'r'), P('gw2', 'l')])
seq('f8', 'gw2', 'm5', [P('gw2', 'r'), P('m5', 'l')], 'Ja', (1150, rM - 8))
seq('f9', 'gw2', 'gm1', [P('gw2', 'b'), (1120, rL), (1400, rL), P('gm1', 'b')], 'Nee', (1128, rM + 44))
seq('f10', 'm5', 'gm1', [P('m5', 'r'), P('gm1', 'l')])
seq('f11', 'gm1', 'm6', [P('gm1', 'r'), P('m6', 'l')])
seq('f12', 'm6', 'gw3', [P('m6', 'r'), P('gw3', 'l')])
seq('f13', 'gw3', 'm8', [P('gw3', 'r'), P('m8', 'l')], 'Ja', (1700, rM - 8))
seq('f14', 'gw3', 'm7', [P('gw3', 't'), P('m7', 'b')], 'Nee', (1678, rM - 40))
seq('f15', 'm7', 'gm2', [P('m7', 'r'), (2090, rU), P('gm2', 't')])
seq('f16', 'm8', 's1', [P('m8', 'b'), P('s1', 't')])
seq('f17', 's1', 'gs', [P('s1', 'r'), P('gs', 'l')])
seq('f18', 'gs', 'm8', [P('gs', 't'), (1950, rM), P('m8', 'r')], 'Nee, terug', (1958, 470))
seq('f19', 'gs', 'gm2', [P('gs', 'r'), (2090, ySR), P('gm2', 'b')], 'Ja', (1984, ySR - 8))
seq('f20', 'gm2', 'm10', [P('gm2', 'r'), P('m10', 'l')])
seq('f21', 'm10', 'm11', [P('m10', 'r'), P('m11', 'l')])
seq('f22', 'm11', 'gw4', [P('m11', 'r'), P('gw4', 'l')])
seq('f23', 'gw4', 'f1', [P('gw4', 'r'), (2800, rM), (2800, yFI - TH / 2)], 'Ja', (2534, rM - 8))
seq('f24', 'gw4', 'a1', [P('gw4', 'b'), P('a1', 't')], 'Nee (bezwaar)', (2508, 470))
seq('f25', 'a1', 'a2', [P('a1', 'r'), P('a2', 'l')])
seq('f26', 'a2', 'f1', [P('a2', 'b'), (2680, yFI), P('f1', 'l')])
seq('f27', 'f1', 'f2', [P('f1', 'r'), P('f2', 'l')])
seq('f28', 'f2', 'f_end', [P('f2', 'r'), P('f_end', 'l')])
# f23 eindigt boven op f1 op x=2800 (links van het midden)
SEQ[[s['id'] for s in SEQ].index('sf_f23')]['pts'][-1] = (2800, yFI - TH / 2)

MSG = []
def msg(i, s, t, pts, label='', lp=None, anchor='start'):
    MSG.append(dict(id=i, s=s, t=t, pts=pts, label=label, lp=lp, anchor=anchor))

GAP = 231  # tussen pools
msg('mf1', 'k1', 'ms', [P('k1', 'b'), P('ms', 't')], 'Vraag of klacht', (408, 200))
msg('mf2', 'me1', 'k2', [P('me1', 't'), (1120, GAP), (2180, GAP), (2180, yK + TH / 2)], 'Antwoord', (1128, 268))
msg('mf3', 'm10', 'k2', [(2240, rM - TH / 2), (2240, yK + TH / 2)], 'Besluit of voorstel', (2248, 330))
msg('mf4', 'k3', 'm11', [(2370, yK + TH / 2), (2370, rM - TH / 2)], 'Akkoord of bezwaar', (2378, 262))
msg('mf5', 'a2', 'k4', [(2680, yAT - TH / 2), (2680, yK + TH / 2)], 'Eindbesluit', (2688, 262))
msg('mf6', 'k5', 'f1', [(2860, yK + TH / 2), (2860, yFI - TH / 2)], 'Rekeningnummer via\nMijn VoyageVista', (2868, 268))
msg('mf7', 'm5', 'LEV', [(1245, rM + TH / 2), (1245, POOL_L[0])], 'Verzoek om\noplossing', (1150, 610), 'end')
msg('mf8', 'LEV', 'm5', [(1275, POOL_L[0]), (1275, rM + TH / 2)], 'Reactie hotel', (1283, 610))

ASSOC = [  # (id, bron, doel, punten, richting)
    ('as1', 'ds', 'm1', [(E['ds']['x'] - 12, rL - 20), (560, rM + TH / 2)], 'in'),
    ('as2', 'm2', 'ds', [(670, rM + TH / 2), (E['ds']['x'] + 14, rL - 20)], 'out'),
    ('as3', 'do', 's1', [(E['do']['x'] + 16, ySR), P('s1', 'l')], 'in'),
]


# ---- ruimte tussen 'Soort contact?' en 'Klacht registreren' ----
DX, TH_X = 40, 960
for e in E.values():
    if e['x'] >= TH_X: e['x'] += DX
def _sh(pts): return [((px + DX) if px >= 900 else px, py) for px, py in pts]
for f in SEQ + MSG:
    f['pts'] = _sh(f['pts'])
    if f['lp'] and f['lp'][0] >= TH_X: f['lp'] = (f['lp'][0] + DX, f['lp'][1])
ASSOC = [(a, b, c, _sh(p), d) for a, b, c, p, d in ASSOC]

VERBETERINGEN = [
    (1, 'Contactmoment vastleggen met vaste velden (kanaal, categorie, samenvatting, vervolgactie) in plaats van één vrij opmerkingenveld. Datum en medewerker vult het systeem zelf in.',
     'Handmatige registratie en geen uniforme afhandeling; collega’s geven verschillende antwoorden (KP1, KP3, GP1)'),
    (2, 'De urgentie wordt automatisch Hoog als de klant op dat moment op reis is.',
     'Moeilijk prioriteren van vragen, lange reactietijden (KP2, KP5)'),
    (3, 'Bij een klant op reis vraagt de medewerker eerst het hotel om een oplossing ter plaatse.',
     'Klachten die al op de bestemming opgelost hadden kunnen worden (interview)'),
    (4, 'De klacht wordt beoordeeld met de volledige klanthistorie, inclusief of de klant de accommodatie zelf koos.',
     'Beperkt inzicht in eerdere contacten (KP4, GP1)'),
    (5, 'De klant vult zelf het rekeningnummer in. VoyageVista slaat het nergens op.',
     'AVG: geen IBAN opslaan (interview)'),
    (6, 'Een tweede medewerker keurt het compensatievoorstel goed. Wie het voorstel indient, mag het niet zelf goedkeuren.',
     'Vier-ogenprincipe; het systeem doet nu een voorstel dat een mens altijd moet controleren (interview)'),
]

# ---------------- SVG ----------------
C = dict(ink='#12263a', quiet='#4a5d70', line='#27425a', task='#dbeafe', taskS='#1e40af', gw='#fde68a', gwS='#a16207',
         start='#bbf7d0', startS='#15803d', end='#fecaca', endS='#b91c1c', msg='#4b6784', badge='#ea580c',
         poolS='#9fb3c8', head='#0f2a44', paper='#ffffff', poolK='#e6f0fb', lev='#e3f2df')

def text_lines(x, y, label, size=12.5, weight=500, anchor='middle', fill=None, lh=None):
    lines = label.split('\n'); lh = lh or size * 1.22
    y0 = y - (len(lines) - 1) * lh / 2 + size * 0.35
    out = [f'<text x="{x:.1f}" y="{y0:.1f}" font-size="{size}" font-weight="{weight}" text-anchor="{anchor}" fill="{fill or C["ink"]}">']
    for k, ln in enumerate(lines):
        out.append(f'<tspan x="{x:.1f}" dy="{0 if k == 0 else lh:.1f}">{xesc(ln)}</tspan>')
    out.append('</text>')
    return ''.join(out)

def path_d(pts):
    return 'M' + ' L'.join(f'{x:.1f} {y:.1f}' for x, y in pts)

USER_ICON = lambda x, y: (f'<g transform="translate({x:.1f} {y:.1f})" fill="none" stroke="{C["taskS"]}" stroke-width="1.3">'
                          f'<circle cx="6" cy="4.5" r="3.2" fill="{C["taskS"]}" fill-opacity=".85" stroke="none"/>'
                          f'<path d="M0.5 14 C0.5 9 11.5 9 11.5 14 Z" fill="{C["taskS"]}" fill-opacity=".85" stroke="none"/></g>')
ENV = lambda x, y, fill='none', stroke=None: (f'<g transform="translate({x:.1f} {y:.1f})"><rect x="0" y="0" width="16" height="11" rx="1.5" fill="{fill}" stroke="{stroke or C["line"]}" stroke-width="1.3"/>'
                                              f'<path d="M0.8 1 L8 6.4 L15.2 1" fill="none" stroke="{"#fff" if fill != "none" else (stroke or C["line"])}" stroke-width="1.3"/></g>')

def svg_diagram():
    o = []
    o.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" role="img" aria-label="BPMN 2.0-diagram: klantvraag of klacht afhandelen bij VoyageVista" font-family="{FONT}">')
    o.append('<defs>'
             f'<marker id="seqArrow" viewBox="0 0 10 10" refX="9.5" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse"><path d="M0 0 L10 5 L0 10 Z" fill="{C["line"]}"/></marker>'
             f'<marker id="msgArrow" viewBox="0 0 10 10" refX="9.5" refY="5" markerWidth="9" markerHeight="9" orient="auto-start-reverse"><path d="M0.5 0.5 L9.5 5 L0.5 9.5 Z" fill="#fff" stroke="{C["msg"]}" stroke-width="1.2"/></marker>'
             f'<marker id="msgStart" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="8" markerHeight="8"><circle cx="5" cy="5" r="3.6" fill="#fff" stroke="{C["msg"]}" stroke-width="1.3"/></marker>'
             f'<marker id="assocArrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M1 1 L9 5 L1 9" fill="none" stroke="{C["quiet"]}" stroke-width="1.3"/></marker>'
             '</defs>')
    o.append(f'<rect x="0" y="0" width="{W}" height="{H}" fill="{C["paper"]}"/>')
    # titelbalk
    o.append(f'<rect x="{X0}" y="10" width="{W - 2 * X0}" height="{TITLE_H - 14}" rx="6" fill="{C["head"]}"/>')
    o.append(f'<text x="{X0 + 18}" y="{10 + (TITLE_H - 14) / 2 + 6}" font-size="19" font-weight="700" fill="#fff">BPMN 2.0 – Subproces: Klantvraag of klacht afhandelen (VoyageVista, gewenste situatie)</text>')
    o.append(f'<text x="{W - X0 - 18}" y="{10 + (TITLE_H - 14) / 2 + 5}" font-size="13" text-anchor="end" fill="#b9cfe4">Onderdeel van hoofdproces ‘Reis verkopen en uitvoeren’ · taak ‘Klantvraag of klacht afhandelen’</text>')

    def pool(y0, y1, name, fill):
        o.append(f'<rect x="{X0}" y="{y0}" width="{W - 2 * X0}" height="{y1 - y0}" rx="6" fill="#fff" stroke="{C["poolS"]}" stroke-width="1.4"/>')
        o.append(f'<rect x="{X0}" y="{y0}" width="{POOL_BAND}" height="{y1 - y0}" rx="6" fill="{fill}" stroke="{C["poolS"]}" stroke-width="1.4"/>')
        cy = (y0 + y1) / 2
        o.append(f'<text transform="translate({X0 + POOL_BAND / 2 + 7} {cy}) rotate(-90)" text-anchor="middle" font-size="18" font-weight="700" fill="{C["ink"]}">{xesc(name)}</text>')

    pool(*POOL_K, 'Klant', C['poolK'])
    pool(*POOL_V, 'VoyageVista', '#dfe9f6')
    for lid, name, y0, y1, col in LANES:
        o.append(f'<rect x="{X0 + POOL_BAND}" y="{y0}" width="{LANE_BAND}" height="{y1 - y0}" fill="{col}" stroke="{C["poolS"]}" stroke-width="1"/>')
        o.append(f'<line x1="{X0 + POOL_BAND + LANE_BAND}" y1="{y1}" x2="{W - X0}" y2="{y1}" stroke="{C["poolS"]}" stroke-width="1"/>' if y1 != POOL_V[1] else '')
        o.append(text_lines(X0 + POOL_BAND + 14, (y0 + y1) / 2, name, size=15, weight=700, anchor='start'))
    # Leverancier (black box)
    o.append(f'<rect x="{X0}" y="{POOL_L[0]}" width="{W - 2 * X0}" height="{POOL_L[1] - POOL_L[0]}" rx="6" fill="{C["lev"]}" stroke="{C["poolS"]}" stroke-width="1.4"/>')
    o.append(f'<text x="{X0 + 18}" y="{(POOL_L[0] + POOL_L[1]) / 2 + 5}" font-size="15" font-weight="700" fill="{C["ink"]}">Leverancier (hotel op de bestemming)</text>')
    o.append(f'<text x="{X0 + 330}" y="{(POOL_L[0] + POOL_L[1]) / 2 + 5}" font-size="12.5" fill="{C["quiet"]}">dichtgeklapte pool: het interne proces van het hotel valt buiten de scope</text>')

    # stromen
    for s in SEQ:
        o.append(f'<path d="{path_d(s["pts"])}" fill="none" stroke="{C["line"]}" stroke-width="1.5" marker-end="url(#seqArrow)"/>')
        if s['label']:
            x, y = s['lp']
            o.append(text_lines(x, y, s['label'], size=12, weight=600, anchor=s['anchor'], fill=C['quiet']))
    for m in MSG:
        o.append(f'<path d="{path_d(m["pts"])}" fill="none" stroke="{C["msg"]}" stroke-width="1.4" stroke-dasharray="6 5" marker-start="url(#msgStart)" marker-end="url(#msgArrow)"/>')
        if m['label']:
            x, y = m['lp']
            o.append(f'<g>{text_lines(x, y, m["label"], size=11.5, weight=500, anchor=m["anchor"], fill=C["msg"])}</g>')
    for aid, s, t, pts, d in ASSOC:
        o.append(f'<path d="{path_d(pts)}" fill="none" stroke="{C["quiet"]}" stroke-width="1.3" stroke-dasharray="2 4" marker-end="url(#assocArrow)"/>')

    # knopen
    for e in E.values():
        t, x, y = e['type'], e['x'], e['y']
        if t in ('task', 'receive'):
            bx, by, bw, bh = bounds(e)
            o.append(f'<rect x="{bx}" y="{by}" width="{bw}" height="{bh}" rx="9" fill="{C["task"]}" stroke="{C["taskS"]}" stroke-width="1.4"/>')
            o.append(ENV(bx + 8, by + 8) if t == 'receive' else USER_ICON(bx + 8, by + 7))
            o.append(text_lines(x + 6, y + 1, e['label'], size=12.5, weight=500))
            if e.get('badge'):
                o.append(f'<circle cx="{bx + bw - 2}" cy="{by + 2}" r="11" fill="{C["badge"]}" stroke="#fff" stroke-width="2"/>'
                         f'<text x="{bx + bw - 2}" y="{by + 6.5}" font-size="12.5" font-weight="700" text-anchor="middle" fill="#fff">{e["badge"]}</text>')
        elif t == 'gateway':
            o.append(f'<path d="M{x} {y - GR} L{x + GR} {y} L{x} {y + GR} L{x - GR} {y} Z" fill="{C["gw"]}" stroke="{C["gwS"]}" stroke-width="1.5"/>')
            if e['label']:
                o.append(text_lines(x, y + GR + 24 if e.get('below') else y - GR - 22, e['label'], size=12, weight=600))
        elif t in ('start', 'msgstart'):
            o.append(f'<circle cx="{x}" cy="{y}" r="{ER}" fill="{C["start"]}" stroke="{C["startS"]}" stroke-width="1.8"/>')
            if t == 'msgstart':
                o.append(ENV(x - 8, y - 5.5, stroke=C['startS']))
            o.append(text_lines(x, y + ER + 20, e['label'], size=12, weight=500, fill=C['quiet']))
        elif t in ('end', 'msgend'):
            o.append(f'<circle cx="{x}" cy="{y}" r="{ER}" fill="{C["end"]}" stroke="{C["endS"]}" stroke-width="3.2"/>')
            if t == 'msgend':
                o.append(ENV(x - 8, y - 5.5, fill=C['endS'], stroke=C['endS']))
            o.append(text_lines(x + ER + 8, y, e['label'], size=12, weight=500, anchor='start', fill=C['quiet']) if e.get('lblright') else text_lines(x, y + ER + 20, e['label'], size=12, weight=500, fill=C['quiet']))
        elif t == 'datastore':
            bx, by, bw, bh = bounds(e)
            o.append(f'<path d="M{bx} {by + 6} v{bh - 12} a{bw / 2} 6 0 0 0 {bw} 0 v{-(bh - 12)}" fill="#f1f5f9" stroke="{C["line"]}" stroke-width="1.3"/>'
                     f'<ellipse cx="{x}" cy="{by + 6}" rx="{bw / 2}" ry="6" fill="#f1f5f9" stroke="{C["line"]}" stroke-width="1.3"/>'
                     f'<path d="M{bx} {by + 12} a{bw / 2} 6 0 0 0 {bw} 0" fill="none" stroke="{C["line"]}" stroke-width="1.1"/>')
            o.append(text_lines(bx + bw + 10, y, e['label'], size=12, weight=500, anchor='start', fill=C['quiet']))
        elif t == 'dataobject':
            bx, by, bw, bh = bounds(e)
            o.append(f'<path d="M{bx} {by} h{bw - 10} l10 10 v{bh - 10} h{-bw} Z" fill="#f8fafc" stroke="{C["line"]}" stroke-width="1.3"/>'
                     f'<path d="M{bx + bw - 10} {by} v10 h10" fill="none" stroke="{C["line"]}" stroke-width="1.3"/>')
            o.append(text_lines(bx - 10, y, e['label'], size=12, weight=500, anchor='end', fill=C['quiet']))

    # legenda
    ly = LEGEND_Y
    o.append(f'<rect x="{X0}" y="{ly}" width="{W - 2 * X0}" height="72" rx="6" fill="#f5f8fc" stroke="{C["poolS"]}" stroke-width="1.2"/>')
    o.append(f'<text x="{X0 + 18}" y="{ly + 42}" font-size="16" font-weight="700" fill="{C["ink"]}">Legenda BPMN 2.0</text>')
    lx = X0 + 210; cy = ly + 36
    def item(w, draw, label):
        nonlocal lx
        o.append(draw(lx, cy)); o.append(text_lines(lx + w + 10, cy, label, size=12.5, anchor='start', fill=C['quiet'])); lx += w + 10 + 9 * max(len(s) for s in label.split('\n')) + 26
    item(34, lambda x, y: f'<circle cx="{x + 17}" cy="{y}" r="15" fill="{C["start"]}" stroke="{C["startS"]}" stroke-width="1.8"/>', 'Startevent')
    item(34, lambda x, y: f'<circle cx="{x + 17}" cy="{y}" r="15" fill="{C["start"]}" stroke="{C["startS"]}" stroke-width="1.8"/>' + ENV(x + 9, y - 5.5, stroke=C['startS']), 'Bericht-\nstartevent')
    item(34, lambda x, y: f'<circle cx="{x + 17}" cy="{y}" r="15" fill="{C["end"]}" stroke="{C["endS"]}" stroke-width="3"/>', 'Eindevent')
    item(34, lambda x, y: f'<circle cx="{x + 17}" cy="{y}" r="15" fill="{C["end"]}" stroke="{C["endS"]}" stroke-width="3"/>' + ENV(x + 9, y - 5.5, fill=C['endS'], stroke=C['endS']), 'Bericht-\neindevent')
    item(40, lambda x, y: f'<path d="M{x + 20} {y - 18} L{x + 38} {y} L{x + 20} {y + 18} L{x + 2} {y} Z" fill="{C["gw"]}" stroke="{C["gwS"]}" stroke-width="1.5"/>', 'Gateway\n(beslissing)')
    item(62, lambda x, y: f'<rect x="{x}" y="{y - 20}" width="62" height="40" rx="7" fill="{C["task"]}" stroke="{C["taskS"]}" stroke-width="1.4"/>' + USER_ICON(x + 6, y - 15), 'Taak\n(medewerker)')
    item(62, lambda x, y: f'<rect x="{x}" y="{y - 20}" width="62" height="40" rx="7" fill="{C["task"]}" stroke="{C["taskS"]}" stroke-width="1.4"/>' + ENV(x + 6, y - 14), 'Ontvangst-\ntaak')
    item(60, lambda x, y: f'<path d="M{x} {y} H{x + 58}" stroke="{C["line"]}" stroke-width="1.5" marker-end="url(#seqArrow)"/>', 'Sequence flow')
    item(60, lambda x, y: f'<path d="M{x + 4} {y} H{x + 58}" stroke="{C["msg"]}" stroke-width="1.4" stroke-dasharray="6 5" marker-start="url(#msgStart)" marker-end="url(#msgArrow)"/>', 'Message flow')
    item(48, lambda x, y: f'<path d="M{x} {y} H{x + 46}" stroke="{C["quiet"]}" stroke-width="1.3" stroke-dasharray="2 4" marker-end="url(#assocArrow)"/>', 'Data-\nassociatie')
    item(30, lambda x, y: f'<path d="M{x + 3} {y - 13} v26 a12 5 0 0 0 24 0 v-26" fill="#f1f5f9" stroke="{C["line"]}" stroke-width="1.3"/><ellipse cx="{x + 15}" cy="{y - 13}" rx="12" ry="5" fill="#f1f5f9" stroke="{C["line"]}" stroke-width="1.3"/>', 'Datastore')
    item(26, lambda x, y: f'<path d="M{x + 3} {y - 16} h14 l8 8 v24 h-22 Z" fill="#f8fafc" stroke="{C["line"]}" stroke-width="1.3"/>', 'Data-\nobject')
    item(24, lambda x, y: f'<circle cx="{x + 12}" cy="{y}" r="11" fill="{C["badge"]}"/><text x="{x + 12}" y="{y + 4.5}" font-size="12.5" font-weight="700" text-anchor="middle" fill="#fff">1</text>', 'Verbetering\n(zie tabel)')
    o.append('</svg>')
    return '\n'.join(o)

svg = svg_diagram()
open(os.path.join(OUT, 'klantenservice-proces.svg'), 'w').write(svg)

# ---------------- BPMN XML ----------------
BTYPE = {'task': 'userTask', 'receive': 'receiveTask', 'gateway': 'exclusiveGateway', 'start': 'startEvent',
         'msgstart': 'startEvent', 'end': 'endEvent', 'msgend': 'endEvent'}
DOC = {f'm{n}': None for n in range(20)}
BADGE_DOC = {v[0]: v[1] for v in VERBETERINGEN}

def flat(label):
    return label.replace('-\n', '-').replace('\n', ' ')

def flow_refs(eid):
    inc = [s['id'] for s in SEQ if s['t'] == eid]
    out = [s['id'] for s in SEQ if s['s'] == eid]
    return ''.join(f'<bpmn:incoming>{i}</bpmn:incoming>' for i in inc) + ''.join(f'<bpmn:outgoing>{i}</bpmn:outgoing>' for i in out)

def node_xml(e):
    t = BTYPE.get(e['type'])
    if not t:
        return ''
    name = xesc(flat(e['label'])) if e['label'] else ''
    inner = ''
    if e.get('badge'):
        inner += f'<bpmn:documentation>Verbetering {e["badge"]}: {xesc(BADGE_DOC[e["badge"]])}</bpmn:documentation>'
    inner += flow_refs(e['id'])
    if e['id'] == 'm1':
        inner += '<bpmn:property id="m1_prop" name="__targetRef_placeholder"/><bpmn:dataInputAssociation id="as1"><bpmn:sourceRef>ds</bpmn:sourceRef><bpmn:targetRef>m1_prop</bpmn:targetRef></bpmn:dataInputAssociation>'
    if e['id'] == 'm2':
        inner += '<bpmn:dataOutputAssociation id="as2"><bpmn:targetRef>ds</bpmn:targetRef></bpmn:dataOutputAssociation>'
    if e['id'] == 's1':
        inner += '<bpmn:property id="s1_prop" name="__targetRef_placeholder"/><bpmn:dataInputAssociation id="as3"><bpmn:sourceRef>do</bpmn:sourceRef><bpmn:targetRef>s1_prop</bpmn:targetRef></bpmn:dataInputAssociation>'
    if e['type'] in ('msgstart', 'msgend'):
        inner += f'<bpmn:messageEventDefinition id="{e["id"]}_med"/>'
    attr = f' name="{name}"' if name else ''
    if e['type'] == 'gateway' and e['id'] in ('gw1', 'gw2', 'gw3', 'gs', 'gw4'):
        default = None
    return f'<bpmn:{t} id="{e["id"]}"{attr}>{inner}</bpmn:{t}>'

def seq_xml(s):
    name = f' name="{xesc(flat(s["label"]))}"' if s['label'] else ''
    return f'<bpmn:sequenceFlow id="{s["id"]}"{name} sourceRef="{s["s"]}" targetRef="{s["t"]}"/>'

k_nodes = [e for e in E.values() if e['pool'] == 'K']
v_nodes = [e for e in E.values() if e['pool'] == 'V']
k_seq = [s for s in SEQ if E[s['s']]['pool'] == 'K']
v_seq = [s for s in SEQ if E[s['s']]['pool'] == 'V']

x = ['<?xml version="1.0" encoding="UTF-8"?>',
     '<bpmn:definitions xmlns:bpmn="http://www.omg.org/spec/BPMN/20100524/MODEL" xmlns:bpmndi="http://www.omg.org/spec/BPMN/20100524/DI" '
     'xmlns:dc="http://www.omg.org/spec/DD/20100524/DC" xmlns:di="http://www.omg.org/spec/DD/20100524/DI" '
     'id="Defs_Klantenservice" targetNamespace="https://github.com/VoyageVista1/GroepInkoop" exporter="GroepInkoop" exporterVersion="1.0">',
     '<bpmn:collaboration id="Collab_Klantenservice">',
     '<bpmn:participant id="P_klant" name="Klant" processRef="Proc_klant"/>',
     '<bpmn:participant id="P_vv" name="VoyageVista" processRef="Proc_vv"/>',
     '<bpmn:participant id="P_lev" name="Leverancier (hotel op de bestemming)"/>']
for m in MSG:
    s = 'P_lev' if m['s'] == 'LEV' else m['s']
    t = 'P_lev' if m['t'] == 'LEV' else m['t']
    x.append(f'<bpmn:messageFlow id="{m["id"]}" name="{xesc(flat(m["label"]))}" sourceRef="{s}" targetRef="{t}"/>')
x.append('</bpmn:collaboration>')
x.append('<bpmn:process id="Proc_klant" isExecutable="false">')
x += [node_xml(e) for e in k_nodes] + [seq_xml(s) for s in k_seq]
x.append('</bpmn:process>')
x.append('<bpmn:process id="Proc_vv" isExecutable="false"><bpmn:laneSet id="LaneSet_vv">')
for lid, name, *_ in LANES:
    refs = ''.join(f'<bpmn:flowNodeRef>{e["id"]}</bpmn:flowNodeRef>' for e in v_nodes if e['lane'] == lid and e['type'] in BTYPE)
    x.append(f'<bpmn:lane id="{lid}" name="{xesc(flat(name))}">{refs}</bpmn:lane>')
x.append('</bpmn:laneSet>')
x += [node_xml(e) for e in v_nodes] + [seq_xml(s) for s in v_seq]
x.append('<bpmn:dataStoreReference id="ds" name="Klantdossier (werkplek)"/>')
x.append('<bpmn:dataObjectReference id="do" name="Compensatierichtlijn (% van reissom)" dataObjectRef="do_obj"/><bpmn:dataObject id="do_obj"/>')
x.append('</bpmn:process>')

# DI
def bnd(b):
    return f'<dc:Bounds x="{b[0]:.0f}" y="{b[1]:.0f}" width="{b[2]:.0f}" height="{b[3]:.0f}"/>'
def wps(pts):
    return ''.join(f'<di:waypoint x="{px:.0f}" y="{py:.0f}"/>' for px, py in pts)
def lbl(e):
    if e['type'] == 'gateway' and e['label']:
        return f'<bpmndi:BPMNLabel>{bnd((e["x"] - 40, (e["y"] + GR + 6) if e.get("below") else (e["y"] - GR - 44), 80, 34))}</bpmndi:BPMNLabel>'
    if e.get('lblright'):
        return f'<bpmndi:BPMNLabel>{bnd((e["x"] + ER + 6, e["y"] - 16, 90, 32))}</bpmndi:BPMNLabel>'
    if e['type'] in ('start', 'end', 'msgstart', 'msgend'):
        return f'<bpmndi:BPMNLabel>{bnd((e["x"] - 50, e["y"] + ER + 6, 100, 30))}</bpmndi:BPMNLabel>'
    if e['type'] == 'datastore':
        return f'<bpmndi:BPMNLabel>{bnd((e["x"] + 34, e["y"] - 16, 110, 32))}</bpmndi:BPMNLabel>'
    if e['type'] == 'dataobject':
        return f'<bpmndi:BPMNLabel>{bnd((e["x"] - 140, e["y"] - 24, 116, 48))}</bpmndi:BPMNLabel>'
    return ''

x.append('<bpmndi:BPMNDiagram id="Diagram_1"><bpmndi:BPMNPlane id="Plane_1" bpmnElement="Collab_Klantenservice">')
x.append(f'<bpmndi:BPMNShape id="P_klant_di" bpmnElement="P_klant" isHorizontal="true">{bnd((X0, POOL_K[0], W - 2 * X0, POOL_K[1] - POOL_K[0]))}</bpmndi:BPMNShape>')
x.append(f'<bpmndi:BPMNShape id="P_vv_di" bpmnElement="P_vv" isHorizontal="true">{bnd((X0, POOL_V[0], W - 2 * X0, POOL_V[1] - POOL_V[0]))}</bpmndi:BPMNShape>')
for lid, name, y0, y1, _ in LANES:
    x.append(f'<bpmndi:BPMNShape id="{lid}_di" bpmnElement="{lid}" isHorizontal="true">{bnd((X0 + 30, y0, W - 2 * X0 - 30, y1 - y0))}</bpmndi:BPMNShape>')
x.append(f'<bpmndi:BPMNShape id="P_lev_di" bpmnElement="P_lev" isHorizontal="true">{bnd((X0, POOL_L[0], W - 2 * X0, POOL_L[1] - POOL_L[0]))}</bpmndi:BPMNShape>')
for e in E.values():
    extra = ' isMarkerVisible="true"' if e['type'] == 'gateway' else ''
    x.append(f'<bpmndi:BPMNShape id="{e["id"]}_di" bpmnElement="{e["id"]}"{extra}>{bnd(bounds(e))}{lbl(e)}</bpmndi:BPMNShape>')
for s in SEQ:
    lab = ''
    if s['label']:
        lx, ly = s['lp']
        lab = f'<bpmndi:BPMNLabel>{bnd((lx - (0 if s["anchor"] == "start" else 70), ly - 12, 80, 16))}</bpmndi:BPMNLabel>'
    x.append(f'<bpmndi:BPMNEdge id="{s["id"]}_di" bpmnElement="{s["id"]}">{wps(s["pts"])}{lab}</bpmndi:BPMNEdge>')
for m in MSG:
    lx, ly = m['lp']
    x.append(f'<bpmndi:BPMNEdge id="{m["id"]}_di" bpmnElement="{m["id"]}">{wps(m["pts"])}<bpmndi:BPMNLabel>{bnd((lx - (0 if m["anchor"] == "start" else 90), ly - 14, 110, 30))}</bpmndi:BPMNLabel></bpmndi:BPMNEdge>')
for aid, s, t, pts, d in ASSOC:
    x.append(f'<bpmndi:BPMNEdge id="{aid}_di" bpmnElement="{aid}">{wps(pts)}</bpmndi:BPMNEdge>')
x.append('</bpmndi:BPMNPlane></bpmndi:BPMNDiagram></bpmn:definitions>')
open(os.path.join(OUT, 'klantenservice-proces.bpmn'), 'w').write('\n'.join(x))

# ---------------- HTML ----------------
rows = '\n'.join(f'<tr><td><span class="nr">{n}</span></td><td>{xesc(a)}</td><td class="muted">{xesc(b)}</td></tr>' for n, a, b in VERBETERINGEN)
tpl = open(os.path.join(os.path.dirname(__file__), 'proces_tpl.html')).read()
html = tpl.replace('{{W}}', str(W)).replace('{{SVG}}', svg).replace('{{ROWS}}', rows)
open(os.path.join(OUT, 'klantenservice-proces.html'), 'w').write(html)
print('ok', len(svg), len(html))
