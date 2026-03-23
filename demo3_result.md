# Demo 3: Bevis for uendelig mange primtall

## 1. Beviset som ble presentert

AI-en presenterte Euklids klassiske bevis ved selvmotsigelse (reductio ad absurdum):

1. **Antagelse:** Anta at det finnes endelig mange primtall: p1, p2, ..., pn.
2. **Konstruksjon:** Konstruer Q = p1 * p2 * ... * pn + 1.
3. **Observasjon:** Q er stoerre enn alle pi.
4. **Delelighetsargument:** Q mod pi = 1 for alle i, saa ingen pi deler Q.
5. **Fundamentalteoremet:** Q > 1 maa ha minst en primfaktor.
6. **Selvmotsigelse:** Denne primfaktoren er ikke blant p1, ..., pn, men vi antok det var alle primtallene.
7. **Konklusjon:** Antagelsen er feil. Det finnes uendelig mange primtall. QED.

## 2. Python-scriptets output

Scriptet verifiserte alle 20 steg med konkrete tall. For hvert steg k tok det de k foerste primtallene, beregnet Q = produkt + 1, og viste at:
- Q mod pi = 1 for alle primtall pi i listen (verifisert)
- Q har primfaktorer som ikke er i den opprinnelige listen (verifisert)

Noen hoeydepunkter:

| k | Q | Primfaktorer utenfor listen | Q er primtall? |
|---|---|---|---|
| 1 | 3 | {3} | Ja |
| 2 | 7 | {7} | Ja |
| 5 | 2311 | {2311} | Ja |
| 6 | 30031 | {59, 509} | Nei |
| 11 | 200560490131 | {200560490131} | Ja |
| 19 | 7858321551080267055879091 | {7858321551080267055879091} | Ja |
| 20 | 557940830126698960967415391 | {1063, 303049, 598841, 2892214489673} | Nei |

Alle 20 steg passerte alle assertions -- bevisets logikk ble bekreftet med konkrete tall.

## 3. Demonstrerer dette genuin resonnering eller reproduksjon av kjente resultater?

**Kort svar: Hovedsakelig reproduksjon, men med noen nyanser.**

Beviset for at det finnes uendelig mange primtall er et av de mest kjente bevisene i matematikkens historie. Det er gjengitt i utallige laereboekerboeker og finnes overalt paa internett. Det er naermest garantert at dette beviset fantes i treningsdataene til AI-modellen, trolig i hundrevis av varianter.

Det AI-en gjorde som gaar utover ren reproduksjon:
- **Strukturering:** Beviset ble presentert steg for steg med klar logisk flyt
- **Verifikasjon:** Python-koden ble skrevet for aa verifisere hvert steg med konkrete tall
- **Korrekt implementasjon:** Faktoriseringen og modulo-sjekkene er riktig implementert
- **Bonusobservasjon:** Tabellen over hvilke Q-verdier som selv er primtall er en relevant tilleggsanalyse

Men det er **ingen grunn til aa tro at modellen "forstaar" beviset** i den forstand at den kan generalisere bevisstrategien til nye, ukjente problemer. Den gjenkjenner moensteret "bevis at noe er uendelig -> bruk selvmotsigelse" fra treningen.

## 4. Hva skjer om man ber om noe virkelig nytt?

Tenk paa dette tankeeksperimentet: Hva om vi ba AI-en bevise noe som **ingen har bevist foer**?

Begrensninger som ville bli tydelige:
- **Ingen treningsdata aa stoette seg paa:** For genuint uloeste problemer (f.eks. Goldbachs formodning, Riemannhypotesen) kan ikke AI-en reprodusere et bevis som ikke eksisterer.
- **Manglende dyp forstaaelse:** AI-en kan ikke bygge nye matematiske intuisjoner fra grunn av. Den kan kombinere kjente teknikker, men har vanskeligheter med aa oppfinne helt nye bevisstrategier.
- **Hallusinering:** Ved press til aa bevise noe ukjent, vil AI-en sannsynligvis produsere noe som *ser ut som* et gyldig bevis, men inneholder subtile logiske feil.
- **Intet arbeidsminne for utforskning:** Matematikere proever mange blindveier, bygger intuisjon over tid, og har "aha-oeyeblikk". AI-en genererer tekst sekvensielt uten denne typen kreativ utforskning.

Et mellomtilfelle: AI-en kan potensielt **kombinere kjente teknikker paa nye maater** -- f.eks. bruke en bevisstrategi fra ett felt paa et problem fra et annet felt. Men dette er noe annet enn genuint nytt matematisk resonnement.

## 5. Hva dette demonstrerer om AI-ens evner og begrensninger

### Styrker
- **Reproduksjon og formidling:** AI-en er utmerket til aa reprodusere kjente bevis og presentere dem klart og strukturert.
- **Kobling mellom teori og kode:** Evnen til aa oversette et abstrakt bevis til konkret, kjoeerende kode er imponerende og nyttig.
- **Korrekthet i implementasjon:** Python-scriptet er korrekt, haandterer store tall, og verifiserer bevisets logikk paa en meningsfull maate.
- **Pedagogisk verdi:** Presentasjonen ville fungert godt i en undervisningssituasjon.

### Begrensninger
- **Ikke genuin matematisk kreativitet:** AI-en oppfinner ikke nye bevis -- den rekombinerer moenstre fra treningsdata.
- **Overbevisende men potensielt feil:** Formatet og strukturen ser alltid overbevisende ut, uavhengig av om innholdet er riktig.
- **Ingen selvkritikk:** AI-en ville ikke spontant si "dette beviset er trivielt og kjent fra foer" med mindre den ble spurt.
- **Begrenset til "distribusjon":** Modellen opererer innenfor distribusjonen av treningsdataene. Jo lenger vi beveger oss fra kjent matematikk, jo mer upaalitelig blir den.

### Konklusjon
Denne demoen viser at AI er et **kraftig verktoy for matematisk kommunikasjon og verifisering**, men ikke (ennaa) en selvstendig matematisk tenker. Verdien ligger i aa **forsterke menneskelig tenkning** -- organisere, formalisere, og verifisere -- heller enn aa erstatte den.
