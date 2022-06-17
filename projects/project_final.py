#!/usr/bin/env

""" We will create an ASCII animation for my 3 favorite characters from naruto with bonus character: Naruto """

""" Credit: Python Animated ASCII Art Tutorila by Learn Learn Scratch Tutorials: from youtube.com """

""" Art Credit: from emojicombos.com """

#We will let individuals choose 3 or 4 if possible of choices from this project.

import os #letting me pull from files and use the clear command
import time #putting a time limit for each frame
import sys #allowing to me read txt files in the same folder

os.system('clear') #terminal - 'clear'

filenames = ["test1.txt","test2.txt","test3.txt"]# these are files I am pulling from

narutofile= ["naruto6.txt","naruto7.txt","naruto8.txt","naruto9.txt","naruto10.txt","naruto11.txt","naruto12.txt","naruto13.txt","naruto.txt","naruto1.txt","naruto.txt","naruto1.txt","naruto2.txt","naruto3.txt","naruto2.txt","naruto3.txt","naruto4.txt","naruto5.txt"]

sasukefile= ["sasuke.txt","sasuke2.txt","sasuke3.txt","sasuke4.txt","sasuke5.txt","sasuke6.txt","sasuke7.txt","sasuke8.txt","sasuke9.txt","sasuke8.txt","sasuke9.txt"]

def animator(filenames,delay=0.1,repeat=10):#creating animation function
    frames = [] #frame is inputed

    for name in filenames:
        with open (name,"r",encoding="utf8") as f: #display output based on what is read from filenames
            frames.append(f.readlines()) #adding frames ontop of another
    for i in range(repeat): 
        for frame in frames:
            print("".join(frame))
            time.sleep(0.025)#the speed of each frame
            os.system('clear')#for each frame, chat will clear itself that way it doesn't look messy.

animator(filenames,delay=0.01,repeat=10)
#next 3 will be copy and paste for each character to perform animation process before printing out their stats

#naruto's animation
def animenaruto(narutofile,delay=1,repeat=50):
    frames=[]

    for name in narutofile:
        with open (name,"r",encoding="utf8") as f:
            frames.append(f.readlines())
    for i in range(repeat):
        for frame in frames:
            print("".join(frame))
            time.sleep(0.5)
            os.system('clear')
#kakashi's animation
def animekakashi(kakashifile,delay=1,repeat=50):
    frames=[]

    for name in kakashifile:
        with open (name,"r",encoding="utf8") as f:
            frames.append(f.readlines())
    for i in range(repeat):
        for frame in frames:
            print("".join(frame))
            time.sleep(0.1)
            os.system('clear')

#sasuke's animation
def animesasuke(sasukefile,delay=1,repeat=50):
    frames=[]

    for name in sasukefile:
        with open (name,"r",encoding="utf8") as f:
            frames.append(f.readlines())
    for i in range(repeat):
        for frame in frames:
            print("".join(frame))
            time.sleep(0.5)
            os.system('clear')


character=['naruto', 'sasuke','kakashi'] #these are my character

#printing out my menu for character of choice
def characterlist():
    print('''

        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣤⣤⣤⣤⣤⣀⡀           ⠀⠀⠀_______________________⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⣠⣶⣿⣿⡿⠿⠿⠿⠿⢿⣿⣿⣷⣦⣄⣀⣤⣶⣶             =(__    ___      __     _)=
⠀⠀⠀⠀⠀⣰⣿⣿⠿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠉⠛⠿⣿⣿⣿⠟⠋               |                     |
⠀⠀⠀⠀⣼⣿⡿⠃⠀⢀⣤⣾⣿⣿⣿⣿⣷⣦⣄⠀⠀⠈⠉⠀⠀⠀               |       Naruto        |
⠀⠀⠀⣸⣿⡿⠁⠀⢠⣿⣿⠟⠉⠀⠈⠉⠛⢿⣿⣷⡄⠀⠀⠀⠀             ⠀  |                     |
⠀⠀⢀⣿⣿⡇⠀⠀⣾⣿⡟⠀⠀⢀⣤⣄⠀⠀⠹⣿⣿⡄⠀⠀⠀⠀               |       Kakashi       |
⠀⠀⣾⣿⣿⡇⠀⠀⢻⣿⣷⡀⠀⠘⣿⣿⡇⠀⠀⣿⣿⡇⠀⠀⠀⠀               |                     |      
⠀⣼⣿⡿⣿⣿⡄⠀⠈⠻⣿⣿⣷⣿⣿⡿⠃⠀⢀⣿⣿⡇⠀⠀⠀⠀               |       Sasuke        |
⣰⣿⣿⠁⠹⣿⣿⣦⡀⠀⠈⠉⠛⠋⠉⠀⠀⣠⣾⣿⡟⠀⠀⠀⠀⠀               |__  __   ___   __  __|
⣿⣿⣧⣤⣤⣬⣿⣿⣿⣶⣦⣤⣤⣤⣴⣶⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀             =(_______________________)=
⠙⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠛⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀

    ''')

characterlist()

c= input("Type the character's name to learn more about him.\n")
#This will let the individual input the character of choice.


def anime():
    while True:
    #creating loop so that user can pick either of the 3 characters.
        if c == 'naruto':
            animenaruto(narutofile,delay=0.1,repeat=2)
            f = open('narutostats.txt', 'r') #opens my txt file with stats,
            file_contents=f.read() #it will not print if pasted into this code,
            print(file_contents)# this is a good alternative
            print("run the program again if you would like to see other characters")
            break# this enables me to print content from txt file

    # the next 2 elif statements will be a copy and paste of the naruto if statement, only difference will be the name of the files 

        #elif c == 'kakashi':
            #animekakashi(kakashifile,delay=0.1,repeat=25)
        elif c == 'sasuke':
            animesasuke(sasukefile,delay=0.1,repeat=2)
            f = open('sasukestat.txt', 'r')
            file_contents=f.read()
            print(file_contents)
            print("run the program again if you would like to see other characters")
            break
        else:
            print("ERROR ERROR...NEXT TIME SPELL THEIR NAME CORRECTLY...ERROR ERROR")
            break
anime()
