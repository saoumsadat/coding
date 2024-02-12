import random

def playRockPaperScissor(rounds):
	choices = ["rock", "paper", "scissor"]
	playerWins = 0
	compWins = 0
	winner = ''

	for x in range(0, n):
		userChoice = input()
		computerChoice = random.choice(choices)
		print("Computer: " + computerChoice)

		if userChoice == "rock" and computerChoice == "paper":
			compWins += 1
		elif userChoice == "rock" and computerChoice == "scissor":
			playerWins += 1
		elif userChoice == "paper" and computerChoice == "scissor":
			compWins += 1
		elif userChoice == "paper" and computerChoice == "rock":
			playerWins += 1
		elif userChoice == "scissor" and computerChoice == "rock":
			compWins += 1
		elif userChoice == "scissor" and computerChoice == "paper":
			playerWins += 1
	
	if playerWins < compWins:
		winner = "Computer has "
	elif compWins < playerWins:
		winner = "You have "
	else:
		winner = "তুমি কি দেখেছো কভু, জীবনের পরাজয়?"
	
	print("Your Score: ", playerWins)
	print("Computer's Score: ", compWins)
	print(winner + "won the game!")
	

n = int(input())
playRockPaperScissor(n)
