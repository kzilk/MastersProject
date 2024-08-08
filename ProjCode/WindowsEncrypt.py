import re
import os

def command():
    os.system("netsh wlan show interfaces > network.txt")
    wireless_name = None
    with open("network.txt", "r") as file:
        for line in file:
            if "SSID" in line:
                wireless_name = line.split(":")[1].strip()
                #print(wireless_name)
                break

    os.system(f"netsh wlan show profile name=\"{wireless_name}\" > authentication.txt")
    with open('authentication.txt', 'r') as file:
        command_output = file.read()
    return command_output

def search_command_output(command_output):
    authentication = re.search(r'Authentication\s*:\s*(.+)', command_output)
    if authentication:
        authentication_type = authentication.group(1).strip()
        return authentication_type
    else:
        return None

def check_authentication():
    command_output = command()
    wifi_authentication = search_command_output(command_output)

    if wifi_authentication is not None:
        return wifi_authentication