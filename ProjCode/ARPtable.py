import re
import os
from collections import defaultdict
from tkinter import *

#create ARP table to parse through its content
def command():

    os.system("arp -a > table.txt")

    # puts the arp table into a temporary file
    with open("table.txt", "r") as file:
        table_contents = file.read()
    return table_contents

def search_table(table_contents):
    expression = re.compile(r'\((.*?)\) at ([\w:]+)')
    arp_results = defaultdict(list)

    for pair in expression.findall(table_contents):
        ip_add, mac_add = pair
        arp_results[mac_add].append(ip_add)
    return arp_results

def repeat(arp_results):

    # stores duplicate MAC addresses
    doubles = {}

    for mac_add, ip_add in arp_results.items():
        if len(ip_add) > 1:
            doubles[mac_add] = ip_add
    return doubles

def check_arp():
    command_output = command()
    arp_table = search_table(command_output)
    arp_duplicate = repeat(arp_table)
    if not arp_duplicate:
            ARPtext= "ARP CHECK PASSED. No duplicate MAC addresses located."
            return ARPtext
    else:
            ARPtext="WARNING! Your ARP tables contains duplicate MAC ADDRESSES!:"
            return ARPtext