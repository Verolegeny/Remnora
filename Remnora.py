print("Welcome adventurer!")

name = input("What's your name? ").strip().title()

print(f"Hello, {name}!")

print("We have to check your age!")

while True:
    age = int(input("What's your age? "))
    if age<13:
        print("You're not eligible to play this game. CLOSE IT")
    else:
        start = input("Are you ready?(yes/no) ").strip().lower()
        if start == "yes":
            print("Good, let's start!")
            break
        else:
            print("Leave!!!")



while True:

    print("choice 1: FOREST")
    print("choice 2: CAVE")
    print("choice 3: BEACH")
    print("choice 4: SMALL VILLAGE")

    choice = int(input("Which drop would you choose?(1/2/3/4) "))

    if choice == 1:
        print("Excellent! You can make fire, catch animals and discover!")
        break

    elif choice == 2:
        print("Terrible choice... You couldn't find the way out, and die of thirst!")

    elif choice == 3:
        print("You're in a survival game, not in a vacation! You got EATEN by 354 seagulls!")

    elif choice == 4:
        print("Good choice! The villagers are kind with you, you get food and clothes.")
        break

print("Day One")

hp = 100
inventory = []

while True:
    if choice == 1:
        print("You got attacked by a pack of wolves!")
        print("Choice 1: Fight back")
        print("Choice 2: Escape")
        choiced1 = int(input("What would you choose?(1, 2) "))
        if choiced1 == 1:
            print("You can't stand a chance.")
            hp -= 100
            if hp <= 0:
                print("Game Over")
        elif choiced1 == 2:
            print("Correct! You somehow climbed a tree. But got injured!")
            hp -= 50
            print(f"-50 HP! Current HP:{hp}")
            break
    elif choice == 4:
        print("You left the village. Found a nearby abandoned mine. Big risk, but possible big loot!")
        print("Choice 1: Go in.")
        print("Choice 2: Leave.")
        choiced1_2 = int(input("What would you choose?(1, 2) "))
        if choiced1_2 == 1:
            print("You get bitten by an unknown spider. It was venomous. -20HP, everyday -5 for 4 days!")
            hp -= 5
            print(f"Current HP: {hp}")
            print("Your loot: 2 golden ore and 5 kg of coal. You can make fire anytime!")
            inventory.append("2 golden ore")
            inventory.append("5 kg of coal")
            print(f"inventory: {inventory}")
            break
        elif choiced1_2 == 2:
            print("You walk all days straight! Absolutely nothing happened to you.")
            break


print("Day Two")

while True:
    if choice == 1:
        if choiced1 == 2:
            print("You're about to collapse, when you get to a river, perfect for you!")
            print("You washed your wound and somehow caught 3 small fish. +30 HP!")
            hp += 30
            print(f"Current HP: {hp}")
            print("You can leave the forest(choice 1) or go deeper(choice2)")
            choiced1_d2 = int(input("What would you choose?(1, 2) "))
            if choiced1_d2 == 1:
                print("You arrive in a flowery field. Some tribe saw you. You get killed and ate!")
                hp -= 100
                if hp <= 0:
                    print("Game Over")
            elif choiced1_d2 == 2:
                print("You found a camp. They were not as lucky as you...")
                print("You found some epic loot!")
                inventory.append("knife")
                inventory.append("axe")
                inventory.append("food for 3 days")
                inventory.append("water for 5 days")
                inventory.append("backpack")
                print(f"Current inventory:{inventory}")
                break
    elif choice == 4:
        if choiced1_2 == 1:
            print("You arrive to a big mountain. Got some idea to build.")
            print("Would you like to climb the mountain(choice 1) or avoid it(choice 2)?")
            choiced1_2_d2 = int(input("What would you choose?(1, 2) "))
            if choiced1_2_d2 == 1:
                print("You found a small cave, and it's safe! This is your base now!")
                hp -= 5
                print(f"Current HP:{hp}")
                break
            elif choiced1_2_d2 == 2:
                print("You walking in a grassfield. Suddenly a heavy storm appears.")
                print("You got absolutely fried by a giant lightning! -1000000 HP!")
                hp -= 1000000
                if hp <= 0:
                    print("Game Over!")
        elif choiced1_2 == 2:
            print("You overslept a big storm. In you way you saw that someone got absolutely demolished")
            print("You borrowed the person's 2 golden ore and some coal. Great loot!")
            inventory.append("2 golden ore")
            inventory.append("3 kg of coal")
            print(f"Current inventory: {inventory}")
            break




print("Day Three")
if choice == 1:
    if choiced1 == 2:
        if choiced1_d2 == 2:
            print("You are the absolute luckiest. This was a weird abandoned social experiment.")
            print("You made the best choices, they bring you back to the labor.")
            print("You realized that the last 3 days was your best days of your life...")
            print("You got the money. 10 000 $. Return to home. You hung yourself in the backyard.")
            print("Game Over")
elif choice == 4:
    if choiced1_2 == 1:
        if choiced1_2_d2 == 1:
            print("You are among the lucky ones. This was a weird abandoned social experiment.")
            print("You made a bunch of good choices. The amnesia pill's effect start to break earlier")
            print("You don't want to go back to the labor. The past 3 days was better than your actual life.")
            print("You start to resist, while the doctors' security grab you. You were accidentally shot.")
            print("Game Over")
    elif choiced1_2 == 2:
        print("You were the most nonchalant. This was a weird abandoned social experiment.")
        print("You are a young person. You just wanted the money.")
        print("You didn't know that the last 3 days are probably one of the best days of your life.")
        print("You return home, and spend all your remaining life just existing...")
        print("Game Over")

print("The name of the game: Remnora")

print("Thanks for playing!")

    






















































