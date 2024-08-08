import subprocess

def testLinuxPassword():
    # Execute the command
    runNetName = subprocess.run("iwgetid -r", shell=True, capture_output=True,
                                text=True)
    #save network name as variable
    netName = runNetName.stdout.strip()

    passwordFake = "Test1234!"

    connectTestCommand = ["timeout", "10", "nmcli", "device", "wifi", "connect", netName, "password", passwordFake]
    connectNet = subprocess.run(connectTestCommand, capture_output=True, text=True)

    print('code = ', connectNet.returncode)
    if connectNet.returncode == 0:
        connectionRes = 'Connected'
        return connectionRes
    elif connectNet.returncode == 10:
        connectionRes = 'Unable to Find Network'
        return connectionRes

'''
0: Success.
1: Unknown error.
2: Invalid user input or command syntax.
3: Timeout error.
4: No valid connection was found.
5: Connection activation failed.
6: NetworkManager is not running.
10: failed connection'''