# Welcome sign

print("|--------------------------------------|")
print("|                                      |")
print("|  WELCOME TO A TERMINAL GAME MADE BY  |")
print("|               by Evie                |")
print("|                                      |")
print("|--------------------------------------|\n")

def game(): 
    def intro():
        print("Welcome to (I dont have a name)!!!")
        print("To play this game all you need to do is")
        print("enter the numbers to play along\n")

    intro()
#----------------------------------------------------------------------------------
    def firstQuestions():
        print("Where would you like to go?")
        print("     1: Go into house")
        print("     2: Go down a path")
        print("     3: Go into a forest")
        print("     4: Walk down the road")
        print("     5: Go to the camp fire\n")

    firstQuestions()
#----------------------------------------------------------------------------------
    StartGame = int(input("(StartGame) pick a number 1-5: "))

    if StartGame == 1:
        print("  1: Sleep")
        print("  2: Fridge")
        print("  3: Exit")

    HouseOpt = int(input("(HouseOpt) Please enter 1-3: "))

    if HouseOpt == 1:
        print("You go to bed. ZzzzZzZzz")

    elif HouseOpt == 2:
        print("You have opened the fridge")
        print("...")
        print("But wait theres something in the fridge, what is it?\n")

        print("  1: Half a pizza")
        print("  2: Apple")
        print("  3: 1/3 Carton of milk")
        print("  4: Half a bottle of juice")
    
    elif HouseOpt == 3:
        game()
            # Learn how to loop this back to start
    
    else:
        print("wrong")


#----------------------------------------------------------------------------------
# Second option

    if StartGame == 2:
        print("You walk down a path...")
        print("You can:")
        print(" 1: Build a stick hut")
        print(" 2: Continue walking")
        print(" 3: Stop and take in the surrondings")
        print(" 4: go back")

    forest_walk = int(input("(forest_walk) number 1-4: "))

    if forest_walk == 1:
        print("You build a cute little stick hut :3")

    elif forest_walk == 2:
        print("Oh no! The roads blocked")

    elif forest_walk == 3:
        print("You take in the beutifil surroundings, the high mountains and the lush forrest.")

    elif forest_walk == 4:
        print("You go back.") 

    else:
        print("wrong")

#----------------------------------------------------------------------------------
# Third Option

    def Opt3():
        if StartGame == 3:
            print("You wonder into the forrest and you start wondering where you are.")
            print("... i aint finna help, but here are 3 options")
            print(" 1: build a stick hut")
            print(" 2: walk into trees")
            print(" 3: continue walking")


    if StartGame == 4:
        print("")

    if StartGame == 5:
        print("")

    else:
        print("Wrong")

#----------------------------------------------------------------------------------

game()