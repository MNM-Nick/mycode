#!/udr/bin/env python3

wordbank= ["four", "spaces"]

tlgstudents= ["Aaron", "Casey", "Donny", "Emmanuel", "Eric", "Jaelen", "James", "Jay", "John", "Ken", "Maurice aka the coolest student in this class", "Mike", "Ryan", "Shamain", "Tuang", "Tyler", "Zhenqian", "Travis"]

num= int(input("Pick a number between 0 and 17\n"))

student_name= tlgstudents[num]

print(f"{student_name} always uses {wordbank[0]} {wordbank[1]} to indent.")
