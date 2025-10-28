print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print("You are at a crossroad. Where do you want to go? ")
user_step1 = input("Type L for left or R for right.\n").upper()
if user_step1 == "L":
    print("You've come to the lake. There is an island in the middle of the lake.")
    user_step2 = input("What do you want to do? Type W to wait for a boat or S to swim across.\n").upper()
    if user_step2 == "W":
        print("You look around the island and see a building with three doors.")
        user_step3 = input("Which door do you open? Type R for red, B for blue, and Y for yellow.\n").upper()
        if user_step3 == "B":
            print("You were eaten by a beast. Game over.")
        elif user_step3 == "R":
            print("You were burned by the fire. Game over.")
        elif user_step3 == "Y":
            print("Congratulations! You found the treasure. You win!")
        else:
            print("You chose the door that doesn't exist. Game over.")
    else:
        print("You got attacked by angry trout. Game over.")
else:
    print("You fell into a hole. Game over.")