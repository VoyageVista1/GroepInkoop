# Scope Productontwikkeling & Inkoop en Klantenservice & Support

**Stand:** 1 oktober 2026 (sprintreview) · **Bronnen:** FigJam-board (sectie *Scope Productontwikkeling & Inkoop* en *Proces*), [interviewanalyse](../interview-analyse.md), [conceptueel ERD](erd-conceptueel.md), [product backlog](../backlog/inkoop-product-backlog.md) · **GitHub:** #48 en #69 (afgerond)

Dit document legt vast welk probleem we oplossen, voor wie, wat in de eerste versie zit en waar ons werk ophoudt. Use cases, flows en schermen staan in de aparte ontwerpdocumenten.

## 1. Probleem en doel

| | Productontwikkeling & Inkoop | Klantenservice & Support |
| --- | --- | --- |
| Probleem | Leveranciers, onderhandelingen en contracten staan verspreid; productdata wordt met de hand overgetypt (I6, I9). Kamertypes zijn onduidelijk (I7). | Gesprekken staan als vrije tekst in één veld (K3); collega’s geven verschillende antwoorden (K5); klachten worden niet volgens één werkwijze afgehandeld (K8, K9). |
| Doel | Eén plek voor leveranciers, onderhandelingen, contracten en reisproducten, met dezelfde actuele gegevens voor iedereen. | Eén klantdossier met alle contactmomenten en klachten, en een vaste werkwijze voor compensatie met vier-ogenprincipe. |
| Gebruikers | Productmedewerker / productmanager, inkoper, manager; medewerkers van andere afdelingen (alleen raadplegen). | Klantenservicemedewerker (ook shop), senior / teamleider, After Travel. |

## 2. In scope: eerste bruikbare versie

**Productontwikkeling & Inkoop**

| Onderdeel | Wat de medewerker ermee kan |
| --- | --- |
| Reisproducten-overzicht | Reisproducten zoeken, bekijken en een nieuw product aanmaken. |
| Reisproduct-formulier en detailpagina | Productinformatie vastleggen en wijzigen: bestemming, reisroute, accommodaties, vervoer en activiteiten. |
| Leveranciersbeheer | Leveranciers en contactgegevens vastleggen en koppelen aan reisonderdelen. |
| Onderhandelingen bijhouden | Per leverancier vastleggen waarover wordt onderhandeld, welke afspraken zijn gemaakt en wat nog moet gebeuren. |
| Contractinformatie beheren | Contractafspraken, looptijden en verwijzingen naar documenten terugvinden. |
| Voortgang en deadlines | Zien hoe ver een reisproduct is en welke acties nog openstaan. |
| Productinformatie beschikbaar maken | Andere onderdelen van de gezamenlijke applicatie werken met dezelfde actuele productgegevens. |

**Klantenservice & Support**

| Onderdeel | Wat de medewerker ermee kan |
| --- | --- |
| Klant zoeken | Op e-mail, telefoon, naam of boekingsnummer; gelijknamige klanten onderscheiden (UC-K02). |
| Klantdossier en tijdlijn | Alle contactmomenten, klachten en boekingen chronologisch bekijken (UC-K03). |
| Contact registreren | Met vaste velden in plaats van één opmerkingenveld (UC-K01). |
| Zaken prioriteren en verdelen | Urgentie automatisch Hoog als de klant op reis is (UC-K04). |
| Klacht en compensatie | Voorstel volgens richtlijn, altijd gecontroleerd door een tweede medewerker (UC-K06, UC-K07). |
| Gegevens verwijderen (AVG) | Op verzoek, geblokkeerd zolang de klant op reis is (UC-K09). |

**Schermen eerste versie (Inkoop):** reisproducten-overzicht (zoekveld, lijst met naam en bestemming, knop “Nieuw reisproduct”), reisproduct aanmaken/bewerken (velden, lijst met reisonderdelen, onderdelen toevoegen/verwijderen, Opslaan en Annuleren) en reisproduct bekijken (Bewerken, terug naar overzicht).

## 3. Buiten scope

| Onderwerp | Waarom | Wie wel |
| --- | --- | --- |
| Boekingen maken en wijzigen | Eigendom van Sales & Boekingen; wij lezen alleen vertrek- en terugkomdatum en reissom. | Team Sales & Boekingen |
| Facturatie, uitbetalen van compensatie, creditfacturen | Financiële verwerking. Wij leveren het goedgekeurde bedrag aan. | Team Financiën & Administratie |
| Klant wijzigt zelf online zijn boeking (selfservice) | Vraagt eigen klantportaal en voorwaarden per reis (I10, K10). | Later / Sales & Boekingen |
| Gesprekken automatisch opnemen of transcriberen | Privacy van klant en medewerker en standpunt ondernemingsraad zijn nog open (K7). | Nu niet (#111, Won’t) |
| Koppeling met beddenbanken en externe systemen | Technische integratie valt buiten de eerste versie. | IT & Innovatie |
| Interne werkwijze van de leverancier (hotel) | Hotel is een externe partij; in BPMN als dichtgeklapte pool. | – |

## 4. Gegevens die we bewust niet opslaan

- Geen IBAN, ook niet na betaling (P1).
- Geen paspoortnummer of andere paspoortgegevens; alleen naam en geboortedatum zoals in het paspoort (P2).
- Klantgegevens blijven bewaard tot de klant thuis is; daarna kan de klant om verwijdering vragen (P3).

## 5. Afhankelijkheden

| Van | Wat we nodig hebben | Voor |
| --- | --- | --- |
| Sales & Boekingen | Boeking met vertrek- en terugkomdatum en reissom | Urgentie bij klant op reis, compensatieberekening, AVG-blokkade |
| Financiën & Administratie | Afspraak hoe een goedgekeurde compensatie en een contract doorlopen naar betaling en facturatie | UC-K06, IN-07, IN-08 |
| IT & Innovatie | Gezamenlijk datamodel en low-code platform | Alle stories |

## 6. Open besluiten

| Vraag | Raakt | Wie beslist |
| --- | --- | --- |
| Wie keurt contracten goed, en vanaf welk bedrag? | IN-10 | Opdrachtgever |
| Klopt de drempel van 50% bezetting en 8 weken vooraf? | IN-11, R11 | Opdrachtgever |
| Binnen hoeveel uur moet een klacht met urgentie Hoog opgepakt zijn? | UC-K04, R5 | Opdrachtgever |
| Mag een compensatie hoger zijn dan de reissom? | UC-K07, R3 | Opdrachtgever |
| Wie mag een compensatievoorstel goedkeuren: elke collega of alleen een senior? | UC-K07, R4 | Opdrachtgever |
| Hoe lang na thuiskomst bewaren we klantgegevens? | UC-K09, R1 | Opdrachtgever / privacy officer |
| Slaan we contractdocumenten zelf op, of alleen een verwijzing? | Contractbeheer | Opdrachtgever / IT |
