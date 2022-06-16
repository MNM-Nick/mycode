#!/usr/bin/python3
import sys
#from termcolor import colored, cprint
# Replace RPG starter project with this code when new instructions are live

#We will create our own game with this code

def showInstructions():
  #print a main menu and the commands

  print('''
, , , , , , , , , , ,______________________________________________________
n#|#|#|#|#|#|#|#|#|#|__________________Ninja Story________________________/
'-'-'-'-'-'-'-'-'-'-|____________________________________________________/

Commands:
  go - direction (north, south, etc)
  buy - item
  get - item
  throw - scrolls 
  swing - attack 
  teleport - location
  
''')



#def game_over():
 # print ("You are dead!")
  

def showStatus():
  #print the player's current statu
  print('[\\\\\\\\\\\]========================-')
  print(f"You are in the {currentRoom}.")
  #print the current inventory
  print(f"Inventory : {str(inventory)}")
  #print an item if there is one
  if "item" in rooms[currentRoom]:
    print('You see a ' + rooms[currentRoom]['item'])
  elif "enemy" in rooms[currentRoom]:
    print('Oh no! You see ' + rooms[currentRoom]['enemy']+". Fight the ninja!")
  elif "closet" in rooms[currentRoom]:
    print("You see your closet besides the wall, there is a seal scroll. You should probably get it..")
  elif "bed" in rooms[currentRoom]:
    print("You see your bed on the floor, sleeping would be nice...")
  elif "fridge" in rooms[currentRoom]:
    print("You see your fridge next to the kitchen, your important drink is in here...")
  print("[\\\\\\\\\\\]========================-")

#attack = []

#an inventory, which is initially empty
inventory = []

#a dictionary linking a room to other rooms
## A dictionary linking a room to other rooms
rooms = {

            'ramen place' : {
                  'north' : 'store',
                  'south' : 'gate',
                  'east'  : 'house',
                  'west'  : 'training field',
                },

            'store' : {
                  'south' : 'ramen place',
                  'item'  : 'teleport scroll',
                },
            'gate' : {
                  'south' : 'forest of element',
                  'north' : 'ramen place',
               },
            'house' : {
                  'west' : 'ramen place',
                  'item': 'seal scroll',
                  'bed'   : 'sleep',
                  'fridge': 'sake',
               },
            'training field' : {
                  'east'    : 'ramen place',
                  'item'     : 'sword',
                  'enemy'    : 'fake ninja',
               },
            'forest of element' : {
                  'south' : 'evil ninja village',
                  'enemy' : 'evil ninja',
                  'north' : 'gate',
            },
            }
 
#start the player in the training field to get them started
currentRoom = 'training field'

showInstructions()

#loop forever
while True:
   

  attack = []

  showStatus()
  #get the player's next 'move'
  #.split() breaks it up into an list array
  #eg typing 'go east' would give the list:
  #['go','east']

  move = ''
  while move == '':
    move = input('>')

  # split allows an items to have a space on them
  # get golden key is returned ["get", "golden key"]          
  move = move.lower().split(" ", 1)

  #if they type 'go' first
  if move[0] == 'go':
    #check that they are allowed wherever they want to go
    if currentRoom == 'gate' and 'seal scroll' not in inventory:
      print('You can\'t go past the gate yet, you need your seal scroll first')
      currentRoom = 'ramen place'
    elif move[1] in rooms[currentRoom]:
      #set the current room to the new room
      currentRoom = rooms[currentRoom][move[1]]
    #there is no door (link) to the new room
    else:
        print('You can\'t go that way!')

  #if they type 'get' first
  if move[0] == 'get' :
    #if the room contains an item, and the item is the one they want to get
    if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
      #add the item to their inventory
      inventory += [move[1]]
      #display a helpful message
      print(move[1] + ' got!')
      #delete the item from the room
      del rooms[currentRoom]['item']
    #otherwise, if the item isn't there to get
    else:
      #tell them they can't get it
      print('Can\'t take ' + move[1] + '!')

  if move[0] == 'swing':
    if 'sword' in inventory and currentRoom in 'training field':
      #set the current room to the new room
      print("You have killed fake ninja")
      print("For killing the fake ninja, you are being offered the teleport scroll at the store for free.99!")
      del rooms[currentRoom]['enemy']
    elif 'sword' and 'seal scroll' in inventory and currentRoom in 'forest of element':
      print("You missed, if only there was a way to restrict his movements")
      attack.append('miss')
      print(attack)
    elif 'miss' in attack[0] and 'end' not in attack[1] and 'sword' and 'seal scroll' in inventory and currentRoom in 'forest of element':
        print("You missed, if only there was a way to restrict his movements")
        attack.append('end')
        print(attack)
    elif 'end' in attack[1]  and 'sword' and 'seal scroll' in inventory and currentRoom in 'forest of element':
        print('''
    ⠀⣠⠤⠀⠐⠒⠂⠀⠤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⡰⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⠄⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢠⠁⠀⠀⠀⠀⣀⣀⣀⠀⠀⠀⠀⠘⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢸⠀⢠⠔⡈⠉⠀⠀⠈⠉⣐⠦⡀⠀⡆⠀⠀⠀⠀⠀⠀
⠀⠀⠸⠀⠁⠈⢹⣿⠂⠀⠐⣿⡏⠀⢰⢀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢢⡣⣀⠈⠁⠀⠀⠀⠈⠁⡠⢎⠌⠀⢀⡠⡪⡉⠀⠀
⠀⠀⠀⠀⠙⢂⠭⠴⣒⣒⡲⠮⢭⡒⠁⢰⢴⢅⢣⠼⠋⠀⠀               GAME OVER!
⠀⠀⠀⢀⠔⠁⠀⠀⠀⠀⠀⠀⠀⠈⠲⡁⡱⣿⠁⠀⠀⠀⠀
⠀⠀⡴⠁⠀⡠⠀⠀⠀⠀⠀⠀⠀⡄⠀⠘⢆⠀⠀⠀⠀⠀⠀
⠀⡜⠀⠀⡜⣇⡀⠀⠀⠀⠀⠀⢀⣙⢆⠀⠈⢆⠀⠀⠀⠀⠀
⢨⠦⢀⡜⡸⠦⠭⠉⠉⠉⠉⠩⠥⠴⡌⢇⠠⠼⡀⠀⠀⠀⠀
⠘⡤⠠⢉⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⢁⠸⠄⠴⠁⠀⠀⠀⠀
⠈⠁⠀⢩⠁⠀⠀⢀⠞⠉⢢⠀⠀⠀⠸⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⡆⠀⠀⠀⡞⠀⠀⠀⢃⠀⠀⠀⠃⠀⠀⠀⠀⠀⠀⠀
⠀⠀⡠⠓⠀⠤⢤⠁⠀⠀⠀⠘⡤⠤⠀⠚⢄⠀⠀⠀⠀⠀⠀
⠀


        ''')
        break 
    elif 'sword' in inventory and 'seal scroll' not in inventory and currentRoom in 'forest of element':
        print("You have killed evil ninja! Go home and enjoy your day!")
        del rooms[currentRoom]['enemy']
        del inventory[0]

  if move[0] == 'throw' :
    if currentRoom == 'forest of element' and 'seal scroll' in inventory:
      print("You have sealed the evil ninja's movement, attack before he break's free!")
      if 'seal scroll'== inventory[1]:
        del inventory[1]
      elif 'seal scroll'== inventory[2]:
        del inventory[2]



  if move[0] == 'tp' :
    if move[1] in 'ramen place' and 'teleport scroll' in inventory:
      #set the current room to the new room
      currentRoom = 'ramen place'
      print("woosh")
    elif move[1] in 'house' and 'teleport scroll' in inventory:
      #set the current room to the new room
      currentRoom = 'house'
      print("woosh")
    elif move[1] in 'store' and 'teleport scroll' in inventory:
      #set the current room to the new room
      currentRoom = 'store'
      print("woosh")
    elif move[1] in 'training field' and 'teleport scroll' in inventory:
      #set the current room to the new room
      currentRoom = 'training field'
      print("woosh")
    elif move[1] in 'gate' and 'teleport scroll' in inventory:
      #set the current room to the new room
      currentRoom = 'gate'
      print("woosh")
    #there is no door (link) to the new room
    else:
        print('You can\'t teleport that way, it\'s only limited to locations you know of!')

  if currentRoom == 'house'and 'sword' not in inventory:
    print('''
    
    You open your fridge and enjoy a nice cold sake.
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢠⣤⣤⣤⣤⣤⣤⣤⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠃⠀⠀⠀⠀⠀⠀⠀⠀⢀⡼⠃⠀⠀⠀⠀⠀⠀⠀⠙⠂⠀⠀⠀⠀⣠⡶⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⠃⠀⠀⠀⠀⠀⠀⠀⢀⡴⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡴⠋⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠞⠁⠀⠀⠀⠀⠀⠀⠠⠞⠉⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡴⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠰⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    
    
    ''')
    break

 
