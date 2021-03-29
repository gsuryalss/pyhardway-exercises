print("You enter a dark room with two doors. Do you go through door #1 or #2?")

door = input("> ")

if door == "1":
    print("There's a giant bear here eating a cheese cake.\n what do you do?")
    print("1. Take the cake.")
    print("2. Scream at the bear.")
    print("3. Punch the bear in the face.")

    bear = input("> ")

    if bear =="1":
        print("The bear eats your face off. Good job!")
    elif bear == "2":
        print("The bear eats your legs off. Good Job!")
    elif bear =="3":
        print("You knock the bear out!")
        print("When the bear falls over, you see a passage\nbehind him. you go through it.")
        print("It's dark in here, and smells kind of funny.\nwhat do you do?")
        print("1. Light a match.")
        print("2. Feel for a lightswitch.")
        print("3. Turn on your mining hat.")

        light = input("> ")

        if light == "1":
            print("Whoops, looks like that smell was a gas leak. KABOOM!")
        elif light == "2":
            print("As you feel along the wall for a switch, you run into an electric fence. ZAP!")
        elif light == "3":
            print("Smart! You find the exit and head home.")
        else:
            print("You huddle up on the floor and die.")
    else:
        print("Well, doing %s is probably better, Bear runs away." % bear)

elif door == "2":
    print("You stare into the endless abyss at Cthuhlu's retina.")
    print("1. Blueberries.")
    print("2. Yellow jacket clothespins.")
    print("3. Understanding revolvers yelling melodies.")

    insanity = input("> ")

    if insanity == "1" or insanity == "2":
        print("Your body survives powered by a mind of jello.\nGood Job!")
    else:
        print("The insanity rots your eyes into a pool of muck.\n Good Job!")

else:
    print("You stumble arounf and fall on a knife and die.\n Good Job!")

