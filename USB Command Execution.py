import os

# Gather data from basic shell commands
ipconfig = os.popen('ipconfig /all').read()
arp = os.popen('arp -a').read()
hostname = os.popen('hostname').read()

