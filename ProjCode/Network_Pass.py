import os

def testWindowsPassword():
    # Get the connected network's SSID
    os.system("netsh wlan show interfaces > network.txt")
    wireless_name = None
    with open("network.txt", "r") as file:
        for line in file:
            if "SSID" in line:
                wireless_name = line.split(":")[1].strip()
                break

    # Get the profile details of the connected network
    os.system(f"netsh wlan show profile name=\"{wireless_name}\" key=clear > pass_check.txt")
    password = None
    with open('pass_check.txt', 'r') as file:
        for line in file:
            if "Key Content" in line:
                password = line.split(":")[1].strip()
                break

    # Check if a password was found
    if password is not None:
        #there is a password requirement
        return "GREEN, Password requirement found"
    else:
        #password field is null
        return "RED, password requirement not found"


#test = testWindowsPassword()
#print(test)
