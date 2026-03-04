import random



player = input("Enter Your Name: ")
traveler1 = input("Enter The First Travelers Name: ")
traveler2 = input("Enter The Second Travelers Name: ")
traveler3 = input("Enter The Third Travelers Name: ")
traveler4 = input("Enter The Forth Travelers Name: ")
traveler5 = input("Enter The Fifth Travelers Name: ")

location = "Albert Lea"
player_heath = 100
player_hunger = 0
player_thirst = 0
player_stamina = 100


running = True

while running == True:
    def status():
        print(location)
        print("Health: " + str(player_heath))
        print("Hunger: " + str(player_hunger))
        print("Thirst: " + str(player_thirst))
        print("Stamina: " + str(player_stamina))    

    def player_turn():
        action = input("What Do You Want To Do? ").lower().strip()
        if action == "travel":
            player_stamina =- 10
            print("Travel")

        elif action == "rest":
            time = input("How Long Do You Want To Rest For? ")
            player_stamina =+ time 
            if player_stamina >= 85:
                print("You Feel Well Rested")
            elif player_stamina <= 85:
                print("You Feel Rested")
            elif player_stamina <= 50:
                print("You Are Still Tired")
            else:
                print("You Are Super Tired")

        elif action == "hunt":
            print("hunt")

        elif action == "status":
            status()

        elif action == "quit":
            print("Thanks For Playing!")
            running = False
        else:
            print("Invalid Try Again")

    player_turn()
    