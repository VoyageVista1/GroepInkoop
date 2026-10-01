# UX-eisen Productontwikkeling & Inkoop en Klantenservice & Support

**Status:** concept voor de sprintreview van 1 oktober 2026, nog te controleren door het team · **GitHub:** #52 (#159, #160) en #75 (#181, #182, #183) staan nog open · **Bronnen:** FigJam-sectie *Proces* (randgevallen), [interviewanalyse](../interview-analyse.md), [risicoanalyse](../productrisicoanalyse-teststrategie.md), [use cases Klantenservice](use-cases-klantenservice.md)

Een UX-eis beschrijft wat de gebruiker moet kunnen begrijpen of doen, niet hoe het scherm eruitziet. Elke eis is terug te voeren op een gebruikersprobleem, een toegankelijkheidsrichtlijn (WCAG 2.2 AA) of een projectbesluit, en is te controleren met een schermbeoordeling of een gebruikstaak. Labels, statussen en tijdsnormen leggen we pas definitief vast als de onderliggende regel is bevestigd (zie [scope, open besluiten](scope.md#6-open-besluiten)).

## 1. Informatiebehoefte per gebruiker

| Gebruiker | Moet in één oogopslag zien | Taak die het vaakst voorkomt |
| --- | --- | --- |
| Productmedewerker / productmanager | Status van elk reisproduct, open acties en deadlines | Reisproduct aanmaken en bijwerken (UC01, UC02) |
| Inkoper | Stand van onderhandelingen, contracten die binnenkort aflopen, bezetting | Onderhandeling bijwerken, contract vastleggen (UC04, UC08) |
| Manager | Wat geëscaleerd is en wat te lang blijft liggen | Dashboard bekijken, deadlines monitoren (UC09) |
| Klantenservicemedewerker | Wie de klant is, of de klant nu op reis is, open zaken en eerdere afspraken | Klant zoeken en contact registreren (UC-K01, UC-K02) |
| Senior / teamleider | Openstaande zaken op urgentie, voorstellen die op goedkeuring wachten | Zaken verdelen, voorstel controleren (UC-K04, UC-K07) |

## 2. UX-eisen

| ID | Geldt voor | De gebruiker moet… | Zo controleren we het | Bron |
| --- | --- | --- | --- | --- |
| UX-01 | Alle formulieren | …zien welke velden verplicht zijn vóórdat hij opslaat. | Schermbeoordeling: verplichte velden zijn gemarkeerd met tekst, niet alleen met kleur. | WCAG 1.4.1, 3.3.2 |
| UX-02 | Alle formulieren | …bij een fout per veld lezen wat er mis is en hoe hij het herstelt, terwijl de rest van zijn invoer blijft staan. | Gebruikstaak: sla een reisproduct op zonder bestemming; de melding staat bij het veld en niets is gewist. | FigJam *Proces*, WCAG 3.3.1, 3.3.3 |
| UX-03 | Opslaan en verzenden | …direct zien of een wijziging is opgeslagen of mislukt. Bij mislukken blijft de invoer staan. | Schermbeoordeling: succes- en foutmelding zijn verschillend en worden voorgelezen door een schermlezer. | FigJam *Proces*, WCAG 4.1.3 |
| UX-04 | Bewerken | …gewaarschuwd worden als een collega hetzelfde product of dossier intussen heeft gewijzigd, en de nieuwe versie kunnen laden. | Gebruikstaak met twee testers die hetzelfde product tegelijk wijzigen. | FigJam *Proces* (versienummer) |
| UX-05 | Annuleren | …bij annuleren weten dat er niets is opgeslagen en terugkeren naar het overzicht. | Schermbeoordeling: na annuleren zijn de bestaande gegevens ongewijzigd. | FigJam *Proces* |
| UX-06 | Overzichten (reisproducten, leveranciers, zaken) | …kunnen zoeken en filteren, en bij geen resultaat een duidelijke melding met een manier om de zoekopdracht aan te passen. | Gebruikstaak: zoek op een niet-bestaande bestemming. | FigJam *Proces*, UC03 |
| UX-07 | Reisproduct, onderhandeling, klacht | …de status in woorden zien (bijv. *Concept*, *In onderhandeling*, *Wacht op goedkeuring*) en weten wat de volgende stap is. | Schermbeoordeling: status staat als tekstlabel; kleur is aanvullend. | #160, WCAG 1.4.1 |
| UX-08 | Klant zoeken | …bij gelijknamige klanten (vader/zoon) de juiste kiezen op basis van geboortedatum, woonplaats en Sr./Jr. | Gebruikstaak: zoek “J. Bakker” en open de juiste klant. | Interview P4, risico R8 |
| UX-09 | Klantdossier | …zonder te scrollen zien of de klant nu op reis is en welke vervolgacties openstaan. | Schermbeoordeling bij 1280 × 800 en op een tablet. | Interview K5, K6 |
| UX-10 | Contact registreren | …gewaarschuwd worden als hij een IBAN of paspoortnummer in een tekstveld typt, vóórdat het wordt opgeslagen. | Gebruikstaak: plak een IBAN in de samenvatting. | Interview P1, P2, risico R2 |
| UX-11 | Compensatievoorstel | …zien hoe het bedrag is berekend (percentage × reissom) en wie het moet goedkeuren; zijn eigen voorstel kan hij niet goedkeuren. | Gebruikstaak: dien een voorstel in en probeer het zelf goed te keuren. | Interview K9, risico R3, R4 |
| UX-12 | Gegevens verwijderen (AVG) | …vóór bevestiging zien wat er verwijderd wordt, en waarom verwijderen geblokkeerd is als de klant op reis is. | Gebruikstaak met een klant die volgende week terugkomt. | Interview P3, risico R1 |
| UX-13 | Alle schermen | …alles met het toetsenbord kunnen bedienen, met een zichtbare focus. | Toetsenbordtest van de drie vaste gebruikstaken. | WCAG 2.1.1, 2.4.7, risico R14 |
| UX-14 | Alle schermen | …tekst kunnen lezen met voldoende contrast, ook op een tablet in de shop. | Contrastmeting: tekst minimaal 4,5 : 1. | WCAG 1.4.3, risico R14 |
| UX-15 | Toegang | …bij een pagina of actie waarvoor hij geen rechten heeft, een duidelijke melding krijgen in plaats van een lege of kapotte pagina. | Gebruikstaak: open een product-URL als medewerker zonder rechten. | FigJam *Proces* |

## 3. Zo testen we de UX-eisen

Per sprint een usability-test met drie gebruikers (hardop denken) op drie vaste taken: **klant zoeken**, **klacht registreren** en **contract vastleggen**. Een eis is gehaald als twee van de drie testers de taak zonder hulp afronden. Bevindingen gaan als issue naar de backlog. Dit sluit aan op de [teststrategie](../productrisicoanalyse-teststrategie.md).

## 4. Nog te doen

- [ ] Team controleert de lijst en koppelt elke eis aan de functionele story (#183).
- [ ] Interactie en foutafhandeling per scherm uitwerken in de wireframes (#182).
- [ ] Definitieve statuslabels en tijdsnormen vastleggen zodra de open besluiten in de [scope](scope.md#6-open-besluiten) beantwoord zijn.
