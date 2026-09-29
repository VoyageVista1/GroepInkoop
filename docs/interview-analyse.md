# Interviewanalyse – Inkoop & Klantenservice

**Bron:** interview met de opdrachtgever (medewerker reisbureau, praktijkvoorbeeld TUI), sprint 2.
**Team:** Productontwikkeling & Inkoop + Klantenservice & Support – casus VoyageVista.

> Let op: de geïnterviewde gaf aan soms **fictieve cijfers** te gebruiken (bedrijfsinformatie). Gebruik de getallen als indicatie, niet als harde requirement.

---

## 1. Belangrijkste bevindingen

### 1.1 Productontwikkeling & Inkoop

| # | Bevinding | Tijdstip | Koppeling casus (§4.4) |
|---|---|---|---|
| I1 | Nieuwe reis ontstaat vanuit productafdeling, accommodatieafdeling en inkoop, met input van een **klantpanel (~2.500 klanten)** en analyse van "witte vlekken" op de kaart. | 24:26–26:35 | GP2 Inefficiënte productontwikkelingscyclus |
| I2 | Productontwikkeling kijkt naar **specifieke wensen van de Nederlandse klant** (NL-sprekende hostess, lange bedden, goede koelkast, ruime woonkamer). | 25:05–26:16 | KP2 Versnipperde productinformatie |
| I3 | Contact met leveranciers (hotels) is **persoonlijk bezoek** door productmanagers: bestaand contact 1×/jaar, nieuw contact 2–3×/jaar; ± 20 hotels per week. | 26:52–27:22 | KP1 Onoverzichtelijke onderhandelingen |
| I4 | Tijdens onderhandeling worden vastgelegd: **basisprijs, marge, onderhandelingsruimte, volumekorting** (bijv. korting bij afname van 5 kamers). | 27:29–27:49 | KP5 Handmatig contractbeheer, GP1 Geen gestandaardiseerde productdata |
| I5 | Ingekochte kamers **moeten verkocht worden** (inkooprisico ligt bij het bedrijf). Inkoop moet dus direct afstemmen met marketing en sales. | 27:49–28:03 | KP3 Moeilijk delen van informatie |
| I6 | Productmanagers laden de gegevens handmatig in een backofficesysteem, dat gekoppeld is met het verkoopsysteem. | 28:16–28:33 | GP1 |
| I7 | **Beddenbanken** (externe voorraad) zetten veel kamertypes automatisch in het systeem. Daardoor is het voor verkoper én klant onduidelijk welke kamer wat heeft (balkon, begane grond, …). | 10:26–11:16 | GP1, KP2 |
| I8 | Producten van **derde partijen** (bijv. De Jong Intra, Sawadee) lopen niet automatisch door naar facturatie. Creditfacturen bij annulering worden handmatig verwerkt. | 3:44–4:05, 15:05–15:21 | Overstijgend met Financiën |
| I9 | Medewerkers werken met **~30 systemen, ~10 per dag**, die deels niet met elkaar communiceren. | 4:51–5:35 | IT GP1 Geen uniforme datastructuur |
| I10 | Elke reis heeft **eigen (annulerings-)voorwaarden** (ANVR). Dat is een van de redenen waarom klanten niet zelf online kunnen wijzigen. | 8:14–8:33 (deel 2) | GP1 Geen gestandaardiseerde productdata |

### 1.2 Klantenservice & Support

| # | Bevinding | Tijdstip | Koppeling casus (§4.3) |
|---|---|---|---|
| K1 | Klant wordt opgezocht in de "Agent Desktop", bij voorkeur op **e-mailadres** (naam geeft te veel resultaten). | 6:03–6:25 | KP4 Beperkt inzicht eerdere contacten |
| K2 | Bij een shopbezoek wordt handmatig een **opportunity** (verkoopkans) aangemaakt: vertrek- en aankomstdatum, reisduur, aantal volwassenen en kinderen. | 6:28–7:18 | KP1 Handmatige registratie |
| K3 | Het gesprek wordt als **vrije tekst in één opmerkingenveld** gezet: wie, wat, waar, wanneer, hoe lang, wat de klant belangrijk vindt, taalbarrière, of de klant de accommodatie zelf koos. | 7:27–8:42 | KP1, KP3 Geen uniforme afhandeling |
| K4 | Vastleggen of de klant de accommodatie **zelf heeft gekozen** is belangrijk om latere klachten te kunnen beoordelen. | 8:21–8:35 | GP2 Geen analyse van klantfeedback |
| K5 | **Elk telefoongesprek wordt geregistreerd.** Shopmedewerkers werken ook voor het contactcentrum. Een consistente "verhaallijn" is nodig, anders krijgt de klant van collega A, B en C verschillende antwoorden. | 29:08–29:47 | GP1 Versnipperde klantcommunicatie |
| K6 | Door handmatige registratie gaat er van alles mis, bijvoorbeeld een brief over vertraging terwijl de klant al op de bestemming is. | 1:11–1:53 (deel 2) | KP5 Lange reactietijden, GP1 |
| K7 | Wens: gesprekken automatisch opnemen of transcriberen. **Maar:** privacy van klant én medewerker, standpunt van de ondernemingsraad en de vraag of een medewerker het verslag nog kan aanpassen zijn nog open. | 8:53–9:07, 2:01–3:18 (deel 2) | KP1 |
| K8 | **Escalatiepad:** shopmedewerker → senior (geïnterviewde) → afdeling **After Travel** (klachten na de reis). | 3:36–4:19 (deel 2) | KP3 Geen uniforme afhandeling |
| K9 | Er zijn **4 A4'tjes met standaardoplossingen** voor klachten, meestal als **percentage van de reissom**. Een systeem/bot doet een voorstel (bijv. 4%), maar een **mens controleert altijd** (klacht kan ongegrond zijn of al ter plekke opgelost). | 4:29–5:26 (deel 2) | KP2 Prioriteren, KP3, GP2 |
| K10 | **~50% van het klantcontact is een servicevraag** (stoel boeken, betaling, wijziging) die de klant eigenlijk zelf zou moeten kunnen doen. | 7:18–8:04 (deel 2) | KP5, GP1 |
| K11 | Betalingen zonder boekingsnummer moeten handmatig aan een boeking gekoppeld worden, vaak vlak voor vertrek ("stress"). | 12:35–14:27 | Overstijgend met Financiën |

### 1.3 Privacy (AVG) – harde randvoorwaarden

Dit zijn **niet-functionele eisen** die in bijna elke user story terugkomen. Ze zijn goed voor het perspectief BIV (beschikbaarheid, integriteit, vertrouwelijkheid) in de toetsmatrijs.

| # | Regel | Tijdstip |
|---|---|---|
| P1 | **Geen bankrekeningnummer (IBAN) opslaan**, ook niet na betaling. Voor een terugbetaling vult de klant het zelf in. | 15:36–16:18 |
| P2 | **Geen paspoortnummers** of andere paspoortgegevens opslaan. Alleen voornaam, achternaam en geboortedatum zoals in het paspoort. | 16:21–16:35 |
| P3 | Klantgegevens moeten bewaard blijven **tot de klant weer thuis is** (calamiteiten, verzekering). Daarna mag de klant om **verwijdering** vragen. | 29:48 – 0:52 (deel 2) |
| P4 | Dubbele namen (vader/zoon) onderscheiden met tweede voornaam of Sr./Jr., en verder via e-mail en telefoon. | 16:56–17:39 |
| P5 | Ongeboren baby's worden geboekt als "Baby <achternaam>" zonder geldige geboortedatum. Aanvullen na de geboorte. | 17:45–18:10 |

---

## 2. Voorstel epics en user stories

Formaat: *Als <rol> wil ik <functie>, zodat <waarde>.* De acceptatiecriteria (AC) staan in Stel/Als/Dan. Het zijn **voorstellen** om tijdens de refinement met de opdrachtgever te valideren.

### Epic A – Leveranciers & contracten (Inkoop)

**A1 – Leverancier registreren**
Als productmanager wil ik een leverancier (hotel, busmaatschappij, rederij) centraal vastleggen, zodat alle collega's dezelfde, actuele gegevens zien.
- AC1: *Stel* ik ben ingelogd als productmanager, *als* ik naam, type, land/bestemming en contactpersoon invul en opsla, *dan* staat de leverancier in het leveranciersoverzicht.
- AC2: *Stel* er bestaat al een leverancier met dezelfde naam en plaats, *als* ik opsla, *dan* krijg ik een waarschuwing voor een mogelijk dubbele invoer.
- AC3: Verplichte velden zijn gemarkeerd. Opslaan zonder verplichte velden geeft een duidelijke foutmelding per veld.

**A2 – Leveranciersbezoek / onderhandeling vastleggen**
Als productmanager wil ik per bezoek de onderhandelingsresultaten vastleggen (basisprijs, marge, volumekorting, status), zodat ik en mijn collega's de stand van de onderhandelingen kunnen volgen.
- AC1: Een onderhandeling heeft een status: *Gepland – Bezocht – In onderhandeling – Akkoord – Afgewezen*.
- AC2: Marge wordt automatisch berekend uit inkoopprijs en verkoopprijs. Een negatieve marge geeft een waarschuwing.
- AC3: Het overzicht is te filteren op status en bestemming, en toont de datum van het laatste bezoek.

**A3 – Contract met voorwaarden vastleggen**
Als inkoper wil ik een contract vastleggen met looptijd, aantal gecontracteerde kamers (allotment), prijzen en **annulerings- en wijzigingsvoorwaarden**, zodat verkoop en klantenservice weten wat er geldt.
- AC1: Een contract hoort bij precies één leverancier en heeft een begin- en einddatum (einddatum ≥ begindatum).
- AC2: *Stel* een contract verloopt binnen 60 dagen, *dan* staat het gemarkeerd in het dashboard "Aflopende contracten".
- AC3: Annuleringsvoorwaarden worden gestructureerd vastgelegd (tot X dagen voor vertrek → Y% kosten), niet als vrije tekst.

**A4 – Bezettingsoverzicht ingekochte kamers**
Als inkoper wil ik zien hoeveel ingekochte kamers al verkocht zijn, zodat ik op tijd marketing en sales kan inschakelen om de rest te vullen.
- AC1: Per contract ziet de inkoper het aantal gecontracteerde, verkochte en beschikbare kamers en een bezettingspercentage.
- AC2: *Stel* de bezetting is < 50% binnen 8 weken voor de periode, *dan* krijgt het contract de status "Actie nodig". *(Drempels valideren bij de opdrachtgever.)*

### Epic B – Gestandaardiseerde productdata (Inkoop)

**B1 – Reisproduct aanmaken met vaste kenmerken**
Als productmanager wil ik een reisproduct aanmaken met gestandaardiseerde kenmerken (bestemming, accommodatie, kamertypes, faciliteiten), zodat verkopers en klanten eenduidige informatie krijgen.
- AC1: Kamertypes kiezen uit een vaste lijst (bijv. 2-persoons standaard, balkon, begane grond). Vrije tekst is niet mogelijk. *(Oplossing voor I7, de beddenbank-chaos.)*
- AC2: Faciliteiten die belangrijk zijn voor de Nederlandse klant (lange bedden, keukenblok, …) zijn aan te vinken en filterbaar.

**B2 – Productstatus in de ontwikkelcyclus**
Als productmanager wil ik de status van een nieuw product volgen (*Idee → Onderzoek → Inkoop → Klaar voor verkoop → Live*) met deadlines, zodat deadlines niet meer gemist worden.
- AC1: Elk product heeft een eigenaar en een streefdatum. Te laat = rood in het overzicht.

### Epic C – Klantdossier & contactregistratie (Klantenservice)

**C1 – Klant zoeken**
Als klantenservicemedewerker wil ik een klant zoeken op e-mailadres, telefoonnummer, of naam + geboortedatum, zodat ik snel het juiste dossier vind.
- AC1: Zoeken op volledig e-mailadres geeft maximaal één resultaat.
- AC2: Zoeken op naam toont naam, geboortedatum en woonplaats, zodat ik vader en zoon met dezelfde naam kan onderscheiden.

**C2 – Klantcontact gestructureerd registreren**
Als klantenservicemedewerker wil ik een contactmoment vastleggen met vaste velden (kanaal, onderwerp/categorie, samenvatting, afspraak, vervolgactie, behandelaar), zodat collega's dezelfde verhaallijn aanhouden.
- AC1: Kanaal kiezen uit *Telefoon – E-mail – Shop – Social media*. Categorie kiezen uit *Informatie – Wijziging – Betaling – Klacht – Overig*.
- AC2: Een contactmoment zonder samenvatting kan niet worden opgeslagen.
- AC3: Datum, tijd en medewerker worden automatisch ingevuld (niet aanpasbaar).

**C3 – Klanttijdlijn**
Als klantenservicemedewerker wil ik alle eerdere contactmomenten, boekingen en klachten van een klant op één tijdlijn zien, zodat ik niet opnieuw informatie hoef te vragen.
- AC1: De tijdlijn staat in omgekeerd chronologische volgorde en is te filteren op categorie.
- AC2: Open vervolgacties staan bovenaan.

**C4 – Reiswensen gestructureerd vastleggen (opportunity)**
Als reisadviseur wil ik de reiswensen vastleggen in vaste velden (periode, reisduur, aantal volwassenen/kinderen, budget, belangrijkste wensen, "accommodatie zelf gekozen: ja/nee"), zodat de afspraken later terug te vinden zijn.
- AC1: Vertrekdatum ligt in de toekomst en de terugkomdatum ligt na de vertrekdatum.
- AC2: Het veld "Accommodatie zelf gekozen door klant" is verplicht bij het omzetten naar een boeking. *(Onderbouwing: K4.)*

### Epic D – Klachtafhandeling (Klantenservice)

**D1 – Klacht registreren met prioriteit**
Als klantenservicemedewerker wil ik een klacht registreren met categorie en urgentie, zodat urgente zaken eerst worden opgepakt.
- AC1: Urgentie wordt voorgesteld op basis van regels (bijv. klant is nu op reis → Hoog) en is handmatig aan te passen.
- AC2: Een klacht heeft een status: *Nieuw – In behandeling – Geëscaleerd (After Travel) – Afgehandeld*.

**D2 – Compensatievoorstel volgens richtlijn**
Als klantenservicemedewerker wil ik op basis van de klachtcategorie een compensatievoorstel (percentage van de reissom) krijgen, zodat klachten uniform worden afgehandeld.
- AC1: Het systeem berekent het bedrag = percentage × reissom en toont welke richtlijn is gebruikt.
- AC2: Een voorstel kan **pas naar de klant nadat een medewerker het heeft goedgekeurd** (vier-ogenprincipe, K9).
- AC3: Afwijken van de richtlijn kan alleen met een verplichte toelichting.

**D3 – Escaleren**
Als medewerker wil ik een klacht kunnen doorzetten naar een senior of naar After Travel, met de volledige historie erbij, zodat de klant zijn verhaal niet opnieuw hoeft te doen.

### Epic E – Privacy (niet-functioneel, geldt voor alle stories)

- **E1:** Er bestaat geen veld voor IBAN of paspoortnummer in het datamodel (P1, P2).
- **E2:** Als medewerker wil ik op verzoek van een klant diens persoonsgegevens verwijderen of anonimiseren, zodat we voldoen aan de AVG. *AC:* verwijderen is geblokkeerd zolang de klant een reis heeft met een terugkomdatum in de toekomst (P3).
- **E3:** Een klant kan worden aangemaakt met de voorlopige naam "Baby <achternaam>" en zonder geboortedatum. Het systeem signaleert dat deze gegevens nog moeten worden aangevuld (P5).

---

## 3. Eerste opzet datamodel (entiteiten)

```
Leverancier (leverancierID, naam, type, land, plaats, contactpersoon, e-mail, telefoon)
  1 ── * Onderhandeling (onderhandelingID, datumBezoek, status, basisprijs, verkoopprijs, marge, volumekorting, notitie, productmanager)
  1 ── * Contract (contractID, begindatum, einddatum, aantalKamers, prijsPerNacht, status)
           1 ── * Annuleringsvoorwaarde (dagenVoorVertrek, kostenPercentage)
Reisproduct (productID, naam, bestemming, status, streefdatum, eigenaar)
  * ── 1 Contract
  1 ── * Kamertype (kamertypeID, omschrijving [vaste lijst], capaciteit)
  * ── * Faciliteit

Klant (klantID, voornaam, tussenvoegsel, achternaam, achtervoegsel [Sr./Jr.], geboortedatum?, e-mail, telefoon, woonplaats)
  ⚠ GEEN iban, GEEN paspoortnummer
  1 ── * Contactmoment (contactID, datumTijd, kanaal, categorie, samenvatting, vervolgactie, medewerker)
  1 ── * Opportunity (opportunityID, vertrekdatum, terugkomdatum, volwassenen, kinderen, budget, wensen, zelfGekozen)
  1 ── * Boeking (boekingID, productID, vertrekdatum, terugkomdatum, reissom, status)
  1 ── * Klacht (klachtID, boekingID, categorie, urgentie, status, compensatiePercentage, compensatieBedrag, goedgekeurdDoor)
Compensatierichtlijn (categorie, percentage, omschrijving)
Medewerker (medewerkerID, naam, rol)
```

Overstijgende koppelingen:
- **Boeking ↔ Contract/Kamertype.** Daarmee kan de inkoop de bezetting zien (A4).
- **Boeking → Factuur.** Dit hoort bij het Financiën-team. Stem de sleutel `boekingID` af.
- **Klant.** Deel dezelfde entiteit met het Marketing-team (360-graden klantbeeld). Spreek af wie de eigenaar is.

---

## 4. Vervolgvragen voor de opdrachtgever

Verzamel ze via Nynke (docent). De opdrachtgever beantwoordt ze per mail.

**Inkoop**
1. Welke gegevens noteert een productmanager precies tijdens een hotelbezoek? Is er een vast format of checklist?
2. Hoe lang loopt een contract met een hotel meestal, en wanneer begint de heronderhandeling?
3. Wat gebeurt er als ingekochte kamers niet verkocht worden? Kunnen ze teruggegeven worden (release-datum)?
4. Wie moet een contract goedkeuren voordat een product live gaat?
5. Welke kamertypes en faciliteiten zijn voor jullie de standaardlijst?

**Klantenservice**
6. Welke categorieën klantvragen en klachten onderscheiden jullie? Mogen we (een geanonimiseerde versie van) de 4 A4'tjes met compensatieregels zien?
7. Wanneer is een vraag of klacht "urgent"? Welke reactietijd is de norm?
8. Welke informatie heeft After Travel nodig bij een escalatie?
9. Welke servicevragen (stoel, betaling, wijziging) komen het vaakst voor? Dat helpt ons bij het prioriteren.
10. Hoe lang na thuiskomst moeten klantgegevens nog bewaard blijven voor klachten of verzekering?

---

## 5. Advies voor sprintplanning

- **Sprint 3 (1 okt – 22 okt, verlengd door herfstvakantie):** C1, C2, A1 en E1. Dit is de basis: klanten en leveranciers vastleggen, met privacy by design.
- **Sprint 4:** C3, A2, A3 en D1.
- **Later:** D2 (compensatie met goedkeuring), A4 (bezetting, overstijgend met Sales/Marketing), B1–B2.
- Overleg met het **Financiën-team** over de factuur voor derde partijen (I8, K11), en met het **Marketing-team** over de gedeelde klantentiteit.
