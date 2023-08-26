import requests
from bs4 import BeautifulSoup

# NAV CANADA api-endpoint
URL = "https://flightplanning.navcanada.ca/cgi-bin/Fore-obs/metar.cgi"

def forecast(aerodrome, filename=None):
    PARAMS = {
        'NoSession': "",
        'Stations': aerodrome,
        'format': "raw",
        'Langue': "anglais",
        'Region': "can",
        'Location': "",
    }

    if filename is None:
        response = requests.get(url=URL, params=PARAMS)

        soup = BeautifulSoup(response.content, 'html.parser')

        for data in soup(['style', 'script']):
            data.decompose()

        content = ' '.join(soup.stripped_strings)

        # Remove anything that isn't actual METAR or TAF data
        content = content[content.find("METAR"):].split("Your", 1)[0]

    else:
        with open(filename, 'r') as f:
            content = f.read()

    return content
