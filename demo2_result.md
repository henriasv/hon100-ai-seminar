# Demo 2: Frost API - Resultat

## Hva scriptet gjor

Scriptet (`demo2_frost.py`) forsaker a:

1. Koble til Meteorologisk institutts Frost API (`frost.met.no`)
2. Hente daglig gjennomsnittstemperatur for Oslo (Blindern, stasjon SN18700) de siste 7 dagene
3. Beregne og skrive ut gjennomsnittstemperaturen

## Kjorte det vellykket?

**Nei.** Scriptet feiler med HTTP 401 (Unauthorized).

## Hvilke feil oppsto

### Feil 1: Manglende `requests`-modul
- Forste forsok feilet med `ModuleNotFoundError: No module named 'requests'`
- Laget et virtuelt miljo og installerte `requests` - dette ble fikset

### Feil 2: HTTP 401 - Ikke autorisert
- Scriptet kjorer teknisk sett, men API-kallet returnerer 401
- Uten gyldig API-nokkel (FROST_CLIENT_ID) er det umulig a hente data
- Ogsa testet med en falsk nokkel (`fake-test-id-12345`) - samme resultat

## Hvorfor feilet det

**Hovedarsak: Manglende API-nokkel.**

Frost API krever registrering pa https://frost.met.no/ for a fa en personlig klient-ID. Denne brukes som brukernavn i HTTP Basic Auth. Uten en gyldig nokkel returnerer API-et 401 Unauthorized.

AI-en kan **ikke** skaffe seg en slik nokkel pa egen hand - det krever manuell registrering med e-postadresse.

### Var koden ellers korrekt?

Koden ser rimelig korrekt ut:
- **Riktig API-endepunkt**: `https://frost.met.no/observations/v0.jsonld` er et gyldig endepunkt
- **Riktig stasjons-ID**: SN18700 er Blindern (Oslo)
- **Riktig autentiseringsmetode**: HTTP Basic Auth med klient-ID som brukernavn
- **Rimelig elementID**: `mean(air_temperature P1D)` er en gyldig elementkode i Frost API

Men: vi kan **ikke verifisere** at responsen faktisk parses korrekt uten en fungerende nokkel. Det kan vaere feil i parsing-logikken som forst viser seg nar man far ekte data.

## Hva dette demonstrerer om AI-begrensninger

1. **AI kan ikke skaffe eksterne ressurser**: Selv om AI-en vet at det trengs en API-nokkel og vet hvordan man registrerer seg, kan den ikke faktisk gjore det. Den kan skrive kode som *ser riktig ut*, men som er umulig a kjore uten menneskelig intervensjon.

2. **Kode som ser riktig ut vs. kode som fungerer**: Scriptet er velskrevet med god feilhandtering og riktig API-bruk. Det *ser* overbevisende ut. Men det er fundamentalt ubrukelig uten en API-nokkel - noe som er umulig a oppdage bare ved a lese koden.

3. **Umulig a verifisere uten ekte miljo**: AI-en kan ikke teste om parsing-logikken faktisk fungerer med ekte API-responser. Selv om endepunkter og parametere *sannsynligvis* er riktige, er det ingen garanti for at responsformatet parses korrekt.

4. **Overbevisende men uverifisert**: Koden bruker kjente, korrekte detaljer (stasjonsnavn, API-URL, autentiseringsmetode) som gir et inntrykk av at alt er riktig. Men den egentlige testen - a faktisk hente og parse data - er umulig uten en gyldig nokkel.

5. **Prompten ba AI-en "fikse feil og iterere til det fungerer"**: AI-en kan ikke oppfylle dette kravet fordi den fundamentale feilen (manglende API-nokkel) ikke er noe AI-en kan fikse. Iterasjonsloopen stopper.
