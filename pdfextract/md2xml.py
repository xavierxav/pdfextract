"""
Transforme un document md transformé avec text2md en XML découpé avec le "zonage" de la cour de cassation.
"""
import argparse
import re
import sys

def main():
    parser = argparse.ArgumentParser("Markdown to XML")
    parser.add_argument('in_file', help="Markdown file")
    args = parser.parse_args()

    with open(args.in_file, "r", encoding="utf-8") as f:
        mddata = f.read()


    # Transform mddata with re here
    # see https://docs.python.org/fr/3/library/re.html
    # document must be a valid XML file
    xmldata = mddata

    # Replace markdown paragraphs with XML <p> elements
    xmldata = re.sub(r'(?<=\n)(.+?)(?=\n)', r'<p>\1</p>', xmldata)


    xml = list()
    xml.append('<?xml version="1.0" encoding="utf-8"?>')
    xml.append('<decision>')
    xml.append(xmldata)
    xml.append('</decision>')

    xml = list()
    xml.append('<?xml version="1.0" encoding="utf-8"?>')
    xml.append('<decision>')
    xml.append(xmldata)
    xml.append('</decision>')

    outdata = '\n'.join(xml)

    with open(args.in_file[:-3] + ".xml", "w", encoding="utf-8") as f:
        f.write(outdata) 

if __name__ == "__main__":
    main()