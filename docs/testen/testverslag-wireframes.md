# Testverslag wireframes – klikbaar eindmodel

Testobject: `prototype/werkplek-v2.html` · testdatum 29 oktober 2026 · ook op het FigJam-board in de sectie "Testverslag wireframes – klikbaar eindmodel".

**Resultaat:** 44 testgevallen, 44 geslaagd. Regressietest: 156 knoppen voor alle 8 rollen zonder fouten.

Het script `testscript-wireframes.js` voert alle testgevallen uit in Chromium (Playwright). Screenshots staan in `bewijs/`.

## Productontwikkeling & Inkoop

| ID | Issue | Testgeval | Rol | Stappen | Verwacht | Werkelijk | Status |
|---|---|---|---|---|---|---|---|
| I-01 | #161 | Productkans zonder verplichte velden | Productontwikkelaar | Nieuwe productkans → leeg opslaan | Opslaan geweigerd, verplichte velden rood met uitleg | 1 veld rood gemarkeerd: "Vul omschrijving in." | Geslaagd ([bewijs](bewijs/I-01.png)) |
| I-02 | #161 | Productkans opslaan | Productontwikkelaar | Velden invullen → Opslaan | Kans krijgt automatisch ID, datum en maker; melding "opgeslagen" | Productkans PK-0014 opgeslagen; detailpagina van PK-0014 geopend | Geslaagd |
| I-03 | #161 | Kansrijke kans doorzetten | Productontwikkelaar | PK-0013 openen → Doorzetten naar reisproduct | Nieuw reisproduct gekoppeld aan de kans | Reisproduct RP-0143 aangemaakt vanuit PK-0013; kans toont "Doorgezet naar" | Geslaagd |
| I-04 | #161 | Zoeken en filteren | Productontwikkelaar | Zoeken op "Madeira", daarna filter conclusie Niet kansrijk | Alleen passende kansen zichtbaar | Madeira: 1 resultaat · Niet kansrijk: 1 resultaat | Geslaagd |
| I-05 | #227 | Reisproduct zonder verplichte velden | Productontwikkelaar | Nieuw reisproduct → leeg opslaan | Opslaan geweigerd met foutmeldingen per veld | 2 velden rood gemarkeerd | Geslaagd |
| I-06 | #227 | Reisproduct aanmaken | Productontwikkelaar | Basisgegevens invullen → Opslaan | Status Concept, versie 1, door naar reisonderdelen | RP-0144 opgeslagen (versie 1); status Concept | Geslaagd |
| I-07 | #227 | Versieconflict bij gelijktijdig bewerken | Productontwikkelaar | RP-0142 wijzigen terwijl Jeroen het ook wijzigt → Opslaan | Waarschuwing en opslaan geblokkeerd tot nieuwste versie geladen is | Niet opgeslagen: Jeroen Bakker heeft dit reisproduct gewijzigd nadat jij het opende (nu versie 4). Herlaad eerst de nieuwste versie, zodat je zijn wijziging niet overschrijft. | Geslaagd ([bewijs](bewijs/I-07.png)) |
| I-08 | #228 | Reisonderdeel toevoegen | Productontwikkelaar | RP-0142 → Reisonderdelen & route → Reisonderdeel → invullen → Opslaan | Onderdeel staat in de route, nummering past zich aan | 6 → 7 onderdelen · Reisonderdeel toegevoegd | Geslaagd |
| I-09 | #228 | Dubbele waarde in vaste lijst | Inkoper | Reisonderdelen → Kamertypes → Waarde toevoegen "tweepersoonskamer" | Geweigerd: waarde bestaat al (ook met andere schrijfwijze) | Opslaan is niet gelukt: controleer het gemarkeerde veld. Deze waarde bestaat al in de lijst Kamertypes. | Geslaagd ([bewijs](bewijs/I-09.png)) |
| I-10 | #228 | Waarde in gebruik verwijderen | Inkoper | Kamertypes → waarde die in reisonderdelen gebruikt wordt | Geen knop Verwijderen, alleen Inactief zetten | 2 waarden in gebruik, geen enkele met Verwijderen | Geslaagd |
| I-11 | #229 | Leverancier zonder verplichte velden | Inkoper | Nieuwe leverancier → leeg opslaan | Opslaan geweigerd met foutmeldingen | 2 velden rood gemarkeerd | Geslaagd |
| I-12 | #229 | Dubbele leverancier | Inkoper | Nieuwe leverancier "Hotel Aegean Blue" invullen → Opslaan | Waarschuwing mogelijk dubbele leverancier | Controleer eerst of dit geen dubbele leverancier is. Klik nogmaals op Opslaan als het echt een nieuwe leverancier is. | Geslaagd ([bewijs](bewijs/I-12.png)) |
| I-13 | #229 | Contactmoment vastleggen | Inkoper | LV-0045 → Contactmoment → invullen → Opslaan | Contactmoment in de lijst met datum en medewerker | Contactmoment vastgelegd | Geslaagd |
| I-14 | #230 | Marge live berekenen | Inkoper | ON-0027 bijwerken → inkoopprijs wijzigen | Marge rekent direct mee | 28.8% (berekend) → 23.7% (berekend) | Geslaagd ([bewijs](bewijs/I-14.png)) |
| I-15 | #230 | Afsluiten met open vervolgacties | Inkoper | ON-0027 → Afsluiten terwijl acties open staan | Afsluiten geblokkeerd met uitleg | Afsluiten kan niet: er staat nog 1 vervolgactie open. Rond eerst alle vervolgacties af. | Geslaagd ([bewijs](bewijs/I-15.png)) |
| I-16 | #230 | Afsluiten met akkoord → contract | Inkoper | Acties afronden → Afsluiten → Akkoord | Contractformulier opent met leverancier en prijs ingevuld | Contractformulier geopend vanuit ON-0027, leverancier "Hotel Aegean Blue" al ingevuld | Geslaagd |
| I-17 | #231 | Einddatum vóór startdatum | Inkoper | Nieuw contract → einddatum vóór startdatum | Geweigerd: einddatum moet na de startdatum liggen | Opslaan is niet gelukt: controleer de einddatum. De einddatum ligt vóór de startdatum. | Geslaagd ([bewijs](bewijs/I-17.png)) |
| I-18 | #231 | Lage bezetting doorgeven | Inkoper → Sales | CT-0087 → Lage bezetting doorgeven → Versturen; daarna als Sales Meldingen openen | Melding komt bij Sales binnen | Verstuurd aan Marketing en Sales · Sales ziet 2 meldingen (was 1) | Geslaagd ([bewijs](bewijs/I-18.png)) |
| I-19 | #231 | Signaal aflopend contract | Inkoper | Contractenoverzicht openen | Contracten binnen 90 dagen gemarkeerd als "Loopt af" | 3× "Loopt af binnen 90 dagen" | Geslaagd |
| I-20 | #232 | Mijlpaal toevoegen | Productontwikkelaar | RP-0142 → Planning → Mijlpaal → invullen → Opslaan | Mijlpaal in de planning met deadline en status | 5 → 6 mijlpalen | Geslaagd |
| I-21 | #232 | Voortgangsstatus berekend | Inkoper | Planning openen | Statussen Op schema / Risico / Achterstand zichtbaar | Op schema, Risico, Achterstand | Geslaagd ([bewijs](bewijs/I-21.png)) |
| I-22 | #233 | Alleen gepubliceerde producten | Sales | Catalogus openen | Alleen status Gepubliceerd zichtbaar | 5 kaarten = 5 gepubliceerde reisproducten | Geslaagd ([bewijs](bewijs/I-22.png)) |
| I-23 | #233 | Prijzen per afdeling | Sales / Marketing | Hetzelfde product openen als Sales en als Marketing | Sales ziet prijzen per periode, Marketing niet; inkoopprijs voor geen van beiden | Sales: 3 prijsregels · Marketing: 0 prijsregels, melding "niet zichtbaar voor jouw afdeling" | Geslaagd ([bewijs](bewijs/I-23.png)) |
| I-24 | #233 | Feedback aan Inkoop | Sales | Product → Feedback aan Inkoop → Versturen | Feedback opgeslagen en bevestigd | Feedback verstuurd naar Inkoop | Geslaagd |

## Klantenservice & Support

| ID | Issue | Testgeval | Rol | Stappen | Verwacht | Werkelijk | Status |
|---|---|---|---|---|---|---|---|
| K-01 | #186 | Klant zoeken | Klantenservice | Zoeken op "jansen", e-mail en boekingsnummer | Passende klanten gevonden | jansen: 3 · anna.jansen@mail.nl: 1 · BK-54820: 1 | Geslaagd ([bewijs](bewijs/K-01.png)) |
| K-02 | #186 | Geen resultaat | Klantenservice | Zoeken op onbekende naam | Melding geen klant gevonden + knop nieuwe klant | Geen klant gevonden voor "Onbekendnaam" | Geslaagd |
| K-03 | #186 | Nieuwe klant met IBAN | Klantenservice | Nieuwe klant → IBAN in een veld → Opslaan | Opslaan geblokkeerd: IBAN mag niet worden opgeslagen | Niet opgeslagen: de invoer bevat een IBAN. VoyageVista bewaart geen IBAN- of paspoortnummers (AVG). | Geslaagd |
| K-04 | #234 | Contact registreren met IBAN | Klantenservice | KL-20931 → Contact registreren → IBAN in samenvatting → Opslaan | Geblokkeerd met uitleg wat je moet aanpassen | Niet opgeslagen: de invoer bevat een IBAN. VoyageVista bewaart geen IBAN- of paspoortnummers (AVG). | Geslaagd ([bewijs](bewijs/K-04.png)) |
| K-05 | #234 | Klant op reis → urgentie Hoog | Klantenservice | KL-20931 (op reis) → Contact registreren → Opslaan | Nieuwe zaak met urgentie Hoog | Zaak KZ-1044 aangemaakt met urgentie Hoog | Geslaagd |
| K-06 | #235 | Zaak toewijzen | Teamleider | Werkvoorraad → KZ-1043 Toewijzen → behandelaar kiezen | Zaak verschijnt bij de behandelaar | KZ-1043 toegewezen aan Fatima el Amrani | Geslaagd ([bewijs](bewijs/K-06.png)) |
| K-07 | #235 | Reactietermijn bewaakt | Klantenservice | Mijn werkvoorraad openen | Melding voor zaken over de termijn (48 u klacht / 24 u vraag) | Melding: KZ-1037 (1 dag te laat). De norm is 48 uur voor een klacht en 24 uur voor een vraag of wijziging. | Geslaagd |
| K-08 | #236 | Antwoord met sjabloon | Klantenservice | KZ-1041 → sjabloon "Transfer niet aanwezig" | Antwoordveld gevuld met sjabloontekst | Antwoordveld gevuld: "Beste Peter, De chauffeur van de transfer wacht bij de uitgang met een bordje "V…" | Geslaagd |
| K-09 | #236 | Afsluiten met open vervolgactie | Klantenservice | KZ-1041 → vervolgactie toevoegen → Afsluiten | Afsluiten geblokkeerd tot de actie klaar is | Afsluiten kan niet met open vervolgacties | Geslaagd |
| K-10 | #237 | Klacht beoordelen | Klantenservice | KZ-1043 → Klacht beoordelen → Gegrond + onderbouwing | Beoordeling vastgelegd, volgende stap compensatievoorstel | Klacht beoordeeld: Gegrond | Geslaagd |
| K-11 | #237 | Bezwaar naar After Travel | After Travel | Als After Travel KZ-0994 openen | Eindbesluit-formulier zichtbaar voor After Travel | Dashboard toont bezwaren; formulier Eindbesluit zichtbaar | Geslaagd |
| K-12 | #238 | Compensatie buiten richtlijn | Klantenservice | KZ-1037 → voorstel 40% zonder motivatie → Indienen | Geweigerd: buiten de richtlijn (5–15%) | Opslaan is niet gelukt: controleer het gemarkeerde veld. Valt buiten de richtlijn (5–15%). Pas het aan of vink aan dat je het bewust zo indient. | Geslaagd ([bewijs](bewijs/K-12.png)) |
| K-13 | #238 | Voorstel indienen | Klantenservice | KZ-1037 → voorstel 10% → Indienen | Status "Te controleren" bij een senior | Voorstel ingediend · een tweede medewerker moet het controleren | Geslaagd |
| K-14 | #238 | Vier-ogenprincipe | Klantenservice | Als Fatima KZ-1022 controleren | Knop Goedkeuren uitgeschakeld met uitleg | Alleen een senior medewerker kan compensatievoorstellen goedkeuren. Wissel naar de rol Senior om te beoordelen. | Geslaagd ([bewijs](bewijs/K-14.png)) |
| K-15 | #238 | Afwijzen zonder reden | Senior | Als Ingrid KZ-1022 → Afwijzen → leeg | Geweigerd: reden is verplicht | Opslaan is niet gelukt: controleer het gemarkeerde veld. Een reden is verplicht bij afwijzen. | Geslaagd |
| K-16 | #238 | Goedkeuren door senior | Senior | Als Ingrid KZ-1022 → Goedkeuren | Voorstel goedgekeurd | Voorstel goedgekeurd · de behandelaar informeert de klant | Geslaagd |
| K-17 | #239 | Verbeteractie aanmaken | Teamleider | Analyse → Verbeteractie → invullen → Aanmaken | Actie in de lijst en doorgestuurd naar de afdeling | Verbeteractie aangemaakt en naar Productontwikkeling & Inkoop gestuurd | Geslaagd ([bewijs](bewijs/K-17.png)) |
| K-18 | #239 | Periodes vergelijken | Teamleider | Analyse → Periodes vergelijken | Q2 en Q3 naast elkaar met verschil | Q2 en Q3 naast elkaar zichtbaar | Geslaagd |
| K-19 | #240 | Verwijderen tijdens reis | Klantenservice | KL-20931 (op reis) → Privacy | Anonimiseren geblokkeerd: klant is op reis | Verwijderen kan nu niet: de klant is op reis tot 4 nov 2026. De gegevens zijn nodig bij calamiteiten. | Geslaagd ([bewijs](bewijs/K-19.png)) |
| K-20 | #240 | Gegevens anonimiseren | Klantenservice | KL-18842 → Privacy → Gegevens anonimiseren → bevestigen | Gegevens geanonimiseerd en vastgelegd in het logboek | Gegevens geanonimiseerd; logboek bijgewerkt | Geslaagd |
