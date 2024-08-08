import subprocess

def checkEncrypt():
    encryptionCheck = subprocess.run("nmcli -t -f active,ssid,mode,chan,rate,signal,bars,"
                                     "security dev wifi | grep '^yes' | awk -F':' "
                                     "'{print $8}'", shell=True, capture_output=True, text=True)

    print(encryptionCheck.stdout.strip())
    encrypType = encryptionCheck.stdout.strip()

    return encrypType