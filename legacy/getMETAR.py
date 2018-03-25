import urllib.parse
import urllib.request
import sys
import re
import datetime
import os
import errno
import xml.etree.ElementTree as ET


# User agent data for submission to the page to be scraped
headers = {
        "user-agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:39.0) Gecko/20100101 Firefox/39.0",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "accept-charset": "ISO-8859-1,utf-8;q=0.7,*;q=0.3",
        "accept-encoding": "gzip,deflate,sdch",
        "accept-language": "en-US,en;q=0.8",
    }


# Raw URL of interest. Should be cleaned up so that it can be specified in
# a function
url = "https://flightplanning.navcanada.ca/cgi-bin/Fore-obs/metar.cgi"

# Create the directory passed in as a string argument
def makeMETARpath(path):
    try:
        os.makedirs(path)
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise

# Collect METAR and TAF data for a given aerodrome. The default arguments for
# page_format, language, and region should never need to be altered unless the
# website is altered first
def getMETAR(station, page_format='raw', language='anglais', region='can'):

	# Create dictionary to pass input arguments to urllib.parse.urlencode
    dict_values = {}
    dict_values['Stations'] = station
    dict_values['format'] = page_format
    dict_values['Langue'] = language
    dict_values['Region'] = region

	# Encode the input data into a URL string for opening the specific
	# station's page
    data = urllib.parse.urlencode(dict_values)

	# Encode data to UTF-8
    binary_data = data.encode("utf-8")

	# Create HTTP URL request string
    req = urllib.request.Request(url, binary_data)

	# Open the request created
    response = urllib.request.urlopen(req)

	# Read the response obtained
    the_page = response.read()

	# Decode the response
    decoded = the_page.decode('unicode_escape')

	# Clean up the received data by removing any angle-bracketed characters
    stripped = re.sub("<.*?>", "", decoded)
	# Remove newlines
    cleaned = stripped.replace('\n', '')

	# Separate the METAR and TAF data
    split = cleaned.split('TAF ', 1)[1]

    return split

# Iteratively collect each aerodrome acronym from Aerodromes.xml, then generate
# an appropriate filename for the data collected for said aerodrome based on
# the date and time that the data is obtained. Next, create a subfolder inside
# the parent path metardata. Finally, collect the intended data with getMETAR(),
# and put the data into the new file created.
def archiveMETARs():

	# Use xml.etree to parse the XML file the aerodrome data is kept in
    doc = ET.parse('Aerodromes.xml')

	# Identify the root level of the XML tree
    root = doc.getroot()

	# Iterate through the children, which correspond to the aerodromes
    for child in root:

		# Get the aerodrome's abbreviation for use in getMETAR()
        dromeID = child[0].text

		# Create a hyphen-delimited timestamp to concatenate with the aerodrome
		# ID to make the filename for the data
        date = datetime.datetime.utcnow().strftime("%Y-%m-%d %H-%M-%S")

		# Eliminate spaces so the resulting date will play nice with Unix-style
		# filenames
        fixed_date = str(date).replace(' ', '_')

		# Combine the two parts of the filename
        filename = str.join('_', (dromeID, fixed_date))

		# Specify the subfolder to store this instance of the data in
        pathname = "%s/%s" % ('metardata', dromeID)

		# Create the path if it doesn't already exist
        makeMETARpath(pathname)

		# Specify the full path for the data file. Should simplify this call to
		# use the pathname variable already created
        METARfile = "%s/%s/%s" % ('metardata', dromeID, filename)

		# Open the file for writing
        out_file = open(METARfile, 'w')

		# Write the collected aerodrome data
        out_file.write(getMETAR(dromeID))

		# Close the file
        out_file.close()


if __name__ == "__main__":
    archiveMETARs()
