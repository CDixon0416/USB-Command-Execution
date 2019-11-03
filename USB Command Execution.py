import os
import re

# Gather data from basic shell commands
ipconfig = os.popen('ipconfig /all').read()
arp = os.popen('arp -a').read()
hostname = os.popen('hostname').read()
print(arp)

arpValues = re.findall("..-..-..-..-..-..", arp)
count = len(arpValues)

arpValues = str(arpValues)
arpValues = arpValues.replace('-', ':')

startString = 2
endString = 10
for i in range(count):
    tempstr = arpValues[startString:endString]
    print(tempstr)
    startString = startString + 21
    endString = endString + 21
print(arpValues)
