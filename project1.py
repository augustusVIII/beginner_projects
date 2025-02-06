
name = input("tell ur name: ")
print("Hello " + name + " welcome to my game!")

should_we_play = input("Do you want to play?: ").lower()
play = should_we_play == "yes"

if (play):
    print("We will play")
else:
    print("We won't play")
