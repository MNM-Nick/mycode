#!/usr/bin/env python3

import time

Abilities= ["Rasengan", "Baryon Mode", "Sage Mode", "Shadow Clone Jutsu"]

Friends= ["Sasuke", "Kakashi", "Garaa"]

naruto= {"Clan": "Uzumaki Clan", "Rank": "Kage", "Abilities": Abilities, "Height": "5'9", "Friends": Friends }

answer= input("Hello, did you know Naruto was an orphan?")

if answer == "yes":

print("Awesome!, here are more facts about Naruto!")

break

else:

print("Well now you do know! Here are more facts about Naruto!")

time.sleep(2)

print( naruto["Clan"]
print( naruto["Rank"]
print( naruto["Abilities"]
print( naruto["Height"]
print( naruto["Friends"]
