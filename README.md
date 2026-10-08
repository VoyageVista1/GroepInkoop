# GroepInkoop – VoyageVista

Repository van **Groep 3: Inkoop & Klantenservice** voor de casus VoyageVista. We ontwerpen en bouwen de onderdelen **Productontwikkeling & Inkoop** en **Klantenservice & Support**.

## Team

| Rol | Naam |
| --- | --- |
| Product Owner | Jared |
| Scrum Master | Khodor |
| Ontwikkelteam | Brett, Yaro, Elia |

## Waar staat wat

| Wat | Waar |
| --- | --- |
| Backlog (epics, user stories, taken) | [Issues](https://github.com/VoyageVista1/GroepInkoop/issues) |
| Sprintbord (status, sprint, schatting) | GitHub-project [Groep 3 Inkoop & Klantenservice](https://github.com/orgs/VoyageVista1/projects/12) |
| Use cases, user flows, BPMN, sprintchecklist | FigJam: [Project Agile Board](https://www.figma.com/board/ManUSFsMrVgktm6UwReajA/Project-Agile-Board) (uitleg in [docs/figma-board.md](docs/figma-board.md)) |
| Documentatie | [docs/](docs) (zie hieronder) |

## Backlog in GitHub

Opbouw: epic → user story → taak, gekoppeld als sub-issues.

| Epic | Inhoud | Stories |
| --- | --- | --- |
| [#2](https://github.com/VoyageVista1/GroepInkoop/issues/2) Analyse en ontwerp Productontwikkeling & Inkoop | scope, use cases, user flows, datamodel, BPMN, UX, wireframes, BIV/AO | #48–#53, #165, #299 |
| [#3](https://github.com/VoyageVista1/GroepInkoop/issues/3) Analyse en ontwerp Klantenservice & Support | idem voor Klantenservice | #69, #70, #73–#76, #168, #301 |
| [#4](https://github.com/VoyageVista1/GroepInkoop/issues/4) Functionele user stories Productontwikkeling & Inkoop | wat de applicatie moet kunnen | #189–#198 en #212–#226 |
| [#5](https://github.com/VoyageVista1/GroepInkoop/issues/5) Functionele user stories Klantenservice & Support | wat de applicatie moet kunnen | #199–#211 |

Elke use case op het board verwijst in het veld **Nummer** naar zijn user stories:

| Use case | User stories | Use case | User stories |
| --- | --- | --- | --- |
| UC01 Nieuw reisproduct ontwikkelen | #190, #191, #192 | UC-K01 t/m UC-K13 | #199 t/m #211 (één story per use case) |
| UC02 Onderhandeling opvolgen | #213, #214, #215 | | |
| UC03 Bestaand reisproduct bijwerken | #193 | | |
| UC04 Productontwikkeling plannen en volgen | #223, #224, #225 | | |
| UC05 Leverancierscontract beheren | #216–#219 | | |
| UC06 Leveranciersrelatie beheren | #194–#198 | | |
| UC07 Leveranciersaanbod vastleggen | #212 | | |
| UC08 Contractverplichtingen bewaken | #220, #221, #222 | | |
| UC09 Productgegevens beschikbaar stellen | #226 | | |
| UC10 Productkans onderzoeken | #189 | | |

De oudere stories #82–#146 (van vóór de refinement) hangen niet meer onder een epic en zijn vervangen door de stories hierboven.

## Mappen

```
docs/
├── backlog/      productbacklog Inkoop (IN-00 t/m IN-17, DoR, DoD, releaseplanning), migratie-overzicht
├── ontwerp/      use cases Klantenservice (UC-K01 t/m UC-K13), conceptueel ERD, opschoonlijst FigJam
├── proces/       BPMN Klantenservice (.bpmn, .svg, .html) en het script dat ze maakt (gen_bpmn.py)
├── figma-board.md                         overzicht van het FigJam-board
├── interview-analyse.md                   bevindingen uit het interview met de opdrachtgever
└── productrisicoanalyse-teststrategie.md  productrisico's en teststrategie
prototype/        klikbaar HTML-prototype (index.html)
```

De BPMN opnieuw maken: `python3 docs/proces/gen_bpmn.py`.
