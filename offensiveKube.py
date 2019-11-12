import os
import sys

templates = ['nmap', 'metasploit', 'other']


def createcontainer():
    select = ""

    print ("Select template from the options below:")

    for value in templates:
        print (value)

    while select not in templates:
            select = input()


createcontainer()