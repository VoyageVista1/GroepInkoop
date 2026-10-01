# Opschoonlijst FigJam-board “Project Agile Board”

Gevonden bij de controle van 30 september 2026. Afvinken als het is aangepast.

## Tikfouten

| Waar | Staat er | Moet zijn |
| --- | --- | --- |
| User flow UC7 en UC8 | Leveranciersdasboard | Leveranciersdashboard |
| User flow UC5 | Leverancier selectereb | Leverancier selecteren |
| User flow UC9 (titel) | CONTRACTVERVALDATUM BEWAGEN | CONTRACTVERVALDATUM BEWAKEN |
| User flows UC2–UC6 | Zoekfilterstoepassen? | Zoekfilters toepassen? |
| Primair diagram Inkoop | Onderhandelingbijwerken | Onderhandeling bijwerken |
| Secundair diagram Inkoop (contract) | Inkopere | Inkoper |
| Secundair diagram K&S | Klantenserive medewerker (4×) | Klantenservicemedewerker |
| Secundair diagram K&S | «incldue» | «include» |
| Secundair diagram K&S | «Include» (zonder >) | «include» |
| Secundair diagram K&S | extend (2×, zonder « ») | «extend» |
| Primair diagram K&S | Klant geschiedenis raadplagen | Klantgeschiedenis raadplegen |
| Secundair diagram K&S | Doorzetten naar andere afdelng | Doorzetten naar andere afdeling |
| Beschrijving UC9 | Systeem controleert der vervaldatums | Het systeem controleert de vervaldatums |
| Beschrijving UC8/UC9 | minsten | minstens |
| Beschrijving UC8 | eindatum | einddatum |

## Dubbele of losse blokken

- [ ] User flow UC5: los blokje “SS” verwijderen.
- [ ] User flow UC9: “Verlengen kiezen” staat 2× — één weghalen.
- [ ] Secundair diagram K&S: dubbel “Klant koppelen aan bestaande zaak”, “Raadplegen interne collega”, “Klacht sluiten”, “Ophalen Klachten/feedback” — telkens één weghalen en de lijnen aan de overgebleven koppelen.
- [ ] “Kopie Work Area”: twee extra versies van het primaire diagram Inkoop — één versie kiezen, de rest verwijderen.
- [ ] Lege sectie “Section 1” verwijderen.
- [ ] Retrospective: lege stickies (“Frame 7” t/m “Frame 14”) invullen of verwijderen.
- [ ] ERD-sectie: `sqlite_master` en `sqlite_sequence` zijn systeemtabellen; conceptueel ERD (`erd-conceptueel.png`) ervoor in de plaats zetten, het fysieke schema als bijlage.

## Consistentie

- [ ] Use cases heten **UC01–UC09** (niet US01); user story apart vermelden.
- [ ] Zelfde naam in diagram, beschrijving en user flow (bijv. “Nieuw reisproduct aanmaken”, “Contract vastleggen”).
- [ ] Primaire actor UC01–UC03: Productmedewerker / Productmanager in plaats van Inkoper.
- [ ] Hoofdscenario’s nummeren; alternatieve scenario’s verwijzen naar een stapnummer (bijv. “9a”).
- [ ] UC02 postconditie: “bestaand reisproduct is bijgewerkt” (niet “nieuw toegevoegd”).
- [ ] UC04: preconditie “status is Nieuw” weghalen; één keer opslaan; “leverancier koppelen” weghalen.
- [ ] UC09: preconditie “contract dat bijna afloopt” weghalen (botst met alternatief “geen contracten”).
- [ ] Literatuurlijst: eerste bron in APA-stijl (auteur, jaar, titel, uitgever) in plaats van alleen een URL.
