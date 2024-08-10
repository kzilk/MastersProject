from OScheck import check_OS
from ARPtable import check_arp

from LinuxEncrypt import checkEncrypt
from LinuxHopTest import checkLinHop
from PasswordTestLinux import testLinuxPassword

from WindowsEncrypt import check_authentication
from WindowsHopTest import checkWinHop
from Network_Pass import testWindowsPassword

from tkinter import *


def runProgram():
    # check operating system
    osTest = "Determining Operating System"
    operatingCheck = Label(window,
                           text=osTest,
                           fg='white',
                           bg='black')
    operatingCheck.pack()
    window.update_idletasks()

    def unknownOperatingSys():
        badOS = Label(window,
                      text='Unknown Operating System, please Exit',
                      fg='red',
                      bg='black')
        badOS.pack()

    def displayOS(displayText):
        osPrint = Label(window,
                        text=displayText,
                        fg='#00FF00',
                        bg='black')
        osPrint.pack()

    operName = check_OS()
    window.update_idletasks()
    # True Linux, False Windows
    if "Linux" in operName:
        osAB = True
        displayText = "Linux Operating System"
        displayOS(displayText)
        window.update_idletasks()

    elif "Windows System" in operName:
        osAB = False
        displayText = "Windows Operating System"
        displayOS(displayText)
        window.update_idletasks()

    else:
        unknownOperatingSys()
        window.update_idletasks()

    #MAC/ARP Check
    ARPtext = "Checking MAC Addresses"

    addressCheck = Label(window,
                         text=ARPtext,
                         fg='white',
                         bg='black')
    addressCheck.pack()
    window.update_idletasks()

    ARPtext = check_arp()
    if ARPtext[0] == 'A':
        resColor = '#00FF00'
    else:
        resColor = 'red'

    macResult = Label(window,
                      text=ARPtext,
                      fg=resColor,
                      bg='black',
                      )
    macResult.pack()
    window.update_idletasks()

    def HopReturn(hoptext, textColor):
        badOS = Label(window,
                      text= hoptext,
                      fg=textColor,
                      bg='black')
        badOS.pack()

    def HopAB(hopText):
        if "Multiple" in hopText:
            textColor = 'red'
            HopReturn(hopText, textColor)
        elif "Single" in hopText:
            textColor = '#00FF00'
            HopReturn(hopText, textColor)

    def encryptReturn(encrypText, textColor):
        encryptProt = Label(window,
                      text= encrypText,
                      fg=textColor,
                      bg='black')
        encryptProt.pack()

    def linuxNotif():
        passwordReturn = Label(window,
                               text="Please note, if no password errors you may be "
                                    "required to re-enter your password at this stage",
                               fg='blue',
                               bg='black')
        passwordReturn.pack()

    def passReturn(PassText, textColor):
        passwordReturn = Label(window,
                            text=PassText,
                            fg=textColor,
                            bg='black')
        passwordReturn.pack()

    def linuxTests():
        #check hops to router
        hopText = checkLinHop()
        HopAB(hopText)
        window.update_idletasks()

        # check encryption protocol
        encrypType =  checkEncrypt()
        window.update_idletasks()
        passwordReq = True

        if encrypType == "--":
            # if no encryption found, no password requirement
            passwordReq = False
            textColor = 'red'
            encrypText = ("No encryption protocol found, Unsafe Network, "
                          "No Password Requirement")
            encryptReturn(encrypText, textColor)
            window.update_idletasks()

        elif encrypType == "WEP":
            textColor = ('yellow')
            encrypText = "WEP Encryption Found, at Risk"
            encryptReturn(encrypText, textColor)
            window.update_idletasks()

        else:
            textColor = ('#00FF00')
            encrypText = "Normal Encryption Protocol"
            encryptReturn(encrypText, textColor)
            window.update_idletasks()

        if passwordReq:
            linuxNotif()
            window.update_idletasks()

            connectionRes = testLinuxPassword()
            if "Connected" in connectionRes:
                textColor = 'red'
                PassText = 'Fake to Extremely Poor Passwork Requirement, Unsafe Network'
                passReturn(PassText, textColor)
                window.update_idletasks()
            else:
                textColor = "#00FF00"
                PassText = 'Legitimate Password'
                passReturn(PassText, textColor)
                window.update_idletasks()

    def windowsTests():
        #check hops to router
        hopText = checkWinHop()
        HopAB(hopText)
        window.update_idletasks()

        #check encryption protocol
        wifi_authentication = check_authentication()
        if wifi_authentication in ["WPA2-Personal", "WPA3-Personal", "WPA2-PSK", "WPA3-PSK"]:
            textColor = ('#00FF00')
            encrypText = "Normal Encryption Protocol"
            encryptReturn(encrypText, textColor)
            passwordReq = True
            window.update_idletasks()

        elif wifi_authentication in "WEP":
            textColor = ('yellow')
            encrypText = "WEP Encryption Found, at Risk"
            encryptReturn(encrypText, textColor)
            passwordReq = True
            window.update_idletasks()

        else:
            passwordReq = False
            textColor = 'red'
            encrypText = ("No encryption protocol found, Unsafe Network, "
                          "No Password Requirement")
            encryptReturn(encrypText, textColor)
            window.update_idletasks()

        if passwordReq:
            winPass = testWindowsPassword()
            if winPass:
                textColor = '#00FF00'
                PassText = 'Password Requirements Found'
                passReturn(PassText, textColor)
                window.update_idletasks()
            else:
                textColor = "red"
                PassText = 'No Real Password Requirement, Potentially Malicious Connection'
                passReturn(PassText, textColor)
                window.update_idletasks()

    if osAB:
        linuxTests()
    else:
        windowsTests()


# generate window
window = Tk()  # window instance
window.geometry("660x420")
window.title("WiFi Security Test")

title = Label(window,
              text="Testing Wireless Network Security",
              fg='#00FF00',
              bg='black',
              relief=RAISED,
              bd=5,
              padx=20,
              pady=10)
title.pack()
# or label.place(x=0, y=0)

# start button
def start():
    runProgram()

start = Button(window,
               text="Start",
               command=start,
               fg='#00FF00',
               bg='black',
               relief=RAISED,
               bd=5,
               padx=10,
               pady=5)
start.place(x=200, y=350)

# exit button
def end():
    exit()


close = Button(window,
               text="Exit",
               command=end,
               fg='#00FF00',
               bg='black',
               relief=RAISED,
               bd=5,
               padx=10,
               pady=5)
close.place(x=395, y=350)

window.config(background="black")
window.mainloop()  # place on screen, listen for events