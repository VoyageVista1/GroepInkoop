# Migratie backlog: VoyageVista → GroepInkoop

Op 29 september 2026 zijn de issues van ons team uit [VoyageVista1/VoyageVista](https://github.com/VoyageVista1/VoyageVista/issues) overgezet naar [GroepInkoop](https://github.com/VoyageVista1/GroepInkoop/issues). **De issues in GroepInkoop zijn vanaf nu de backlog.**

## Correctie 30 september 2026

De issues van **Sales & Boekingen**, **IT & Innovatie** en de **hele klas** horen niet (alleen) bij ons team en waren per ongeluk meegekopieerd. De originelen in VoyageVista zijn weer geopend en de kopieën in GroepInkoop zijn gesloten (not planned):

| Team | VoyageVista (heropend) | GroepInkoop (gesloten) |
| --- | --- | --- |
| Sales & Boekingen | #4, #5–#10, #26, #67–#72 | #7, #8, #16–#26 |
| IT & Innovatie | #18–#25 | #10, #27–#33 |

| Hele klas (designsprint, standup) | #11–#17, #33–#36, #38–#45, #56, #57, #73, #74 | #1, #6, #9, #11–#15, #34–#47 |

In GroepInkoop blijven alleen de issues van Productontwikkeling & Inkoop en Klantenservice & Support open (epics #2–#5 met hun stories en taken).

## Wat er is gebeurd

| | Aantal |
| --- | --- |
| Issues in VoyageVista (open) | 154 |
| Overgezet (1-op-1 of samengevoegd) | 145 |
| Niet overgezet (test, leeg of dubbel) | 9 |
| Nieuw toegevoegd (interview en casus) | 10 |
| Nieuw als parent (ontbrak) | 1 |
| **Totaal in GroepInkoop** | **146** |

**Structuur.** Epic (type *Feature*, label *Epic*) → User Story (type *User Story*) → Taak (type *Task*), gekoppeld als sub-issues. Labels: afdeling (*Inkoop*, *Klantenservice*, *Algemeen*), fase (*Designsprint*, *Ontwerp*), MoSCoW (*Moet hebben*, *Zou moeten hebben*, *Kan hebben*, *Nu niet*), storypoints (*SP 2*, *SP 3*, *SP 5*) en *Nieuw (interview)*.

**Controle en verbeteringen**

- De 57 functionele stories die alleen een titel hadden, hebben nu een user story, acceptatiecriteria (Stel/Als/Dan), prioriteit, een voorstel voor storypoints, bron (casus/interview) en risico-ID.
- K1–K10 waren dubbel met functionele stories en zijn daarmee **samengevoegd** (zie tabel). K11 had geen tegenhanger en is een eigen story gebleven.
- **K10 is inhoudelijk aangepast.** “Automatisch verwijderen zodra de reis is afgerond” botst met het interview: gegevens moeten bewaard blijven tot de klant thuis is, en klachten komen vaak ná de reis. Nu: verwijderen op verzoek, geblokkeerd zolang de reis loopt; bewaartermijn is een open vraag.
- Voor Inkoop ontbrak een story voor use cases; die is toegevoegd als parent van “Use-casebeschrijvingen controleren” ([#49](https://github.com/VoyageVista1/GroepInkoop/issues/49)).
- Bij twee parent-stories (#48, #50) noemden de sub-issues 1–3 die nooit als issue bestonden; dat staat nu in de tekst vermeld.
- De standup-comments van sprint 2 staan nog in het oude issue VoyageVista#73.

## Niet overgezet

| Oud | Titel | Reden |
| --- | --- | --- |
| VoyageVista#1 | Example: Authentication | Voorbeeld-issue van GitHub |
| VoyageVista#26 | Registreren Boeking | Lege sjabloontekst (“Als ... wil ik..”) |
| VoyageVista#27 | Primairy Usecase | Geen inhoud (“dgs”) |
| VoyageVista#28 | Secundairy usecase | Geen inhoud |
| VoyageVista#29 | Test | Testissue |
| VoyageVista#30 | tyy | Testissue |
| VoyageVista#31 | yriryiy | Testissue |
| VoyageVista#32 | yretre | Testissue |
| VoyageVista#57 | Klantreis opstellen | Dubbel met #56 |

## Nieuwe stories uit interview en casus

- [#86](https://github.com/VoyageVista1/GroepInkoop/issues/86) Bezetting ingekochte kamers bewaken
- [#107](https://github.com/VoyageVista1/GroepInkoop/issues/107) Lage bezetting doorgeven aan Marketing en Sales
- [#108](https://github.com/VoyageVista1/GroepInkoop/issues/108) Vaste lijsten voor kamertypes en faciliteiten beheren
- [#109](https://github.com/VoyageVista1/GroepInkoop/issues/109) Annuleringsvoorwaarden gestructureerd vastleggen
- [#110](https://github.com/VoyageVista1/GroepInkoop/issues/110) Leveranciersbezoek plannen
- [#111](https://github.com/VoyageVista1/GroepInkoop/issues/111) Klantgesprekken automatisch vastleggen (Nu niet – onderzoek)
- [#143](https://github.com/VoyageVista1/GroepInkoop/issues/143) Leverancier inschakelen voor oplossing ter plaatse
- [#144](https://github.com/VoyageVista1/GroepInkoop/issues/144) Compensatierichtlijnen beheren
- [#145](https://github.com/VoyageVista1/GroepInkoop/issues/145) Voorlopige klant registreren (bijv. ongeboren baby)
- [#146](https://github.com/VoyageVista1/GroepInkoop/issues/146) Geen onterechte berichten naar een klant die al op reis is

## Oude nummers → nieuwe nummers

| VoyageVista | GroepInkoop |
| --- | --- |
| #74 | [#1](https://github.com/VoyageVista1/GroepInkoop/issues/1) Epic: Designsprint – analyse en basisontwerp |
| #75 | [#2](https://github.com/VoyageVista1/GroepInkoop/issues/2) Epic: Analyse en ontwerp Productontwikkeling & Inkoop |
| #78 | [#3](https://github.com/VoyageVista1/GroepInkoop/issues/3) Epic: Analyse en ontwerp Klantenservice & Support |
| #77 | [#4](https://github.com/VoyageVista1/GroepInkoop/issues/4) Epic: Functionele user stories Productontwikkeling & Inkoop |
| #79 | [#5](https://github.com/VoyageVista1/GroepInkoop/issues/5) Epic: Functionele user stories Klantenservice & Support |
| #73 | [#6](https://github.com/VoyageVista1/GroepInkoop/issues/6) Sprint 2 – Daily Standup Log |

### Epic Designsprint

| VoyageVista | GroepInkoop |
| --- | --- |
| #4 | [#7](https://github.com/VoyageVista1/GroepInkoop/issues/7) |
| #67 | [#8](https://github.com/VoyageVista1/GroepInkoop/issues/8) |
| #56 | [#9](https://github.com/VoyageVista1/GroepInkoop/issues/9) |
| #18 | [#10](https://github.com/VoyageVista1/GroepInkoop/issues/10) |
| #11 | [#11](https://github.com/VoyageVista1/GroepInkoop/issues/11) |
| #33 | [#12](https://github.com/VoyageVista1/GroepInkoop/issues/12) |
| #34 | [#13](https://github.com/VoyageVista1/GroepInkoop/issues/13) |
| #35 | [#14](https://github.com/VoyageVista1/GroepInkoop/issues/14) |
| #36 | [#15](https://github.com/VoyageVista1/GroepInkoop/issues/15) |
| #5 | [#16](https://github.com/VoyageVista1/GroepInkoop/issues/16) |
| #6 | [#17](https://github.com/VoyageVista1/GroepInkoop/issues/17) |
| #7 | [#18](https://github.com/VoyageVista1/GroepInkoop/issues/18) |
| #8 | [#19](https://github.com/VoyageVista1/GroepInkoop/issues/19) |
| #9 | [#20](https://github.com/VoyageVista1/GroepInkoop/issues/20) |
| #10 | [#21](https://github.com/VoyageVista1/GroepInkoop/issues/21) |
| #68 | [#22](https://github.com/VoyageVista1/GroepInkoop/issues/22) |
| #69 | [#23](https://github.com/VoyageVista1/GroepInkoop/issues/23) |
| #70 | [#24](https://github.com/VoyageVista1/GroepInkoop/issues/24) |
| #71 | [#25](https://github.com/VoyageVista1/GroepInkoop/issues/25) |
| #72 | [#26](https://github.com/VoyageVista1/GroepInkoop/issues/26) |
| #19 | [#27](https://github.com/VoyageVista1/GroepInkoop/issues/27) |
| #20 | [#28](https://github.com/VoyageVista1/GroepInkoop/issues/28) |
| #21 | [#29](https://github.com/VoyageVista1/GroepInkoop/issues/29) |
| #22 | [#30](https://github.com/VoyageVista1/GroepInkoop/issues/30) |
| #23 | [#31](https://github.com/VoyageVista1/GroepInkoop/issues/31) |
| #25 | [#32](https://github.com/VoyageVista1/GroepInkoop/issues/32) |
| #24 | [#33](https://github.com/VoyageVista1/GroepInkoop/issues/33) |
| #12 | [#34](https://github.com/VoyageVista1/GroepInkoop/issues/34) |
| #13 | [#35](https://github.com/VoyageVista1/GroepInkoop/issues/35) |
| #14 | [#36](https://github.com/VoyageVista1/GroepInkoop/issues/36) |
| #15 | [#37](https://github.com/VoyageVista1/GroepInkoop/issues/37) |
| #16 | [#38](https://github.com/VoyageVista1/GroepInkoop/issues/38) |
| #17 | [#39](https://github.com/VoyageVista1/GroepInkoop/issues/39) |
| #38 | [#40](https://github.com/VoyageVista1/GroepInkoop/issues/40) |
| #39 | [#41](https://github.com/VoyageVista1/GroepInkoop/issues/41) |
| #40 | [#42](https://github.com/VoyageVista1/GroepInkoop/issues/42) |
| #41 | [#43](https://github.com/VoyageVista1/GroepInkoop/issues/43) |
| #42 | [#44](https://github.com/VoyageVista1/GroepInkoop/issues/44) |
| #43 | [#45](https://github.com/VoyageVista1/GroepInkoop/issues/45) |
| #44 | [#46](https://github.com/VoyageVista1/GroepInkoop/issues/46) |
| #45 | [#47](https://github.com/VoyageVista1/GroepInkoop/issues/47) |

### Epic Analyse en ontwerp Productontwikkeling & Inkoop

| VoyageVista | GroepInkoop |
| --- | --- |
| #76 | [#48](https://github.com/VoyageVista1/GroepInkoop/issues/48) |
| — (nieuw) | [#49](https://github.com/VoyageVista1/GroepInkoop/issues/49) |
| #97 | [#50](https://github.com/VoyageVista1/GroepInkoop/issues/50) |
| #102 | [#51](https://github.com/VoyageVista1/GroepInkoop/issues/51) |
| #107 | [#52](https://github.com/VoyageVista1/GroepInkoop/issues/52) |
| #111 | [#53](https://github.com/VoyageVista1/GroepInkoop/issues/53) |
| #112 | [#54](https://github.com/VoyageVista1/GroepInkoop/issues/54) |
| #113 | [#55](https://github.com/VoyageVista1/GroepInkoop/issues/55) |
| #114 | [#56](https://github.com/VoyageVista1/GroepInkoop/issues/56) |
| #116 | [#57](https://github.com/VoyageVista1/GroepInkoop/issues/57) |
| #117 | [#58](https://github.com/VoyageVista1/GroepInkoop/issues/58) |
| #83 | [#59](https://github.com/VoyageVista1/GroepInkoop/issues/59) |
| #96 | [#60](https://github.com/VoyageVista1/GroepInkoop/issues/60) |
| #101 | [#61](https://github.com/VoyageVista1/GroepInkoop/issues/61) |
| #103 | [#62](https://github.com/VoyageVista1/GroepInkoop/issues/62) |
| #104 | [#63](https://github.com/VoyageVista1/GroepInkoop/issues/63) |
| #105 | [#64](https://github.com/VoyageVista1/GroepInkoop/issues/64) |
| #106 | [#65](https://github.com/VoyageVista1/GroepInkoop/issues/65) |
| #108 | [#66](https://github.com/VoyageVista1/GroepInkoop/issues/66) |
| #109 | [#67](https://github.com/VoyageVista1/GroepInkoop/issues/67) |
| #110 | [#68](https://github.com/VoyageVista1/GroepInkoop/issues/68) |

### Epic Analyse en ontwerp Klantenservice & Support

| VoyageVista | GroepInkoop |
| --- | --- |
| #149 | [#69](https://github.com/VoyageVista1/GroepInkoop/issues/69) |
| #150 | [#70](https://github.com/VoyageVista1/GroepInkoop/issues/70) |
| #151 | [#71](https://github.com/VoyageVista1/GroepInkoop/issues/71) |
| #152 | [#72](https://github.com/VoyageVista1/GroepInkoop/issues/72) |
| #153 | [#73](https://github.com/VoyageVista1/GroepInkoop/issues/73) |
| #154 | [#74](https://github.com/VoyageVista1/GroepInkoop/issues/74) |
| #155 | [#75](https://github.com/VoyageVista1/GroepInkoop/issues/75) |
| #156 | [#76](https://github.com/VoyageVista1/GroepInkoop/issues/76) |
| #157 | [#77](https://github.com/VoyageVista1/GroepInkoop/issues/77) |
| #158 | [#78](https://github.com/VoyageVista1/GroepInkoop/issues/78) |
| #159 | [#79](https://github.com/VoyageVista1/GroepInkoop/issues/79) |
| #160 | [#80](https://github.com/VoyageVista1/GroepInkoop/issues/80) |
| #161 | [#81](https://github.com/VoyageVista1/GroepInkoop/issues/81) |

### Epic Functionele user stories Productontwikkeling & Inkoop

| VoyageVista | GroepInkoop |
| --- | --- |
| #125 | [#82](https://github.com/VoyageVista1/GroepInkoop/issues/82) |
| #129 | [#83](https://github.com/VoyageVista1/GroepInkoop/issues/83) |
| #131 | [#84](https://github.com/VoyageVista1/GroepInkoop/issues/84) |
| #132 | [#85](https://github.com/VoyageVista1/GroepInkoop/issues/85) |
| — (nieuw) | [#86](https://github.com/VoyageVista1/GroepInkoop/issues/86) |
| #126 | [#87](https://github.com/VoyageVista1/GroepInkoop/issues/87) |
| #127 | [#88](https://github.com/VoyageVista1/GroepInkoop/issues/88) |
| #128 | [#89](https://github.com/VoyageVista1/GroepInkoop/issues/89) |
| #130 | [#90](https://github.com/VoyageVista1/GroepInkoop/issues/90) |
| #133 | [#91](https://github.com/VoyageVista1/GroepInkoop/issues/91) |
| #134 | [#92](https://github.com/VoyageVista1/GroepInkoop/issues/92) |
| #135 | [#93](https://github.com/VoyageVista1/GroepInkoop/issues/93) |
| #136 | [#94](https://github.com/VoyageVista1/GroepInkoop/issues/94) |
| #137 | [#95](https://github.com/VoyageVista1/GroepInkoop/issues/95) |
| #138 | [#96](https://github.com/VoyageVista1/GroepInkoop/issues/96) |
| #139 | [#97](https://github.com/VoyageVista1/GroepInkoop/issues/97) |
| #140 | [#98](https://github.com/VoyageVista1/GroepInkoop/issues/98) |
| #141 | [#99](https://github.com/VoyageVista1/GroepInkoop/issues/99) |
| #142 | [#100](https://github.com/VoyageVista1/GroepInkoop/issues/100) |
| #143 | [#101](https://github.com/VoyageVista1/GroepInkoop/issues/101) |
| #144 | [#102](https://github.com/VoyageVista1/GroepInkoop/issues/102) |
| #145 | [#103](https://github.com/VoyageVista1/GroepInkoop/issues/103) |
| #146 | [#104](https://github.com/VoyageVista1/GroepInkoop/issues/104) |
| #147 | [#105](https://github.com/VoyageVista1/GroepInkoop/issues/105) |
| #148 | [#106](https://github.com/VoyageVista1/GroepInkoop/issues/106) |
| — (nieuw) | [#107](https://github.com/VoyageVista1/GroepInkoop/issues/107) |
| — (nieuw) | [#108](https://github.com/VoyageVista1/GroepInkoop/issues/108) |
| — (nieuw) | [#109](https://github.com/VoyageVista1/GroepInkoop/issues/109) |
| — (nieuw) | [#110](https://github.com/VoyageVista1/GroepInkoop/issues/110) |

### Epic Functionele user stories Klantenservice & Support

| VoyageVista | GroepInkoop |
| --- | --- |
| — (nieuw) | [#111](https://github.com/VoyageVista1/GroepInkoop/issues/111) |
| #162 | [#112](https://github.com/VoyageVista1/GroepInkoop/issues/112) |
| #163 | [#113](https://github.com/VoyageVista1/GroepInkoop/issues/113) |
| #164 | [#114](https://github.com/VoyageVista1/GroepInkoop/issues/114) |
| #166 | [#115](https://github.com/VoyageVista1/GroepInkoop/issues/115) |
| #167 | [#116](https://github.com/VoyageVista1/GroepInkoop/issues/116) |
| #168 | [#117](https://github.com/VoyageVista1/GroepInkoop/issues/117) |
| #169 | [#118](https://github.com/VoyageVista1/GroepInkoop/issues/118) |
| #170 | [#119](https://github.com/VoyageVista1/GroepInkoop/issues/119) |
| #172 + #118 (K2) | [#120](https://github.com/VoyageVista1/GroepInkoop/issues/120) |
| #173 + #115 (K1) | [#121](https://github.com/VoyageVista1/GroepInkoop/issues/121) |
| #174 | [#122](https://github.com/VoyageVista1/GroepInkoop/issues/122) |
| #175 | [#123](https://github.com/VoyageVista1/GroepInkoop/issues/123) |
| #176 + #119 (K3) | [#124](https://github.com/VoyageVista1/GroepInkoop/issues/124) |
| #178 | [#125](https://github.com/VoyageVista1/GroepInkoop/issues/125) |
| #179 + #120 (K4) | [#126](https://github.com/VoyageVista1/GroepInkoop/issues/126) |
| #180 + #121 (K5) | [#127](https://github.com/VoyageVista1/GroepInkoop/issues/127) |
| #181 | [#128](https://github.com/VoyageVista1/GroepInkoop/issues/128) |
| #182 | [#129](https://github.com/VoyageVista1/GroepInkoop/issues/129) |
| #183 + #122 (K6) | [#130](https://github.com/VoyageVista1/GroepInkoop/issues/130) |
| #184 + #123 (K7) | [#131](https://github.com/VoyageVista1/GroepInkoop/issues/131) |
| #185 + #124 (K8) | [#132](https://github.com/VoyageVista1/GroepInkoop/issues/132) |
| #186 | [#133](https://github.com/VoyageVista1/GroepInkoop/issues/133) |
| #187 | [#134](https://github.com/VoyageVista1/GroepInkoop/issues/134) |
| #188 | [#135](https://github.com/VoyageVista1/GroepInkoop/issues/135) |
| #189 | [#136](https://github.com/VoyageVista1/GroepInkoop/issues/136) |
| #190 | [#137](https://github.com/VoyageVista1/GroepInkoop/issues/137) |
| #191 | [#138](https://github.com/VoyageVista1/GroepInkoop/issues/138) |
| #192 + #171 (K10) | [#139](https://github.com/VoyageVista1/GroepInkoop/issues/139) |
| #193 + #165 (K9) | [#140](https://github.com/VoyageVista1/GroepInkoop/issues/140) |
| #194 | [#141](https://github.com/VoyageVista1/GroepInkoop/issues/141) |
| #177 (K11) | [#142](https://github.com/VoyageVista1/GroepInkoop/issues/142) |
| — (nieuw) | [#143](https://github.com/VoyageVista1/GroepInkoop/issues/143) |
| — (nieuw) | [#144](https://github.com/VoyageVista1/GroepInkoop/issues/144) |
| — (nieuw) | [#145](https://github.com/VoyageVista1/GroepInkoop/issues/145) |
| — (nieuw) | [#146](https://github.com/VoyageVista1/GroepInkoop/issues/146) |

## Stories uit `inkoop-product-backlog.md` (IN-xx)

| IN | Issue |
| --- | --- |
| IN-00 | [#51](https://github.com/VoyageVista1/GroepInkoop/issues/51) |
| IN-01, IN-02, IN-03 | [#93](https://github.com/VoyageVista1/GroepInkoop/issues/93) |
| IN-04 | [#97](https://github.com/VoyageVista1/GroepInkoop/issues/97) |
| IN-05 | [#96](https://github.com/VoyageVista1/GroepInkoop/issues/96) |
| IN-06 | [#110](https://github.com/VoyageVista1/GroepInkoop/issues/110) |
| IN-07 | [#98](https://github.com/VoyageVista1/GroepInkoop/issues/98) |
| IN-08 | [#109](https://github.com/VoyageVista1/GroepInkoop/issues/109) |
| IN-09 | [#99](https://github.com/VoyageVista1/GroepInkoop/issues/99) |
| IN-11 | [#86](https://github.com/VoyageVista1/GroepInkoop/issues/86) |
| IN-12 | [#107](https://github.com/VoyageVista1/GroepInkoop/issues/107) |
| IN-13 | [#85](https://github.com/VoyageVista1/GroepInkoop/issues/85) |
| IN-14 | [#108](https://github.com/VoyageVista1/GroepInkoop/issues/108) |
| IN-15 | [#100](https://github.com/VoyageVista1/GroepInkoop/issues/100) |
| IN-16 | [#105](https://github.com/VoyageVista1/GroepInkoop/issues/105) |
| IN-17 | [#84](https://github.com/VoyageVista1/GroepInkoop/issues/84) |
| IN-10 (contract laten goedkeuren, Kan hebben) | nog niet als issue; kan worden toegevoegd na antwoord van de opdrachtgever |

## Nog te doen

- [ ] Originele issues in VoyageVista sluiten met een link naar GroepInkoop (zodat er geen dubbele backlog is).
- [ ] Een GitHub Project-bord maken voor GroepInkoop en de issues toevoegen (kolommen *Backlog*, *Sprint*, *In progress*, *Review/Test*, *Done*; veld *Iteration* voor sprints).
- [ ] Storypoints samen schatten met planning poker; de huidige waarden zijn een voorstel.
- [ ] Open vragen uit de stories bundelen en aan de opdrachtgever voorleggen.
