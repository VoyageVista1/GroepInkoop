# FigJam-board: Project Agile Board

**Link:** [Project Agile Board (FigJam)](https://www.figma.com/board/ManUSFsMrVgktm6UwReajA/Project-Agile-Board?node-id=0-1&p=f&t=Bxb2WEIrRXCM9J36-0)

Dit document beschrijft wat er op het FigJam-board staat, zodat de repo en het board naar elkaar verwijzen. Stand: 30 september 2026. Het board zelf blijft de bron; dit is een overzicht plus een lijst met verbeterpunten.

---

## 1. Indeling van het board

| Sectie | Inhoud |
| --- | --- |
| **Productontwikkeling & Inkoop** | Primaire use cases (actoren Inkoper, Manager, Medewerker), toelichting casus, problemen uit de casus en de uitgewerkte use cases met `<<include>>`/`<<extend>>`. |
| **Klantenservice & Support** | Primaire use cases (Klantenservicemedewerker, Manager) en de uitgewerkte use cases. |
| **Use case descriptions: Productontwikkeling & inkoop** | Tabellen voor US01–US09: doel, primaire actor, trigger, preconditie, hoofdscenario, postconditie, alternatieve scenario's. |
| **User flows productontwikkeling & inkoop** | Activiteitendiagrammen (START → EINDE, met beslisruiten) voor use case 1 t/m 9. |
| **Scope Productontwikkeling & Inkoop** | Wat we bouwen, welke schermen nodig zijn en welke gegevens een reisproduct en reisonderdeel hebben. |
| **Proces** | Tabel met randgevallen en het verwachte gedrag van het systeem. |
| **ERD** | Datamodel (als afbeelding). |
| **Retrospectives** | Wat ging goed / blijven doen / stoppen / kan beter. |
| **Interview TUI** | Tekst van de sprintreview van sprint 1 (sprintdoel, rollen, status backlog). |
| **Kopie Work Area** | Tweede, oudere versie van de primaire use cases Productontwikkeling & Inkoop. |
| **Literatuurlijst** | Links naar de UML 2.5.1-specificatie (OMG) en een voorbeeldhoofdstuk over use cases (Pearson). |

## 2. Use cases Productontwikkeling & Inkoop

| Nr. | Use case | Actor | Kern van de user flow |
| --- | --- | --- | --- |
| US01 | Nieuw reisproduct aanmaken | Inkoper | Formulier invullen → reisonderdelen en optionele gegevens toevoegen → opslaan → velden geldig? → publiceren of als concept opslaan. |
| US02 | Reisproduct bijwerken / productinfo wijzigen | Inkoper | Productdashboard → zoeken/filteren → product selecteren → aanpassen → velden geldig? → publiceren of als concept opslaan. |
| US03 | Reisproduct filteren | Inkoper | Productdashboard → zoeken → eventueel filters → product selecteren en bekijken. |
| US04 | Onderhandeling met leverancier bijwerken | Inkoper | Onderhandelingsdashboard → zoeken/filteren → status invoeren, leverancier koppelen → opslaan → velden geldig? → eventueel escaleren naar een persoon. |
| US05 | Leveranciersoverzicht raadplegen | Inkoper | Leveranciersdashboard → overzicht en prijsgeschiedenis → filteren → leverancier selecteren → contractstatus → exporteren naar PDF of delen met manager. |
| US06 | Productinfo raadplegen door andere afdeling | Medewerker andere afdeling | Productdashboard → zoeken/filteren → informatie bekijken → feedback geven, exporteren naar PDF of als favoriet opslaan. |
| US07 | Nieuwe leverancier registreren | Inkoper / medewerker P&I | Leveranciersdashboard → "Nieuw" → gegevens invullen → opslaan → gegevens geldig? (verplichte velden, e-mailadres). |
| US08 | Contract vastleggen/opvolgen bij leverancier | Inkoper | Leverancier zoeken en selecteren → contract aanmaken → gegevens en start-/einddatum invullen → gegevens geldig? → koppelen aan leverancier → versturen naar leverancier. |
| US09 | Contractvervaldatum bewaken / deadline monitoren | Inkoper | Contractdashboard → contracten ophalen → datums controleren → bijna verlopen? → waarschuwing → contract kiezen → verlengen (datums aanpassen) of onderhandelen (naar US04). |

Daarnaast staan in het use-casediagram nog: *Dashboard bekijken*, *Melding ontvangen* en *Marktonderzoek verwerken*. Die hebben (nog) geen beschrijving of user flow.

## 3. Use cases Klantenservice & Support

Klantcontact registreren · Klantgeschiedenis/klacht raadplegen · Openstaande zaken prioriteren en verdelen · Klantvraag beantwoorden · Klacht behandelen · Terugkerende klantproblemen onderzoeken · Vergoedingsvoorstel controleren · Klantgegevens verwijderen (AVG) · Klant zoeken op e-mailadres.

Deze sluiten aan op de interviewbevindingen K1–K11 en P1–P5 in [interview-analyse.md](interview-analyse.md).

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
