#!/usr/bin/env python3
"""Genereert het klantenserviceproces (BPMN 2.0) als SVG, HTML en .bpmn uit één model."""
from xml.sax.saxutils import escape as xesc
import os

OUT = os.path.dirname(os.path.abspath(__file__))
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
POOL_K = (70, 262)        # Klant
POOL_V = (282, 1052)      # VoyageVista
LANES = [                 # (id, naam, y0, y1, kleur)
    ('L_ks', 'Klantenservice-\nmedewerker\n(shop en\ncontactcenter)', 282, 642, '#ece4fb'),
    ('L_tl', 'Teamleider\nklantenservice', 642, 742, '#e6ddf8'),
    ('L_sr', 'Senior\nklantenservice', 742, 842, '#e2d8f6'),
    ('L_at', 'After Travel', 842, 942, '#f2e3f7'),
    ('L_fi', 'Financiën &\nAdministratie', 942, 1052, '#dde9f8'),
]
POOL_L = (1070, 1124)     # Leverancier (dichtgeklapt)
LEGEND_Y = 1152
H = 1244
W = 4680

yK, yKL = 135, 215
rU, rM, rL = 340, 450, 560
yLOW = 632                # retourroute onderin de lane Klantenservice
yTL, ySR, yAT, yFI = 692, 792, 892, 997

# element: id -> dict(type, x, y, label, lane, extra)
E = {}
def el(i, t, x, y, label='', pool='V', lane=None, **kw):
    E[i] = dict(id=i, type=t, x=x, y=y, label=label, pool=pool, lane=lane, **kw)

# Klant
el('k_start', 'start', 270, yK, 'Klant heeft vraag\nof klacht', 'K')
el('k1', 'task', 400, yK, 'Neemt contact op\n(telefoon, e-mail,\nshop, social media)', 'K')
el('k2', 'task', 3070, yK, 'Ontvangt antwoord,\nbesluit of voorstel', 'K')
el('kg1', 'gateway', 3210, yK, 'Besluit op\nklacht?', 'K')
el('k_end0', 'end', 3210, yKL, 'Klant\ngeholpen', 'K', lblright=True)
el('k3', 'task', 3350, yK, 'Reageert op\nbesluit (akkoord\nof bezwaar)', 'K')
el('kg2', 'gateway', 3490, yK, 'Akkoord?', 'K')
el('k4', 'task', 3650, yKL, 'Ontvangt\neindbesluit', 'K')
el('km', 'gateway', 3760, yK, '', 'K')
el('kc', 'gateway', 3870, yK, 'Compensatie\ntoegekend?', 'K')
el('k_end2', 'end', 3870, yKL, 'Klant\ngeholpen', 'K', lblright=True)
el('k5', 'task', 4010, yK, 'Vult zelf rekening-\nnummer in', 'K', badge=5)
el('k_end', 'end', 4140, yK, 'Klant\ngeholpen', 'K', lblright=True)

# Klantenservice-medewerker
el('ms', 'msgstart', 400, rM, 'Contact\nontvangen', lane='L_ks')
el('m1', 'task', 530, rM, 'Klant en boeking\nzoeken (e-mail,\ntelefoon, naam)', lane='L_ks')
el('m2', 'task', 700, rM, 'Contactmoment\nvastleggen in\nklantdossier', lane='L_ks', badge=1)
el('gz', 'gateway', 850, rM, 'Bestaande\nzaak?', lane='L_ks', below=True)
el('mz1', 'task', 980, rU, 'Contact toevoegen\naan zaak (zo nodig\nheropenen)', lane='L_ks', badge=8)
el('mz2', 'task', 980, rM, 'Klantzaak aanmaken\nen classificeren', lane='L_ks')
el('gzm', 'gateway', 1120, rM, '', lane='L_ks')
el('gim', 'gateway', 1340, rM, '', lane='L_ks')
el('gi', 'gateway', 1440, rM, 'Informatie\nvolledig?', lane='L_ks', below=True)
el('ma', 'task', 1440, rU, 'Klant om\naanvulling vragen', lane='L_ks', badge=10)
el('gw1', 'gateway', 1670, rM, 'Soort\nzaak?', lane='L_ks', below=True)
el('v1', 'task', 1810, rU, 'Vraag onderzoeken\n(FAQ, template,\ncollega)', lane='L_ks')
el('v2', 'task', 1970, rU, 'Antwoord opstellen\nof doorzetten naar\nandere afdeling', lane='L_ks')
el('gw2', 'gateway', 1810, rM, 'Klant nu\nop reis?', lane='L_ks')
el('m5', 'task', 1950, rL, 'Hotel vragen om\noplossing ter\nplaatse', lane='L_ks', badge=3)
el('got', 'gateway', 2090, rL, 'Opgelost ter\nplaatse?', lane='L_ks')
el('gm1', 'gateway', 2230, rM, '', lane='L_ks')
el('m6', 'task', 2370, rM, 'Klacht beoordelen\n(historie, bewijs,\nzelf gekozen?)', lane='L_ks', badge=4)
el('gw3', 'gateway', 2510, rM, 'Klacht\ngegrond?', lane='L_ks')
el('m7', 'task', 2510, rL, 'Ongegrond\nverklaren met\nonderbouwing', lane='L_ks')
el('m8', 'task', 2650, rM, 'Compensatie-\nvoorstel volgens\nrichtlijn', lane='L_ks')
el('gm3', 'gateway', 2880, rL, '', lane='L_ks')
el('gm2', 'gateway', 2930, rM, '', lane='L_ks')
el('m10', 'task', 3070, rM, 'Klant informeren\n(antwoord, besluit\nof voorstel)', lane='L_ks', badge=7)
el('gv2', 'gateway', 3210, rM, 'Reactie klant\nnodig?', lane='L_ks')
el('m11', 'receive', 3350, rM, 'Reactie klant\nverwerken', lane='L_ks')
el('tm', 'timer', 3395, rM + TH / 2, 'Geen reactie\nna 7 dagen', lane='L_ks', attached='m11')
el('mh', 'task', 3330, rL, 'Herinnering sturen\nen contactpoging\nvastleggen', lane='L_ks', badge=11)
el('mh_end', 'end', 3448, rL, 'Herinnering\nverstuurd', lane='L_ks')
el('gw4', 'gateway', 3490, rM, 'Klant\nakkoord?', lane='L_ks')
el('gcm', 'gateway', 3570, rM, '', lane='L_ks')
el('gc', 'gateway', 3650, rM, 'Compensatie\ntoegekend?', lane='L_ks', below=True)
el('ge1', 'gateway', 4150, rM, '', lane='L_ks')
el('ge2', 'gateway', 4280, rM, '', lane='L_ks')
el('m12', 'task', 4420, rM, 'Uitkomst vastleggen\nen klantzaak\nafsluiten', lane='L_ks', badge=9)
el('m_end', 'end', 4570, rM, 'Zaak\nafgesloten', lane='L_ks')
el('ds', 'datastore', 615, rL, 'Klantdossier\n(werkplek)', lane='L_ks')

# Teamleider
el('t1', 'task', 1250, yTL, 'Urgentie bepalen\nen behandelaar\ntoewijzen', lane='L_tl', badge=2)

# Senior
el('s1', 'task', 2650, ySR, 'Voorstel\ncontroleren\n(vier ogen)', lane='L_sr', badge=6)
el('gs', 'gateway', 2790, ySR, 'Goed-\ngekeurd?', lane='L_sr', below=True)
el('do', 'dataobject', 2480, ySR, 'Compensatie-\nrichtlijn\n(% van reissom)', lane='L_sr')

# After Travel
el('a1', 'task', 3490, yAT, 'Klacht opnieuw\nbeoordelen\n(maatwerk)', lane='L_at')
el('a2', 'task', 3650, yAT, 'Eindbesluit\nvastleggen en\ncommuniceren', lane='L_at')

# Financiën
el('f1', 'receive', 4010, yFI, 'Rekeningnummer\nontvangen en\nuitbetalen', lane='L_fi')

def bounds(e):
    t = e['type']
    if t in ('task', 'receive'):
        return e['x'] - TW / 2, e['y'] - TH / 2, TW, TH
    if t == 'gateway':
        return e['x'] - GR, e['y'] - GR, 2 * GR, 2 * GR
    if t in ('start', 'end', 'msgstart', 'msgend', 'timer'):
        return e['x'] - ER, e['y'] - ER, 2 * ER, 2 * ER
    if t == 'datastore':
        return e['x'] - 24, e['y'] - 20, 48, 40
    if t == 'dataobject':
        return e['x'] - 16, e['y'] - 21, 32, 42

def P(i, side):
    e = E[i]; x, y, w, h = bounds(e)
    return {'l': (x, y + h / 2), 'r': (x + w, y + h / 2), 't': (x + w / 2, y), 'b': (x + w / 2, y + h)}[side]

# ---------------- Stromen ----------------
SEQ = []
def seq(i, s, t, pts, label='', lp=None, anchor='start'):
    SEQ.append(dict(id='sf_' + i, s=s, t=t, pts=pts, label=label, lp=lp, anchor=anchor))
def line(i, s, t, label='', lp=None):
    seq(i, s, t, [P(s, 'r'), P(t, 'l')], label, lp)

# Klant
line('fk1', 'k_start', 'k1')
line('fk2', 'k1', 'k2')
line('fk3', 'k2', 'kg1')
line('fk4', 'kg1', 'k3', 'Ja', (3242, yK - 8))
seq('fk5', 'kg1', 'k_end0', [P('kg1', 'b'), P('k_end0', 't')], 'Nee', (3218, yK + 44))
line('fk6', 'k3', 'kg2')
line('fk7', 'kg2', 'km', 'Ja', (3522, yK - 8))
seq('fk8', 'kg2', 'k4', [P('kg2', 'b'), (3490, yKL), P('k4', 'l')], 'Nee (bezwaar)', (3482, yK + 46), 'end')
seq('fk9', 'k4', 'km', [P('k4', 'r'), (3760, yKL), P('km', 'b')])
line('fk10', 'km', 'kc')
line('fk11', 'kc', 'k5', 'Ja', (3902, yK - 8))
seq('fk12', 'kc', 'k_end2', [P('kc', 'b'), P('k_end2', 't')], 'Nee', (3878, yK + 44))
line('fk13', 'k5', 'k_end')

# VoyageVista
line('f1', 'ms', 'm1')
line('f2', 'm1', 'm2')
line('f3', 'm2', 'gz')
seq('f4', 'gz', 'mz1', [P('gz', 't'), (850, rU), P('mz1', 'l')], 'Ja', (858, rU + 30))
line('f5', 'gz', 'mz2', 'Nee', (874, rM - 8))
seq('f6', 'mz1', 'gzm', [P('mz1', 'r'), (1120, rU), P('gzm', 't')])
line('f7', 'mz2', 'gzm')
seq('f8', 'gzm', 't1', [P('gzm', 'b'), (1120, yTL), P('t1', 'l')])
seq('f9', 't1', 'gim', [P('t1', 'r'), (1340, yTL), P('gim', 'b')])
line('f9a', 'gim', 'gi')
line('f9b', 'gi', 'gw1', 'Ja', (1472, rM - 8))
seq('f9c', 'gi', 'ma', [P('gi', 't'), P('ma', 'b')], 'Nee', (1448, rU + 52))
seq('f9d', 'ma', 'gim', [P('ma', 'l'), (1340, rU), P('gim', 't')])
seq('f10', 'gw1', 'v1', [P('gw1', 't'), (1670, rU), P('v1', 'l')], 'Vraag of wijziging', (1662, rU - 12), 'end')
line('f11', 'v1', 'v2')
seq('f12', 'v2', 'gm2', [P('v2', 'r'), (2930, rU), P('gm2', 't')])
line('f13', 'gw1', 'gw2', 'Klacht', (1702, rM - 8))
seq('f14', 'gw2', 'm5', [P('gw2', 'b'), (1810, rL), P('m5', 'l')], 'Ja', (1818, rL - 10))
line('f15', 'gw2', 'gm1', 'Nee', (1842, rM - 8))
line('f16', 'm5', 'got')
seq('f17', 'got', 'gm1', [P('got', 'r'), (2230, rL), P('gm1', 'b')], 'Nee', (2122, rL - 8))
seq('f18', 'got', 'gm3', [P('got', 'b'), (2090, yLOW), (2880, yLOW), P('gm3', 'b')], 'Ja', (2098, rL + 46))
line('f19', 'gm1', 'm6')
line('f20', 'm6', 'gw3')
line('f21', 'gw3', 'm8', 'Ja', (2542, rM - 8))
seq('f22', 'gw3', 'm7', [P('gw3', 'b'), P('m7', 't')], 'Nee', (2518, rM + 46))
line('f23', 'm7', 'gm3')
seq('f23a', 'gm3', 'gm2', [P('gm3', 't'), (2880, rM), P('gm2', 'l')])
seq('f24', 'm8', 's1', [P('m8', 'b'), P('s1', 't')])
line('f25', 's1', 'gs')
seq('f26', 'gs', 'm8', [P('gs', 't'), (2790, rM), P('m8', 'r')], 'Nee (met reden),\nterug', (2798, ySR - 70))
seq('f27', 'gs', 'gm2', [P('gs', 'r'), (2930, ySR), P('gm2', 'b')], 'Ja', (2824, ySR - 8))
line('f28', 'gm2', 'm10')
line('f29', 'm10', 'gv2')
line('f30', 'gv2', 'm11', 'Ja', (3242, rM - 8))
seq('f31', 'gv2', 'ge2', [P('gv2', 'b'), (3210, yLOW), (4280, yLOW), P('ge2', 'b')], 'Nee', (3218, rM + 46))
line('f32', 'm11', 'gw4')
seq('ft1', 'tm', 'mh', [P('tm', 'b'), (E['tm']['x'], rL - TH / 2)])
line('ft2', 'mh', 'mh_end')
line('f33', 'gw4', 'gcm', 'Ja', (3522, rM - 8))
line('f33a', 'gcm', 'gc')
seq('f34', 'gw4', 'a1', [P('gw4', 'b'), P('a1', 't')], 'Nee (bezwaar)', (3498, yTL - 12))
line('f35', 'a1', 'a2')
seq('f36', 'a2', 'gcm', [P('a2', 't'), (3650, 600), (3570, 600), P('gcm', 'b')])
seq('f37', 'gc', 'f1', [P('gc', 'r'), (3970, rM), (3970, yFI - TH / 2)], 'Ja', (3710, rM - 8))
seq('f38', 'gc', 'ge1', [P('gc', 't'), (3650, rU), (4150, rU), P('ge1', 't')], 'Nee', (3658, rU + 30))
seq('f39', 'f1', 'ge1', [P('f1', 'r'), (4150, yFI), P('ge1', 'b')])
line('f40', 'ge1', 'ge2')
line('f41', 'ge2', 'm12')
line('f42', 'm12', 'm_end')

MSG = []
def msg(i, s, t, pts, label='', lp=None, anchor='start'):
    MSG.append(dict(id=i, s=s, t=t, pts=pts, label=label, lp=lp, anchor=anchor))

msg('mf1', 'k1', 'ms', [P('k1', 'b'), P('ms', 't')], 'Vraag of klacht', (408, 300))
msg('mf8', 'ma', 'KLANT', [(1425, rU - TH / 2), (1425, POOL_K[1])], 'Vraag om aanvulling', (1417, 292), 'end')
msg('mf9', 'KLANT', 'ma', [(1455, POOL_K[1]), (1455, rU - TH / 2)], 'Aanvulling', (1463, 292))
msg('mf2', 'm10', 'k2', [P('m10', 't'), P('k2', 'b')], 'Antwoord, besluit\nof voorstel', (3078, 300))
msg('mf3', 'k3', 'm11', [P('k3', 'b'), P('m11', 't')], 'Akkoord of\nbezwaar', (3358, 300))
msg('mf4', 'a2', 'k4', [(3700, yAT - TH / 2), (3700, yKL + TH / 2)], 'Eindbesluit', (3708, 520))
msg('mf5', 'k5', 'f1', [(4040, yK + TH / 2), (4040, yFI - TH / 2)], 'Rekeningnummer via\nMijn VoyageVista', (4048, 300))
msg('mf6', 'm5', 'LEV', [(1935, rL + TH / 2), (1935, POOL_L[0])], 'Verzoek om\noplossing', (1925, 760), 'end')
msg('mf7', 'LEV', 'm5', [(1965, POOL_L[0]), (1965, rL + TH / 2)], 'Reactie hotel', (1973, 760))

ASSOC = [  # (id, bron, doel, punten, richting)
    ('as1', 'ds', 'm1', [(E['ds']['x'] - 12, rL - 20), (560, rM + TH / 2)], 'in'),
    ('as2', 'm2', 'ds', [(670, rM + TH / 2), (E['ds']['x'] + 14, rL - 20)], 'out'),
    ('as3', 'do', 's1', [(E['do']['x'] + 16, ySR), P('s1', 'l')], 'in'),
    ('as4', 'do', 'm8', [(E['do']['x'], ySR - 21), (E['do']['x'], 700), (2610, 700), (2610, rM + TH / 2)], 'in'),
]

VERBETERINGEN = [
    (1, 'Contactmoment vastleggen met vaste velden (kanaal, categorie, samenvatting, vervolgactie) in plaats van één vrij opmerkingenveld. Datum en medewerker vult het systeem zelf in. IBAN- en paspoortnummers worden geblokkeerd.',
     'Handmatige registratie en geen uniforme afhandeling (KP1, KP3, GP1); AVG: geen IBAN of paspoort opslaan (interview) · UC-K02, UC-K13'),
    (2, 'De teamleider bepaalt de urgentie en wijst een behandelaar toe; is de klant op reis, dan is de urgentie automatisch Hoog. Herverdelen gaat met een overdrachtsnotitie.',
     'Moeilijk prioriteren van vragen, lange reactietijden (KP2, KP5) · UC-K05, UC-K06'),
    (3, 'Bij een klant op reis vraagt de medewerker eerst het hotel om een oplossing ter plaatse. Lukt dat, dan bevestigt de medewerker de oplossing aan de klant en sluit de zaak af.',
     'Klachten die al op de bestemming opgelost hadden kunnen worden (interview) · UC-K08'),
    (4, 'De klacht wordt beoordeeld met de volledige klanthistorie en het bewijs, inclusief of de klant de accommodatie zelf koos.',
     'Beperkt inzicht in eerdere contacten (KP4, GP1) · UC-K03, UC-K08'),
    (5, 'Alleen bij toegekende compensatie vult de klant zelf het rekeningnummer in. Financiën betaalt pas uit als het binnen is; VoyageVista slaat het nergens op.',
     'AVG: geen IBAN opslaan (interview) · UC-K09, UC-K13'),
    (6, 'Een tweede medewerker keurt het compensatievoorstel goed. Wie het voorstel indient, mag het niet zelf goedkeuren.',
     'Vier-ogenprincipe; het systeem doet nu een voorstel dat een mens altijd moet controleren (interview) · UC-K09'),
    (7, 'Voor het versturen controleert het systeem de reisstatus, zodat de klant geen onterecht bericht krijgt (zoals een vertragingsbrief terwijl hij al op de bestemming is).',
     'Fouten door handmatige registratie (interview K6, KP5) · UC-K10'),
    (8, 'Nieuw contact over een bestaande zaak komt in die zaak; een afgesloten zaak wordt heropend in plaats van dubbel aangemaakt.',
     'Versnipperde klantcommunicatie; collega’s geven verschillende antwoorden (GP1) · UC-K04'),
    (9, 'Afsluiten kan pas met een vastgelegde uitkomst en als alle vervolgacties klaar zijn. Daarna mag de klant om verwijdering van gegevens vragen.',
     'Geen uniforme afhandeling (KP3); bewaren tot de klant thuis is (interview P3) · UC-K04, UC-K12'),
    (10, 'Is de informatie niet volledig, dan vraagt de behandelaar de klant om aanvulling (status Wacht op klant) en pakt de zaak daarna weer op.',
     'Zaken die niet beoordeeld kunnen worden door ontbrekende gegevens (walkthrough #266) · UC-K07, UC-K08'),
    (11, 'Reageert de klant niet op een besluit of voorstel, dan gaat na 7 dagen een herinnering en wordt de contactpoging vastgelegd. De zaak blijft wachten op de reactie.',
     'Zaken die blijven openstaan als de klant niet reageert (walkthrough #266) · UC-K08, UC-K10'),
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
                o.append(text_lines(x + e.get('ldx', 0), y + GR + 24 if e.get('below') else y - GR - 22, e['label'], size=12, weight=600))
        elif t in ('start', 'msgstart'):
            o.append(f'<circle cx="{x}" cy="{y}" r="{ER}" fill="{C["start"]}" stroke="{C["startS"]}" stroke-width="1.8"/>')
            if t == 'msgstart':
                o.append(ENV(x - 8, y - 5.5, stroke=C['startS']))
            o.append(text_lines(x, y + ER + 20, e['label'], size=12, weight=500, fill=C['quiet']))
        elif t == 'timer':
            o.append(f'<circle cx="{x}" cy="{y}" r="{ER}" fill="#fff" stroke="{C["line"]}" stroke-width="1.5" stroke-dasharray="4 3"/>'
                     f'<circle cx="{x}" cy="{y}" r="{ER - 4}" fill="#fff" stroke="{C["line"]}" stroke-width="1.3" stroke-dasharray="4 3"/>'
                     f'<circle cx="{x}" cy="{y}" r="{ER - 8}" fill="none" stroke="{C["line"]}" stroke-width="1.3"/>'
                     f'<path d="M{x} {y - 7} V{y} L{x + 5} {y + 3}" fill="none" stroke="{C["line"]}" stroke-width="1.4"/>')
            o.append(text_lines(x - ER - 8, y + 18, e['label'], size=12, weight=500, anchor='end', fill=C['quiet']))
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
    item(34, lambda x, y: f'<circle cx="{x + 17}" cy="{y}" r="15" fill="#fff" stroke="{C["line"]}" stroke-width="1.5" stroke-dasharray="4 3"/><circle cx="{x + 17}" cy="{y}" r="11" fill="none" stroke="{C["line"]}" stroke-width="1.3" stroke-dasharray="4 3"/><path d="M{x + 17} {y - 6} V{y} L{x + 21} {y + 3}" fill="none" stroke="{C["line"]}" stroke-width="1.4"/>', 'Timer (niet-\nonderbrekend)')
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
         'msgstart': 'startEvent', 'end': 'endEvent', 'msgend': 'endEvent', 'timer': 'boundaryEvent'}
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
    if e['id'] == 'm8':
        inner += '<bpmn:property id="m8_prop" name="__targetRef_placeholder"/><bpmn:dataInputAssociation id="as4"><bpmn:sourceRef>do</bpmn:sourceRef><bpmn:targetRef>m8_prop</bpmn:targetRef></bpmn:dataInputAssociation>'
    if e['id'] == 's1':
        inner += '<bpmn:property id="s1_prop" name="__targetRef_placeholder"/><bpmn:dataInputAssociation id="as3"><bpmn:sourceRef>do</bpmn:sourceRef><bpmn:targetRef>s1_prop</bpmn:targetRef></bpmn:dataInputAssociation>'
    if e['type'] in ('msgstart', 'msgend'):
        inner += f'<bpmn:messageEventDefinition id="{e["id"]}_med"/>'
    if e['type'] == 'timer':
        inner += f'<bpmn:timerEventDefinition id="{e["id"]}_ted"><bpmn:timeDuration xsi:type="bpmn:tFormalExpression">P7D</bpmn:timeDuration></bpmn:timerEventDefinition>'
    attr = f' name="{name}"' if name else ''
    if e['type'] == 'timer':
        attr += f' attachedToRef="{e["attached"]}" cancelActivity="false"'
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
     'xmlns:dc="http://www.omg.org/spec/DD/20100524/DC" xmlns:di="http://www.omg.org/spec/DD/20100524/DI" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" '
     'id="Defs_Klantenservice" targetNamespace="https://github.com/VoyageVista1/GroepInkoop" exporter="GroepInkoop" exporterVersion="1.0">',
     '<bpmn:collaboration id="Collab_Klantenservice">',
     '<bpmn:participant id="P_klant" name="Klant" processRef="Proc_klant"/>',
     '<bpmn:participant id="P_vv" name="VoyageVista" processRef="Proc_vv"/>',
     '<bpmn:participant id="P_lev" name="Leverancier (hotel op de bestemming)"/>']
for m in MSG:
    PART = {'LEV': 'P_lev', 'KLANT': 'P_klant'}
    s, t = PART.get(m['s'], m['s']), PART.get(m['t'], m['t'])
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
        return f'<bpmndi:BPMNLabel>{bnd((e["x"] - 40 + e.get("ldx", 0), (e["y"] + GR + 6) if e.get("below") else (e["y"] - GR - 44), 80, 34))}</bpmndi:BPMNLabel>'
    if e.get('lblright'):
        return f'<bpmndi:BPMNLabel>{bnd((e["x"] + ER + 6, e["y"] - 16, 90, 32))}</bpmndi:BPMNLabel>'
    if e['type'] in ('start', 'end', 'msgstart', 'msgend'):
        return f'<bpmndi:BPMNLabel>{bnd((e["x"] - 50, e["y"] + ER + 6, 100, 30))}</bpmndi:BPMNLabel>'
    if e['type'] == 'timer':
        return f'<bpmndi:BPMNLabel>{bnd((e["x"] - ER - 92, e["y"] + 2, 86, 32))}</bpmndi:BPMNLabel>'
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
