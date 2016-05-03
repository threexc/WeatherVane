import re
from lxml import etree

infile = "Aerodromes_original.md"
outfile = "Aerodromes.xml"

pattern = re.compile(r'[\(][A-Z]{3,4}[\)]')

def formatAerodromes(read_file, write_file):
    in_file = open(read_file, "r")
    out_file = open(write_file, "wb")
    for line in in_file:
        out_file.write(oneLineXML(line))
    in_file.close()
    out_file.close()


def oneLineXML(line):
    if pattern.search(line):
        re.sub(pattern, "", line)
    results = re.split(r" - ", line)
    #print(results[0])
    root = etree.Element("Aerodrome")
    etree.SubElement(root, "ID").text = (results[0])[0:4]
    etree.SubElement(root, "Name").text = results[1].strip()
    etree.SubElement(root, "Location").text = results[2].strip()
    out_xml = etree.tostring(root, pretty_print=True)
    result_string = out_xml
    return result_string

if __name__ == "__main__":
    formatAerodromes(infile, outfile)
