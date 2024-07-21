import encrpytion_protocol
import ARPtable
import Signal_Strength
import WindowsTest
import Network_Pass




password_test = Network_Pass.testWindowsPassword()
if password_test == "RED":
    print("Password test failed")
elif password_test == "GREEN":
    print("Password test passed")


windows_hop_test=WindowsTest.checkWinHop()
if windows_hop_test == "RED":
    print("Hop test failed")
elif windows_hop_test == "GREEN":
    print("Hop test passed")

encrpytion_command = encrpytion_protocol.command()
encrpytion_search = encrpytion_protocol.search_command_output(encrpytion_command)
encryption_test = encrpytion_protocol.check_authentication()
if encryption_test == "RED":
    print("Encrpytion test failed")
elif encryption_test == "GREEN":
    print("Encrpytion test passed")

arp_command = ARPtable.command()
search_table = ARPtable.search_table(arp_command)
duplicates = ARPtable.repeat(search_table)
arp_test = ARPtable.check_arp()

if arp_test == "RED":
    print("ARP test failed!")
elif arp_test == "GREEN":
    print("ARP test passed")


signal_command = Signal_Strength.command()
Signal_Strength.search_command_output(signal_command)
signal_test = Signal_Strength.signal_check()

if signal_test == "RED":
    print("Signal test failed")
elif signal_test == "GREEN":
    print("Signal test Passed")




if signal_test == "GREEN" and arp_test == "GREEN" and encryption_test == "GREEN" and windows_hop_test == "GREEN":
    print("CONNECTION SECURE")
else:
    print("CONNECTION NOT SECURE! CONSIDER USING ANOTHER WIRELESS NETWORK!")
