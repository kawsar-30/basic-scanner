import subprocess 
import re 
import sys 
import time


port=sys.argv[1]
ip_addr=sys.argv[2]


command=["nmap", "-sT", "-sV", "-O", "-p", port, ip_addr]
result=subprocess.run(command,capture_output=True,text=True)

# Primary Information
# match=re.search(r"(\d+)/(w+)\s+(\w+)\s+(\w+)\s+(\w+)\s+(\d+\.\d+\.\d+)", result.stdout)
match=re.search( r"(\d+)/(tcp|udp)\s+(\w+)\s+(\S+)\s*(.*)",result.stdout)
if match.group(3) == "open":
    print("Port is open")
    print("Wait a some moment... ")
    time.sleep(3)
    print(f"port is : {match.group(1)}")
    print(f"protocol is : {match.group(2)}")
    print(f"STATE is : {match.group(3)}")
    print(f"SERVICE is : {match.group(4)}")
    print(f"VERSIONS : {match.group(5)} ")
    
else:
    print("Port not open")





# Mac address releated Information
mac_addr_macth=re.search(r"MAC Address: (([A-F0-9a-f]{2}:){5}[A-F0-9a-f]{2})\s*\(VMware\)",result.stdout)
# ^MAC Address:\s*([0-9A-Fa-f]{2}:){5}[0-9A-Fa-f]{2}\s*\(VMware\)$
if mac_addr_macth:
    print(f"the mac address is : {mac_addr_macth.group(1)}")

else:
 print('<mac address not found>')


#Operating System releated Information
os_match=re.search(r"Running:\s+(\w+)\s+([0-9A-Za-z-](\.[0-9A-Za-z-]+)+)",result.stdout)


if os_match:
   print(f"The service operating syestem running on : {os_match.group(1)} {os_match.group(2)}")

else:
   print(f"os information not found")


os_details_match=(r"OS details:\s+(\w+)\s+([0-9A-Za-z-](\.[0-9A-Za-z-]+)+)",result.stdout)

if os_details_match:
  print(f"os details : {os_details_match.group(1)} {os_details_match.group(2)}")

else: 
   print("No Os Details Found")






