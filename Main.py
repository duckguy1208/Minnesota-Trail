import random

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
        hunger_recover()
        print("You Bought Food")
    elif store_choice == "2":
        thirst_recover()
        print("You Bought Water")
    elif store_choice == "3":
        health_recover()
        print("You Bought Medicine")
    elif store_choice == "4":
        print("Thanks For Visiting The Store!")
    else:
        print("Invalid Try Again")

#player attributes
def health_drain():
    global player_health, gameover
    player_health -= 5 # Decrement
    if player_health <= 0:
        print("You Died")
        gameover = True
             
def health_recover():
    global player_health
    player_health += 5 # Increment
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

#proffesion attributes
def farmer():
    global player_health, player_hunger, player_thirst, player_stamina, player_money
    player_health += 10
    player_hunger -= 10
    player_thirst -= 10
    player_stamina += 10
    player_money = 500

def carpenter():
    global player_health, player_hunger, player_thirst, player_stamina, player_money
    player_health += 5
    player_hunger -= 5
    player_thirst -= 5
    player_stamina += 15
    player_money = 1000


def banker():
    global player_health, player_hunger, player_thirst, player_stamina, player_money
    player_health += 15
    player_hunger -= 15
    player_thirst -= 15
    player_stamina += 5
    player_money = 2000

#character creation

profesion = input("Choose Your Profession (Farmer, Carpenter, Banker): ").lower().strip()
if profesion == "farmer":
    farmer()
    print("You Chose Farmer")   
elif profesion == "carpenter":
    carpenter()
    print("You Chose Carpenter")
elif profesion == "banker":
    banker()
    print("You Chose Banker")
else:
    print("Invalid Try Again")

player = input("Enter Your Name: ")
traveler1 = input("Enter The First Travelers Name: ")
traveler2 = input("Enter The Second Travelers Name: ")
traveler3 = input("Enter The Third Travelers Name: ")
traveler4 = input("Enter The Forth Travelers Name: ")



#game loop
while gameover == False:
    #player turn
    action = input("\nWhat Do You Want To Do? ").lower().strip()
    if action == "travel":
        travel()
    elif action == "rest":
        rest()
    elif action == "hunt":
        hunt()
    elif action == "status":
        status()
    elif action == "shop": #not working properly
        store()
    elif action == "quit":
        print("Thanks For Playing!")
        gameover = True
    else:
        print("Invalid Try Again")
    
    if gameover == True:
        break
    