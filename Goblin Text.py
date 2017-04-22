cdef game():
	answer1 = input("Hello!, This game is called The Adventure, it is about a man who wants to find treasure, your goal is to find it. It's a dangerous world out there, a single wrong choice could kill you. Do you want to play? *note answers are case sensitive* Y/N ")
	if answer1 == "Y":
		print("Ok, lets start! You leave your hometown and travel for two days.")
		choice1 = input("Eventually you come to a crossroads, you can take the bridge over a treacherous river or a long road. pick 'bridge' or 'road' ")
		if choice1 == "bridge":
			print("You cross the bridge and a goblin jumps out at you, luckily you have your sword and you kill the goblin, but break your sword in the process, you loot the goblin and find a bow.")
			choice2 = input("You arrive at a new crossroad with another bridge, pick 'bridge' or 'road' ")
			if choice2 == "road":
				choice3 = input("As you walk the road, you spot a group of goblins, you shoot them from a distance with your bow. Choose to approach them and loot them or carry on. Choose 'loot' or 'pass' ")
				if choice3 == "pass":
					choice4 = input("As you skirt around the dead goblins, you see one of them open an eye. Yikes that was close! As you pass them, you see a forest in the distance. If you want to go in the forest type 'enter' if not, type 'pass' ")
					if choice4 == "enter":
						choice5 = input("You enter the forest slightly fearful, you see a huge mushroom growth on a tree, pick the mushrooms or keep going, type 'pick' for the shrooms and 'pass' for passing ")
						if choice5 == "pick":
							print("You begin picking the mushrooms when you see a little gleam reflect off of the sunlight underneath. You spend a while digging until you uncover even more shine. It's buried treasure! You win!")
							restart()
						else:
							print("You get eaten by a carnivorous plant.")
							print("Game Over.")
							restart()
					else:
						print("You find a goblin disguised as a traveler, you notice too late and he kills you.")
						print("Game Over.")
						restart()
				else:
					print("One of the faked it and killed you.")
					print("Game Over.")
					restart()
			else:
				print("You cross the bridge and find a goblin hiding at the end, he kills you.")
				print("Game Over.")
				restart()
		else:
			print("You see goblins up ahead, you attack them but they swarm you.")
			print("Game Over.")
			restart()
	else:
		exit()

def restart():
	choice = input("Would you like to restart? Y/N ")
	if choice == "Y":
		game()
	else:
		exit()

game()
