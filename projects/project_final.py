#!/usr/bin/env

""" We will create an ASCII animation for my 3 favorite characters from naruto with bonus character: Naruto """

""" Credit: Python Animated ASCII Art Tutorila by Learn Learn Scratch Tutorials """

#We will let individuals choose 3 or 4 if possible of choices from this project.

import os #letting me pull from files and use the clear command
import time #putting a time limit for each frame

os.system('clear') #terminal - 'clear'

filenames = ["test1.txt","test3.txt"]# these are files I am pulling from

narutofile= ["naruto.txt","naruto1.txt"]

def animator(filenames,delay=1,repeat=50):#creating animation function
    frames = [] #frame is inputed

    for name in filenames:
        with open (name,"r",encoding="utf8") as f:
            frames.append(f.readlines())
    for i in range(repeat):
        for frame in frames:
            print("".join(frame))
            time.sleep(0.1)
            os.system('clear')

animator(filenames,delay=0.1,repeat=25)

def animenaruto(narutofile,delay=1,repeat=50):
    frames=[]

    for name in narutofile:
        with open (name,"r",encoding="utf8") as f:
            frames.append(f.readlines())
    for i in range(repeat):
        for frame in frames:
            print("".join(frame))
            time.sleep(0.1)#the speed of each frame
            os.system('clear')#for each frame, chat will clear itself that way it doesn't look messy.

character=['naruto', 'sasuke','kakashi'] #these are my character
#printing out my menu for character of choice
print('''

        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣤⣤⣤⣤⣤⣀⡀    -Naruto⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⣠⣶⣿⣿⡿⠿⠿⠿⠿⢿⣿⣿⣷⣦⣄⣀⣤⣶⣶  
⠀⠀⠀⠀⠀⣰⣿⣿⠿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠉⠛⠿⣿⣿⣿⠟⠋     -Kakashi
⠀⠀⠀⠀⣼⣿⡿⠃⠀⢀⣤⣾⣿⣿⣿⣿⣷⣦⣄⠀⠀⠈⠉⠀⠀⠀
⠀⠀⠀⣸⣿⡿⠁⠀⢠⣿⣿⠟⠉⠀⠈⠉⠛⢿⣿⣷⡄⠀⠀⠀⠀      -Sasuke⠀
⠀⠀⢀⣿⣿⡇⠀⠀⣾⣿⡟⠀⠀⢀⣤⣄⠀⠀⠹⣿⣿⡄⠀⠀⠀⠀
⠀⠀⣾⣿⣿⡇⠀⠀⢻⣿⣷⡀⠀⠘⣿⣿⡇⠀⠀⣿⣿⡇⠀⠀⠀⠀
⠀⣼⣿⡿⣿⣿⡄⠀⠈⠻⣿⣿⣷⣿⣿⡿⠃⠀⢀⣿⣿⡇⠀⠀⠀⠀
⣰⣿⣿⠁⠹⣿⣿⣦⡀⠀⠈⠉⠛⠋⠉⠀⠀⣠⣾⣿⡟⠀⠀⠀⠀⠀
⣿⣿⣧⣤⣤⣬⣿⣿⣿⣶⣦⣤⣤⣤⣴⣶⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀
⠙⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠛⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀

''')

c= input("Type the character's name to learn more about him.\n")

while True:
#creating loop so that user can pick either of the 3 characters.
    if c == 'naruto':
        animenaruto(narutofile,delay=0.1,repeat=25) #using my function from above to print out animation
    #elif c == 'kakashi':
        #animekakashi(kakashifile,delay=0.1,repeat=25)
    #elif c == 'sasuke':
        #animesasuke(sasukefile,delay=0.1,repeat=25)

