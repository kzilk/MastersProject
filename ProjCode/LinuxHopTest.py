import subprocess

def checkLinHop():
    #run check for IP Address
    ipCheck = subprocess.run("ip route | grep default | awk '{print $3}'",
                             shell=True, capture_output=True, text=True)
    #save IP as variable
    ipAddress = ipCheck.stdout.strip()

    traceCommand = f"traceroute {ipAddress} | tail -n 1"
    routeTest = subprocess.run(traceCommand, shell=True, capture_output=True, text=True)

    #get number of hops
    output = routeTest.stdout.strip()
    lastLine = output
    connectionCount = lastLine[:2].strip()

    if connectionCount != "1":
        hopText = 'Multiple hops to router'
        return hopText
    else:
        hopText = 'Single connection hop'
        return hopText
