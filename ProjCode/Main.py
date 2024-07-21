from OScheck import check_OS
from ARPtable import check_arp

from LinuxEncrypt import checkEncrypt
from LinuxHopTest import checkLinHop
from PasswordTestLinux import testLinuxPassword

from WindowsEncrypt import check_authentication
from WindowsHopTest import checkWinHop
from Network_Pass import testWindowsPassword

#osCheck
osAB = check_OS()
#True Linux, False Windows

#check MAC
check_arp()

#linux checks
if osAB:
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

    #check hops to router
    checkWinHop()

    #check encryption protocol
    if check_authentication():
        print('Test Password')
        testWindowsPassword()

    else:
        exit()

