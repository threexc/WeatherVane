import re
from lxml import etree

# This file is just used to take a collected list of aerodrome data and
# transform it into an easily-accessible XML format, which will be called by
# the central functions of the WeatherData collection program

# The original file to read from and the final file to be written to
infile = "Aerodromes_original.md"
outfile = "Aerodromes.xml"

# Create the pattern to use for searching the original file. Need to clarify
# what this pattern actually consists of. Used to remove unneeded bracketed
# aerodrome abbreviations, e.g. YYZ for Toronto
pattern = re.compile(r'[\(][A-Z]{3,4}[\)]')

# Send the transformed XML data for each aerodrome to the final file
def formatAerodromes(read_file, write_file):

	# open the original file for reading and the final file for writing binary
    in_file = open(read_file, "r")
    out_file = open(write_file, "wb")

	# Convert each line in the input file to XML one-by-one
    for line in in_file:
        out_file.write(oneLineXML(line))

	# Close them up when done
    in_file.close()
    out_file.close()

# Convert an input line to XML format as specified
def oneLineXML(line):

	# Find the specified bracket pattern
    if pattern.search(line):
		# Strip out the bracket pattern
        re.sub(pattern, "", line)

	# Split the remaining line, which is delimited by hyphens. Each component
	# will eventually become its own XML element
    results = re.split(r" - ", line)

	# Create the ElementTree root for the line
    root = etree.Element("Aerodrome")

	# Create the elements of the root from the line that was split
    etree.SubElement(root, "ID").text = (results[0])[0:4]
    etree.SubElement(root, "Name").text = results[1].strip()
    etree.SubElement(root, "Location").text = results[2].strip()

	# Create the XML string to print to file in a nice format
    out_xml = etree.tostring(root, pretty_print=True)

	# Not really necessary, but will leave for now
    result_string = out_xml

	# return the results for use in formatAerodromes
    return result_string

if __name__ == "__main__":
    formatAerodromes(infile, outfile)
