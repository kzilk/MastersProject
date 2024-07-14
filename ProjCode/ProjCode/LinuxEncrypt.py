import subprocess

def checkEncrypt():
    encryptionCheck = subprocess.run("nmcli -t -f active,ssid,mode,chan,rate,signal,bars,"
                                     "security dev wifi | grep '^yes' | awk -F':' "
                                     "'{print $8}'", shell=True, capture_output=True, text=True)

    print(encryptionCheck.stdout.strip())
    encrypType = encryptionCheck.stdout.strip()
    passwordReq = True

    #if no encryption protocol then no password requirement
    if encrypType == "--":
        print('No encryption found, no password requirement')
        passwordReq = False
        return passwordReq
    elif encrypType == "WEP":
        print('WEP detected')
        return passwordReq
    else:
        print('Normal Protocol')
        return passwordReq