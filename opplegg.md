# HON1000 — Seminar: Autonom AI og kodeagenter (2 timer)

---

## Leselekse

**Obligatorisk (to tekster, motstridende perspektiver):**

1. Matt Shumer: *"Something big is happening"* (Fortune, 11. feb. 2026)
   https://fortune.com/2026/02/11/something-big-is-happening-ai-february-2020-moment-matt-shumer/
   AI-gründer som hevder vi er i en "februar 2020"-fase — at kodeagenter allerede gjør jobben hans bedre enn ham selv. Lest 80+ millioner ganger.

2. Paulo Carvão: *"The problem with tech's latest 'something big is happening' manifesto"* (Forbes, 13. feb. 2026)
   https://www.forbes.com/sites/paulocarvao/2026/02/13/the-problem-with-techs-latest-something-big-is-happening-manifesto/
   Harvard-forsker som svarer at Shumers budskap er et salgsargument forkledd som advarsel. Skiller mellom teknologisk kapabilitet, kommersielle insentiver og sosial tilpasning.

**Valgfritt tillegg:**

3. Peter Cappelli: *"Something big is happening in AI, but panic is the wrong reaction"* (Fortune, 28. feb. 2026)
   https://fortune.com/2026/02/28/peter-cappelli-wharton-something-big-happening-in-ai-but-not-panic-robots-are-coming/
   Wharton-professor som setter debatten i historisk perspektiv: roboter siden 1964, selvkjørende biler "innen 2019", produktivitetsløfter som aldri kom.

**Refleksjonsspørsmål:** Er Shumers pandemi-analogi treffende eller villedende? Hvem har mest å vinne på at folk er bekymret? Hva ville "autonom AI" bety for ditt eget fag?

---

## Seminarstruktur

### 1. Diskusjon av tekstene (~30 min)
Hva er Shumers sterkeste og svakeste argument? Hva tilfører kritikerne? Hvem har bevisbyrden?

### 2. Live-demo av Claude Code (~40 min)
Vis en kodeagent i aksjon — først noe som imponerer, deretter noe som avslører svakheter. Se foreslåtte prompts nedenfor. Diskuter underveis.

### 3. Gruppearbeid (~30 min)
Tverrfaglige grupper velger en oppgave fra ett av sine fag som en AI-agent i prinsippet kunne utføre. Diskuter kapabilitet, pålitelighet og konsekvenser av feil.

### 4. Oppsummering (~20 min)
Når er et system "autonomt" i meningsfull forstand? Hva er forskjellen mellom verktøy og agent?

---

## Claude Code-prompts for demonstrasjon

### Prompt 1: "Det imponerende" — fungerende nettside fra ingenting

```
Lag en interaktiv nettside som viser Norges befolkningsutvikling fra 1900 til 2024.

Krav:
- Bruk reelle tall fra SSB (hardkod dataene direkte i koden — ikke bruk API)
- Vis dataene som et interaktivt linjediagram med Chart.js
- Brukeren skal kunne hover over datapunkter for å se årstall og befolkningstall
- Inkluder en kort forklarende tekst på norsk over diagrammet
- Alt skal være i én HTML-fil

Etter at du har skrevet koden: åpne filen, test at den fungerer,
og fiks eventuelle problemer. Iterer til diagrammet rendrer korrekt
og interaksjonen fungerer. Ikke lever fra deg før du har verifisert
at siden fungerer.
```

**Poeng å diskutere:** Hastigheten. At naturlig språk er "programmeringsspråket." At Shumer beskriver nøyaktig dette.

### Prompt 2: "Det problematiske" — hallusinasjon og falsk selvsikkerhet

```
Skriv et Python-script som henter sanntids værdata for Oslo fra
Meteorologisk institutts Frost API (frost.met.no), beregner
gjennomsnittlig temperatur for de siste 7 dagene, og printer resultatet.

Bruk riktig autentisering og feilhåndtering. Test at scriptet kjører
og returnerer korrekte data. Fiks eventuelle feil og iterer til det fungerer.
```

**Poeng å diskutere:** Claude Code vil sannsynligvis generere kode som *ser* riktig ut men feiler — den kjenner kanskje ikke API-et korrekt, den har ikke API-nøkkel, den kan hallusinere endepunkter. Koden ser profesjonell ut, men fungerer ikke. Hva betyr det for tillit?

### Prompt 3 (alternativ): Faglig resonering

```
Bevis at det finnes uendelig mange primtall. Presenter beviset steg for steg,
og skriv deretter et Python-script som verifiserer de første 20 stegene
i resonnementet ditt med konkrete tall. Test scriptet og vis output.
```

**Poeng å diskutere:** Skillet mellom å reprodusere et kjent bevis (som den klarer) og å resonnere selvstendig. Hva skjer om du ber om et *uløst* problem i stedet?

---

## Studentene prøver selv

Oppfordre studentene til å prøve Claude Code (krever Claude Pro, $20/mnd) eller Claude i chat (gratis) på noe fra sitt eget fag. Dokumenter hva som fungerte og hva som ikke fungerte — ta med til neste gang.

Quickstart: https://code.claude.com/docs/en/quickstart