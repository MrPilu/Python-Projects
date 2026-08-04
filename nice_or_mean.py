import random

def title():
    print("=" * 50)
    print("        NICE OR MEAN ADVENTURE")
    print("=" * 50)


def difficulty():
    while True:
        print("\nChoose Difficulty")
        print("1. Easy")
        print("2. Normal")
        print("3. Hard")

        choice = input("Selection: ")

        if choice == "1":
            return 120
        elif choice == "2":
            return 100
        elif choice == "3":
            return 80
        else:
            print("Invalid choice.")


def random_event(player):

    events = [

        {
            "name": "Old Wizard",
            "nice":
                ("The wizard gives you a magic potion.",
                 {"rep":2,"gold":10,"health":10,"item":"Potion"}),

            "mean":
                ("The wizard curses you.",
                 {"rep":-2,"health":-20})
        },

        {
            "name":"Lost Child",
            "nice":
                ("You help the child find home.",
                 {"rep":3,"gold":5}),

            "mean":
                ("You scare the child.",
                 {"rep":-3})
        },

        {
            "name":"Merchant",
            "nice":
                ("The merchant rewards your kindness.",
                 {"gold":20,"rep":2}),

            "mean":
                ("The merchant refuses to trade.",
                 {"rep":-2})
        },

        {
            "name":"Knight",
            "nice":
                ("The knight gives you armor.",
                 {"health":15,"item":"Armor","rep":2}),

            "mean":
                ("The knight challenges you.",
                 {"health":-25})
        },

        {
            "name":"Hungry Dog",
            "nice":
                ("The dog becomes your friend.",
                 {"item":"Dog","rep":2}),

            "mean":
                ("The dog bites you.",
                 {"health":-10})
        }

    ]

    event = random.choice(events)

    print("\nYou meet:", event["name"])

    while True:

        action = input("Be Nice or Mean? (n/m): ").lower()

        if action == "n":

            text, reward = event["nice"]

            break

        elif action == "m":

            text, reward = event["mean"]

            break

        else:
            print("Please type n or m.")

    print("\n" + text)

    player["health"] += reward.get("health",0)
    player["gold"] += reward.get("gold",0)
    player["rep"] += reward.get("rep",0)

    if "item" in reward:
        player["inventory"].append(reward["item"])
        print("You received:", reward["item"])


def stats(player):

    print("\n----------------------------")
    print("Health:",player["health"])
    print("Gold:",player["gold"])
    print("Reputation:",player["rep"])

    if player["inventory"]:
        print("Inventory:",", ".join(player["inventory"]))
    else:
        print("Inventory: Empty")

    print("----------------------------")


def ending(player):

    if player["health"] <= 0:
        print("\nYou have died...")
        return True

    if player["rep"] >= 10:
        print("\nYou became the HERO of the Kingdom!")
        return True

    if player["rep"] <= -10:
        print("\nYou became the Kingdom's MOST WANTED criminal!")
        return True

    if player["gold"] >= 100:
        print("\nYou became the richest merchant in town!")
        return True

    return False


def play():

    title()

    name = input("What is your name? ")

    health = difficulty()

    player = {

        "name":name,
        "health":health,
        "gold":20,
        "rep":0,
        "inventory":[]

    }

    print("\nWelcome,",name)

    while True:

        random_event(player)

        stats(player)

        if ending(player):
            break

    print("\nFinal Results")
    stats(player)

    again = input("\nPlay Again? (y/n): ").lower()

    if again == "y":
        play()

    else:
        print("\nThanks for playing!")


play()