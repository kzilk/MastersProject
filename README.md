Oscar Quiles
Kevin Zielke

Lewis University Master's Project 
CPSC 69100 003
Professor Ziad Al Sharif

Requirements:

User must have a Windows or Linux operating system, with this being tested on Windows 10 and an Ubuntu distribution of Linux.

Python3 is required to run this program
    https://www.python.org/downloads/

Any system running this program must have a wireless network connection and the ability to access the command line.


Common Issues:

Ensure the Tkinter module is set on your path to ensure proper display

Please note below instructions for Linux password outputs

Windows Usage:
    To run the program, simply download and execute the WiFiSecurityTest.exe program file.

Linux Usage:
    For this, ensure your system has the latest version of Python installed and set to PATH as stated above. Download all files and run the python file Main.py to begin.
    
Once active, the window will display and the user may click the 'Start' button to begin a series of wireless network security tests as follows:

1. Operating System Check:
    This determines whether the system is a Windows or Linux operating system to follow correct procedure for future tests

2. MAC Address Check:
   This forms an ARP table to check for duplicate MAC addresses visibile to your device. Duplicate MAC addresses can be a sign that there is a device pretending to be something it is not to trick users into accessing it and can be a danger to your deivce.

3. Hop Test:
   This tests the number of 'hops' it takes to connect your device to the network. If there is something between you and the network that may be viewing your traffic or manipulating what you are sending and receiving, this would return that there are more than one 'hops' between you and the network.

4. Encryption Protocol:
   This tests the encryption protocol of the network you are connected to. Some networks use broken or falsified encryption protocols meaning their connections are not secure.

5. Password Test:
   This tests the password requirements of the network you are connected to. Malicious access points may set up prompts for false password requirements to steal inputs from users or give a false sense of security.

   FOR WINDOWS SYSTEMS: This is able to check the network requirements to ensure that there are requirements for the network password and is unlikely to be a fake

   FOR LINUX SYSTEMS: This works by attempting to reconnect to the network with a fake password 'Test1234!'. If the password requirement is fake, it will allow you to connect despite using the fake password, otherwise, the connection will fail and you will need to reconnect manually. On some systems, your operating system will automatically prompt you to enter the password before this program is done executing.
