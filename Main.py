import random

#locations
location = "Albert Lea"
locations = ["Albert Lea", "Rochester", "Mankato", "Lakeville", "Minneapolis", "Hutchinson", "St. Cloud", "Sauk Center", "Brainerd", "Duluth", "Hibbing",  "Grand Rapids", "Bemidji", "Thief River Falls", "Warroad",]
list_iterator = iter(locations)
store_location = False

#store locations
if location == "Albert Lea":
    store_location == True
elif location == "Minneapolis":
    store_location == True
elif location == "Brainerd":
    store_location == True
elif location == "Bemidji":
    store_location == True
else:
    store_location == False


player_health = 100
player_hunger = 0 
player_thirst = 0
player_stamina = 100

gameover = False

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

#attributes: health, hunger, thirst, stamina
def health_drain():
    player_health =- 5
    if player_health <= 0:
        print("You Died")
        gameover = True
             
def health_recover():
    player_health =+ 5
    if player_health >= 100:
        print("You Are Fully Healed")

def hunger_drain(): #not working properly wont drain
    player_hunger =+ 5
    if player_hunger >= 100:
        print("You Died Of Starvation")
        gameover = True
            

def hunger_recover():
    player_hunger =- 5
    if player_hunger <= 0:
        print("You Are Full")

def thirst_drain(): #not working properly wont drain
    player_thirst =+ 5
    if player_thirst >= 100:
        print("You Died Of Dehydration")
        gameover = True
           

def thirst_recover(): 
    player_thirst =- 5
    if player_thirst <= 0:
        print("You Are Fully Hydrated")
    
def stamina_drain(): #not working properly wont drain
    player_stamina =- 5
    if player_stamina <= 0:
        print("You Died Of Exhaustion")
        gameover = True
          
    
def stamina_recover():
    player_stamina =+ 5

#actions: travel, rest, hunt, status
def status(): #not working properly wont display drained stats
    print(location)
    print("Health: " + str(player_health))
    print("Hunger: " + str(player_hunger))
    print("Thirst: " + str(player_thirst))
    print("Stamina: " + str(player_stamina))    

def travel():
    stamina_drain()
    print("Traveling")
    location = next(list_iterator) #not working properly

def rest():
    time = input("How Long Do You Want To Rest For? ")
    stamina_recover()
    if player_stamina >= 85:
        print("You Feel Well Rested")
    elif player_stamina <= 85:
        print("You Feel Rested")
    elif player_stamina <= 50:
        print("You Are Still Tired")
    else:
        print("You Are Super Tired")

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



#character creation
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
    