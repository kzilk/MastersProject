from wifiname import wireless_network_name
import subprocess

def testWindowsPassword():

    NetName = wireless_network_name()

    passwordFake = "Test1234!"

    connectTestCommand = ["netsh", "wlan", "connect", "name=\"", NetName,"\""]
    connectNet = subprocess.run(connectTestCommand, capture_output=True, text=True)

    print('code = ', connectNet.returncode)
    if connectNet.returncode == 0:
        print('Connected')
    elif connectNet.returncode == 10:
        print('No network to test')


'''
0: Success.
1: Unknown error.
2: Invalid user input or command syntax.
3: Timeout error.
4: No valid connection was found.
5: Connection activation failed.
6: NetworkManager is not running.
10: failed connection'''