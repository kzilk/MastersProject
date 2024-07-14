from OScheck import check_OS
from ARPtable import check_arp

from LinuxEncrypt import checkEncrypt
from LinuxHopTest import checkLinHop
from PasswordTestLinux import testLinuxPassword

from WindowsEncrypt import check_authentication
from WindowsHopTest import checkWinHop

#osCheck
osAB = check_OS()
#True Linux, False Windows

#check MAC
check_arp()

#linux checks
if osAB:
    print('Please note if your device prompts you to enter a password during this '
          'test, it may be a sign of a malicious access point.')
    #check hops to router
    checkLinHop()
    # check encryption protocol
    if checkEncrypt():
        #test password if encryption protocol found
        testLinuxPassword()
    else:
        exit()

#windows checks
else:
    #check encryption protocol
    check_authentication()
    #check hops to router
    checkWinHop()
