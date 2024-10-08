import re
import os

#wifi_name = input(str('Please enter the name of the WiFi network you have connected to: '))

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
            #print("The encrpytion protocol that is used by " + wifi_name + " is: ", wifi_authentication)
            if wifi_authentication in ["WPA2-Personal", "WPA3-Personal", "WPA2-PSK", "WPA3-PSK"]:
                return "GREEN"

            else:
                #print("Poor encrpytion")
                return "RED"
    #else:
       # print("Error! No encrpytion protocol found!")


#print(check_authentication())
