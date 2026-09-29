# Product Backlog – Productontwikkeling & Inkoop

> **Let op (29 sep 2026):** de backlog staat nu als issues in GitHub. Zie [migratie-overzicht.md](migratie-overzicht.md) voor de nummers. Dit document blijft de uitleg van werkwijze, Definition of Ready en Definition of Done.

**Casus:** VoyageVista · **Team:** GroepInkoop · **Versie:** 29 september 2026 (vóór refinement sprint 3)

De backlog telt **18 items (62 storypoints)** in 5 epics. Sprint 3 t/m 7 bevatten 50 punten; 12 punten (Could) staan klaar als er tijd over is. De volgorde is een voorstel van het team en wordt door de Product Owner met de opdrachtgever bevestigd.

> Alle stories komen uit het interview met de opdrachtgever (I1–I10 in [interviewanalyse](../interview-analyse.md)) en de casus §4.4 (KP = klein probleem, GP = groot probleem). Risico-ID’s verwijzen naar de [productrisicoanalyse](../productrisicoanalyse-teststrategie.md).

## Inhoud

1. [Productdoel en stakeholders](#1-productdoel-en-stakeholders)
2. [Werkwijze backlog](#2-werkwijze-backlog)
3. [Definition of Ready](#3-definition-of-ready)
4. [Definition of Done](#4-definition-of-done)
5. [Backlogoverzicht](#5-backlogoverzicht)
6. [Releaseplanning en sprintdoelen](#6-releaseplanning-en-sprintdoelen)
7. [User stories met acceptatiecriteria](#7-user-stories-met-acceptatiecriteria)
8. [Importeren in Azure DevOps](#8-importeren-in-azure-devops)
9. [Open vragen](#9-open-vragen)

## 1. Productdoel en stakeholders

**Productdoel.** Inkoop legt leveranciers, onderhandelingen, contracten en reisproducten op één plek vast, zodat iedereen bij VoyageVista met dezelfde, betrouwbare gegevens werkt en ingekochte kamers op tijd verkocht worden.

| Stakeholder | Belang | Wat zij van ons nodig hebben |
| --- | --- | --- |
| Productmanagers | Leveranciers bezoeken, onderhandelen, nieuwe reizen ontwikkelen | Snel vastleggen na een bezoek; overzicht van onderhandelingen |
| Inkopers | Contracten afsluiten en bewaken | Contracten, voorwaarden, aflopende contracten, bezetting |
| Sales & Boekingen | Reizen verkopen | Eenduidige productinformatie en kamertypes |
| Marketing & Communicatie | Campagnes op kamers die leeg dreigen te blijven | Signaal bij lage bezetting |
| Klantenservice | Klanten juist informeren | Productinformatie en annuleringsvoorwaarden |
| Financiën & Administratie | Correcte facturen en kosten | Contractprijzen en annuleringsvoorwaarden |
| IT & Innovatie | Onderhoudbare applicatie | Uniform datamodel en documentatie |
| Opdrachtgever (docent) | Werkend, getest product | Stories die zijn waarde leveren en aantoonbaar getest zijn |

**Rollen in het team.** Product Owner: _[naam]_ · Scrum Master: _[naam]_ · Ontwikkelteam: _[namen]_

## 2. Werkwijze backlog

- **Schatten:** planning poker in storypoints (1, 2, 3, 5, 8, 13). Referentiestory: **IN-02 Leveranciers zoeken en filteren = 2 punten.** Een story van 8 of meer wordt gesplitst.
- **Prioriteit:** MoSCoW. Must = nodig voor een bruikbare eerste versie; Should = belangrijk, niet blokkerend; Could = als er tijd is; Won’t = niet in dit project (externe koppelingen met leveranciers, zie casus §5.2).
- **Velocity:** aangenomen 12–13 punten per 2 weken voor dit team. Na sprint 3 vervangen we dit door de gemeten velocity en passen we de releaseplanning aan.
- **Refinement:** elke werksessie (donderdag) 30 minuten. De bovenste 2 sprints aan stories voldoen aan de Definition of Ready.
- **Traceerbaarheid:** elke story verwijst naar een probleem uit de casus of het interview, en naar een risico waar dat van toepassing is.
- **Oude nummers:** de voorlopige stories uit de interviewanalyse en risicoanalyse heten nu: A1 → IN-01, A2 → IN-04, A3 → IN-07 en IN-08, A4 → IN-11, B1 → IN-13, B2 → IN-15.

## 3. Definition of Ready

Een story mag de sprint in als:

- [ ] de story in de vorm “Als … wil ik … zodat …” staat en waarde heeft voor een stakeholder;
- [ ] er minimaal twee testbare acceptatiecriteria zijn (Given/When/Then), inclusief minstens één foutsituatie;
- [ ] de story geschat is met planning poker en kleiner is dan 8 punten;
- [ ] bekend is welke gegevens uit het datamodel de story leest en vastlegt;
- [ ] er een wireframe of schets is voor elk nieuw scherm;
- [ ] het productrisico (klasse A, B of C) bepaald is;
- [ ] afhankelijkheden met andere stories of teams bekend en afgesproken zijn;
- [ ] de Product Owner de story heeft besproken met de opdrachtgever.

## 4. Definition of Done

Een story is klaar als:

**Bouw**

- [ ] de functionaliteit in de low-code applicatie werkt volgens alle acceptatiecriteria;
- [ ] foutmeldingen staan bij het juiste veld en zeggen hoe de gebruiker het oplost;
- [ ] een ander teamlid de configuratie of code heeft gereviewd (vier ogen) en de review staat in DevOps;
- [ ] er geen persoonsgegevens worden opgeslagen die niet nodig zijn (AVG).

**Test**

- [ ] testgevallen zijn opgesteld met de testontwerptechniek uit de teststrategie en gekoppeld aan de story in Azure Test Plans;
- [ ] alle testgevallen zijn uitgevoerd; per testgeval staan status, tester, datum en bevindingen;
- [ ] bij risicoklasse A heeft een tweede tester afgetekend;
- [ ] er zijn geen open bugs met prioriteit 1 of 2;
- [ ] de story is gedemonstreerd met realistische testdata.

**Documentatie**

- [ ] het datamodel, de wireframes en het procesmodel zijn bijgewerkt, met een link vanuit de story in DevOps;
- [ ] de werking is beschreven zodat VoyageVista de applicatie zelf kan onderhouden (casus §5.2);
- [ ] de Product Owner heeft de story geaccepteerd.

## 5. Backlogoverzicht

Gesorteerd op prioriteit. SP = storypoints.

| ID | Epic | User story | SP | MoSCoW | Sprint | Risico |
| --- | --- | --- | --- | --- | --- | --- |
| [IN-00](#in-00-datamodel-inkoop-opstellen) | E1 | Datamodel Inkoop opstellen | 3 | Must | 3 | – |
| [IN-01](#in-01-leverancier-registreren) | E1 | Leverancier registreren | 3 | Must | 3 | R9 |
| [IN-02](#in-02-leveranciers-zoeken-en-filteren) | E1 | Leveranciers zoeken en filteren | 2 | Must | 3 | – |
| [IN-04](#in-04-bezoek-en-onderhandeling-vastleggen) | E2 | Bezoek en onderhandeling vastleggen | 5 | Must | 3 | R7 |
| [IN-05](#in-05-overzicht-van-alle-onderhandelingen) | E2 | Overzicht van alle onderhandelingen | 3 | Must | 4 | – |
| [IN-03](#in-03-leveranciersgegevens-wijzigen-met-historie) | E1 | Leveranciersgegevens wijzigen met historie | 3 | Should | 4 | – |
| [IN-07](#in-07-contract-vastleggen) | E3 | Contract vastleggen | 5 | Must | 5 | R6 |
| [IN-09](#in-09-signaal-aflopende-contracten) | E3 | Signaal aflopende contracten | 2 | Should | 5 | – |
| [IN-08](#in-08-annuleringsvoorwaarden-gestructureerd-vastleggen) | E3 | Annuleringsvoorwaarden gestructureerd vastleggen | 3 | Must | 6 | R6 |
| [IN-11](#in-11-bezetting-per-contract-bekijken) | E4 | Bezetting per contract bekijken | 5 | Should | 6 | R11 |
| [IN-12](#in-12-lage-bezetting-doorgeven-aan-marketing-en-sales) | E4 | Lage bezetting doorgeven aan Marketing en Sales | 3 | Should | 6 | R11 |
| [IN-13](#in-13-reisproduct-aanmaken-met-vaste-kenmerken) | E5 | Reisproduct aanmaken met vaste kenmerken | 5 | Should | 7 | – |
| [IN-14](#in-14-vaste-lijsten-voor-kamertypes-en-faciliteiten-beheren) | E5 | Vaste lijsten voor kamertypes en faciliteiten beheren | 3 | Should | 7 | – |
| [IN-15](#in-15-voortgang-productontwikkeling-volgen) | E5 | Voortgang productontwikkeling volgen | 5 | Should | 7 | – |
| [IN-06](#in-06-signaal-voor-volgend-leveranciersbezoek) | E2 | Signaal voor volgend leveranciersbezoek | 3 | Could | – | – |
| [IN-10](#in-10-contract-laten-goedkeuren) | E3 | Contract laten goedkeuren | 3 | Could | – | – |
| [IN-16](#in-16-productcatalogus-voor-andere-afdelingen) | E5 | Productcatalogus voor andere afdelingen | 3 | Could | – | – |
| [IN-17](#in-17-klantwensen-koppelen-aan-productideeën) | E5 | Klantwensen koppelen aan productideeën | 3 | Could | – | – |
| | | **Totaal** | **62** | | | |

| Epic | Doel | Items | SP |
| --- | --- | --- | --- |
| E1 Leveranciersbeheer | Eén centrale, betrouwbare plek voor alle leveranciers (hotels, appartementen, vervoerders, rederijen). | 4 | 11 |
| E2 Onderhandelingen | De stand van elke onderhandeling is voor iedereen zichtbaar, met prijzen en marge. | 3 | 11 |
| E3 Contractbeheer | Contracten met prijzen, aantallen en annuleringsvoorwaarden zijn gestructureerd vastgelegd. | 4 | 13 |
| E4 Bezetting en afstemming met verkoop | Ingekochte kamers worden op tijd verkocht; Marketing en Sales krijgen een signaal als dat achterloopt. | 2 | 8 |
| E5 Gestandaardiseerde productdata | Reisproducten hebben vaste kenmerken, zodat verkoper en klant precies weten wat er geboekt wordt. | 5 | 19 |

## 6. Releaseplanning en sprintdoelen

| Sprint | Periode | Duur | Sprintdoel | Stories | SP |
| --- | --- | --- | --- | --- | --- |
| 3 | 1 okt – 22 okt 2026 | 3 weken (incl. herfstvakantie) | Een productmanager kan een leverancier registreren en na een bezoek de onderhandeling met marge vastleggen, op basis van een goedgekeurd datamodel. | IN-00, IN-01, IN-02, IN-04 | 13 |
| 4 | 22 okt – 29 okt 2026 | 1 week | De inkoopmanager ziet in één overzicht hoe alle onderhandelingen ervoor staan, en wijzigingen aan leveranciers zijn herleidbaar. | IN-03, IN-05 | 6 |
| 5 | 12 nov – 19 nov 2026 | 1 week | Een inkoper kan een contract vastleggen en ziet welke contracten binnenkort aflopen. | IN-07, IN-09 | 7 |
| 6 | 19 nov – 3 dec 2026 | 2 weken | Inkoop ziet de bezetting van ingekochte kamers en kan lage bezetting doorgeven aan Marketing en Sales. | IN-08, IN-11, IN-12 | 11 |
| 7 | 3 dec – 17 dec 2026 | 2 weken | Reisproducten hebben vaste kenmerken en de voortgang van productontwikkeling is zichtbaar. | IN-13, IN-14, IN-15 | 13 |
| Reserve | bij hogere velocity | – | Could-stories | IN-06, IN-10, IN-16, IN-17 | 12 |

Sprint 8 (januari) is gereserveerd voor herkansing en wordt niet gepland.

## 7. User stories met acceptatiecriteria

### Epic E1: Leveranciersbeheer

_Eén centrale, betrouwbare plek voor alle leveranciers (hotels, appartementen, vervoerders, rederijen)._

#### IN-00 Datamodel Inkoop opstellen

> Als ontwikkelteam wil ik een datamodel (ERD) voor leverancier, onderhandeling, contract, annuleringsvoorwaarde, reisproduct en kamertype, zodat alle Inkoop-stories op dezelfde gegevens bouwen en de applicatie later onderhoudbaar is.

| SP | MoSCoW | Sprint | Bron | Risico | Afhankelijk van |
| --- | --- | --- | --- | --- | --- |
| 3 | Must | 3 | Casus §5.2, IT GP1 | – | – |

**Acceptatiecriteria**

1. Het ERD bevat alle entiteiten, attributen, sleutels en relaties die de stories IN-01 t/m IN-15 nodig hebben.
2. Per entiteit staat beschreven welke story hem aanmaakt, leest of wijzigt.
3. De opdrachtgever en het Financiën-team hebben de koppeling contract → boeking → factuur gezien.
4. Het ERD staat in DevOps gekoppeld (link naar SharePoint) en in de repo onder docs.

_Opmerking: Technische story (enabler). Nodig voor bijna alle andere stories._

#### IN-01 Leverancier registreren

> Als productmanager wil ik een leverancier één keer centraal vastleggen met naam, type, land, plaats en contactpersoon, zodat alle collega’s dezelfde, actuele gegevens zien.

| SP | MoSCoW | Sprint | Bron | Risico | Afhankelijk van |
| --- | --- | --- | --- | --- | --- |
| 3 | Must | 3 | KP2, KP3 · interview I6 | R9 | IN-00 |

**Acceptatiecriteria**

1. Given ik ben ingelogd als productmanager, When ik naam, type, land en plaats invul en opsla, Then staat de leverancier in het leveranciersoverzicht.
2. Given een verplicht veld is leeg, When ik opsla, Then zie ik per veld een foutmelding en wordt er niets opgeslagen.
3. Given er bestaat al een leverancier met dezelfde naam en plaats, When ik opsla, Then krijg ik een waarschuwing voor dubbele invoer en kan ik bewust doorgaan.
4. Given ik vul een ongeldig e-mailadres in, When ik opsla, Then zie ik de melding “Dit is geen geldig e-mailadres” onder het veld.

_Opmerking: Type kiezen uit vaste lijst: Hotel, Appartement, Busvervoer, Rederij, Excursie._

#### IN-02 Leveranciers zoeken en filteren

> Als inkoper wil ik leveranciers zoeken op naam, plaats of land en filteren op onderhandelingsstatus, zodat ik snel de juiste leverancier en de stand van zaken vind.

| SP | MoSCoW | Sprint | Bron | Risico | Afhankelijk van |
| --- | --- | --- | --- | --- | --- |
| 2 | Must | 3 | KP1 | – | IN-01 |

**Acceptatiecriteria**

1. Given er zijn leveranciers, When ik een deel van de naam, plaats of het land typ, Then zie ik alleen de leveranciers die daarop passen.
2. Given ik kies de status “In onderhandeling”, When het filter actief is, Then zie ik alleen leveranciers waarvan de laatste onderhandeling die status heeft.
3. Given mijn zoekopdracht geeft geen resultaat, Then zie ik een melding met een tip om de zoekterm aan te passen.

#### IN-03 Leveranciersgegevens wijzigen met historie

> Als inkoper wil ik gegevens van een leverancier wijzigen en zien wie wat wanneer heeft aangepast, zodat fouten te herleiden zijn en de gegevens betrouwbaar blijven.

| SP | MoSCoW | Sprint | Bron | Risico | Afhankelijk van |
| --- | --- | --- | --- | --- | --- |
| 3 | Should | 4 | KP2, GP1 | – | IN-01 |

**Acceptatiecriteria**

1. Given ik open een leverancier, When ik een gegeven wijzig en opsla, Then is de nieuwe waarde direct zichtbaar voor iedereen.
2. Given een gegeven is gewijzigd, When ik de historie open, Then zie ik de oude en nieuwe waarde, de medewerker en de datum.
3. De datum en de medewerker vult het systeem zelf in; ik kan ze niet aanpassen.

### Epic E2: Onderhandelingen

_De stand van elke onderhandeling is voor iedereen zichtbaar, met prijzen en marge._

#### IN-04 Bezoek en onderhandeling vastleggen

> Als productmanager wil ik na een leveranciersbezoek de basisprijs, verkoopprijs, volumekorting, status en notities vastleggen, zodat mijn collega’s de onderhandeling kunnen volgen zonder mijn mailbox.

| SP | MoSCoW | Sprint | Bron | Risico | Afhankelijk van |
| --- | --- | --- | --- | --- | --- |
| 5 | Must | 3 | KP1 · interview I3, I4 | R7 | IN-01 |

**Acceptatiecriteria**

1. Given ik open een leverancier, When ik een bezoek vastleg met datum, status, inkoopprijs en verkoopprijs, Then staat het bezoek bovenaan in de lijst van die leverancier.
2. Given ik vul inkoop- en verkoopprijs in, Then berekent het systeem direct de marge in euro en procent.
3. Given de verkoopprijs ligt onder de inkoopprijs, Then zie ik een waarschuwing “negatieve marge” voordat ik opsla.
4. Status kiezen uit: Gepland, Bezocht, In onderhandeling, Akkoord, Afgewezen.

_Opmerking: Grenswaarden marge: −1, 0, +1 euro (zie teststrategie)._

#### IN-05 Overzicht van alle onderhandelingen

> Als inkoopmanager wil ik één overzicht van alle onderhandelingen met status, marge en productmanager, zodat ik zie welke onderhandelingen aandacht nodig hebben.

| SP | MoSCoW | Sprint | Bron | Risico | Afhankelijk van |
| --- | --- | --- | --- | --- | --- |
| 3 | Must | 4 | KP1, KP4 | – | IN-04 |

**Acceptatiecriteria**

1. Given er zijn onderhandelingen, When ik het overzicht open, Then zie ik per regel leverancier, bezoekdatum, status, marge en productmanager.
2. Given ik klik op een kolomkop, Then wordt het overzicht op die kolom gesorteerd.
3. Given een bezoek ligt in de toekomst, Then staat bij die regel “over X dagen”.

#### IN-06 Signaal voor volgend leveranciersbezoek

> Als productmanager wil ik een signaal krijgen als een leverancier te lang niet bezocht is, zodat goede contacten warm blijven.

| SP | MoSCoW | Sprint | Bron | Risico | Afhankelijk van |
| --- | --- | --- | --- | --- | --- |
| 3 | Could | Reserve | Interview I3 | – | IN-04 |

**Acceptatiecriteria**

1. Given een leverancier met status Akkoord is meer dan 12 maanden niet bezocht, Then staat hij in de lijst “Bezoek plannen”.
2. Given een nieuwe leverancier (minder dan 1 jaar contact) is meer dan 6 maanden niet bezocht, Then staat hij ook in die lijst.

_Opmerking: Termijnen komen uit het interview (bestaand contact 1× per jaar, nieuw 2–3× per jaar). Laten bevestigen._

### Epic E3: Contractbeheer

_Contracten met prijzen, aantallen en annuleringsvoorwaarden zijn gestructureerd vastgelegd._

#### IN-07 Contract vastleggen

> Als inkoper wil ik een contract vastleggen met looptijd, kamertype, aantal gecontracteerde kamers en inkoopprijs, zodat verkoop en klantenservice weten wat er is afgesproken.

| SP | MoSCoW | Sprint | Bron | Risico | Afhankelijk van |
| --- | --- | --- | --- | --- | --- |
| 5 | Must | 5 | KP5 · GP1 | R6 | IN-00, IN-04 |

**Acceptatiecriteria**

1. Given de onderhandeling heeft status Akkoord, When ik een contract vastleg met begin- en einddatum, kamertype, aantal kamers en prijs, Then staat het contract bij de leverancier.
2. Given de einddatum ligt vóór de begindatum, When ik opsla, Then zie ik “De einddatum moet op of na de begindatum liggen”.
3. Given het aantal kamers is 0 of geen heel getal, When ik opsla, Then zie ik een foutmelding onder het veld.
4. Het kamertype kies ik uit de vaste lijst (IN-14).

#### IN-08 Annuleringsvoorwaarden gestructureerd vastleggen

> Als inkoper wil ik per contract de annuleringsvoorwaarden vastleggen als regels “vanaf X dagen vóór vertrek: Y% kosten”, zodat klantenservice en Financiën de juiste kosten kunnen berekenen.

| SP | MoSCoW | Sprint | Bron | Risico | Afhankelijk van |
| --- | --- | --- | --- | --- | --- |
| 3 | Must | 6 | KP5 · interview I10 | R6 | IN-07 |

**Acceptatiecriteria**

1. Given ik leg een contract vast, When ik annuleringsregels invul, Then worden ze gesorteerd opgeslagen van meeste naar minste dagen.
2. Given een percentage ligt onder 0 of boven 100, When ik opsla, Then zie ik een foutmelding.
3. Given een contract heeft annuleringsregels, Then zijn ze leesbaar voor Sales, Klantenservice en Financiën.

_Opmerking: Voorwaarden volgen de ANVR-systematiek per reis (interview)._

#### IN-09 Signaal aflopende contracten

> Als inkoper wil ik een signaal zien bij contracten die binnen 60 dagen aflopen, zodat ik op tijd kan heronderhandelen.

| SP | MoSCoW | Sprint | Bron | Risico | Afhankelijk van |
| --- | --- | --- | --- | --- | --- |
| 2 | Should | 5 | KP4 · GP2 | – | IN-07 |

**Acceptatiecriteria**

1. Given een contract loopt af over 60 dagen of minder, Then staat bij het contract “Loopt af over X dagen”.
2. Given een contract loopt af over 61 dagen, Then staat dat signaal er niet.
3. Het dashboard toont het aantal contracten met een signaal.

_Opmerking: Grenswaarden 60/61 dagen._

#### IN-10 Contract laten goedkeuren

> Als inkoopmanager wil ik een contract goedkeuren voordat het actief wordt, zodat er geen contracten met verkeerde prijzen of voorwaarden live gaan.

| SP | MoSCoW | Sprint | Bron | Risico | Afhankelijk van |
| --- | --- | --- | --- | --- | --- |
| 3 | Could | Reserve | KP5 | – | IN-07 |

**Acceptatiecriteria**

1. Given een inkoper legt een contract vast, Then krijgt het de status “Wacht op goedkeuring”.
2. Given ik ben de indiener, Then kan ik mijn eigen contract niet goedkeuren.
3. Given een collega keurt goed, Then wordt het contract actief en staat de goedkeurder in de historie.

_Opmerking: Open vraag aan opdrachtgever: wie keurt contracten goed, en vanaf welk bedrag?_

### Epic E4: Bezetting en afstemming met verkoop

_Ingekochte kamers worden op tijd verkocht; Marketing en Sales krijgen een signaal als dat achterloopt._

#### IN-11 Bezetting per contract bekijken

> Als inkoper wil ik per contract zien hoeveel ingekochte kamers al verkocht zijn, zodat ik weet waar ingekochte kamers dreigen leeg te blijven.

| SP | MoSCoW | Sprint | Bron | Risico | Afhankelijk van |
| --- | --- | --- | --- | --- | --- |
| 5 | Should | 6 | Interview I5 | R11 | IN-07 |

**Acceptatiecriteria**

1. Given een contract met aantal kamers, Then zie ik gecontracteerd, verkocht, beschikbaar en het bezettingspercentage.
2. Given de bezetting is onder 50% en de periode begint binnen 8 weken, Then krijgt het contract het signaal “Actie nodig”.
3. Given de bezetting is precies 50%, Then is er geen signaal.

_Opmerking: Drempel 50% en 8 weken zijn aannames; staan als open vraag bij de opdrachtgever._

#### IN-12 Lage bezetting doorgeven aan Marketing en Sales

> Als inkoper wil ik een contract met lage bezetting met één klik doorgeven aan Marketing en Sales, zodat zij er een actie op kunnen zetten voordat de kamers leeg blijven.

| SP | MoSCoW | Sprint | Bron | Risico | Afhankelijk van |
| --- | --- | --- | --- | --- | --- |
| 3 | Should | 6 | Interview I5 · Marketing GP2 | R11 | IN-11, Marketing-team |

**Acceptatiecriteria**

1. Given een contract heeft het signaal “Actie nodig”, When ik op “Doorgeven aan verkoop” klik, Then ziet het Marketing-team het contract in hun lijst met de bezetting en periode.
2. Given het signaal is doorgegeven, Then staat bij het contract wie het wanneer heeft doorgegeven.

_Opmerking: Overstijgende story: afstemmen met het Marketing-team._

### Epic E5: Gestandaardiseerde productdata

_Reisproducten hebben vaste kenmerken, zodat verkoper en klant precies weten wat er geboekt wordt._

#### IN-13 Reisproduct aanmaken met vaste kenmerken

> Als productmanager wil ik een reisproduct aanmaken met bestemming, accommodatie, kamertypes en faciliteiten uit vaste lijsten, zodat verkopers en klanten eenduidige informatie krijgen.

| SP | MoSCoW | Sprint | Bron | Risico | Afhankelijk van |
| --- | --- | --- | --- | --- | --- |
| 5 | Should | 7 | GP1 · KP2 · interview I2, I7 | – | IN-07, IN-14 |

**Acceptatiecriteria**

1. Given ik maak een reisproduct aan, When ik kamertypes kies, Then kan ik alleen kiezen uit de vaste lijst (geen vrije tekst).
2. Given ik vink faciliteiten aan (bijv. lange bedden, keukenblok), Then kunnen verkopers daarop filteren.
3. Given een reisproduct is gekoppeld aan een contract, Then zie ik bij het product de prijs en de annuleringsvoorwaarden van dat contract.

_Opmerking: Lost de onduidelijke kamertypes uit beddenbanken op (interview I7)._

#### IN-14 Vaste lijsten voor kamertypes en faciliteiten beheren

> Als productmanager wil ik de lijsten met kamertypes en faciliteiten beheren, zodat iedereen dezelfde omschrijvingen gebruikt.

| SP | MoSCoW | Sprint | Bron | Risico | Afhankelijk van |
| --- | --- | --- | --- | --- | --- |
| 3 | Should | 7 | GP1 · interview I7 | – | IN-00 |

**Acceptatiecriteria**

1. Given ik voeg een kamertype toe, Then is het direct te kiezen bij contracten en reisproducten.
2. Given een kamertype is in gebruik, When ik het wil verwijderen, Then kan dat niet en zie ik waar het gebruikt wordt.

#### IN-15 Voortgang productontwikkeling volgen

> Als productmanager wil ik per nieuw reisproduct de fase en streefdatum zien (Idee → Onderzoek → Inkoop → Klaar voor verkoop → Live), zodat deadlines niet meer gemist worden.

| SP | MoSCoW | Sprint | Bron | Risico | Afhankelijk van |
| --- | --- | --- | --- | --- | --- |
| 5 | Should | 7 | KP4 · GP2 | – | IN-13 |

**Acceptatiecriteria**

1. Given een reisproduct heeft een eigenaar en streefdatum, Then staat het in het overzicht met zijn fase.
2. Given de streefdatum is verstreken en de fase is niet Live, Then is de regel rood gemarkeerd.
3. Given ik zet een product een fase verder, Then legt het systeem datum en medewerker vast.

#### IN-16 Productcatalogus voor andere afdelingen

> Als medewerker Sales of Klantenservice wil ik de actuele productinformatie van Inkoop kunnen inzien (alleen lezen), zodat ik klanten de juiste informatie geef.

| SP | MoSCoW | Sprint | Bron | Risico | Afhankelijk van |
| --- | --- | --- | --- | --- | --- |
| 3 | Could | Reserve | KP3 · GP1 | – | IN-13 |

**Acceptatiecriteria**

1. Given ik ben medewerker Sales of Klantenservice, Then kan ik reisproducten en hun kenmerken bekijken maar niet wijzigen.
2. Given Inkoop wijzigt een product, Then zie ik de wijziging direct.

_Opmerking: Overstijgende story: afstemmen met Sales en Klantenservice._

#### IN-17 Klantwensen koppelen aan productideeën

> Als productmanager wil ik bij een productidee vastleggen welke klantwensen (bijv. uit het klantpanel) eraan ten grondslag liggen, zodat we reizen ontwikkelen die de Nederlandse klant echt wil.

| SP | MoSCoW | Sprint | Bron | Risico | Afhankelijk van |
| --- | --- | --- | --- | --- | --- |
| 3 | Could | Reserve | Interview I1, I2 | – | IN-15 |

**Acceptatiecriteria**

1. Given ik maak een productidee aan, Then kan ik één of meer klantwensen met bron (klantpanel, klantenservice, marketing) toevoegen.
2. Given een klantwens hoort bij meerdere ideeën, Then zie ik bij de wens alle gekoppelde ideeën.

## 8. Importeren in Azure DevOps

Het bestand [`inkoop-backlog-azure-devops.csv`](inkoop-backlog-azure-devops.csv) bevat alle epics, features en Product Backlog Items, met beschrijving, acceptatiecriteria, effort (storypoints), business value en tags.

1. Ga in Azure DevOps naar **Boards → Work items → Import work items**.
2. Kies het CSV-bestand en klik op **Import**.
3. Controleer de voorbeeldweergave en klik op **Save items**.
4. Zet daarna per PBI het **Iteration Path** op de juiste sprint (kolom Sprint in dit document; staat ook als tag).

Het bestand gaat uit van het **Scrum-proces** (Epic → Feature → Product Backlog Item, veld *Effort*). Gebruikt jullie project het Agile-proces, vervang dan in de kolom *Work Item Type* “Product Backlog Item” door “User Story” en hernoem de kolom *Effort* naar *Story Points*.

## 9. Open vragen

- [ ] Wie keurt contracten goed, en is er een bedrag waarboven dat moet? (IN-10)
- [ ] Klopt de drempel van 50% bezetting en 8 weken vóór de periode voor het signaal “Actie nodig”? (IN-11)
- [ ] Hoe vaak moet een bestaande en een nieuwe leverancier bezocht worden? Nu aangenomen: 12 en 6 maanden. (IN-06)
- [ ] Welke kamertypes en faciliteiten horen in de standaardlijst? (IN-14)
- [ ] Hoe loopt een contract door naar de facturatie? Af te stemmen met het Financiën-team. (IN-07, IN-08)
