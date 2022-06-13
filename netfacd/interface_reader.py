#!/usr/bin/env python3

import netifaces

print(netifaces.interfaces())

for i in netifaces.interfaces():
    print('\n*****************Details of Interface - ' + i + ' **************')
    try:#always remember when a new line is created, you will have to indent the code below
        print('MAC: ', end='')# this ensures statement will print MAC wihtout end of line
        print(netifaces.ifaddresses(i)[netifaces.AF_LINK][0]['addr'])
        #^ this will print out the mac address
        print('IP: ', end='')#this ensures statement will print IP without end of line
        print(netifaces.ifaddresses(i)[netifaces.AF_INET][0]['addr'])
        #^ this will print out the ip address

        #note this will only work on Linux Terminal.
    except: #again new line
        print('Could not collect adapter information')
        #^ this will print out an error message if no info is collected from NIC


