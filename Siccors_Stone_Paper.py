import random
loop = 1 
your_choice = [""]
enemy_choice = ["",""] 

def enter_your_choice():
	try:
		your_choice[0] = int(input("Enter 1:Schere | 2:Stein | 3:Papier:"))-1
	except ValueError :
		print("Enter a number")
		enter_your_choice()
def CPU_mades_a_choice():
	enemy_choice[0] = random.randint(1, 3)

def Question():
	question = input("Do you want to play again? Y/N ")
	if "y" in str.lower(question):
		loop = 1
	elif "n" in str.lower(question):
		loop = 0
	else:
		print("Invalid answer")
		Question()


while loop == 1:
	enter_your_choice()
	CPU_mades_a_choice()
	if your_choice[0] == 1 & enemy_choice[0] == 3:
		print("Win; Schere schneidet Papier")
	elif your_choice[0] == 1 & enemy_choice[0] == 2:
		print("Lose; Stein schlägt Schere")		  
	elif your_choice[0] == 2 & enemy_choice[0] == 1: 
		print("Win; Stein schlägt Schere")					
	elif your_choice[0] == 2 & enemy_choice[0] == 3:  
		print("Lose; Papier umhüllt Stein")
	elif your_choice[0] == 3 & enemy_choice[0] == 2: 
		print("Win; Papier umhüllt Stein")	
	elif your_choice[0] == 3 & enemy_choice[0] == 1: 
		print("Lose; Schere schneidet Papier")
	else : 
		print("Draw") 
	if enemy_choice[0] == 1:
		enemy_choice[1] = "Schere"
	elif enemy_choice[0] == 2: 
		enemy_choice[1] = "Stein"
	else :
		enemy_choice[1] = "Papier"	
	print("Der CPU wählte "+enemy_choice[1])
	your_choice[0] = ""
	enemy_choice[0] = ""
	enemy_choice[1] = ""
	Question()	
	
	


	 


