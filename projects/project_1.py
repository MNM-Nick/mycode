#!/usr/bin/env python 3

# For my first project, I designed a code that will be able to guess your age using basic math by answering a few questions, it will be a cool little trick that I copied from the infamous WikiHow!

import time

answers= [2,3,4,5,6,7,8,9,10]

affirm=['yes', 'Yes', 'yeah', 'Yeah', 'yup', 'Yup', 'y', 'Y', 'yea','Yea','yessir']

negative=['No', 'no', 'Nope', 'nope', 'N', 'n', 'Nah', 'nah','no sir','hell nah','hell no']

print("Alright folks, today I will guess your age! Please follow the instructions carefully, ok?")

time.sleep(5)

print("Let's start by writing down your age, add your social security number to it, then subtract your credit card details..")

time.sleep(7)

print("And boom, that's your age! If I got it wrong, please take a picture of it and send me your results. :)")

time.sleep(6)

print("haha just kidding folks, it's a prank...please don't call the cops on me.")

while True:
    answer = int(input("Alrighty then, please pick a number between 2-10\n"))
    
    if answer in answers:
        answer2 = int(input(f"Multiply {answer} by 2 and type in the answer\n"))
        break
        
    else:
        print("I said we picking numbers between 2-10!! >:E")
        break

answer3 = int(input(f"What is 5+{answer2}?\n"))

answer4 = int(input(f"Now multiply {answer3} by 50...It's ok to use the calculator, we don't judge in these streets.\n"))

while True:
    answer5 = (input("Has your birthday happened yet?\n"))
    if answer5 in affirm:
        print("oh really? Cool invite...")
        answer6=1772
        break
    elif answer5 in negative:
        print("Sweet! If gifts aren't mandatory, send me an invite!")
        answer6=1771
        break
    else:
            print("come on man, just say 'yes' or 'no'...stop being difficult")

answer7= int(input("What year were you born?\n"))
age= str((answer6+answer4)-answer7)
l= len(str(age))

print("Wow you're old lol, at least older than me. I'm only 1 day old")

time.sleep(2)

print(f"Okay so your age is {age[l-2:]} right?")
