import os
import re
import xml.etree.ElementTree

# Only needed to remove unnecessary elements in original xml file
# treeinit = xml.etree.ElementTree.parse('OUI.xml')
# rootinit = tree.getroot()
# for elem in root.iter():
#     for child in list(elem):
#         if child.tag == 'isPrivate':
#             elem.remove(child)
#         if child.tag == 'companyAddress':
#             elem.remove(child)
#         if child.tag == 'countryCode':
#             elem.remove(child)
#         if child.tag == 'assignmentBlockSize':
#             elem.remove(child)
#         if child.tag == 'dateCreated':
#             elem.remove(child)
#         if child.tag == 'dateUpdated':
#             elem.remove(child)
#
# tree.write('OUI2.xml')

# Gather data from basic shell commands
ipconfig = os.popen('ipconfig /all').read()
arp = os.popen('arp -a').read()
hostname = os.popen('hostname').read()
hostname = hostname.rstrip() + '.txt'

# Create the list of MAC addresses and gather the number of results for iterating through
arpValues = re.findall("..-..-..-..-..-..", arp)
count = len(arpValues)
arpValues = str(arpValues)

# Replace the '-' with a ':' for comparing the OUI values against the xml file
arpValues = arpValues.replace('-', ':')

# Declare the index's of the OUI portion of the MAC addresses
startString = 2
endString = 10

# Import the xml file that contains the list of known OUIs
tree = xml.etree.ElementTree.parse('OUI2.xml')
root = tree.getroot()
results = []

# Iterate over the list of arpValues
for arpValuesEntry in range(count):
    # Grab OUI portion of MAC address
    oui = arpValues[startString:endString]
    oui = oui.upper()
    xmlEntry = 0
    # Iterate through the tree structure of xml document
    for record in root:
        rootHolder = root[xmlEntry].findtext("oui")
        if rootHolder == oui:
            # Create results list
            results.append([root[xmlEntry].findtext("oui"), root[xmlEntry].findtext("companyName")])
        # Increment entry in xml document
        xmlEntry = xmlEntry + 1
    # Increment entry in list of arpValues
    startString = startString + 21
    endString = endString + 21

# Save document to text file
file = open(hostname, 'w+')
ipResult = re.findall('IPv4 Address.*', str(ipconfig))
ipResult = str(ipResult)
ipResult = ipResult.replace(". ", "")
ipResult = ipResult.replace("[", "")
ipResult = ipResult.replace("]", "")
ipResult = ipResult.replace(" '", "'")
ipResult = ipResult.replace(",", "\n")
ipResult = ipResult.replace("'", "")
results = str(results)
results = results.replace("],", "\n")
results = results.replace("[[", "")
results = results.replace("[", "")
results = results.replace("]", "")
results = results.replace(" '", "'")
results = results.replace(",'", "-->")
results = results.replace("'", "")
file.write("List of known IP addresses\n")
file.write(ipResult)
file.write("\n\n")
file.write("List of known network adapters from arp table\n")
file.write(results)
file.close
