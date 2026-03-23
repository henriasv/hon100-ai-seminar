"""
Henter sanntids værdata for Oslo fra Meteorologisk institutts Frost API (frost.met.no),
beregner gjennomsnittlig temperatur for de siste 7 dagene, og printer resultatet.
"""

import requests
import os
from datetime import datetime, timedelta

# Frost API-konfigurasjon
FROST_API_URL = "https://frost.met.no/observations/v0.jsonld"
CLIENT_ID = os.environ.get("FROST_CLIENT_ID", "")

if not CLIENT_ID:
    print("ADVARSEL: Miljøvariabelen FROST_CLIENT_ID er ikke satt.")
    print("Du kan registrere deg på https://frost.met.no/ for å få en klient-ID.")
    print("Sett den med: export FROST_CLIENT_ID='din-klient-id'")
    print()

# Oslo (Blindern) værstasjon
STATION_ID = "SN18700"

# Beregn datoer for de siste 7 dagene
end_date = datetime.now()
start_date = end_date - timedelta(days=7)

# Formater datoer for API-et
start_str = start_date.strftime("%Y-%m-%d")
end_str = end_date.strftime("%Y-%m-%d")

print(f"Henter temperaturdata for Oslo (Blindern) fra {start_str} til {end_str}...")
print()

# Sett opp parametere for API-kallet
parameters = {
    "sources": STATION_ID,
    "elements": "mean(air_temperature P1D)",
    "referencetime": f"{start_str}/{end_str}",
}

try:
    # Gjør API-kallet med autentisering (client_id som brukernavn, tomt passord)
    response = requests.get(FROST_API_URL, params=parameters, auth=(CLIENT_ID, ""))

    print(f"HTTP-statuskode: {response.status_code}")

    if response.status_code == 200:
        data = response.json()

        if "data" not in data:
            print("Feil: Ingen 'data'-felt i responsen.")
            print(f"Respons: {data}")
        else:
            observations = data["data"]
            temperatures = []

            for obs in observations:
                ref_time = obs["referenceTime"][:10]
                for element in obs["observations"]:
                    if "mean(air_temperature" in element.get("elementId", ""):
                        temp = element["value"]
                        temperatures.append(temp)
                        print(f"  {ref_time}: {temp:.1f} °C")

            if temperatures:
                avg_temp = sum(temperatures) / len(temperatures)
                print()
                print(f"Gjennomsnittlig temperatur siste {len(temperatures)} dager: {avg_temp:.1f} °C")
            else:
                print("Ingen temperaturdata funnet i responsen.")

    elif response.status_code == 401:
        print("Feil 401: Ikke autorisert. Sjekk at FROST_CLIENT_ID er korrekt.")
        print(f"Brukt klient-ID: '{CLIENT_ID[:8]}...' " if len(CLIENT_ID) > 8 else f"Brukt klient-ID: '{CLIENT_ID}'")

    elif response.status_code == 404:
        print("Feil 404: Ressursen ble ikke funnet. Sjekk URL og parametere.")
        print(f"URL: {response.url}")

    else:
        print(f"Feil: Uventet statuskode {response.status_code}")
        print(f"Respons: {response.text[:500]}")

except requests.exceptions.ConnectionError as e:
    print(f"Tilkoblingsfeil: Kunne ikke koble til {FROST_API_URL}")
    print(f"Detaljer: {e}")

except requests.exceptions.Timeout:
    print("Feil: Forespørselen tok for lang tid (timeout).")

except Exception as e:
    print(f"Uventet feil: {type(e).__name__}: {e}")
