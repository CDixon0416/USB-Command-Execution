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
tree = xml.etree.ElementTree.parse('OUI.xml')
root = tree.getroot()
ouiList = []
for record in root.findall('record'):
    oui = record.find('oui').text
    manufacturer = record.find('companyName').text
    ouiList.append([oui, manufacturer])

for i in range(count):
    tempstr = arpValues[startString:endString]
    startString = startString + 21
    endString = endString + 21
