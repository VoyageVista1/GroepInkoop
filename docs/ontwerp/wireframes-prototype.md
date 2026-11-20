# Klikbaar prototype — nieuwe wireframes Productontwikkeling & Inkoop

**Bestand:** `prototype/wireframes.html` (één zelfstandige pagina, geen build nodig)
**Bron:** FigJam *Project Agile Board*, sectie **Nieuwe Wireframes** en de 71 schermen `WF • PK01` t/m `WF • RP10`
**Navigatietest:** `tests/wireframes-navigatie.cjs` (Playwright)

Alle 71 wireframes zijn als klikbare schermen nagebouwd. Elk scherm heeft dezelfde inhoud, velden, knoppen en voorbeeldgegevens als in FigJam. Onder elk scherm staat het documentatieblok uit de wireframe: ERD-entiteiten, functiescheiding, navigatie en ERD-controle. Daar staan ook de uitgaande links.

## Figma Make — in de werkplek (hoofdversie)

**Make-bestand:** https://www.figma.com/make/ii7T5U9jz3XvIrHVqe355R — *VoyageVista Stijl Demo 2.0 + nieuwe wireframes* (team *739242's team*).

Dit is een volledige kopie van *VoyageVista Stijl Demo 2.0*, met de wireframes verwerkt in de werkplek. Open de demo-werkplek en ga naar **Productontwikkeling & Inkoop** in de zijbalk:

- **Productontwikkeling:** Nieuw · Dashboard, Productkansen, Reisproducten, Reisonderdelen, Planning, Catalogus en Testflows user stories
- **Inkoop:** Nieuw · Leveranciers, Aanbiedingen, Onderhandelingen, Contracten, Autorisatie en Schermindex

De route is `#wf.<SCHERM>`, bijvoorbeeld `#wf.CT05`. De wireframe wordt binnen de werkplek getoond. Het kruimelpad, de actieve link in de zijbalk en de meldingen volgen het scherm. Wijzigingen ten opzichte van het origineel (zie `prototype/make-integratie/`):

- `wireframes.html` en `wireframes-app.js` zijn nieuw.
- `navigation.js`: de wireframe-items staan in de groepen Productontwikkeling en Inkoop, en de route `wf` hoort bij Inkoop.
- `index.html`: één regel voor de actieve link in de zijbalk en één scripttag.
- Paden naar afbeeldingen, data en video's zijn relatief gemaakt, zodat de app als statische site draait.

Integratietest: `node tests/werkplek-wireframes.cjs <url-van-de-app>`. Laatste uitvoering: **30 geslaagd, 0 mislukt**. De test controleert dat de bestaande routes nog werken, de zijbalk, de iframe, een flow, of de zijbalk en het kruimelpad meeschuiven, een diepe link na herladen, en dat er geen 404's of JavaScript-fouten zijn.

## Figma Make — losse versie

**Make-bestand:** https://www.figma.com/make/hgj5dVUs8nEYel700Fl1ET (team *739242's team*). Bestaat uit `index.html` (= `prototype/wireframes.html`) en `images/voyagevista-logo-light.png`.

De zijbalk volgt de werkplek: **Algemeen** (Dashboard), **Productontwikkeling** (Productkansen, Reisproducten, Reisonderdelen, Planning, Catalogus), **Inkoop** (Leveranciers, Aanbiedingen, Onderhandelingen, Contracten) en **Beheer** (Autorisatie).

## Handmatig in een ander Make-bestand zetten

1. Open het Make-bestand *VoyageVista Stijl Demo 2.0*.
2. Maak in de map `public/` een nieuw bestand `wireframes.html` en plak de volledige inhoud van `prototype/wireframes.html` erin.
3. Open de preview op route `/wireframes.html`. Een scherm open je direct met bijvoorbeeld `/wireframes.html#/CT01`.
4. Optioneel: zet in de bestaande werkplek een link naar `/wireframes.html`, bijvoorbeeld onder *Help & documentatie*.

De pagina heeft geen invloed op `index.html` en de bestaande routes. Hij gebruikt dezelfde lettertypen (Urbanist en Poppins) en de groene kleuren van de werkplek.

## Opbouw

| Module | Schermen | Startscherm |
|---|---|---|
| 00 Dashboard | DA01, DA02 | DA01 |
| 01 Productkansen | PK01–PK06 | PK01 |
| 02 Reisproducten | RP01–RP10 | RP01 |
| 03 Reisonderdelen | RD01–RD07 | RD01 |
| 04 Leveranciers | LV01–LV07 | LV01 |
| 05 Aanbiedingen | AB01–AB05 | AB01 |
| 06 Onderhandelingen | ON01–ON08 | ON01 |
| 07 Contracten | CT01–CT13 | CT01 |
| 08 Planning | PL01–PL06 | PL01 |
| 09 Catalogus | CA01–CA06 | CA01 |
| 10 Autorisatie | AU01 | AU01 |

In de zijbalk staan ook **Testflows user stories** (`#/flows`) en **Schermindex** (`#/index`). De schermindex toont alle schermen met hun uitgaande verbindingen.

Uitzonderingsschermen die je in het echte proces alleen via een fout bereikt, zijn te openen via een gestreepte balk **Testscenario (uitzondering)**. Voorbeelden: versieconflict, verbinding valt weg, geen rechten, zoeken zonder resultaat.

## Gedrag (volgens de testbeschrijvingen op het board)

- Verplichte velden: leeg opslaan wordt geweigerd. De velden worden rood met uitleg en er verschijnt een samenvatting bovenaan.
- Contract en verlenging: een einddatum vóór de begindatum wordt geweigerd.
- Leverancier: een ongeldig e-mailadres geeft een melding. “Sakura Hotels” in Tokio geeft een waarschuwing voor een dubbele leverancier. Klik nogmaals om bewust door te gaan.
- Beoordelen (CT05, PK04, RP04, PL04): goedkeuren kan pas als alle controlepunten zijn aangevinkt. Terugsturen, afwijzen, parkeren en archiveren vragen verplicht om een reden.
- Onderhandeling afsluiten (ON05): akkoord wordt geweigerd zolang er een vervolgactie openstaat. Na ON06 *Taak opslaan* gaat akkoord door naar het contractformulier (CT03).
- Annuleren met ingevulde gegevens vraagt om bevestiging.
- In lijsten werken zoeken, het statusfilter en CSV-export. Zoeken zonder resultaat linkt naar het lege-resultatenscherm (PK05, CA03, ON07).
- Op een mobiel scherm klapt het menu in. Toetsenbord: tabelrijen openen met Enter, en de skiplink en focusmarkering zijn aanwezig.

## User story — contractbeheerder

*Als contractbeheerder wil ik de belangrijkste contracthandelingen in een prototype kunnen doorlopen, zodat ik kan beoordelen of registreren, goedkeuren en verlengen logisch verlopen.*

| Flow | Route |
|---|---|
| C1 Registreren | CT01 → + Nieuw → CT03 (validatie, datumcontrole) → Voorwaarden → CT04 → Opslaan → CT02 |
| C2 Goedkeuren / terugsturen | CT01 → CON-031 → CT05 → Goedkeuren → CT02 · of Terugsturen (reden) → CT06 → CT03 |
| C3 Verlengen | CT01 → KPI *Loopt af* → CT08 → CT07 → CT02 → Ter goedkeuring → CT05 |
| C4 Onderhandeling → contract | ON02 → ON05 (geblokkeerd) → ON06 → ON05 → Akkoord → CT03 |
| C5 Bezetting en archiveren | CT02 → CT12 → CT13 → PL02 · CT02 → CT11 (reden) → CT01 |
| Uitzonderingen | CT08 aflopend · CT09 geen rechten · CT10 opslaan mislukt · CT06 afwijzen |

## User story — productmanager

*Als productmanager wil ik de belangrijkste product- en leveranciersprocessen in een klikbaar prototype kunnen doorlopen, zodat ik kan beoordelen of de navigatie logisch werkt.*

| Flow | Route |
|---|---|
| P1 Productkans → reisproduct | PK01 → PK03 → PK02 → PK04 → Kansrijk → RP03 |
| P2 Reisproduct publiceren | RP01 → RP03 → RP07 → RD01 → RD03 → RD04 → RP02 → RP04 → RP10 → CA02 |
| P3 Teruggestuurd | RP04 → Terugsturen (reden) → RP05 → RP03 |
| P4 Leverancier en contact | LV01 → LV03 (validatie, dubbel) → LV02 → LV05 → LV07 |
| P5 Aanbod vergelijken en koppelen | LV02 → AB01 → AB05 → AB02 → AB04 → RD02 |
| P6 Catalogus en feedback | CA01 → CA02 → CA05 → CA06 |
| Uitzonderingen | PK05 · RP06 · RP08 · RP09 · RD06 · CA03 · CA04 · ON07 |

## Navigatiecontrole

```bash
node tests/wireframes-navigatie.cjs prototype/wireframes.html
```

De test opent alle 71 schermen en controleert ongeveer 500 links en knoppen op een bestaand doel. Hij controleert ook dat elk scherm minstens één inkomende link heeft, en doorloopt alle flows hierboven inclusief de foutpaden. Verder test hij de mobiele weergave en of er JavaScript-fouten optreden.

Laatste uitvoering: **791 geslaagd, 0 mislukt**.

## Afwijkingen van de wireframes

Hieronder staan alleen de plekken waar de wireframe zichtbaar fout of onvolledig was:

- **AU01:** de velden bevatten opvultekst (“MedewerkerID: MEDEWERKER”). Vervangen door een rechtenmatrix per rol. AU01 valt in de zijbalk onder *10 Autorisatie*, niet onder Dashboard.
- **PK06:** de detailvelden bevatten tijdlijntekst. Vervangen door product, resultaat, reden, datum en beoordelaar.
- **PK01:** de KPI *Beoordeeld* heet nu *Goedgekeurd*, net als de fase in de tabel. De eigenaar is een naam in plaats van een rol.
- **Veldlabels:** labels met databasenamen zijn leesbaar gemaakt (bijv. `ReisduurDagen` → “Reisduur (dagen)”, `AantalKamersPerNacht` → “Aantal kamers per nacht”).
- **Datums:** deadlines hebben nu een jaartal (bijv. 28-10-2026).
- **Extra knoppen:** waar het navigatieblok van de wireframe een vervolgscherm noemt zonder dat er een knop voor was, is die knop toegevoegd. Voorbeelden: CT03 → *Voorwaarden* / *Ter goedkeuring*, CT02 → *Bezetting* / *Archiveren*, ON02 → *Voorwaarden* / *Vervolgactie*.
- **Indexkaart:** de indexkaart op het board noemt 70 schermen, RP01–RP09 en alleen DA01 onder Autorisatie. Op het board staan er 71 (met RP10, AU01 en DA02). De indexkaart moet nog worden bijgewerkt.

## Definition of Done — status

| Punt | Status |
|---|---|
| Afgesproken flows klikbaar, knoppen naar de juiste bestemming | ✅ zie test |
| Uitzonderingssituaties bereikbaar | ✅ |
| Navigatie volledig gecontroleerd, fouten opgelost | ✅ automatisch. Nog in de Figma Make-preview controleren na het plakken |
| Ander teamlid heeft de flows getest | ⏳ via de pagina *Testflows user stories* |
| Prototype-link toegevoegd aan het backlogitem | ⏳ na publicatie in Figma Make |
