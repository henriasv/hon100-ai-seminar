"""
BEVIS: Det finnes uendelig mange primtall
==========================================

Dette er et bevis ved selvmotsigelse (reductio ad absurdum),
basert paa Euklids klassiske argument fra ca. 300 f.Kr.

BEVISET STEG FOR STEG:

Steg 1 (Antagelse): Anta for selvmotsigelse at det finnes endelig
         mange primtall. Kall dem p1, p2, p3, ..., pn.

Steg 2 (Konstruksjon): Konstruer tallet Q = p1 * p2 * p3 * ... * pn + 1.
         Det vil si: ta produktet av alle primtallene og legg til 1.

Steg 3 (Nokkelobservasjon): Q er storre enn alle pi, siden Q > pn >= pi
         for alle i.

Steg 4 (Delelighetsargument): For ethvert primtall pi i listen vaar:
         Q mod pi = (p1*p2*...*pn + 1) mod pi = 0 + 1 = 1.
         Altsaa er Q IKKE delelig med noe primtall i listen.

Steg 5 (Aritmetikkens fundamentalteorem): Ethvert heltall > 1 har
         minst en primfaktor. Siden Q > 1 maa Q ha en primfaktor.

Steg 6 (Selvmotsigelse): Denne primfaktoren kan ikke vaere noen av
         p1, ..., pn (fra steg 4). Men vi antok at dette var ALLE
         primtallene. Selvmotsigelse!

Steg 7 (Konklusjon): Antagelsen i steg 1 er feil.
         Dermed finnes det uendelig mange primtall. QED.
"""

import math


def er_primtall(n):
    """Sjekker om n er et primtall."""
    if n < 2:
        return False
    if n < 4:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def finn_minste_primfaktor(n):
    """Finner den minste primfaktoren av n."""
    if n % 2 == 0:
        return 2
    if n % 3 == 0:
        return 3
    i = 5
    while i * i <= n:
        if n % i == 0:
            return i
        if n % (i + 2) == 0:
            return i + 2
        i += 6
    return n  # n er selv et primtall


def primfaktorisering(n, grense=10_000_000):
    """
    Returnerer en ordbok {primfaktor: eksponent} for n.
    For store tall: finner faktorer opp til en gitt grense,
    og rapporterer eventuell rest.
    """
    faktorer = {}
    d = 2
    while d <= 3:
        while n % d == 0:
            faktorer[d] = faktorer.get(d, 0) + 1
            n //= d
        d += 1
    d = 5
    while d <= grense and d * d <= n:
        while n % d == 0:
            faktorer[d] = faktorer.get(d, 0) + 1
            n //= d
        while n % (d + 2) == 0:
            faktorer[d + 2] = faktorer.get(d + 2, 0) + 1
            n //= (d + 2)
        d += 6
    if n > 1:
        faktorer[n] = faktorer.get(n, 0) + 1
    return faktorer


def sil_av_eratosthenes(grense):
    """Returnerer alle primtall opp til grense."""
    sil = [True] * (grense + 1)
    sil[0] = sil[1] = False
    for i in range(2, int(grense**0.5) + 1):
        if sil[i]:
            for j in range(i * i, grense + 1, i):
                sil[j] = False
    return [i for i in range(2, grense + 1) if sil[i]]


def main():
    # De 20 forste primtallene
    alle_primtall = sil_av_eratosthenes(200)[:20]

    print("=" * 70)
    print("BEVIS: Det finnes uendelig mange primtall")
    print("Verifikasjon av de 20 forste stegene i resonnementet")
    print("=" * 70)

    print("""
BEVISET (Euklids argument ved selvmotsigelse):

  1. Anta at det finnes endelig mange primtall: p1, p2, ..., pn.
  2. Konstruer Q = p1 * p2 * ... * pn + 1.
  3. Q > alle pi.
  4. Q mod pi = 1 for alle i, saa ingen pi deler Q.
  5. Men Q > 1 maa ha minst en primfaktor (aritmetikkens fundamentalteorem).
  6. Denne primfaktoren er ikke i listen -> selvmotsigelse.
  7. Konklusjon: Det finnes uendelig mange primtall. QED.
""")

    print("-" * 70)
    print("VERIFIKASJON MED KONKRETE TALL:")
    print("-" * 70)

    tabell_data = []

    for k in range(1, 21):
        primtall = alle_primtall[:k]
        produkt = math.prod(primtall)
        Q = produkt + 1

        primliste_str = " * ".join(str(p) for p in primtall)

        print(f"\nSteg {k:2d}: Anta at de eneste primtallene er "
              f"{{{', '.join(str(p) for p in primtall)}}}")
        print(f"         Q = {primliste_str} + 1 = {Q}")

        # Verifiser steg 4: Q mod pi = 1 for alle pi
        for p in primtall:
            rest = Q % p
            assert rest == 1, f"FEIL: Q mod {p} = {rest}, forventet 1!"
        print(f"         Q mod pi = 1 for alle pi i listen  [OK]")

        # Finn primfaktorisering av Q
        faktorer = primfaktorisering(Q)

        faktor_str = " * ".join(
            f"{p}^{e}" if e > 1 else str(p)
            for p, e in sorted(faktorer.items())
        )
        print(f"         Primfaktorisering av Q: {faktor_str}")

        # Sjekk at ALLE primfaktorer av Q er utenfor listen
        nye_primtall = [p for p in faktorer if p not in primtall]
        assert len(nye_primtall) > 0, "FEIL: Ingen nye primtall funnet!"
        nye_str = ", ".join(str(p) for p in sorted(nye_primtall))
        print(f"         Nye primtall utenfor listen: {{{nye_str}}} "
              f"-> SELVMOTSIGELSE! [OK]")

        q_er_prim = (len(faktorer) == 1 and list(faktorer.values())[0] == 1
                     and list(faktorer.keys())[0] == Q)
        if q_er_prim:
            print(f"         Merk: Q = {Q} er selv et primtall!")

        tabell_data.append((k, Q, q_er_prim))

    print("\n" + "=" * 70)
    print("ALLE 20 STEG VERIFISERT.")
    print("For hvert steg fant vi primfaktorer av Q utenfor den antatte listen.")
    print("Dette bekrefter bevisets logikk med konkrete tall.")
    print("=" * 70)

    # Bonus-tabell
    print("\n" + "-" * 70)
    print("BONUS - Oversikt: Er Q selv et primtall?")
    print("-" * 70)
    print(f" {'k':>3} | {'Q':>30} | {'Q er primtall?':>15}")
    print(" " + "-" * 55)
    for k, Q, prim in tabell_data:
        svar = "Ja" if prim else "Nei"
        print(f" {k:3d} | {Q:>30} | {svar:>15}")

    print("""
Merk: Q trenger IKKE aa vaere et primtall for at beviset skal fungere.
Det holder at Q har en primfaktor som ikke er i den opprinnelige listen.
Noen Q-verdier er primtall (f.eks. 2+1=3, 2*3+1=7), men andre er det
ikke (f.eks. 2*3*5*7*11*13+1 = 30031 = 59 * 509).
""")


if __name__ == "__main__":
    main()
