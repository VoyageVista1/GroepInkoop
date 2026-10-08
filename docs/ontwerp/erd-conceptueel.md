# Conceptueel ERD – Inkoop & Klantenservice

Hoofdentiteiten van Productontwikkeling & Inkoop en Klantenservice & Support, met sleutels en kardinaliteiten. Dit is het **conceptuele** model: alleen de entiteiten en relaties die nodig zijn om de use cases uit te voeren. Het fysieke databaseschema (alle kolommen en datatypes) werkt dit later uit.

Afbeelding: [`erd-conceptueel.png`](erd-conceptueel.png)

```mermaid
erDiagram
    LEVERANCIER ||--o{ ONDERHANDELING : "voert"
    LEVERANCIER ||--o{ CONTRACT : "sluit"
    ONDERHANDELING |o--o| CONTRACT : "leidt tot"
    CONTRACT ||--|{ ANNULERINGSREGEL : "heeft"
    LEVERANCIER ||--o{ REISONDERDEEL : "levert"
    CONTRACT |o--o{ REISONDERDEEL : "dekt"
    KAMERTYPE |o--o{ REISONDERDEEL : "typeert"
    REISPRODUCT ||--|{ REISONDERDEEL : "bestaat uit"
    MEDEWERKER ||--o{ ONDERHANDELING : "is verantwoordelijk voor"
    MEDEWERKER ||--o{ REISPRODUCT : "is eigenaar van"
    KLANT ||--o{ BOEKING : "maakt"
    REISPRODUCT ||--o{ BOEKING : "wordt geboekt in"
    KLANT ||--o{ KLANTZAAK : "heeft"
    BOEKING |o--o{ KLANTZAAK : "gaat over"
    KLANTZAAK ||--|{ CONTACTMOMENT : "bevat"
    KLANTZAAK ||--o| KLACHT : "is een"
    COMPENSATIERICHTLIJN ||--o{ KLACHT : "bepaalt voorstel"
    LEVERANCIER |o--o{ KLACHT : "betreft"
    KLANTZAAK ||--o{ VERVOLGACTIE : "heeft"
    MEDEWERKER ||--o{ KLANTZAAK : "behandelt"
    MEDEWERKER ||--o{ CONTACTMOMENT : "registreert"

    LEVERANCIER {
        int LeverancierID PK
        string Naam
        string Type
        string Land
        string Plaats
        string Email
    }
    ONDERHANDELING {
        int OnderhandelingID PK
        int LeverancierID FK
        int MedewerkerID FK
        date Bezoekdatum
        string Status
        decimal Inkoopprijs
        decimal Verkoopprijs
        date Deadline
    }
    CONTRACT {
        int ContractID PK
        int LeverancierID FK
        int OnderhandelingID FK
        date Begindatum
        date Einddatum
        int AantalKamers
        decimal Inkoopprijs
        string Documentlink
    }
    ANNULERINGSREGEL {
        int RegelID PK
        int ContractID FK
        int DagenVoorVertrek
        int KostenPercentage
    }
    KAMERTYPE {
        int KamertypeID PK
        string Omschrijving
    }
    REISPRODUCT {
        int ReisproductID PK
        int EigenaarID FK
        string Naam
        string Bestemming
        string Status
        int Versienummer
    }
    REISONDERDEEL {
        int OnderdeelID PK
        int ReisproductID FK
        int LeverancierID FK
        int ContractID FK
        int KamertypeID FK
        string Soort
        int Volgorde
    }
    MEDEWERKER {
        int MedewerkerID PK
        string Naam
        string Afdeling
        string Rol
    }
    KLANT {
        int KlantID PK
        string Voornaam
        string Achternaam
        date Geboortedatum
        string Email UK
        string Telefoon
    }
    BOEKING {
        int BoekingID PK
        int KlantID FK
        int ReisproductID FK
        date Vertrekdatum
        date Terugkomdatum
        decimal Reissom
    }
    KLANTZAAK {
        int ZaakID PK
        int KlantID FK
        int BoekingID FK
        int BehandelaarID FK
        string Categorie
        string Urgentie
        string Status
        datetime GeopendOp
        datetime GeslotenOp
    }
    CONTACTMOMENT {
        int ContactID PK
        int ZaakID FK
        int MedewerkerID FK
        string Kanaal
        datetime Tijdstip
        string Samenvatting
    }
    KLACHT {
        int KlachtID PK
        int ZaakID FK
        int RichtlijnID FK
        int LeverancierID FK
        decimal VoorgesteldBedrag
        int VoorgesteldDoor FK
        int GoedgekeurdDoor FK
        string Uitkomst
    }
    COMPENSATIERICHTLIJN {
        int RichtlijnID PK
        string Klachtcategorie
        int Percentage
    }
    VERVOLGACTIE {
        int ActieID PK
        int ZaakID FK
        int EigenaarID FK
        string Omschrijving
        date Deadline
        bool Afgerond
    }
```

## Toelichting per entiteit

| Entiteit | Afdeling | Waarom nodig | Bron |
| --- | --- | --- | --- |
| Leverancier | Inkoop | Eén centrale plek voor hotels, vervoerders en rederijen | KP1, GP1, interview I6 |
| Onderhandeling | Inkoop | Eigen tabel in plaats van één statuskolom, zodat eerdere voorstellen bewaard blijven | KP1, interview I3–I4 |
| Contract | Inkoop | Looptijd, aantal kamers en inkoopprijs; einddatum ≥ begindatum | KP5, interview I5 |
| Annuleringsregel | Inkoop | Voorwaarden als regels (“vanaf X dagen: Y%”) in plaats van vrije tekst | Interview I10 |
| Kamertype | Inkoop | Vaste lijst, zodat klant en verkoper hetzelfde verstaan onder een kamer | Interview I7 |
| Reisproduct / Reisonderdeel | Inkoop | Product is opgebouwd uit onderdelen van verschillende leveranciers | KP2, GP1 |
| Medewerker | Beide | Wie is verantwoordelijk, wie registreert, wie keurt goed (vier ogen) | KP2, K8 |
| Klant | Klantenservice | Uniek via e-mailadres; alleen gegevens zoals in het paspoort, **geen IBAN of paspoortnummer** | P1–P4 |
| Boeking | Sales (verwijzing) | Nodig om te zien of de klant op reis is; eigendom van Sales & Boekingen | K1, P3 |
| Klantzaak / Contactmoment | Klantenservice | Eén dossier per vraag of klacht, met alle contacten chronologisch | KP1, KP4, GP1 |
| Klacht / Compensatierichtlijn | Klantenservice | Voorstel = percentage × reissom; voorgesteld en goedgekeurd door verschillende medewerkers | K9, KP3 |
| Vervolgactie | Klantenservice | Wat er nog moet gebeuren, met eigenaar en deadline | K6 |

## Bedrijfsregels in het model

- `KLANT.Email` is uniek (UK).
- `CONTRACT.Einddatum ≥ CONTRACT.Begindatum`; `AantalKamers > 0`.
- `ANNULERINGSREGEL.KostenPercentage` tussen 0 en 100.
- `KLACHT.GoedgekeurdDoor ≠ KLACHT.VoorgesteldDoor` (vier-ogenprincipe).
- Klantgegevens mogen pas worden verwijderd of geanonimiseerd als de terugkomdatum van alle boekingen voorbij is.
- Een klantzaak kan niet worden afgesloten zolang er open vervolgacties zijn.
