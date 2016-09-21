import urllib.parse
import urllib.request
import sys
import re
import datetime
import os
import errno
import xml.etree.ElementTree as ET

headers = {
        "user-agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:39.0) Gecko/20100101 Firefox/39.0",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "accept-charset": "ISO-8859-1,utf-8;q=0.7,*;q=0.3",
        "accept-encoding": "gzip,deflate,sdch",
        "accept-language": "en-US,en;q=0.8",
    }

url = "https://flightplanning.navcanada.ca/cgi-bin/Fore-obs/metar.cgi"

def makeMETARpath(path):
    try:
        os.makedirs(path)
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise

def getMETAR(station, page_format='raw', language='anglais', region='can'):

    dict_values = {}
    dict_values['Stations'] = station
    dict_values['format'] = page_format
    dict_values['Langue'] = language
    dict_values['Region'] = region

    data = urllib.parse.urlencode(dict_values)
    binary_data = data.encode("utf-8")
    req = urllib.request.Request(url, binary_data)
    response = urllib.request.urlopen(req)
    the_page = response.read()

    decoded = the_page.decode('unicode_escape')
    stripped = re.sub("<.*?>", "", decoded)
    cleaned = stripped.replace('\n', '')
    split = cleaned.split('TAF ', 1)[1]
    return split

def archiveMETARs():
    doc = ET.parse('Aerodromes.xml')
    root = doc.getroot()
    for child in root:
        dromeID = child[0].text
        date = datetime.datetime.utcnow().strftime("%Y-%m-%d %H-%M-%S")
        fixed_date = str(date).replace(' ', '_')
        filename = str.join('_', (dromeID, fixed_date))
        #print (combined)
        pathname = "%s/%s" % ('metardata', dromeID)
        makeMETARpath(pathname)
        METARfile = "%s/%s/%s" % ('metardata', dromeID, filename)
        out_file = open(METARfile, 'w')
        out_file.write(getMETAR(dromeID))
        out_file.close()


if __name__ == "__main__":
    archiveMETARs()
