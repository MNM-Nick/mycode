#!/usr/bin/env python3

import time

#setup for the story

inventory = ["wand"]
locations = {
    "Cafeteria":{"gh_chars":["Dumbledore", "Snape", "Lupin", "Ron", "Hermione", "Malfoy"]},
    "Commonroom":{"cr_chars":["Ron", "Neville"]},
    "Outside":"Dementor"}
spells = {"Expecto Patronum":45, "Confundo":3, "Expelliarmus":5}
harry = {"health":55}
dementor = {"health":43, "attack":17}




#collecting user information in the beginning of the game
def user_info():
    user_name = input("What is your name?")
    user_age = int(input("How old are you?"))
    print("Nice to meet you " + user_name + ". You'll like it here in Hogwarts.")
#Introduction to the game
def intro():
    print("You step off the train, arriving at Hogwarts.\n")
    input("Hagrid: \"Welcome to Hogwarts, 3rd-year students!\"")
    input("Hagrid: \"Hello, Harry. Nice to see you again. You'll do well, just like your mother and father.\"")
    input("Hagrid: \"I made some rock cakes for you, Ron, and Hermione whenever you can visit!\"")
    input("Hagrid: \"Let's go 3rd years! On to Hogwarts!\"\n\n")

def gh():
    input("You are in the Cafeteria\n")
    for person in locations["Cafeteria"]["gh_chars"]:
        print("- ", person)
    for location in locations:
        print("- ", location)
    while True:
        choice = input("Who do you want to talk to? Or where do you want to go?\n>").title()
        if choice == "Dumbledore":
            print("Dumbledore: \"Hello Harry. Wanna watch me do the twerkulator?\n")
            time.sleep(3)
        elif choice == "Snape":
            print("Snape: \"Planning to mess up again this year, Mr. Potter?\nWithout a doubt you certainly will. Just like your father....\"\n")
            time.sleep(3)
        elif choice == "Lupin":
            print("Lupin: \"Hello, Harry. Be careful around the grounds. Dementors are loose to hunt for Sirius Black.\"\n")
            time.sleep(3)
        elif choice == "Ron":
            print("Ron: \"Nearly Headless Nick floated over my food! Yuck!\"\n")
            time.sleep(3)
        elif choice == "Hermione":
            print("I signed up for too many classes this year! My schedule is overfilled. Good thing I have something to help me out...\n")
            time.sleep(3)
        elif choice == "Malfoy":
            print("\"What happened on the train, Potter? Dementor got your tongue? HAHAHAAHAHA\"\n")
            time.sleep(3)
        elif choice == "Commonroom":
            common_room()
        elif choice == "Outside":
            outside()
        else:
            print("I am sorry. I didn't understand that.")

def common_room():
    input("You are in the commonroom.")
    for person in  locations["Commonroom"]["cr_chars"]:
        print("- ", person)
    for location in locations:
        print("- ", location)
    while True:
        choice = input("Who do you want to talk to? Or where do you want to go?\n>").title()
        if choice == "Ron":
            print("\nRon: \"Why do you think those dementors attack you Harry?\"\nHarry: \" I don't know exactly Ron. Maybe because I'm emo af.\"\n")
            time.sleep(5)
        elif choice == "Neville":
            print("\nNeville: \"Ron, can you hook me up with Ginny bro? She hot af no cap. ya feel me fam?\nRon: \"Wanna get rocked, Neville?\"\nNeville: \"Understood. Have a nice day.\"")
            time.sleep(3)
        elif choice == "Cafeteria":
            gh()
        elif choice == "Outside":
            outside()
        else:
            print("I'm sorry. I didn't understand that.")

def outside():
    input("You are outside\n\n")
    print("- ", locations["Outside"])
    for location in locations:
        print("- ", location)
    while True:
        choice = input("Who do you want to talk to? Or where do you want to go?\n>").title()
        if choice == "Dementor":
            print("You encountered a dementor!")
            dementor_combat()
        elif choice == "Cafeteria":
            gh()
        elif choice == "Commonroom":
            common_room()
        else:
            print("I'm sorry. I didn't understand that.")

def dementor_combat():
    #combat statistics and setup
    for spell in spells:
        print("- ", spell)
    while True:
        if harry["health"] <= 0:
            print("You died")
        if dementor["health"] <= 0:
            print("You won!\n")
            outside()
        attack_choice = input("What spell would you like to use?\n>").title()
        if attack_choice == "Expecto Patronum":
            print("You attacked the dementor with Expecto Patronum!")
            dementor["health"] = dementor["health"] - spells["Expecto Patronum"]
            print("The dementor's health is now ", dementor["health"])
            time.sleep(3)
            print("The dementor is attacking with dementor's kiss!")
            harry["health"] = harry["health"] - dementor["attack"]
            print("Harry's health is now ", harry["health"])
        elif attack_choice == "Confundo":
            print("You attacked the dementor with Confundo!")
            dementor["health"] = dementor["health"] - spells["Confundo"]
            print("The dementor's health is now ", dementor["health"])
            time.sleep(3)
            print("The dementor is attacking with dementor's kiss!")
            harry["health"] = harry["health"] - dementor["attack"]
            print("Harry's health is now ", harry["health"])
        elif attack_choice == "Expelliarmus":
            print("You attacked the dementor with Expelliarmus!")
            dementor["health"] = dementor["health"] - spells["Expelliarmus"]
            print("The dementor's health is now ", dementor["health"])
            time.sleep(3)
            print("The dementor is attacking with dementor's kiss!")
            harry["health"] = harry["health"] - dementor["attack"]
            print("Harry's health is now ", harry["health"])
        else:
            print("Sorry. I didn't understand that.")







        


#Main story interaction 

intro()
gh()
