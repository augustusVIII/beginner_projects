import path

name = input("tell ur name: ")
print("Hello " + name + " welcome to my game!")

should_we_play = input("Do you want to play?: ").lower()
play = should_we_play == ("yes" or "y")

if play:
    print("We will play")
    weapon = input("choose a weapon (bow/sword)").lower()
    pathway = input("please choose a path (swim/ bridge)").lower()
    if pathway == "swim":
        if weapon == "sword":
            print("You met a crocodile and killed it with your sword, successfully crossing the river")
        else:
            print("You got killed by a crocodile, game end!")

    elif pathway == "bridge":
        print("You walked cross the river successfully")

    else:
        print("wrong input, you die, game end!")

else:
    print("We won't play")
