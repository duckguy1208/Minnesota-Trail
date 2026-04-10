def Shop():
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