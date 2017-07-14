"""
This script reboot an Polycom HDX endpoint
by using telnet

"""

import telnetlib
import time
import subprocess
import sys

password = sys.argv[1]
telnet_port = 23
telnet_timeout = 15
reading_timeout = 15

#List of HDX Video conference endpoints passed as arguments
endpoints = [ sys.argv[2], sys.argv[3]]

for i in endpoints:
    ping_endpoint = subprocess.call(['ping','-c','1','-w','1',i])
    if ping_endpoint == 0:
        telnet = telnetlib.Telnet(i, telnet_port, telnet_timeout)
        time.sleep(4)
        output = telnet.read_until("Password:", reading_timeout)
        time.sleep(4)
        telnet.write(password + "\n")
        time.sleep(4)
        telnet.write("\n")
        time.sleep(4)
        #Rebooting the device
        telnet.write("reboot now\n")
    else:
	    print 'HDX '+i+' is Unreachable'
           

