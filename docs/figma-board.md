# FigJam-board: Project Agile Board

**Link:** [Project Agile Board (FigJam)](https://www.figma.com/board/ManUSFsMrVgktm6UwReajA/Project-Agile-Board?node-id=0-1&p=f&t=Bxb2WEIrRXCM9J36-0)

Dit document beschrijft wat er op het FigJam-board staat, zodat de repo en het board naar elkaar verwijzen. Stand: 8 oktober 2026 (na het koppelen van de use cases aan de stories #189–#226). Het board zelf blijft de bron; dit is een overzicht plus een lijst met verbeterpunten.

---

## 1. Indeling van het board

| Sectie | Inhoud |
| --- | --- |
| **Productontwikkeling & Inkoop** | Primaire use cases (actoren Inkoper, Manager, Medewerker), toelichting casus, problemen uit de casus en de uitgewerkte use cases met `<<include>>`/`<<extend>>`. |
| **Klantenservice & Support** | Primaire use cases (Klantenservicemedewerker, Manager) en de uitgewerkte use cases. |
| **Use case descriptions: Productontwikkeling & inkoop** | Tabellen voor UC01–UC10: doel, primaire actor, trigger, preconditie, hoofdscenario, postconditie, alternatieve scenario's. |
| **Use case Refinement** | Tabel per afdeling: welke primaire use cases zijn hernoemd, verbreed of secundair geworden. |
| **User flows Productontwikkeling & Inkoop (na refinement)** | Activiteitendiagrammen (START → EINDE, met beslisruiten en foutpaden) voor UC01–UC10. |
| **User flows productontwikkeling & inkoop (OUD – vóór refinement)** | De eerdere flows met de oude nummering. Kunnen weg. |
| **Scope Productontwikkeling & Inkoop** | Wat we bouwen, welke schermen nodig zijn en welke gegevens een reisproduct en reisonderdeel hebben. |
| **Proces** | Tabel met randgevallen en het verwachte gedrag van het systeem. |
| **ERD** | Datamodel (als afbeelding). |
| **Retrospectives** | Wat ging goed / blijven doen / stoppen / kan beter. |
| **Interview TUI** | Tekst van de sprintreview van sprint 1 (sprintdoel, rollen, status backlog). |
| **Kopie Work Area** | Tweede, oudere versie van de primaire use cases Productontwikkeling & Inkoop. |
| **Literatuurlijst** | Links naar de UML 2.5.1-specificatie (OMG) en een voorbeeldhoofdstuk over use cases (Pearson). |

## 2. Use cases en user flows Productontwikkeling & Inkoop

Na de use case refinement (oktober) zijn er tien primaire use cases. De user flows staan op het board in de sectie **"User flows Productontwikkeling & Inkoop (na refinement)"**. De oude flows (nummering van vóór de refinement) staan ernaast in de sectie met "(OUD – vóór refinement)" in de naam en kunnen weg.

Kleuren in de flows: blauw = start/einde, paars = actie van de gebruiker, turquoise = actie van het systeem, groen = beslissing, rood = foutmelding (terug naar de invoer).

| Nr. | Use case | Actor | User stories | Kern van de user flow |
| --- | --- | --- | --- | --- |
| UC01 | Nieuw reisproduct ontwikkelen | Inkoper | #190–#192 | Formulier openen → productgegevens, reisonderdelen en kenmerken invullen → optioneel leverancier, deadline, media → opslaan → velden geldig? (nee: foutmelding, terug) → publiceren of opslaan als concept. |
| UC02 | Onderhandeling opvolgen | Inkoper | #213–#215 | Dashboard → zoeken/filteren → selecteren → status invoeren, leverancier koppelen, optioneel notitie/vervolgafspraak → opslaan → geldig? → escaleren naar manager? → onderhandeling afgerond? → afsluiten. |
| UC03 | Bestaand reisproduct bijwerken | Inkoper | #193 | Dashboard → zoeken/filteren → product selecteren → aanpassen → opslaan → geldig? → systeem logt wijziging → publiceren of concept. |
| UC04 | Productontwikkeling plannen en volgen | Inkoper | #223–#225 | Planningsoverzicht → mijlpalen tonen → mijlpaal bijwerken? → opslaan → geldig? → deadline nadert? (ja: melding) → dashboard met voortgang. |
| UC05 | Leverancierscontract beheren | Inkoper | #216–#219 | Leverancier zoeken/filteren en selecteren → contract aanmaken → afspraken en start-/einddatum → opslaan → geldig? → contract gekoppeld aan leverancier. |
| UC06 | Leveranciersrelatie beheren | Inkoper | #194–#198 | Leveranciersoverzicht → filteren → *nieuwe leverancier registreren* (invullen → geldig? → opslaan) of *leverancier bekijken* (prijshistorie, contractstatus → exporteren naar PDF of delen met manager). |
| UC07 | Leveranciersaanbod vastleggen | Inkoper | #212 | Leverancier selecteren → aanbod toevoegen → gegevens, prijs en voorwaarden → zelf controleren → opslaan → geldig? → aanbod zichtbaar in dashboard. |
| UC08 | Contractverplichtingen bewaken | Inkoper | #220–#222 | Contractendashboard → termijnen en bezetting bekijken → aflopend contract of lage bezetting? → melding → verlengen, heronderhandelen (naar UC02) of doorgeven aan Marketing & Sales → besluit vastleggen. |
| UC09 | Productgegevens beschikbaar stellen | Medewerker andere afdeling | #226 | Productdashboard → zoeken/filteren → gevonden? (nee: "Geen reisproducten gevonden") → details bekijken → exporteren, feedback geven of als favoriet opslaan. |
| UC10 | Productkans onderzoeken | Inkoper | #189 | Trends en klantbehoeftes vastleggen → klantwensen koppelen aan productideeën → onderzoeksrapport → kansrijk idee? → doorzetten naar UC01. |

### Use case descriptions (bijgewerkt 8 oktober)

De tien descriptions zijn op het board opnieuw opgezet, in dezelfde tabelstijl als Klantenservice, zodat ze één op één aansluiten op de flows en op GitHub:

- Vaste opbouw: Use case, Nummer (met de GitHub-issues), Doel, Primaire actor, Trigger, Preconditie, genummerd hoofdscenario, Postconditie en genummerde alternatieve scenario's (bijv. "6a.").
- Het veld Nummer verwijst naar de functionele stories van epic #4 (#189–#198, #212–#226), niet meer naar de oude stories #82–#146.
- De stappen zijn gecontroleerd tegen de acceptatiecriteria van die stories. Dubbele of verkeerde stappen zijn eruit (UC07: "vergelijken" verwijderd; geldigheidsperiode toegevoegd).
- Foutpaden staan als alternatief scenario in elke description, net als in de flows.
- De sectie staat in een raster van vier kolommen, op volgorde UC01–UC10.

**Nog open (Inkoop):** de reisroute en volgorde van reisonderdelen (#191) en het beheer van de vaste lijsten voor kamertypes en faciliteiten (#192) staan nog niet als stap in UC01. De flow van UC10 noemt nog een "onderzoeksrapport"; de description en #189 spreken van de conclusie van het onderzoek.

## 3. Use cases en user flows Klantenservice & Support

Op 8 oktober zijn de descriptions van Klantenservice opnieuw opgezet en daarna gekoppeld aan de functionele stories van epic #5 (één story per use case, #199–#211). De volledige tekst staat ook in [ontwerp/use-cases-klantenservice.md](ontwerp/use-cases-klantenservice.md), met de flows als Mermaid-diagram. De sectie staat in een raster van vier kolommen, op volgorde UC-K01–UC-K13. De descriptions hebben dezelfde opbouw als bij Inkoop en de user flows zijn opnieuw gemaakt in de sectie **"User flows Klantenservice & Support (na refinement)"**. De oude flows (UC-K01–UC-K09 met de namen van vóór de refinement) hebben "(OUD – vóór refinement)" in de naam gekregen.

Wat er mis was: de descriptions waren half omgenummerd (UC-K04 stond er twee keer in, UC-K06 had de postconditie en alternatieve scenario's van "Klacht behandelen"), en de flows hadden nog de oude namen, terwijl de use-casediagrammen dertien use cases hebben.

| Nr. | Use case | Actor | User story |
| --- | --- | --- | --- |
| UC-K01 | Klant en boeking opzoeken | Klantenservicemedewerker | #199 |
| UC-K02 | Klantcontact registreren | Klantenservicemedewerker | #200 |
| UC-K03 | Klantdossier en contactgeschiedenis raadplegen | Klantenservicemedewerker | #201 |
| UC-K04 | Klantzaak beheren | Klantenservicemedewerker | #202 |
| UC-K05 | Klantzaken prioriteren en toewijzen | Manager (teamleider) | #203 |
| UC-K06 | Werkvoorraad en reactietijden bewaken | Klantenservicemedewerker | #204 |
| UC-K07 | Klantvraag onderzoeken en beantwoorden | Klantenservicemedewerker | #205 |
| UC-K08 | Klacht volgens vaste werkwijze afhandelen | Klantenservicemedewerker | #206 |
| UC-K09 | Oplossing of compensatie vastleggen | Indiener en senior medewerker | #207 |
| UC-K10 | Klant informeren en zaak opvolgen | Klantenservicemedewerker | #208 |
| UC-K11 | Klachten en klantfeedback analyseren | Manager (teamleider) | #209 |
| UC-K12 | Klantgegevens en bewaartermijnen beheren | Klantenservicemedewerker | #210 |
| UC-K13 | Privacy en gevoelige gegevens bewaken | Systeem | #211 |

De descriptions gebruiken de interviewbevindingen uit [interview-analyse.md](interview-analyse.md): zoeken op e-mailadres (K1), escalatiepad naar After Travel (K8), compensatie als percentage van de reissom met controle door een tweede medewerker (K9), geen IBAN of paspoortnummer opslaan (P1, P2) en gegevens bewaren tot de klant thuis is (P3).

**Nog te doen:** het primaire use-casediagram van Klantenservice toont negen use cases. Klantzaak beheren, Werkvoorraad en reactietijden bewaken, Klant informeren en zaak opvolgen en Privacy en gevoelige gegevens bewaken staan wel in de uitgewerkte diagrammen, maar nog niet in het primaire diagram en de refinement-tabel.

**Nog open (Klantenservice), gevonden bij de controle tegen GitHub:**

- UC-K02: de vervolgactie uit #200 staat niet in de stappen.
- UC-K11: het opvolgen van een structurele verbeteractie (#209) ontbreekt.
- UC-K13: de privacycontrole moet volgens #211 ook werken bij een directe opslagactie, niet alleen in het scherm.
- Flows tegenover descriptions: in de flow van UC-K09 stelt het systeem het klachttype vast en berekent het het percentage, in de description doet de medewerker dat; de flow van UC-K06 heeft een stap "Zaak met hoogste urgentie oppakken" en de flow van UC-K10 een controle op reisstatus die niet in de description staan.

### BPMN en sprintchecklist

- **BPMN Klantenservice & Support** (issue #168): herzien op 8 oktober, met de lanes Klantenservice, Teamleider, Senior medewerker, After Travel en Financiën. Bron en export staan in [proces/](proces) (`gen_bpmn.py` maakt de .svg, .bpmn en .html).
- **Walkthrough BPMN** (test VoyageVista#266, 22 oktober): zeven scenario's doorlopen. Aangepast: lus voor aanvullende informatie, bevestiging aan de klant als het hotel het oplost, bezwaar ook bij een ongegronde klacht, rekeningnummer alleen bij toegekende compensatie, Financiën wacht op het rekeningnummer, herinnering na 7 dagen zonder reactie, en afkeuren door de senior alleen met reden. Het volledige testverslag staat in `proces/klantenservice-proces.html`. Open vraag voor de opdrachtgever: is 7 dagen de juiste termijn voor een herinnering?
- **Sprint planning checklist:** op het board staat een afvinklijst voor de sprintplanning, om aan de docenten te laten zien.

## 4. Scope en gegevens (uit het board)

**Schermen:** reisproducten-overzicht (zoekveld, lijst met naam en bestemming, knop "Nieuw reisproduct"), reisproduct aanmaken/bewerken (velden, lijst met reisonderdelen, Opslaan/Annuleren) en reisproduct bekijken (knop Bewerken, terug naar overzicht).

**Reisproduct:** productnummer (automatisch, uniek, niet aanpasbaar), productnaam (verplicht), bestemming (verplicht), omschrijving (optioneel), reisonderdelen (0..n), laatst gewijzigd (automatisch), versienummer (automatisch, tegen ongemerkt overschrijven).

**Reisonderdeel:** onderdeelnummer (automatisch, uniek), soort (accommodatie, vervoer of activiteit), naam (verplicht), omschrijving (optioneel), bijbehorend reisproduct (automatisch gekoppeld).

**Randgevallen (sectie Proces):** verplicht veld ontbreekt, onvolledig onderdeel, annuleren bij aanmaken of bewerken, geen zoekresultaten, opslaan mislukt, gelijktijdige wijziging door een collega, geen toegang (ook bij direct openen van de pagina of de opslagactie) en een productnummer dat niet bestaat. Deze sluiten aan op de teststrategie in [productrisicoanalyse-teststrategie.md](productrisicoanalyse-teststrategie.md).

## 5. Retrospective sprint 1

- Echt vaste contactmomenten aan het begin van elke projectdag (daily stand-up).
- De communicatie via Discord werkt niet goed.
- Meer contact met de andere teams in onze groep.
- Een beter overzicht van de backlog maken.

---

## 6. Verbeterpunten voor het board

Gevonden bij het doorlezen. Handig om voor de volgende review op te pakken.

> Deze lijst is van 30 september en gebruikt de oude nummering (US01–US09). Sinds de refinement staan de stappen in de descriptions grotendeels in de goede volgorde. De punten onder **User flows** zijn opgelost met de nieuwe flows. De openstaande punten voor de descriptions staan in sectie 2.

**Nummering en consistentie**

- De wireframe-lijst (sectie "Toelichting Casus") gebruikt een andere nummering dan de use case descriptions: *Contractafspraken (UC06)* en *Productontwikkeling volgen (UC07)*, terwijl US06 = productinfo raadplegen en US07 = leverancier registreren. Ook worden US10 en US13 genoemd, die niet in de beschrijvingen staan. Kies één nummering (US01–US14) en gebruik die overal, ook in de GitHub-issues.
- De sprintreview noemt 14 user stories; op het board staan er 9 beschreven. Geef aan waar US10–US14 staan.
- Er zijn twee versies van "Primaire Use Cases – Productontwikkeling & Inkoop" (de versie in *Kopie Work Area* heeft andere use cases, zoals *Productkans onderzoeken* en *Inkoopvoorstel registreren*). Markeer de oude versie als verouderd of verwijder hem.

**Use case descriptions**

- De stappen in het hoofdscenario staan bij meerdere use cases in de verkeerde volgorde. Voorbeelden: bij US07 valideert het systeem vóórdat de gebruiker iets invult; bij US02 past de gebruiker velden aan vóórdat het product is geselecteerd; bij US06 wordt feedback gegeven vóór het filteren en selecteren.
- De preconditie is alleen bij US01 ingevuld ("De gebruiker is ingelogd"); bij US02–US09 is die leeg.
- De alternatieve scenario's lijken verschoven: onder US07 staan stappen over contracten (afspraken, start-/einddatum, koppelen aan leverancier) die bij US08 horen, en onder US08 staat verlengen/heronderhandelen, wat bij US09 hoort. Onder US02 staan stappen over een onderhandeling (hoort bij US04).
- De user flow van US08 eindigt met "Contract versturen naar leverancier"; dat staat niet in de beschrijving.
- Wijzigingsgeschiedenis, AVG en foutafhandeling staan wel in de uitgewerkte use cases en de sectie Proces, maar niet als alternatief scenario in de beschrijvingen.

**User flows**

- US09: "Verlengen kiezen" staat twee keer.
- US05: er staat een los label "SS" bij een pijl.

**Typfouten**

BEWAGEN → BEWAKEN (titel use case 9), Leveranciersdasboard → Leveranciersdashboard, selectereb → selecteren, Inkopere → Inkoper, raadplagen → raadplegen, `<<incldue>>` → `<<include>>`, Klantenserive → Klantenservice, afdelng → afdeling, "der vervaldatums" → "de vervaldatums". Ook zijn sommige spaties weggevallen (Onderhandelingbijwerken, Zoekfilterstoepassen, Feedback gevenaan inkoper, Meldingontvangen).

**Structuur**

- De sectie "Interview TUI" bevat de tekst van de sprintreview, niet het interview. Hernoem de sectie naar bijvoorbeeld "Sprintreview sprint 1".
- De sectie "Toelichting Casus" bij Productontwikkeling & Inkoop bevat de lijst met wireframes.
- De secties "Section 1" en "Interview" zijn leeg.
- In de sectie Klantenservice & Support staat een kleine, lege tekstlaag (id `60:1078`) met een ongepaste laagnaam. Die is op het canvas bijna niet te zien, maar wel in het lagenpaneel. Verwijder hem voordat het board gedeeld of beoordeeld wordt.
