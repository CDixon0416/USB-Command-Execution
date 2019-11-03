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

for i in range(count):
    oui = arpValues[startString:endString]
    oui = oui.upper()
    x = 0
    for record in root:
        rootHolder = root[x].findtext("oui")
        if rootHolder == oui:
            print(root[x].findtext("oui"), root[x].findtext("companyName"))
        x = x + 1
    startString = startString + 21
    endString = endString + 21
