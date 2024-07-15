import subprocess
import re


def checkWinHop():
    # Run check for IP Address
    ipCheck = subprocess.run("ipconfig", shell=True, capture_output=True, text=True)

    # get the ip address
    ipAddress = re.search(r'Default Gateway[ .:]*([0-9.]+)', ipCheck.stdout)
    ipAddress = ipAddress.group(1)


    traceCommand = f"tracert -h 1 {ipAddress}"
    routeTest = subprocess.run(traceCommand, shell=True, capture_output=True, text=True)

    # Get the number of hops
    output = routeTest.stdout.strip()
    lastLine = output
    connectionCount = lastLine.count('*')

    if connectionCount > 1:
        #multiple hops to router
        return 'RED'
    else:
        #1 hop to router
        return 'GREEN'


#test=checkWinHop()
#print(test)