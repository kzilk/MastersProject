import os

def wireless_network_name():
    os.system("netsh wlan show interfaces > network.txt")
    wireless_name = None
    with open("network.txt", "r") as file:
        for line in file:
            if "SSID" in line:
                wireless_name = line.split(":")[1].strip()
                break
    return wireless_name

test = wireless_network_name()

print(test)
