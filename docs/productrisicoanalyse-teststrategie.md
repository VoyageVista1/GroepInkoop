# Productrisicoanalyse en teststrategie

**Team:** Productontwikkeling & Inkoop + Klantenservice & Support – casus VoyageVista
**Versie:** 29 september 2026 · online versie: [Claude Docs](https://claude.ai/code/artifact/63b02a6f-4e1f-4e7e-8294-cd43abf1d436)

Voor VoyageVista Klantenservice en Inkoop testen we het zwaarst op privacy (AVG), de compensatieberekening bij klachten en het vier-ogenprincipe. Fouten daar raken de klant direct, kosten geld of zijn in strijd met de wet.

---

## 1. Scope en aanpak

Deze analyse dekt de user stories van sprint 3 en 4 uit de [interviewanalyse](interview-analyse.md). Na elke refinement werken we haar bij.

| ID | User story | Afdeling |
| --- | --- | --- |
| C1 | Klant zoeken op e-mail, telefoon of naam | Klantenservice |
| C2 | Contactmoment gestructureerd registreren | Klantenservice |
| C3 | Klanthistorie (tijdlijn) bekijken | Klantenservice |
| D1 | Klacht registreren met urgentie | Klantenservice |
| D2 | Compensatievoorstel volgens richtlijn, met goedkeuring | Klantenservice |
| E2 | Persoonsgegevens verwijderen (AVG) | Klantenservice |
| A1 | Leverancier registreren | Inkoop |
| A2 | Onderhandeling vastleggen met marge | Inkoop |
| A3 | Contract met annuleringsvoorwaarden vastleggen | Inkoop |
| A4 | Bezetting ingekochte kamers bewaken | Inkoop |

**Zo bepalen we het risico.** Per risico scoren we de kans op een fout en de impact als die fout in productie komt, elk op 1 (laag), 2 (middel) of 3 (hoog). Risico = kans × impact.

| Score | Risicoklasse | Betekenis |
| --- | --- | --- |
| 6–9 | A · hoog | Grondig testen, meerdere technieken, altijd een tweede tester |
| 3–4 | B · middel | Gestructureerd testen met één passende techniek |
| 1–2 | C · laag | Verkennend testen of een korte checklist |

Impact is hoog als de fout de wet raakt (AVG), geld kost, of de klant op reis in de problemen brengt. Kans is hoog bij rekenwerk, datums, afhankelijkheden tussen gegevens en logica met rollen.

## 2. Productrisico's

Vijf van de vijftien risico's vallen in klasse A. Alle vijf gaan over privacy, geld of een klant die op reis is. Kwaliteitskenmerken volgen ISO 25010.

| ID | Risico | Story | Kwaliteitskenmerk | Kans | Impact | Score | Klasse |
| --- | --- | --- | --- | --- | --- | --- | --- |
| R1 | Persoonsgegevens worden verwijderd terwijl de klant nog op reis is; bij een calamiteit weten we niet wie er aan boord zit | E2 | Functionele juistheid | 2 | 3 | 6 | A |
| R2 | Er belandt toch een IBAN of paspoortnummer in het systeem, bijvoorbeeld via een vrij tekstveld | C2, E2 | Beveiliging: vertrouwelijkheid | 2 | 3 | 6 | A |
| R3 | Het compensatiebedrag wordt verkeerd berekend (percentage, reissom of afronding) | D2 | Functionele juistheid | 2 | 3 | 6 | A |
| R4 | Een medewerker keurt zijn eigen compensatievoorstel goed | D2 | Beveiliging: verantwoording | 2 | 3 | 6 | A |
| R5 | Een klacht van een klant die nu op reis is, krijgt niet automatisch urgentie Hoog | D1 | Functionele juistheid | 2 | 3 | 6 | A |
| R6 | Een contract krijgt een einddatum vóór de begindatum, of ongeldige annuleringsvoorwaarden | A3 | Functionele juistheid | 2 | 2 | 4 | B |
| R7 | De marge wordt verkeerd berekend of een negatieve marge wordt niet gesignaleerd | A2 | Functionele juistheid | 2 | 2 | 4 | B |
| R8 | Bij gelijke namen (vader en zoon) wordt de verkeerde klant geopend | C1 | Functionele juistheid | 1 | 3 | 3 | B |
| R9 | Dezelfde leverancier wordt twee keer aangemaakt | A1 | Functionele juistheid: gegevensintegriteit | 3 | 1 | 3 | B |
| R10 | Een contactmoment wordt opgeslagen zonder bruikbare samenvatting, of met verkeerde tijd of medewerker | C2 | Beveiliging: verantwoording | 2 | 2 | 4 | B |
| R11 | Het bezettingssignaal (onder 50%) verschijnt niet of te laat | A4 | Functionele juistheid | 2 | 2 | 4 | B |
| R12 | Medewerkers begrijpen een formulier niet en voeren gegevens verkeerd in | Alle | Bruikbaarheid | 2 | 2 | 4 | B |
| R13 | De klanthistorie toont niet alle contactmomenten, of in de verkeerde volgorde | C3 | Functionele volledigheid | 1 | 2 | 2 | C |
| R14 | Het scherm is lastig te gebruiken op een tablet in de shop of met het toetsenbord | Alle | Bruikbaarheid: toegankelijkheid | 2 | 1 | 2 | C |
| R15 | Zoeken wordt traag bij een groot klantenbestand | C1 | Prestatie-efficiëntie | 1 | 2 | 2 | C |

## 3. Risicomatrix

Vijf risico's in klasse A, allemaal met kans 2 en impact 3.

| Impact ↓ / Kans → | Laag (1) | Middel (2) | Hoog (3) |
| --- | --- | --- | --- |
| **Hoog (3)** | B · 3 — R8 | **A · 6 — R1, R2, R3, R4, R5** | A · 9 — geen |
| **Middel (2)** | C · 2 — R13, R15 | B · 4 — R6, R7, R10, R11, R12 | A · 6 — geen |
| **Laag (1)** | C · 1 — geen | C · 2 — R14 | B · 3 — R9 |

De rechterbovenhoek is leeg: geen enkel risico heeft zowel een hoge kans als een hoge impact.

## 4. Teststrategie

Hoe hoger de risicoklasse, hoe meer technieken, hoe hoger de dekking en hoe strenger het vier-ogenprincipe.

| Klasse | Testintensiteit | Technieken | Dekking | Wie test |
| --- | --- | --- | --- | --- |
| A · hoog | Grondig, bij elke wijziging opnieuw (regressie) | Grenswaardenanalyse, beslistabel, toestandsovergangen, plus een geautomatiseerde UI-test van het hoofdpad | Alle regels in de beslistabel, alle grenswaarden, alle overgangen | Bouwer en tweede tester van een ander teamlid; de tweede tester tekent af in DevOps |
| B · middel | Gestructureerd, eenmalig per sprint | Equivalentieklassen of grenswaarden (één techniek) | Elke klasse minstens één keer, geldig en ongeldig | Tweede tester van een ander teamlid |
| C · laag | Licht | Verkennend testen (sessie van 30 minuten) of een checklist | Hoofdpad en één foutpad | Een teamlid dat niet de bouwer is |

**Niet-functionele kwaliteit** testen we apart, omdat die buiten de user stories valt.

| Kwaliteitskenmerk | Hoe we testen | Risico's |
| --- | --- | --- |
| Bruikbaarheid | Usability-test met 3 gebruikers per sprint (think-aloud) op 3 vaste taken: klant zoeken, klacht registreren, contract vastleggen | R12 |
| Toegankelijkheid | Checklist: alles met toetsenbord te bedienen, zichtbare focus, contrast 4,5:1, foutmelding onder het veld; tablet- en schermbreedte 390 px | R14 |
| Beveiliging: vertrouwelijkheid | Review van het datamodel op IBAN- en paspoortvelden; negatieve test die een IBAN in een tekstveld plakt | R2 |
| Beveiliging: verantwoording | Controleren dat datum, tijd en medewerker automatisch worden vastgelegd en niet aan te passen zijn | R4, R10 |
| Prestatie-efficiëntie | Zoektest met 10.000 testklanten; zoeken op e-mail moet binnen 2 seconden een resultaat geven | R15 |

**Testniveaus.** Per user story testen we eerst de losse regels (unittest van de berekening en de validatie), daarna het scherm (UI-test), en tijdens de review de hele keten (acceptatietest met de opdrachtgever en realistische testdata).

## 5. Testontwerptechnieken

Elke user story krijgt de techniek die past bij het hoogste risico erin. Samen zijn dat 54 testgevallen voor sprint 3 en 4.

| Story | Risico's | Klasse | Techniek | Testgevallen |
| --- | --- | --- | --- | --- |
| D2 Compensatie | R3, R4 | A | Grenswaarden (percentage), toestandsovergangen (status), geautomatiseerde UI-test | 12 |
| E2 AVG-verwijdering | R1, R2 | A | Beslistabel, grenswaarden (terugkomdatum) | 6 |
| D1 Klacht registreren | R5 | A | Grenswaarden (vertrek- en terugkomdatum) | 4 |
| C2 Contactmoment | R2, R10 | A | Grenswaarden (lengte samenvatting), negatieve test met IBAN | 5 |
| A3 Contract | R6 | B | Grenswaarden (datums, 0–100%) | 6 |
| C1 Klant zoeken | R8, R15 | B | Equivalentieklassen (e-mail, telefoon, naam; gevonden, niet gevonden) | 6 |
| A1 Leverancier | R9 | B | Equivalentieklassen (uniek, dubbel, ongeldig e-mailadres) | 5 |
| A2 Onderhandeling | R7 | B | Grenswaarden (marge −1, 0, +1) | 4 |
| A4 Bezetting | R11 | B | Grenswaarden (49% en 50%; 56 en 57 dagen) | 4 |
| C3 Klanthistorie | R13 | C | Verkennend testen | 2 |

### Voorbeeld 1: grenswaarden compensatiepercentage (D2)

Klacht KL-3001, reissom € 1.320,00, richtlijn 4%. Geldig is 0 tot en met 100%. Wijkt het percentage af van 4%, dan is een toelichting verplicht.

| TC | Invoer | Verwacht resultaat | Status |
| --- | --- | --- | --- |
| D2-01 | −0,5% | Foutmelding onder het veld: percentage tussen 0 en 100 | Niet gestart |
| D2-02 | 0%, geen toelichting | Foutmelding: toelichting verplicht; bedrag € 0,00 | Niet gestart |
| D2-03 | 4%, geen toelichting | Voorstel ingediend; bedrag € 52,80; status Wacht op goedkeuring | Niet gestart |
| D2-04 | 4,5%, met toelichting | Voorstel ingediend; bedrag € 59,40 | Niet gestart |
| D2-05 | 100%, met toelichting | Voorstel ingediend; bedrag € 1.320,00 | Niet gestart |
| D2-06 | 100,5% | Foutmelding onder het veld: percentage tussen 0 en 100 | Niet gestart |

### Voorbeeld 2: beslistabel AVG-verwijdering (E2)

Testdatum 29 september 2026. Een streepje betekent: maakt niet uit.

| Conditie of actie | Regel 1 | Regel 2 | Regel 3 |
| --- | --- | --- | --- |
| Klant heeft een reis met terugkomst op of na vandaag | Ja | Nee | Nee |
| Bevestiging “VERWIJDEREN” correct getypt | – | Nee | Ja |
| **Verwijderen geblokkeerd, melding met terugkomdatum** | **X** | | |
| **Foutmelding onder het bevestigingsveld** | | **X** | |
| **Persoonsgegevens verwijderd, boekingen anoniem bewaard** | | | **X** |

Grenswaarden bij regel 1: terugkomst 29 sep (vandaag) moet blokkeren, terugkomst 28 sep moet verwijderen toestaan.

### Voorbeeld 3: toestandsovergangen klacht (D2)

| Van | Actie | Door | Naar |
| --- | --- | --- | --- |
| Nieuw | Voorstel indienen | Medewerker A | Wacht op goedkeuring |
| Wacht op goedkeuring | Goedkeuren | Medewerker B | Afgehandeld |
| Wacht op goedkeuring | Terugsturen | Medewerker B | In behandeling |
| Wacht op goedkeuring | Goedkeuren | Medewerker A (indiener) | Niet toegestaan: knop uitgeschakeld |
| Nieuw | Escaleren | Medewerker | Geëscaleerd (After Travel) |
| Nieuw | Ongegrond verklaren met onderbouwing | Medewerker | Ongegrond |

De vierde regel is de belangrijkste negatieve test: die bewijst het vier-ogenprincipe (R4).

## 6. Testproces in Azure DevOps

Alles wat we testen staat in Azure Test Plans en is gekoppeld aan een user story. Zo is voor elke story te zien wie wat heeft getest, wanneer, en met welk resultaat.

1. **Test plan per sprint.** Daarin een test suite per user story, gekoppeld aan het Product Backlog Item.
2. **Testgeval.** Titel met ID (bijv. D2-03), risico-ID in de tags (bijv. R3), stappen met invoer en verwacht resultaat, en de gebruikte techniek.
3. **Uitvoeren.** De tester voert het testgeval uit in de testrunner. DevOps legt status, tester en datum vast.
4. **Bevinding.** Een gefaald testgeval wordt een Bug, gekoppeld aan de story. De bug bevat de doorlopen stappen, het verwachte en het werkelijke resultaat, en een screenshot.
5. **Oplossen.** De bouwer beschrijft de oorzaak en de oplossing in de bug.
6. **Hertest door een ander.** Een teamlid dat de story niet heeft gebouwd, test opnieuw en sluit de bug. Dat is het vier-ogenprincipe.

**Entrycriteria: we beginnen met testen als**

- de user story acceptatiecriteria heeft die de opdrachtgever heeft gezien;
- de testgevallen in DevOps staan en een ander teamlid ze heeft gereviewd;
- de testdata klaarstaat (fictieve klanten, boekingen en leveranciers, zie het [prototype](../prototype/index.html)).

**Exitcriteria: een story is klaar voor de review als**

- alle testgevallen van klasse A en B zijn uitgevoerd;
- geen enkele bug met prioriteit 1 of 2 open staat;
- voor klasse A een tweede tester heeft afgetekend;
- de geautomatiseerde UI-test van het hoofdpad slaagt.

**Regressie.** Na elke wijziging aan D2, E2 of D1 draaien we de testgevallen van klasse A opnieuw. Het geautomatiseerde deel draait bij elke oplevering.

## 7. Open vragen voor de opdrachtgever

De antwoorden kunnen kans en impact van een risico veranderen. Daarom vragen we ze vóór de refinement van sprint 3.

- [ ] Binnen hoeveel uur moet een klacht met urgentie Hoog opgepakt zijn? (R5)
- [ ] Mag een compensatie hoger zijn dan de reissom, bijvoorbeeld bij een volledig mislukte reis? (R3)
- [ ] Hoe lang na thuiskomst moeten klantgegevens bewaard blijven voor klachten en verzekering? (R1)
- [ ] Wie mag een compensatievoorstel goedkeuren: elke collega, of alleen een senior? (R4)
- [ ] Welke bezettingsgrens en hoeveel weken vóór de periode moet de inkoper gewaarschuwd worden? Nu aangenomen: 50% en 8 weken. (R11)
