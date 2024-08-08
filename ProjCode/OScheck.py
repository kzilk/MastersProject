import os
import subprocess

def check_OS():
    linuxCheck = subprocess.run("uname", shell=True, capture_output=True, text=True).stdout.strip()

    if "Linux" in linuxCheck:
        operName = 'Linux System'
        return operName
    else:
        windowsCheck = subprocess.run("ver", shell=True, capture_output=True, text=True).stdout
        osName = windowsCheck.strip()
        if "Microsoft Windows" in osName:
            operName ='Windows System'
            return operName
        else:
            operName = 'Unknown OS'
            return operName

'''def check_windows():
    windowsCheck = subprocess.run("ver", shell=True, capture_output=True, text=True).stdout
    osName = windowsCheck.strip()
    if "Microsoft Windows" in osName:
        print('Windows System')
        return False
    else:
        print('Unknown OS')
        exit()
'''
