import requests
from bs4 import BeautifulSoup

# NAV CANADA api-endpoint
URL = "https://flightplanning.navcanada.ca/cgi-bin/Fore-obs/metar.cgi"

def _get(aerodrome, filename=None):
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

def forecast(aerodrome, filename=None):
    return _get(aerodrome, filename).split(" TAF ")[1]

# Observations are more complicated to extract than forecasts. We need
# to take the first split of the _get result, split on occurrences of
# "METAR", and filter out the first two elements in the list (which will
# be indicators of aerodrome location). Then, since there are
# potentially multiple METARs (as opposed to a single TAF), strip
# whitespace from each and then join them into a single string with
# newlines.
def observations(aerodrome, filename=None):
    result = _get(aerodrome, filename).split(" TAF ")[0].split("METAR")[2:]
    return '\n'.join(line.strip() for line in result)

