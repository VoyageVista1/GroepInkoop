# Use cases Klantenservice & Support

Beschrijvingen en user flows bij het use-casediagram Klantenservice op het FigJam-board ([Project Agile Board](https://www.figma.com/board/ManUSFsMrVgktm6UwReajA/Project-Agile-Board)). Deze tekst is gelijk aan de beschrijvingstabellen op het board. Nummering: **UC-K01 t/m UC-K13**. Elke use case hoort bij één user story uit epic #5 (#199 t/m #211).

Actoren: **Klantenservicemedewerker** (ook shopmedewerker), **Manager** (teamleider klantenservice), **Senior medewerker** (tweede beoordelaar), **After Travel** (eindbesluit bij bezwaar), **Systeem**, **Klant** (secundair).

| Use case | Naam | User story |
| --- | --- | --- |
| [UC-K01](#uc-k01-klant-en-boeking-opzoeken) | Klant en boeking opzoeken | #199 |
| [UC-K02](#uc-k02-klantcontact-registreren) | Klantcontact registreren | #200 |
| [UC-K03](#uc-k03-klantdossier-en-contactgeschiedenis-raadplegen) | Klantdossier en contactgeschiedenis raadplegen | #201 |
| [UC-K04](#uc-k04-klantzaak-beheren) | Klantzaak beheren | #202 |
| [UC-K05](#uc-k05-klantzaken-prioriteren-en-toewijzen) | Klantzaken prioriteren en toewijzen | #203 |
| [UC-K06](#uc-k06-werkvoorraad-en-reactietijden-bewaken) | Werkvoorraad en reactietijden bewaken | #204 |
| [UC-K07](#uc-k07-klantvraag-onderzoeken-en-beantwoorden) | Klantvraag onderzoeken en beantwoorden | #205 |
| [UC-K08](#uc-k08-klacht-volgens-vaste-werkwijze-afhandelen) | Klacht volgens vaste werkwijze afhandelen | #206 |
| [UC-K09](#uc-k09-oplossing-of-compensatie-vastleggen) | Oplossing of compensatie vastleggen | #207 |
| [UC-K10](#uc-k10-klant-informeren-en-zaak-opvolgen) | Klant informeren en zaak opvolgen | #208 |
| [UC-K11](#uc-k11-klachten-en-klantfeedback-analyseren) | Klachten en klantfeedback analyseren | #209 |
| [UC-K12](#uc-k12-klantgegevens-en-bewaartermijnen-beheren) | Klantgegevens en bewaartermijnen beheren | #210 |
| [UC-K13](#uc-k13-privacy-en-gevoelige-gegevens-bewaken) | Privacy en gevoelige gegevens bewaken | #211 |

---

## UC-K01 Klant en boeking opzoeken

| | |
| --- | --- |
| Use case | UC-K01 - Klant en boeking opzoeken |
| Nummer | UC-K01 (user stories #199) |
| Doel | De medewerker kan een klant snel en eenduidig terugvinden en de bijbehorende boekingen en reisproductgegevens raadplegen. |
| Primaire actor | Klantenservicemedewerker |
| Trigger | Een klant neemt contact op en de medewerker wil de klant en/of boeking terugvinden. |
| Preconditie | De medewerker is ingelogd. |
| Hoofdscenario | 1. De medewerker opent Klant zoeken.<br>2. De medewerker vult een zoekgegeven in (bij voorkeur het e-mailadres; ook telefoon, naam of boekingsnummer).<br>3. Het systeem zoekt en toont de gevonden klant.<br>4. De medewerker opent het klantprofiel.<br>5. Het systeem toont de klantgegevens en gekoppelde boekingen.<br>6. De medewerker raadpleegt de boeking en de reisproductgegevens. |
| Postconditie | De klant is geïdentificeerd; klantgegevens, boekingen en reisproducten zijn getoond. |
| Alternatieve scenario’s | **2a.** Geen zoekgegeven ingevuld: het systeem vraagt om een zoekgegeven.<br>**3a.** Geen klant gevonden: het systeem toont een melding; de medewerker zoekt opnieuw of maakt een nieuwe klant aan (UC-K02).<br>**3b.** Meerdere klanten gevonden: het systeem toont een lijst met geboortedatum en woonplaats; de medewerker kiest de juiste klant.<br>**4a.** De klant kan zich niet voldoende identificeren: de medewerker vraagt aanvullende gegevens.<br>**5a.** De klant heeft geen boekingen: alleen de klantgegevens worden getoond.<br>**5b.** De klant heeft meerdere boekingen: de medewerker selecteert de juiste boeking. |

## UC-K02 Klantcontact registreren

| | |
| --- | --- |
| Use case | UC-K02 - Klantcontact registreren |
| Nummer | UC-K02 (user stories #200) |
| Doel | De medewerker kan elk contactmoment vastleggen (kanaal, onderwerp, samenvatting, datum, medewerker), zodat collega's dezelfde verhaallijn zien. |
| Primaire actor | Klantenservicemedewerker |
| Trigger | De medewerker heeft contact gehad met een klant (telefoon, e-mail, chat of shop). |
| Preconditie | De medewerker is ingelogd. |
| Hoofdscenario | 1. De medewerker zoekt en identificeert de klant (UC-K01).<br>2. De medewerker kiest Contact registreren.<br>3. De medewerker vult kanaal, categorie, onderwerp en samenvatting in.<br>4. De medewerker koppelt het contact aan een bestaande klantzaak of maakt een nieuwe zaak aan (UC-K04).<br>5. De medewerker klikt op Opslaan.<br>6. Het systeem controleert de verplichte velden en controleert op gevoelige gegevens (UC-K13).<br>7. Het systeem legt contactdatum en medewerker vast en slaat het contact op in de klanthistorie.<br>8. Het systeem stuurt de klant een bevestiging. |
| Postconditie | Het contact staat met datum en medewerker in de klanthistorie; de klant heeft een bevestiging ontvangen. |
| Alternatieve scenario’s | **1a.** Klant niet gevonden: de medewerker maakt een nieuwe klant aan; een voorlopige klant is mogelijk (bijv. "Baby <achternaam>").<br>**3a.** De medewerker voegt een bijlage toe (extend).<br>**6a.** Verplicht veld ontbreekt: het systeem toont een foutmelding bij het veld. Terug naar stap 3.<br>**6b.** De invoer bevat een IBAN of paspoortnummer: het systeem blokkeert opslaan en toont een waarschuwing (UC-K13). |

## UC-K03 Klantdossier en contactgeschiedenis raadplegen

| | |
| --- | --- |
| Use case | UC-K03 - Klantdossier en contactgeschiedenis raadplegen |
| Nummer | UC-K03 (user stories #201) |
| Doel | De medewerker kan het klantdossier en de contactgeschiedenis raadplegen, zodat hij of zij weet wat er eerder is besproken en afgehandeld. |
| Primaire actor | Klantenservicemedewerker |
| Trigger | De medewerker wil weten wat er eerder met de klant is besproken. |
| Preconditie | De medewerker is ingelogd; de klant is gevonden (UC-K01). |
| Hoofdscenario | 1. De medewerker opent het klantprofiel.<br>2. Het systeem toont een tijdlijn met contactmomenten, klantzaken en open vervolgacties.<br>3. De medewerker bekijkt de interacties.<br>4. Het systeem toont de gekoppelde boekingen en reisproducten. |
| Postconditie | De klantgeschiedenis en interacties zijn getoond; de medewerker heeft een compleet beeld van de klant. |
| Alternatieve scenario’s | **2a.** Nog geen eerdere contacten: het systeem toont een lege tijdlijn met uitleg.<br>**2b.** De medewerker filtert op periode of type contact (extend).<br>**3a.** De medewerker opent een zaak of klacht direct vanuit de geschiedenis (extend).<br>**3b.** De medewerker voegt een notitie toe (extend). |

## UC-K04 Klantzaak beheren

| | |
| --- | --- |
| Use case | UC-K04 - Klantzaak beheren |
| Nummer | UC-K04 (user stories #202) |
| Doel | De medewerker kan een klantzaak aanmaken, classificeren, koppelen aan een klant en de status bijhouden tot de zaak is afgesloten of overgedragen. |
| Primaire actor | Klantenservicemedewerker |
| Trigger | Een klant meldt een vraag, klacht of probleem dat als zaak moet worden vastgelegd. |
| Preconditie | De medewerker is ingelogd; de klant is gevonden (UC-K01). |
| Hoofdscenario | 1. De medewerker kiest Nieuwe klantzaak.<br>2. De medewerker koppelt de zaak aan de klant en de boeking.<br>3. De medewerker classificeert de zaak (type en categorie).<br>4. De medewerker klikt op Opslaan.<br>5. Het systeem valideert de velden en slaat de zaak op met zaaknummer en status Nieuw.<br>6. De medewerker werkt de status bij tijdens de afhandeling.<br>7. De medewerker sluit de zaak af met een uitkomst. |
| Postconditie | De klantzaak is gekoppeld aan de klant, geclassificeerd en afgesloten of overgedragen; de statushistorie is bewaard. |
| Alternatieve scenario’s | **1a.** Er is al een zaak: de medewerker voegt het contact toe aan de bestaande zaak.<br>**5a.** Verplicht veld ontbreekt: het systeem toont een foutmelding. Terug naar stap 3.<br>**6a.** De medewerker draagt de zaak over aan een collega met een overdrachtsnotitie.<br>**7a.** Er staan nog vervolgacties open: het systeem blokkeert afsluiten en toont welke acties openstaan.<br>**7b.** Een afgesloten zaak wordt heropend met een reden. |

## UC-K05 Klantzaken prioriteren en toewijzen

| | |
| --- | --- |
| Use case | UC-K05 - Klantzaken prioriteren en toewijzen |
| Nummer | UC-K05 (user stories #203) |
| Doel | Urgente zaken worden eerst opgepakt en elke openstaande zaak heeft een behandelaar. |
| Primaire actor | Manager (teamleider klantenservice) |
| Trigger | Het begin van de dienst, of een melding over een te lang wachtende zaak (UC-K06). |
| Preconditie | De manager is ingelogd; er zijn openstaande zaken. |
| Hoofdscenario | 1. De manager opent het overzicht openstaande zaken.<br>2. Het systeem toont de zaken gesorteerd op urgentie en ouderdom; zaken van klanten die nu op reis zijn krijgen automatisch urgentie Hoog.<br>3. De manager beoordeelt de urgentie en past die zo nodig aan.<br>4. De manager bekijkt de capaciteit en werkverdeling.<br>5. De manager wijst een behandelaar toe.<br>6. Het systeem zet de zaak in de werkvoorraad van de behandelaar en legt vast wie wanneer toewees. |
| Postconditie | Elke openstaande zaak heeft een urgentie en een behandelaar. |
| Alternatieve scenario’s | **2a.** Geen openstaande zaken: het systeem toont een lege staat met uitleg.<br>**2b.** De manager filtert op achterstallige of lang wachtende zaken (extend).<br>**5a.** Herverdelen: de manager wijst een zaak opnieuw toe met een overdrachtsnotitie (extend).<br>**6a.** Er zijn nog zaken zonder behandelaar: terug naar stap 3. |

## UC-K06 Werkvoorraad en reactietijden bewaken

| | |
| --- | --- |
| Use case | UC-K06 - Werkvoorraad en reactietijden bewaken |
| Nummer | UC-K06 (user stories #204) |
| Doel | De medewerker kan de eigen werkvoorraad en de reactie- en oplostijden bewaken, zodat achterstallige zaken tijdig worden gesignaleerd. |
| Primaire actor | Klantenservicemedewerker |
| Trigger | De medewerker begint aan het werk of wil controleren of de afgesproken termijnen gehaald worden. |
| Preconditie | De medewerker is ingelogd. |
| Hoofdscenario | 1. De medewerker opent de werkvoorraad.<br>2. Het systeem haalt de openstaande zaken op met status, prioriteit, urgentie en verantwoordelijke medewerker.<br>3. Het systeem controleert de reactie- en oplostijden tegen de norm.<br>4. Het systeem markeert zaken die de norm overschrijden als achterstallig.<br>5. De medewerker bekijkt het resultaat. |
| Postconditie | De werkvoorraad en de status van de reactie- en oplostijden zijn getoond en kunnen worden gebruikt om te bepalen wat eerst moet |
| Alternatieve scenario’s | **2a.** De werkvoorraad is leeg of niet goed ingevuld: het systeem toont een lege staat met uitleg.<br>**3a.** Voor een zaak zijn geen reactie- of oplostijden bekend: het systeem toont dit bij de zaak.<br>**4a.** Een termijn is overschreden: het systeem stuurt een melding.<br>**4b.** Er kan geen ontvanger voor de melding worden bepaald: het systeem toont een waarschuwing.<br>**5a.** De medewerker bekijkt de werkvoorraad per medewerker of per categorie (extend).<br>**5b.** De medewerker bekijkt de capaciteit en werkverdeling (extend); er zijn geen capaciteitsgegevens beschikbaar. |

## UC-K07 Klantvraag onderzoeken en beantwoorden

| | |
| --- | --- |
| Use case | UC-K07 - Klantvraag onderzoeken en beantwoorden |
| Nummer | UC-K07 (user stories #205) |
| Doel | De medewerker kan een klantvraag onderzoeken, beantwoorden en het antwoord laten registreren, zo nodig met hulp van templates, veelgestelde vragen of collega's. |
| Primaire actor | Klantenservicemedewerker |
| Trigger | Er staat een klantvraag in de werkvoorraad van de medewerker. |
| Preconditie | De medewerker is ingelogd; de vraag staat als klantzaak in het systeem en is aan de medewerker toegewezen (UC-K05). |
| Hoofdscenario | 1. De medewerker opent de vraag vanuit de werkvoorraad.<br>2. De medewerker bekijkt de klantgeschiedenis (UC-K03).<br>3. De medewerker zoekt het antwoord (veelgestelde vragen of antwoordtemplate).<br>4. De medewerker schrijft het antwoord.<br>5. De medewerker verstuurt het antwoord.<br>6. Het systeem registreert antwoord, contactmoment en afhandeltijd en zet de status op Afgehandeld. |
| Postconditie | De vraag is beantwoord en geregistreerd in de klanthistorie. |
| Alternatieve scenario’s | **2a.** Informatie onvolledig: de medewerker vraagt de klant om aanvulling; status Wacht op klant.<br>**3a.** De medewerker raadpleegt een interne collega (extend).<br>**3b.** Een andere afdeling is nodig: de medewerker zet de vraag door (extend).<br>**5a.** Het antwoord is leeg: het systeem blokkeert versturen.<br>**6a.** De medewerker registreert een vervolgafspraak (extend). |

## UC-K08 Klacht volgens vaste werkwijze afhandelen

| | |
| --- | --- |
| Use case | UC-K08 - Klacht volgens vaste werkwijze afhandelen |
| Nummer | UC-K08 (user stories #206) |
| Doel | De medewerker kan een klacht volgens de vaste werkwijze onderzoeken, een oplossing bepalen, de klant informeren en de uitkomst vastleggen. |
| Primaire actor | Klantenservicemedewerker |
| Trigger | Een klant dient een klacht in die moet worden afgehandeld. |
| Preconditie | De medewerker is ingelogd; de klacht staat als klantzaak in het systeem (UC-K04). |
| Hoofdscenario | 1. De medewerker opent de klacht; de status wordt In behandeling.<br>2. Het systeem toont of de klant nu op reis is.<br>3. De medewerker onderzoekt de klacht (feiten, bewijsmateriaal, of de klant de accommodatie zelf koos).<br>4. De medewerker beoordeelt de klacht als gegrond.<br>5. De medewerker bepaalt de oplossing of compensatie (UC-K09).<br>6. De medewerker informeert de klant.<br>7. De klant gaat akkoord.<br>8. De medewerker legt de uitkomst vast en sluit de klacht af. |
| Postconditie | De klacht is afgesloten met een vastgelegde uitkomst; de klant is geïnformeerd. |
| Alternatieve scenario’s | **2a.** De klant is nu op reis: de medewerker schakelt het hotel of de leverancier in voor een oplossing ter plaatse (extend); bij succes uitkomst "Opgelost ter plaatse".<br>**2b.** De leverancier is niet bereikbaar of niet geselecteerd: de medewerker gaat verder met stap 3.<br>**3a.** De medewerker voegt bewijsmateriaal toe (extend); is het bestand te groot of het type ongeldig, dan toont het systeem een foutmelding.<br>**3b.** Er is onvoldoende informatie voor een beoordeling: de medewerker vraagt de klant om aanvulling.<br>**4a.** Ongegrond: de medewerker legt een verplichte onderbouwing vast en sluit af als "Ongegrond".<br>**5a.** De medewerker escaleert de klacht naar de bestemming van de klant (extend); is er geen bestemming geselecteerd, dan toont het systeem een foutmelding.<br>**6a.** De klant is niet bereikbaar: de contactpoging wordt vastgelegd en later opnieuw geprobeerd.<br>**7a.** De klant maakt bezwaar: de klacht wordt geëscaleerd naar After Travel, dat het eindbesluit neemt.<br>**8a.** Er staan nog vervolgacties open: het systeem blokkeert afsluiten.<br>**8b.** Een afgesloten klacht wordt heropend met een reden. |

## UC-K09 Oplossing of compensatie vastleggen

| | |
| --- | --- |
| Use case | UC-K09 - Oplossing of compensatie vastleggen |
| Nummer | UC-K09 (user stories #207) |
| Doel | De medewerker kan het klachttype vaststellen, een compensatievoorstel bepalen en dit laten controleren. |
| Primaire actor | Klantenservicemedewerker (indiener) en senior medewerker (goedkeurder) |
| Trigger | Een klacht is als gegrond beoordeeld en er moet een oplossing of compensatie voor worden bepaald (UC-K08 stap 4). |
| Preconditie | De medewerker is ingelogd. Er is een klacht in behandeling met status gegrond |
| Hoofdscenario | 1. De medewerker stelt het klachttype vast.<br>2. De medewerker raadpleegt de compensatierichtlijn en bepaalt het compensatievoorstel.<br>3. De medewerker controleert het voorstel en dient het in; status "Te controleren".<br>4. Een tweede medewerker opent het voorstel.<br>5. De tweede medewerker keurt het voorstel goed.<br>6. Het systeem legt indiener, beoordelaar en besluit vast bij de klacht. |
| Postconditie | Het besluit (goedgekeurd of afgewezen, met beoordelaar) is bij de klacht opgeslagen. |
| Alternatieve scenario’s | **1a.** Het klachttype kan niet worden bepaald.<br>**1b.** De medewerker raadpleegt vergelijkbare klachten (extend); er zijn geen vergelijkbare klachten gevonden.<br>**2a.** Het voorstel valt buiten de toegestane grenzen: het systeem toont een waarschuwing.<br>**3a.** De medewerker past het voorstel aan voordat het wordt beoordeeld.<br>**4a.** De indiener probeert zijn eigen voorstel goed te keuren: het systeem blokkeert dit (vier-ogenprincipe).<br>**5a.** Het voorstel wordt afgewezen: een reden is verplicht; het voorstel gaat terug naar de indiener (stap 3). |

## UC-K10 Klant informeren en zaak opvolgen

| | |
| --- | --- |
| Use case | UC-K10 - Klant informeren en zaak opvolgen |
| Nummer | UC-K10 (user stories #208) |
| Doel | De medewerker kan de status van een zaak raadplegen, de klant over de voortgang informeren en de opvolging (afspraken, acties, escalatie) vastleggen. |
| Primaire actor | Klantenservicemedewerker |
| Trigger | De medewerker wil de klant op de hoogte brengen van de voortgang of de zaak verder opvolgen. |
| Preconditie | De medewerker is ingelogd. De klant staat in het systeem met een open zaak |
| Hoofdscenario | 1. De medewerker opent de klantzaak en raadpleegt de zaakstatus.<br>2. Het systeem toont de status, de laatste communicatie en de open vervolgacties.<br>3. De medewerker informeert de klant over de voortgang.<br>4. Het systeem registreert het verzonden bericht bij de zaak.<br>5. De medewerker legt de opvolging vast: een vervolgafspraak met de klant of een interne vervolgactie met verantwoordelijke en datum.<br>6. Het systeem slaat de opvolging op bij de zaak. |
| Postconditie | De klant is geïnformeerd over de voortgang en eventuele vervolgstappen zijn vastgelegd. |
| Alternatieve scenario’s | **1a.** De zaak is niet gevonden of de status is niet bekend.<br>**3a.** Er zijn geen contactgegevens van de klant bekend.<br>**3b.** De klant is niet bereikbaar: de poging wordt vastgelegd.<br>**5a.** Geen datum ingevuld bij de vervolgafspraak: het systeem toont een foutmelding.<br>**5b.** Geen verantwoordelijke gekozen bij de interne vervolgactie: het systeem toont een foutmelding.<br>**5c.** De medewerker escaleert de zaak naar een collega, leidinggevende of andere afdeling (extend); een reden is verplicht.<br>**6a.** Er komt een reactie of besluit van de klant, een collega of een andere afdeling: de medewerker legt dit vast bij de zaak. |

## UC-K11 Klachten en klantfeedback analyseren

| | |
| --- | --- |
| Use case | UC-K11 - Klachten en klantfeedback analyseren |
| Nummer | UC-K11 (user stories #209) |
| Doel | Trends in klachten zien en er verbeteracties aan koppelen. |
| Primaire actor | Manager (teamleider klantenservice) |
| Trigger | Periodieke analyse (bijv. maandelijks) of een opvallend aantal klachten. |
| Preconditie | De manager is ingelogd; er zijn afgesloten klachten. |
| Hoofdscenario | 1. De manager opent het klachtendashboard.<br>2. De manager kiest een periode.<br>3. Het systeem toont het aantal klachten per categorie, bestemming en leverancier, gesorteerd op frequentie.<br>4. De manager vergelijkt onderwerpen en periodes.<br>5. De manager maakt een verbeteractie aan met afdeling, eigenaar en deadline. |
| Postconditie | Er is een verbeteractie vastgelegd bij de verantwoordelijke afdeling. |
| Alternatieve scenario’s | **3a.** Geen klachten in de gekozen periode: het systeem toont een melding.<br>**4a.** Geen trend gevonden: de use case eindigt zonder verbeteractie.<br>**4b.** De manager bekijkt de onderliggende zaken (extend).<br>**5a.** De actie gaat naar een andere afdeling, bijv. Inkoop bij een hotel met veel klachten (extend).<br>**5b.** De manager exporteert een rapport en deelt het met het management (extend). |

## UC-K12 Klantgegevens en bewaartermijnen beheren

| | |
| --- | --- |
| Use case | UC-K12 - Klantgegevens en bewaartermijnen beheren |
| Nummer | UC-K12 (user stories #210) |
| Doel | Persoonsgegevens worden verwijderd of geanonimiseerd zodra dat mag, zonder gegevens te verliezen die nog nodig zijn. |
| Primaire actor | Klantenservicemedewerker |
| Trigger | De klant vraagt om verwijdering van zijn of haar gegevens. |
| Preconditie | De medewerker is ingelogd; de klant is gevonden (UC-K01). |
| Hoofdscenario | 1. De medewerker kiest Gegevens verwijderen.<br>2. Het systeem controleert de reisstatus: alle terugkomdatums liggen in het verleden.<br>3. Het systeem controleert de bewaartermijn.<br>4. Het systeem toont wat verwijderd wordt en vraagt om bevestiging.<br>5. De medewerker bevestigt.<br>6. Het systeem anonimiseert naam, geboortedatum, e-mail, telefoon en woonplaats, wist contactsamenvattingen en bewaart boekingen anoniem voor de financiële administratie.<br>7. Het systeem logt de verwijdering en stuurt de klant een bevestiging. |
| Postconditie | De klant is niet meer herleidbaar; de verwijdering is gelogd. |
| Alternatieve scenario’s | **2a.** De klant is op reis of vertrekt nog: het systeem blokkeert en toont de terugkomdatum (gegevens nodig bij calamiteiten).<br>**3a.** De bewaartermijn loopt nog: het systeem legt een uitzondering vast met de datum waarop verwijderen wel mag.<br>**5a.** De medewerker annuleert: er wordt niets verwijderd. |

## UC-K13 Privacy en gevoelige gegevens bewaken

| | |
| --- | --- |
| Use case | UC-K13 - Privacy en gevoelige gegevens bewaken |
| Nummer | UC-K13 (user stories #211) |
| Doel | Voorkomen dat gegevens worden opgeslagen die niet bewaard mogen worden, zoals een IBAN of paspoortnummer. |
| Primaire actor | Systeem (bij invoer door de klantenservicemedewerker) |
| Trigger | De medewerker slaat invoer op (bijv. in UC-K02, UC-K04 of UC-K07). |
| Preconditie | De medewerker is ingelogd. |
| Hoofdscenario | 1. De medewerker vult velden of vrije tekst in.<br>2. De medewerker klikt op Opslaan.<br>3. Het systeem controleert de invoer op verboden gegevens (IBAN, paspoortnummer).<br>4. Het systeem vindt geen verboden gegevens en slaat de invoer op. |
| Postconditie | Er zijn geen IBAN- of paspoortnummers opgeslagen. |
| Alternatieve scenario’s | **3a.** Verboden gegeven gevonden: het systeem blokkeert opslaan, toont een waarschuwing en markeert de plek; de medewerker past de invoer aan (terug naar stap 1).<br>**3b.** Er blijkt al een verboden gegeven opgeslagen: de medewerker registreert een privacy-incident (extend). |

---

## User flows

Overgenomen uit de sectie *User flows Klantenservice* op het board. Afbeelding: [`user-flows-klantenservice.png`](user-flows-klantenservice.png) (oudere versie, het board is leidend).

### UC-K01 Klant en boeking opzoeken
```mermaid
flowchart LR
    N0(["START"])
    N1["Klant zoeken openen"]
    N2["Zoekgegeven invullen (bij voorkeur e-mail)"]
    N3["Systeem zoekt klant"]
    N4{"Aantal resultaten?"}
    N5["Lijst met geboortedatum en woonplaats; juiste klant kiezen"]
    N6["Melding: geen klant gevonden"]
    N7["Klantprofiel openen"]
    N8["Systeem toont klantgegevens en boekingen"]
    N9{"Boeking raadplegen?"}
    N10["Boeking en reisproduct-gegevens raadplegen"]
    N11(["EINDE"])
    N0 --> N1
    N1 --> N2
    N2 --> N3
    N3 --> N4
    N4 -- "Meer dan 1" --> N5
    N6 --> N2
    N4 -- "0" --> N6
    N5 --> N7
    N4 -- "1" --> N7
    N7 --> N8
    N8 --> N9
    N9 -- "JA" --> N10
    N10 --> N11
    N9 -- "NEE" --> N11
```

### UC-K02 Klantcontact registreren
```mermaid
flowchart LR
    N0(["START"])
    N1["Klant zoeken (UC-K01)"]
    N2{"Klant gevonden?"}
    N3["Nieuwe klant aanmaken"]
    N4["Contact registreren kiezen"]
    N5["Kanaal, categorie, onderwerp en samenvatting invullen"]
    N6{"Bestaande zaak?"}
    N7["Koppelen aan bestaande zaak"]
    N8["Nieuwe zaak aanmaken (UC-K04)"]
    N9["Op Opslaan klikken"]
    N10["Systeem controleert velden en gevoelige gegevens"]
    N11{"Geldig en geen IBAN of paspoort-nummer?"}
    N12["Foutmelding of privacy-waarschuwing"]
    N13["Systeem slaat contact op met datum en medewerker"]
    N14["Systeem stuurt klant een bevestiging"]
    N15(["EINDE"])
    N0 --> N1
    N1 --> N2
    N2 -- "NEE" --> N3
    N3 --> N4
    N2 -- "JA" --> N4
    N4 --> N5
    N5 --> N6
    N6 -- "JA" --> N7
    N6 -- "NEE" --> N8
    N8 --> N9
    N7 --> N9
    N9 --> N10
    N10 --> N11
    N12 --> N5
    N11 -- "NEE" --> N12
    N11 -- "JA" --> N13
    N13 --> N14
    N14 --> N15
```

### UC-K03 Klantdossier en contactgeschiedenis raadplegen
```mermaid
flowchart LR
    N0(["START"])
    N1["Klantprofiel openen"]
    N2["Systeem toont tijdlijn, zaken en open vervolgacties"]
    N3{"Filteren?"}
    N4["Filteren op periode of type"]
    N5["Interacties bekijken"]
    N6["Systeem toont gekoppelde boekingen en producten"]
    N7{"Vervolgactie?"}
    N8["Zaak of klacht openen"]
    N9["Notitie toevoegen en opslaan"]
    N10(["EINDE"])
    N0 --> N1
    N1 --> N2
    N2 --> N3
    N3 -- "JA" --> N4
    N4 --> N5
    N3 -- "NEE" --> N5
    N5 --> N6
    N6 --> N7
    N7 -- "Zaak openen" --> N8
    N7 -- "Notitie" --> N9
    N9 --> N10
    N8 --> N10
    N7 -- "Geen" --> N10
```

### UC-K04 Klantzaak beheren
```mermaid
flowchart LR
    N0(["START"])
    N1["Klant zoeken (UC-K01)"]
    N2{"Bestaande zaak?"}
    N3["Contact aan bestaande zaak toevoegen"]
    N4["Nieuwe klantzaak kiezen"]
    N5["Zaak koppelen aan klant en boeking"]
    N6["Zaak classificeren (type en categorie)"]
    N7["Op Opslaan klikken"]
    N8["Systeem valideert de velden"]
    N9{"Velden geldig?"}
    N10["Foutmelding tonen"]
    N11["Systeem slaat zaak op met status Nieuw"]
    N12["Status bijwerken tijdens afhandeling"]
    N13{"Volgende stap?"}
    N14["Zaak overdragen met overdrachts-notitie"]
    N15{"Open vervolgacties?"}
    N16["Systeem blokkeert afsluiten en toont open acties"]
    N17["Zaak afsluiten met uitkomst"]
    N18(["EINDE"])
    N0 --> N1
    N1 --> N2
    N2 -- "JA" --> N3
    N2 -- "NEE" --> N4
    N4 --> N5
    N5 --> N6
    N6 --> N7
    N7 --> N8
    N8 --> N9
    N10 --> N6
    N9 -- "NEE" --> N10
    N9 -- "JA" --> N11
    N11 --> N12
    N3 --> N12
    N12 --> N13
    N13 -- "Overdragen" --> N14
    N13 -- "Afsluiten" --> N15
    N16 --> N12
    N15 -- "JA" --> N16
    N15 -- "NEE" --> N17
    N14 --> N18
    N17 --> N18
```

### UC-K05 Klantzaken prioriteren en toewijzen
```mermaid
flowchart LR
    N0(["START"])
    N1["Overzicht openstaande zaken openen"]
    N2{"Zaken aanwezig?"}
    N3["Lege staat met uitleg tonen"]
    N4(["EINDE"])
    N5["Systeem sorteert op urgentie en ouderdom"]
    N6["Urgentie beoordelen en zo nodig aanpassen"]
    N7["Capaciteit en werkverdeling bekijken"]
    N8["Behandelaar toewijzen"]
    N9["Systeem zet zaak in werkvoorraad en legt toewijzing vast"]
    N10{"Nog zaken zonder behandelaar?"}
    N11(["EINDE"])
    N0 --> N1
    N1 --> N2
    N2 -- "NEE" --> N3
    N3 --> N4
    N2 -- "JA" --> N5
    N5 --> N6
    N6 --> N7
    N7 --> N8
    N8 --> N9
    N10 -- "JA" --> N6
    N9 --> N10
    N10 -- "NEE" --> N11
```

### UC-K06 Werkvoorraad en reactietijden bewaken
```mermaid
flowchart LR
    N0(["START"])
    N1["Werkvoorraad openen"]
    N2["Systeem haalt toegewezen zaken op"]
    N3{"Zaken aanwezig?"}
    N4["Lege werkvoorraad tonen"]
    N5(["EINDE"])
    N6["Systeem controleert reactie- en oplostijden"]
    N7{"Norm overschreden?"}
    N8["Zaak als achterstallig markeren en manager melden"]
    N9["Zaak met hoogste urgentie oppakken"]
    N10(["EINDE"])
    N0 --> N1
    N1 --> N2
    N2 --> N3
    N3 -- "NEE" --> N4
    N4 --> N5
    N3 -- "JA" --> N6
    N6 --> N7
    N7 -- "JA" --> N8
    N8 --> N9
    N7 -- "NEE" --> N9
    N9 --> N10
```

### UC-K07 Klantvraag onderzoeken en beantwoorden
```mermaid
flowchart LR
    N0(["START"])
    N1["Vraag openen uit werkvoorraad"]
    N2["Klantgeschiedenis bekijken (UC-K03)"]
    N3{"Informatie compleet?"}
    N4["Klant om aanvulling vragen; status Wacht op klant"]
    N5(["EINDE"])
    N6{"Andere afdeling nodig?"}
    N7["Doorzetten naar andere afdeling"]
    N8["Antwoord zoeken (FAQ of template)"]
    N9["Antwoord schrijven"]
    N10{"Antwoord ingevuld?"}
    N11["Systeem blokkeert versturen"]
    N12["Antwoord versturen"]
    N13["Systeem registreert antwoord en afhandeltijd; status Afgehandeld"]
    N14(["EINDE"])
    N0 --> N1
    N1 --> N2
    N2 --> N3
    N3 -- "NEE" --> N4
    N4 --> N5
    N3 -- "JA" --> N6
    N6 -- "JA" --> N7
    N6 -- "NEE" --> N8
    N8 --> N9
    N9 --> N10
    N11 --> N9
    N10 -- "NEE" --> N11
    N10 -- "JA" --> N12
    N12 --> N13
    N13 --> N14
    N7 --> N14
```

### UC-K08 Klacht volgens vaste werkwijze afhandelen
```mermaid
flowchart LR
    N0(["START"])
    N1["Klacht openen; status In behandeling"]
    N2{"Klant nu op reis?"}
    N3["Hotel of leverancier inschakelen voor oplossing ter plaatse"]
    N4{"Opgelost ter plaatse?"}
    N5["Afsluiten: Opgelost ter plaatse"]
    N6["Klacht onderzoeken en bewijs vastleggen"]
    N7{"Gegrond?"}
    N8["Onderbouwing vastleggen; afsluiten als Ongegrond"]
    N9["Oplossing of compensatie bepalen (UC-K09)"]
    N10["Klant informeren"]
    N11{"Klant akkoord?"}
    N12["Escaleren naar After Travel"]
    N13["Uitkomst vastleggen en klacht sluiten"]
    N14(["EINDE"])
    N0 --> N1
    N1 --> N2
    N2 -- "JA" --> N3
    N3 --> N4
    N4 -- "JA" --> N5
    N4 -- "NEE" --> N6
    N2 -- "NEE" --> N6
    N6 --> N7
    N7 -- "NEE" --> N8
    N7 -- "JA" --> N9
    N9 --> N10
    N10 --> N11
    N11 -- "NEE" --> N12
    N11 -- "JA" --> N13
    N13 --> N14
    N12 --> N14
    N8 --> N14
    N5 --> N14
```

### UC-K09 Oplossing of compensatie vastleggen
```mermaid
flowchart LR
    N0(["START"])
    N1["Systeem stelt klachttype vast en haalt richtlijn op"]
    N2["Systeem berekent percentage × reissom"]
    N3{"Afwijken van richtlijn?"}
    N4["Percentage aanpassen met verplichte toelichting"]
    N5["Voorstel controleren en indienen"]
    N6["Tweede medewerker opent voorstel"]
    N7{"Zelfde medewerker als indiener?"}
    N8["Systeem blokkeert: vier-ogenprincipe"]
    N9{"Goedkeuren?"}
    N10["Afwijzen met reden; terug naar indiener"]
    N11["Systeem legt goedkeuring vast en geeft voorstel vrij"]
    N12(["EINDE"])
    N0 --> N1
    N1 --> N2
    N2 --> N3
    N3 -- "JA" --> N4
    N4 --> N5
    N3 -- "NEE" --> N5
    N5 --> N6
    N6 --> N7
    N8 --> N6
    N7 -- "JA" --> N8
    N7 -- "NEE" --> N9
    N10 --> N5
    N9 -- "NEE" --> N10
    N9 -- "JA" --> N11
    N11 --> N12
```

### UC-K10 Klant informeren en zaak opvolgen
```mermaid
flowchart LR
    N0(["START"])
    N1["Klantzaak openen"]
    N2["Systeem toont zaakstatus en open vervolgacties"]
    N3{"Escaleren nodig?"}
    N4["Zaak escaleren (senior, daarna After Travel)"]
    N5["Vervolgactie of vervolgafspraak registreren"]
    N6["Update voor klant opstellen"]
    N7["Systeem controleert reisstatus klant"]
    N8{"Bericht past bij reisstatus?"}
    N9["Waarschuwing: niet automatisch versturen"]
    N10["Systeem verstuurt bericht en registreert het in klanthistorie"]
    N11{"Reactie van klant?"}
    N12["Reactie of besluit registreren"]
    N13(["EINDE"])
    N0 --> N1
    N1 --> N2
    N2 --> N3
    N3 -- "JA" --> N4
    N4 --> N5
    N3 -- "NEE" --> N5
    N5 --> N6
    N6 --> N7
    N7 --> N8
    N9 --> N6
    N8 -- "NEE" --> N9
    N8 -- "JA" --> N10
    N10 --> N11
    N11 -- "JA" --> N12
    N12 --> N13
    N11 -- "NEE" --> N13
```

### UC-K11 Klachten en klantfeedback analyseren
```mermaid
flowchart LR
    N0(["START"])
    N1["Klachtendashboard openen"]
    N2["Periode kiezen"]
    N3{"Klachten in periode?"}
    N4["Melding: geen gegevens"]
    N5(["EINDE"])
    N6["Systeem toont aantallen per categorie, bestemming en leverancier"]
    N7["Onderwerpen en periodes vergelijken"]
    N8{"Trend gevonden?"}
    N9["Verbeteractie aanmaken met afdeling, eigenaar en deadline"]
    N10{"Rapport delen?"}
    N11["Rapport exporteren en delen met management"]
    N12(["EINDE"])
    N0 --> N1
    N1 --> N2
    N2 --> N3
    N3 -- "NEE" --> N4
    N4 --> N5
    N3 -- "JA" --> N6
    N6 --> N7
    N7 --> N8
    N8 -- "JA" --> N9
    N9 --> N10
    N10 -- "JA" --> N11
    N11 --> N12
    N10 -- "NEE" --> N12
    N8 -- "NEE" --> N12
```

### UC-K12 Klantgegevens en bewaartermijnen beheren
```mermaid
flowchart LR
    N0(["START"])
    N1["Gegevens verwijderen kiezen"]
    N2{"Klant terug van reis?"}
    N3["Blokkeren en terugkomdatum tonen"]
    N4(["EINDE"])
    N5{"Bewaartermijn verstreken?"}
    N6["Uitzondering vastleggen met datum"]
    N7["Systeem toont wat verwijderd wordt en vraagt bevestiging"]
    N8{"Bevestigd?"}
    N9["Annuleren: niets verwijderd"]
    N10["Anonimiseren, loggen en klant bevestigen"]
    N11(["EINDE"])
    N0 --> N1
    N1 --> N2
    N2 -- "NEE" --> N3
    N3 --> N4
    N2 -- "JA" --> N5
    N6 --> N4
    N5 -- "NEE" --> N6
    N5 -- "JA" --> N7
    N7 --> N8
    N8 -- "NEE" --> N9
    N8 -- "JA" --> N10
    N10 --> N11
    N9 --> N11
```

### UC-K13 Privacy en gevoelige gegevens bewaken
```mermaid
flowchart LR
    N0(["START"])
    N1["Velden of vrije tekst invullen"]
    N2["Op Opslaan klikken"]
    N3["Systeem controleert op IBAN en paspoortnummer"]
    N4{"Verboden gegeven gevonden?"}
    N5["Opslaan blokkeren, waarschuwing tonen en plek markeren"]
    N6["Systeem slaat de invoer op"]
    N7(["EINDE"])
    N0 --> N1
    N1 --> N2
    N2 --> N3
    N3 --> N4
    N5 --> N1
    N4 -- "JA" --> N5
    N4 -- "NEE" --> N6
    N6 --> N7
```
