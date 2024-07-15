import re
import os


def command():
    os.system("netsh wlan show interfaces > signal.txt")
    with open('signal.txt', 'r') as file:
        command_output = file.read()
    return command_output

def search_command_output(command_output):
    search_signal_strength = re.search(r'Signal\s*:\s*(\d+)%', command_output)
    if search_signal_strength:
        signal_strength = int(search_signal_strength.group(1))
        return signal_strength
    else:
        return None

def signal_check():
    run_method = command()
    wifi_strength = search_command_output(run_method)
    if wifi_strength is not None:
            #print("Your wireless network signal strength is: ", wifi_strength)
            if wifi_strength >= 99:
                return "RED"
            else:
                return "GREEN"
    else:
            print("Could not detect wireless signal strength")

#print(signal_check())