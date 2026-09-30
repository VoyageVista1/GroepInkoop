# Use cases Klantenservice & Support

Beschrijvingen en user flows bij het primaire use-casediagram “Klantvragen en klachten afhandelen” op het FigJam-board. Opbouw gelijk aan de beschrijvingen van Productontwikkeling & Inkoop. Nummering: **UC-K01 t/m UC-K09**; de bijbehorende user story staat erbij.

Actoren: **Klantenservicemedewerker** (ook shopmedewerker), **Teamleider klantenservice** (in het diagram: Manager), **After Travel** (secundair), **Klant** (secundair, ontvangt berichten).

---

## UC-K01 Klantcontact registreren

| | |
| --- | --- |
| Use case | UC-K01 Klantcontact registreren (user story #121) |
| Doel | Elk contact met een klant wordt gestructureerd vastgelegd, zodat het niet verloren gaat en collega’s dezelfde verhaallijn zien. |
| Primaire actor | Klantenservicemedewerker |
| Trigger | Een klant belt, mailt, komt in de shop of stuurt een bericht via social media. |
| Preconditie | De medewerker is ingelogd. |
| Hoofdscenario | 1. De medewerker zoekt de klant op (include UC-K02).<br>2. Het systeem toont het klantprofiel met open zaken.<br>3. De medewerker kiest “Contact registreren”.<br>4. De medewerker kiest kanaal en categorie en vult onderwerp en samenvatting in.<br>5. De medewerker koppelt het contact aan een open zaak of maakt een nieuwe zaak.<br>6. De medewerker klikt op Opslaan.<br>7. Het systeem controleert de verplichte velden en controleert de samenvatting op IBAN- of paspoortnummers.<br>8. Het systeem slaat het contact op met datum, tijd en medewerker en toont het bovenaan de klanthistorie. |
| Postconditie | Het contactmoment staat in het klantdossier, gekoppeld aan een klantzaak. |
| Alternatieve scenario’s | **2a. Klant bestaat nog niet:** de medewerker maakt een nieuwe klant aan (extend) en gaat verder bij stap 3.<br>**5a. Vervolgcontact:** de medewerker koppelt aan de bestaande zaak (extend).<br>**6a. Bijlage:** de medewerker voegt een bestand toe (extend).<br>**7a. Verplicht veld leeg:** het systeem toont per veld een foutmelding; de invoer blijft staan.<br>**7b. IBAN of paspoortnummer gevonden:** het systeem waarschuwt en slaat de tekst niet op (AVG, interview P1–P2). |

## UC-K02 Klant zoeken op e-mailadres

| | |
| --- | --- |
| Use case | UC-K02 Klant zoeken op e-mailadres (user story #120) |
| Doel | De medewerker vindt altijd de juiste, unieke klant. |
| Primaire actor | Klantenservicemedewerker |
| Trigger | De medewerker wil een klant of boeking opzoeken. |
| Preconditie | De medewerker is ingelogd. |
| Hoofdscenario | 1. De medewerker opent “Klant zoeken”.<br>2. De medewerker vult een e-mailadres, telefoonnummer, naam of boekingsnummer in.<br>3. Het systeem zoekt.<br>4. Het systeem toont precies één klantprofiel.<br>5. De medewerker opent het profiel. |
| Postconditie | Het juiste klantprofiel is geopend. |
| Alternatieve scenario’s | **4a. Zoeken op naam geeft meerdere klanten:** het systeem toont geboortedatum en woonplaats per klant en waarschuwt voor gelijknamige klanten (bijv. Sr./Jr.); de medewerker kiest de juiste.<br>**4b. Geen resultaat:** het systeem toont “Geen klant gevonden” en een knop “Nieuwe klant”. |

## UC-K03 Klantgeschiedenis raadplegen

| | |
| --- | --- |
| Use case | UC-K03 Klantgeschiedenis raadplegen (user story #124) |
| Doel | De medewerker ziet direct wat er eerder met de klant is gebeurd en hoeft niets opnieuw te vragen. |
| Primaire actor | Klantenservicemedewerker |
| Trigger | De medewerker wil een klant verder helpen. |
| Preconditie | De medewerker is ingelogd en de klant is gevonden (UC-K02). |
| Hoofdscenario | 1. De medewerker opent het klantprofiel.<br>2. Het systeem toont de tijdlijn: contactmomenten, klachten en boekingen, nieuwste eerst.<br>3. Het systeem toont open vervolgacties bovenaan.<br>4. De medewerker bekijkt de relevante contacten en afspraken. |
| Postconditie | De medewerker heeft een volledig beeld van de klant. |
| Alternatieve scenario’s | **2a. Filteren:** de medewerker filtert op periode of type (extend).<br>**4a. Zaak openen:** de medewerker opent een klacht direct vanuit de tijdlijn (extend).<br>**4b. Notitie:** de medewerker voegt een interne notitie toe (extend).<br>**2b. Nog geen contacten:** het systeem toont “Nog geen contactgeschiedenis”. |

## UC-K04 Openstaande zaken prioriteren en verdelen

| | |
| --- | --- |
| Use case | UC-K04 Openstaande zaken prioriteren en verdelen (user stories #126, #127) |
| Doel | Urgente zaken worden eerst opgepakt en elke zaak heeft een behandelaar. |
| Primaire actor | Teamleider klantenservice |
| Trigger | Het begin van de dienst, of een melding over een te lang wachtende zaak. |
| Preconditie | De teamleider is ingelogd; er zijn openstaande zaken. |
| Hoofdscenario | 1. De teamleider opent het overzicht openstaande zaken.<br>2. Het systeem toont de zaken gesorteerd op urgentie en ouderdom; zaken van klanten die nu op reis zijn staan automatisch op urgentie Hoog.<br>3. De teamleider beoordeelt de urgentie en past die zo nodig aan.<br>4. De teamleider wijst een behandelaar toe.<br>5. Het systeem zet de zaak in de werkvoorraad van de behandelaar en legt vast wie wanneer toewees. |
| Postconditie | Elke openstaande zaak heeft een urgentie en een behandelaar. |
| Alternatieve scenario’s | **2a. Achterstallige zaken:** de teamleider filtert op zaken die de reactienorm overschrijden (extend).<br>**4a. Herverdelen:** de teamleider wijst een zaak opnieuw toe met een overdrachtsnotitie (extend).<br>**4b. Capaciteit:** de teamleider bekijkt hoeveel zaken elke medewerker heeft (extend).<br>**2b. Geen openstaande zaken:** het systeem toont een lege staat met uitleg. |

## UC-K05 Klantvraag beantwoorden

| | |
| --- | --- |
| Use case | UC-K05 Klantvraag beantwoorden (user story #130) |
| Doel | De klant krijgt een antwoord en het antwoord is terug te vinden. |
| Primaire actor | Klantenservicemedewerker |
| Trigger | Er staat een vraag in de werkvoorraad van de medewerker. |
| Preconditie | De medewerker is ingelogd; de zaak is aan de medewerker toegewezen. |
| Hoofdscenario | 1. De medewerker opent de vraag.<br>2. De medewerker bekijkt de klantgeschiedenis (include UC-K03).<br>3. De medewerker schrijft het antwoord.<br>4. De medewerker verstuurt het antwoord en zet de zaak op “Afgehandeld”.<br>5. Het systeem slaat het antwoord op als contactmoment en berekent de afhandeltijd. |
| Postconditie | De klant heeft een antwoord; de zaak is afgehandeld en het antwoord staat in de historie. |
| Alternatieve scenario’s | **3a. Informatie ontbreekt:** de medewerker vraagt de klant om aanvulling; de zaak krijgt status “Wacht op klant” (extend).<br>**3b. Standaardantwoord:** de medewerker gebruikt een antwoordsjabloon (extend).<br>**3c. Andere afdeling nodig:** de medewerker zet de vraag door (bijv. naar Sales) (extend).<br>**4a. Antwoord leeg:** het systeem blokkeert afhandelen. |

## UC-K06 Klacht behandelen

| | |
| --- | --- |
| Use case | UC-K06 Klacht behandelen (user stories #131, #134, #143) |
| Doel | Elke klacht wordt volgens dezelfde werkwijze behandeld en afgesloten. |
| Primaire actor | Klantenservicemedewerker |
| Trigger | Een klant dient een klacht in (UC-K01). |
| Preconditie | De medewerker is ingelogd; de klacht is geregistreerd. |
| Hoofdscenario | 1. De medewerker opent de klacht (status “Nieuw”) en zet die op “In behandeling”.<br>2. Het systeem toont de klanthistorie en of de klant de accommodatie zelf heeft gekozen.<br>3. De medewerker onderzoekt de klacht en voegt bewijsmateriaal toe.<br>4. De medewerker beoordeelt de klacht als gegrond.<br>5. De medewerker laat het systeem een compensatievoorstel berekenen (include UC-K07).<br>6. Na goedkeuring informeert het systeem de klant over het voorstel.<br>7. De klant gaat akkoord; de medewerker legt de uitkomst vast.<br>8. De medewerker sluit de klacht af met eindresultaat “Gecompenseerd”. |
| Postconditie | De klacht is afgesloten met een vastgelegde uitkomst; de klant is geïnformeerd. |
| Alternatieve scenario’s | **2a. Klant is nu op reis:** de medewerker benadert het hotel voor een oplossing ter plaatse (escaleren naar bestemming, extend); bij succes eindresultaat “Opgelost ter plaatse”.<br>**4a. Ongegrond:** de medewerker legt een verplichte onderbouwing vast en sluit af als “Ongegrond”.<br>**7a. Klant maakt bezwaar:** het systeem zet de klacht op “Geëscaleerd (After Travel)”; After Travel neemt het eindbesluit.<br>**8a. Open vervolgacties:** het systeem blokkeert afsluiten en toont welke acties openstaan. |

## UC-K07 Vergoedingsvoorstel controleren

| | |
| --- | --- |
| Use case | UC-K07 Vergoedingsvoorstel controleren (user story #132) |
| Doel | Geen compensatie gaat naar de klant zonder controle door een tweede medewerker. |
| Primaire actor | Klantenservicemedewerker (indiener) en senior medewerker (goedkeurder) |
| Trigger | Een klacht is als gegrond beoordeeld (UC-K06 stap 5). |
| Preconditie | De klacht heeft een klachtcategorie; er is een compensatierichtlijn voor die categorie. |
| Hoofdscenario | 1. Het systeem stelt het klachttype vast en haalt het richtlijnpercentage op.<br>2. Het systeem berekent het bedrag: percentage × reissom, en toont het als “Te controleren”.<br>3. De indiener controleert het voorstel en dient het in.<br>4. Een andere medewerker opent het voorstel.<br>5. De goedkeurder keurt het voorstel goed.<br>6. Het systeem legt indiener, goedkeurder en datum vast en geeft het voorstel vrij voor de klant. |
| Postconditie | Er is een goedgekeurd compensatievoorstel, gecontroleerd door twee verschillende medewerkers. |
| Alternatieve scenario’s | **3a. Afwijken van de richtlijn:** de indiener past het percentage aan; een toelichting is verplicht (extend).<br>**3b. Vergelijkbare klachten:** de indiener bekijkt eerdere klachten van dezelfde categorie (extend).<br>**4a. Indiener probeert zelf goed te keuren:** het systeem blokkeert dit (vier-ogenprincipe).<br>**5a. Afgewezen:** de goedkeurder vult een reden in; het voorstel gaat terug naar de indiener.<br>**2a. Percentage < 0 of > 100:** het systeem toont een foutmelding. |

## UC-K08 Terugkerende klantproblemen onderzoeken

| | |
| --- | --- |
| Use case | UC-K08 Terugkerende klantproblemen onderzoeken (user stories #140, #141) |
| Doel | Trends in klachten zien en er verbeteracties aan koppelen. |
| Primaire actor | Teamleider klantenservice |
| Trigger | Periodieke analyse (bijv. maandelijks) of een opvallend aantal klachten. |
| Preconditie | De teamleider is ingelogd; er zijn afgesloten klachten. |
| Hoofdscenario | 1. De teamleider opent het klachtendashboard.<br>2. De teamleider kiest een periode.<br>3. Het systeem toont het aantal klachten per categorie, bestemming en leverancier, gesorteerd op frequentie.<br>4. De teamleider vergelijkt onderwerpen en periodes.<br>5. De teamleider maakt een verbeteractie aan met afdeling, eigenaar en deadline. |
| Postconditie | Er is een verbeteractie vastgelegd bij de verantwoordelijke afdeling. |
| Alternatieve scenario’s | **5a. Naar andere afdeling:** de actie gaat naar Inkoop (bijv. hotel met veel klachten) (extend).<br>**5b. Rapport:** de teamleider exporteert een rapport en deelt het met het management (extend).<br>**3a. Te weinig gegevens:** het systeem meldt dat er in de periode geen klachten zijn. |

## UC-K09 Klantgegevens verwijderen (AVG)

| | |
| --- | --- |
| Use case | UC-K09 Klantgegevens verwijderen (AVG) (user story #139) |
| Doel | Persoonsgegevens worden verwijderd of geanonimiseerd zodra dat mag, zonder gegevens te verliezen die nog nodig zijn. |
| Primaire actor | Klantenservicemedewerker |
| Trigger | De klant vraagt om verwijdering van zijn gegevens. |
| Preconditie | De medewerker is ingelogd; de klant is gevonden (UC-K02). |
| Hoofdscenario | 1. De medewerker kiest “Gegevens verwijderen”.<br>2. Het systeem controleert de reisstatus: alle terugkomdatums liggen in het verleden.<br>3. Het systeem controleert de bewaartermijn.<br>4. Het systeem toont wat verwijderd wordt en vraagt om bevestiging.<br>5. De medewerker bevestigt.<br>6. Het systeem anonimiseert naam, geboortedatum, e-mail, telefoon en woonplaats, wist contactsamenvattingen en bewaart boekingen anoniem voor de financiële administratie.<br>7. Het systeem logt de verwijdering en stuurt de klant een bevestiging. |
| Postconditie | De klant is niet meer herleidbaar; de verwijdering is gelogd. |
| Alternatieve scenario’s | **2a. Klant is op reis of vertrekt nog:** het systeem blokkeert en toont de terugkomdatum (gegevens nodig bij calamiteiten, interview P3).<br>**3a. Bewaartermijn loopt nog:** het systeem legt een uitzondering vast met de datum waarop verwijderen wel mag.<br>**5a. Medewerker annuleert:** er wordt niets verwijderd. |

---

## User flows

Afbeelding met alle flows: [`user-flows-klantenservice.png`](user-flows-klantenservice.png)

### UC-K01 Klantcontact registreren
```mermaid
flowchart LR
    S(["START"]) --> A["Klant zoeken"] --> B{"Klant gevonden?"}
    B -- "NEE" --> C["Nieuwe klant aanmaken"] --> D
    B -- "JA" --> D["Contact registreren kiezen"]
    D --> E["Kanaal, categorie, onderwerp en samenvatting invullen"]
    E --> F{"Bestaande zaak?"}
    F -- "JA" --> G["Koppelen aan zaak"] --> H
    F -- "NEE" --> G2["Nieuwe zaak aanmaken"] --> H
    H["Opslaan"] --> I{"Gegevens geldig en geen IBAN of paspoortnummer?"}
    I -- "NEE" --> J["Foutmelding of waarschuwing tonen"] --> E
    I -- "JA" --> K["Contact opgeslagen in klanthistorie"] --> Z(["EINDE"])
```

### UC-K02 Klant zoeken op e-mailadres
```mermaid
flowchart LR
    S(["START"]) --> A["Klant zoeken openen"] --> B["E-mail, telefoon, naam of boekingsnummer invullen"] --> C{"Aantal resultaten?"}
    C -- "0" --> D["Melding: geen klant gevonden"] --> E{"Nieuwe klant aanmaken?"}
    E -- "JA" --> F["Klant aanmaken"] --> Z(["EINDE"])
    E -- "NEE" --> Z
    C -- "1" --> G["Klantprofiel openen"] --> Z
    C -- "Meer dan 1" --> H["Lijst met geboortedatum en woonplaats tonen"] --> I["Juiste klant kiezen"] --> G
```

### UC-K03 Klantgeschiedenis raadplegen
```mermaid
flowchart LR
    S(["START"]) --> A["Klantprofiel openen"] --> B["Tijdlijn en open vervolgacties tonen"] --> C{"Filteren?"}
    C -- "JA" --> D["Filter op periode of type"] --> E
    C -- "NEE" --> E{"Zaak openen?"}
    E -- "JA" --> F["Klacht of vraag openen"] --> Z(["EINDE"])
    E -- "NEE" --> G{"Notitie toevoegen?"}
    G -- "JA" --> H["Notitie opslaan"] --> Z
    G -- "NEE" --> Z
```

### UC-K04 Openstaande zaken prioriteren en verdelen
```mermaid
flowchart LR
    S(["START"]) --> A["Overzicht openstaande zaken openen"] --> B{"Zaken aanwezig?"}
    B -- "NEE" --> C["Lege staat tonen"] --> Z(["EINDE"])
    B -- "JA" --> D["Sorteren op urgentie en ouderdom"] --> E["Urgentie beoordelen"] --> F["Behandelaar toewijzen"] --> G["Zaak in werkvoorraad behandelaar"] --> H{"Nog zaken zonder behandelaar?"}
    H -- "JA" --> E
    H -- "NEE" --> Z
```

### UC-K05 Klantvraag beantwoorden
```mermaid
flowchart LR
    S(["START"]) --> A["Vraag openen uit werkvoorraad"] --> B["Klantgeschiedenis bekijken"] --> C{"Informatie compleet?"}
    C -- "NEE" --> D["Klant om aanvulling vragen"] --> E["Status: Wacht op klant"] --> Z(["EINDE"])
    C -- "JA" --> F{"Andere afdeling nodig?"}
    F -- "JA" --> G["Doorzetten naar afdeling"] --> Z
    F -- "NEE" --> H["Antwoord schrijven"] --> I{"Antwoord ingevuld?"}
    I -- "NEE" --> H
    I -- "JA" --> J["Versturen en status Afgehandeld"] --> K["Contactmoment en afhandeltijd opgeslagen"] --> Z
```

### UC-K06 Klacht behandelen
```mermaid
flowchart LR
    S(["START"]) --> A["Klacht openen: In behandeling"] --> B{"Klant nu op reis?"}
    B -- "JA" --> C["Hotel benaderen"] --> D{"Opgelost ter plaatse?"}
    D -- "JA" --> E["Afsluiten: Opgelost ter plaatse"] --> Z(["EINDE"])
    D -- "NEE" --> F
    B -- "NEE" --> F["Klacht onderzoeken"] --> G{"Gegrond?"}
    G -- "NEE" --> H["Onderbouwing vastleggen en afsluiten als Ongegrond"] --> Z
    G -- "JA" --> I["Compensatievoorstel (UC-K07)"] --> J["Klant informeren"] --> K{"Klant akkoord?"}
    K -- "JA" --> L["Uitkomst vastleggen en afsluiten"] --> Z
    K -- "NEE" --> M["Escaleren naar After Travel"] --> Z
```

### UC-K07 Vergoedingsvoorstel controleren
```mermaid
flowchart LR
    S(["START"]) --> A["Klachttype vaststellen"] --> B["Percentage x reissom berekenen"] --> C{"Afwijken van richtlijn?"}
    C -- "JA" --> D["Percentage aanpassen met toelichting"] --> E
    C -- "NEE" --> E["Voorstel indienen"] --> F["Tweede medewerker opent voorstel"] --> G{"Zelfde medewerker als indiener?"}
    G -- "JA" --> H["Blokkeren: vier-ogenprincipe"] --> F
    G -- "NEE" --> I{"Goedkeuren?"}
    I -- "NEE" --> J["Afwijzen met reden, terug naar indiener"] --> C
    I -- "JA" --> K["Goedkeuring vastleggen en vrijgeven"] --> Z(["EINDE"])
```

### UC-K08 Terugkerende klantproblemen onderzoeken
```mermaid
flowchart LR
    S(["START"]) --> A["Klachtendashboard openen"] --> B["Periode kiezen"] --> C{"Klachten in periode?"}
    C -- "NEE" --> D["Melding: geen gegevens"] --> Z(["EINDE"])
    C -- "JA" --> E["Aantallen per categorie, bestemming en leverancier tonen"] --> F{"Trend gevonden?"}
    F -- "NEE" --> Z
    F -- "JA" --> G["Verbeteractie aanmaken met afdeling, eigenaar en deadline"] --> H{"Rapport delen?"}
    H -- "JA" --> I["Rapport exporteren en delen met management"] --> Z
    H -- "NEE" --> Z
```

### UC-K09 Klantgegevens verwijderen (AVG)
```mermaid
flowchart LR
    S(["START"]) --> A["Gegevens verwijderen kiezen"] --> B{"Alle terugkomdatums voorbij?"}
    B -- "NEE" --> C["Blokkeren en terugkomdatum tonen"] --> Z(["EINDE"])
    B -- "JA" --> D{"Bewaartermijn verstreken?"}
    D -- "NEE" --> E["Uitzondering vastleggen met datum"] --> Z
    D -- "JA" --> F["Overzicht tonen en bevestiging vragen"] --> G{"Bevestigd?"}
    G -- "NEE" --> Z
    G -- "JA" --> H["Anonimiseren, loggen en klant bevestigen"] --> Z
```
