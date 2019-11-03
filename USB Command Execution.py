import os
import re
import xml

# Gather data from basic shell commands
import xml.etree.ElementTree

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
ouiList = []

# Only needed to remove unnecessary elements in original xml file
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

# for record in root.findall('record'):
#
#     oui = record.find('oui').text
#     manufacturer = record.find('companyName').text
#     ouiList.append([oui, manufacturer])
#
# ouiList = str(ouiList)
# for i in range(count):
#     tempstr = arpValues[startString:endString]
#     print(tempstr)
#     match = re.findall(tempstr, ouiList)
#     print(match)
#     startString = startString + 21
#     endString = endString + 21
