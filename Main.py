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

    
#proffesion attributes
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

#main

#character creation

profesion = input("Choose Your Profession (Farmer, Carpenter, Banker): ").lower().strip()
if profesion == "farmer":
    farmer()
    print("\nYou Chose Farmer")   
elif profesion == "carpenter":
    carpenter()
    print("\nYou Chose Carpenter")
elif profesion == "banker":
    banker()
    print("\nYou Chose Banker")
else:
    print("\nInvalid Try Again")

player = input("\nEnter Your Name: ")
traveler1 = input("Enter The First Travelers Name: ")
traveler2 = input("Enter The Second Travelers Name: ")
traveler3 = input("Enter The Third Travelers Name: ")
traveler4 = input("Enter The Forth Travelers Name: ")

#starting store
total_food = 0
total_water = 0
total_medicine = 0
total_ammo = 0
total_oxen = 0
total_wheels = 0
total_axles = 0

print("Welcome To Tieler's Shop")
print("\nPrices:")
print("Food - $10 Per LB")
print("Water - $5 Per Gallon")
print("Medicine - $20 Per Dose")
print("Ammo - $15 Per Round")
print("Oxen - $15 Each")
print("Wheels - $10 Each")
print("Axles - $10 Each")

food_amt = int(input("How Many LBs Of Food Do You Want To Buy? "))
if food_amt > 0 and food_amt * 10 <= player_money:
    player_money -= food_amt * 10
    total_food += food_amt 
    print(f"You Bought {food_amt} LBs Of Food")
    print(f"You Have ${player_money} Left")
else:
    print("You Didn't Buy Any Food")
    print(f"You Have ${player_money} Left")

water_amt = int(input("How Many Gallons Of Water Do You Want To Buy? "))
if water_amt > 0 and water_amt * 5 <= player_money:
    player_money -= water_amt * 5
    total_water += water_amt 
    print(f"You Bought {water_amt} Gallons Of Water")
    print(f"You Have ${player_money} Left")
else:
    print("You Didn't Buy Any Water")
    print(f"You Have ${player_money} Left")

med_amt = int(input("How Much Medicine Do You Want To Buy? "))
if med_amt > 0 and med_amt * 20 <= player_money:
    player_money -= med_amt * 20
    total_medicine += med_amt 
    print(f"You Bought {med_amt} Medicine")
    print(f"You Have ${player_money} Left")
else:
    print("You Didn't Buy Any Medicine")
    print(f"You Have ${player_money} Left")

ammo_amt = int(input("How Many Rounds Of Ammo Do You Want To Buy? "))
if ammo_amt > 0 and ammo_amt * 15 <= player_money:
    player_money -= ammo_amt * 15
    total_ammo += ammo_amt 
    print(f"You Bought {ammo_amt} Rounds Of Ammo")
    print(f"You Have ${player_money} Left")
else:
    print("You Didn't Buy Any Ammo")
    print(f"You Have ${player_money} Left")

ox_amt = int(input("How Many Oxen Do You Want To Buy? "))
if ox_amt > 0 and ox_amt * 15 <= player_money:
    player_money -= ox_amt * 15
    total_oxen += ox_amt 
    print(f"You Bought {ox_amt} Oxen")
    print(f"You Have ${player_money} Left")
else:
    print("You Didn't Buy Any Oxen")
    print(f"You Have ${player_money} Left")

wheel_amt = int(input("How Many Spare Wheels Do You Want To Buy? "))
if wheel_amt > 0 and wheel_amt * 10 <= player_money:
    player_money -= wheel_amt * 10
    total_wheels += wheel_amt 
    print(f"You Bought {wheel_amt} Spare Wheels")
    print(f"You Have ${player_money} Left")
else:
    print("You Didn't Buy Any Spare Wheels")
    print(f"You Have ${player_money} Left")

axle_amt = int(input("How Many Spare Axles Do You Want To Buy? "))
if axle_amt > 0 and axle_amt * 10 <= player_money:
    player_money -= axle_amt * 10
    total_axles += axle_amt
    print(f"You Bought {axle_amt} Spare Axles")
    print(f"You Have ${player_money} Left")
else:
    print("You Didn't Buy Any Spare Axles")
    print(f"You Have ${player_money} Left")

print("\nYou Bought: ")
print(f"Food: {total_food} LBs")
print(f"Water: {total_water} Gallons")
print(f"Medicine: {total_medicine}")
print(f"Ammo: {total_ammo}")
print(f"Oxen: {total_oxen}")
print(f"Spare Wheels: {total_wheels}")
print(f"Spare Axles: {total_axles}")

print("\nThanks For Visiting Tieler's Shop!")

#starting status
print(status())


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
    elif action == "shop": 
        store()
    elif action == "quit":
        print("Thanks For Playing!")
        gameover = True
    else:
        print("Invalid Try Again")
    
    if gameover == True:
        break
    