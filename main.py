import random
from interface import interface
from player import Player
from game import Game

#locations
location = "Albert Lea"
locations = ["Rochester", "Mankato", "Lakeville", "Minneapolis", "Hutchinson", "St. Cloud", "Sauk Center", "Brainerd", "Duluth", "Hibbing",  "Grand Rapids", "Bemidji", "Thief River Falls", "Warroad",]
list_iterator = iter(locations)
store_location = False

gameover = False
if location in ["Albert Lea", "Minneapolis", "Brainerd", "Bemidji"]:
    store_location = True
else:
    store_location = False

#total supply amounts
total_food = 0
total_water = 0
total_medicine = 0
total_ammo = 0
total_oxen = 0
total_wheels = 0
total_axles = 0

#default player attributes
player_health = 100
player_hunger = 0 
player_thirst = 0
player_stamina = 100
player_money = 0



def store():
    store_choice = ""
    if store_location == True:
        print("Welcome To The Store")
        print("1. Food - $10")
        print("2. Water - $5")
        print("3. Medicine - $20")
        print("4. Rest - $15")
        print("5. Exit Store")
        store_choice = input("What Do You Want To Buy? ")
    if store_choice == "1":
        total_food += 1
        player_money -= 10
        print("You Bought Food")
    
    elif store_choice == "2":
        total_water += 1
        player_money -= 5
        print("You Bought Water")
        
    elif store_choice == "3":
        total_medicine += 1
        player_money -= 20
        print("You Bought Medicine")
        
    elif store_choice == "4":
        stamina_recover()
        player_money -= 15
        print("You Rested At The Store")
        
    elif store_choice == "5":
        print("Thanks For Visiting The Store!")

    else:
        print("No Store in "+ location)

#player attributes
def health_drain():
    global player_health, gameover
    player_health -= 5 
    if player_health <= 0:
        print("You Died")
        gameover = True

def health_recover():
    global player_health
    player_health += 5 
    total_medicine -= 1
    if player_health >= 100:
        player_health = 100
        print("You Are Fully Healed")

def hunger_drain(): 
    global player_hunger, gameover
    player_hunger += 5
    if player_hunger >= 100:
        print("You Died Of Starvation")
        gameover = True

def hunger_recover():
    global player_hunger
    player_hunger -= 5
    total_food -= 1
    if player_hunger <= 0:
        player_hunger = 0
        print("You Are Full")

def thirst_drain(): 
    global player_thirst, gameover
    player_thirst += 5
    if player_thirst >= 100:
        print("You Died Of Dehydration")
        gameover = True

def thirst_recover(): 
    global player_thirst
    player_thirst -= 5
    total_water -= 1
    if player_thirst <= 0:
        player_thirst = 0
        print("You Are Fully Hydrated")
    
def stamina_drain(): 
    global player_stamina, gameover
    player_stamina -= 5
    if player_stamina <= 0:
        print("You Died Of Exhaustion")
        gameover = True

def stamina_recover():
    global player_stamina
    player_stamina += 5
    if player_stamina > 100: player_stamina = 100

def status():
    print(f"\n--- STATUS ---")
    print(f"Location: {location}")
    print(f"Health: {player_health}")
    print(f"Hunger: {player_hunger}")
    print(f"Thirst: {player_thirst}")
    print(f"Stamina: {player_stamina}")
    print(f"Money: ${player_money}")

def travel():
    global location, store_location
    stamina_drain()
    try:
        location = next(list_iterator)
        print(f"Traveling to {location}...")
        # Update if the new city has a store
        if location in ["Albert Lea", "Minneapolis", "Brainerd", "Bemidji"]:
            store_location = True
        else:
            store_location = False
    except StopIteration:
        print("You have reached the end of the trail!")

def rest():
    time = input("How Long Do You Want To Rest For? ")
    stamina_recover()
    if player_stamina >= 85:
        print("You Feel Well Rested")
    else:
        print("You Feel Rested")

def hunt():
    hunt_chance = random.randint(1, 10)
    if hunt_chance >= 5:
        print("You Successfully Hunted")
        hunger_recover()
        thirst_recover()
        stamina_recover()
    else:
        print("You Failed To Hunt")
        hunger_drain()
        thirst_drain()
        stamina_drain()

"""
work in progress, will add more events and make them more complex

def travel_event():
    event_chance = random.randint(1, 10)
    if event_chance >= 7:
        print("You Encountered A Bandit!")
        health_drain()
        hunger_drain()
        thirst_drain()
        stamina_drain()
    elif event_chance >= 4:
        print("You Found A Stream!")
        thirst_recover()
    else:
        print("The Travel Was Uneventful")
"""

    
#profession attributes
def farmer():
    global player_health, player_hunger, player_thirst, player_stamina, player_money
    player_health += 10
    player_stamina += 10
    player_money = 500

def carpenter():
    global player_health, player_hunger, player_thirst, player_stamina, player_money
    player_health += 5
    player_stamina += 15
    player_money = 1000


def banker():
    global player_health, player_hunger, player_thirst, player_stamina, player_money
    player_health += 15
    player_stamina += 5
    player_money = 2000

def main():
    interface.printWelcome()
    playerConfig = {
        "name": interface.getName(),
        "profession": interface.getProfession()
    }
    player = Player(playerConfig)
    game = Game({ "player": player })
    game.start()

if __name__ == "__main__":
    main()