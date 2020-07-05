from tkinter import *
import random

root = Tk()
#random choise for computer
p=["rock","paper","scissors"]
computer = random.choice(p)
#game structure
def rpsfunction(computer, player):
	if player == computer:
	    print("Tie!")
	elif player == "rock":
	    if computer == "paper":
	        print("You lose!", computer, "covers", player)
	    else:
	        print("You win!", player, "smashes", computer)
	elif player == "paper":
	    if computer == "scissors":
	        print("You lose!", computer, "cut", player)
	    else:
	        print("You win!", player, "covers", computer)
	elif player == "scissors":
	    if computer == "rock":
	        print("You lose...", computer, "smashes", player)
	    else:
	        print("You win!", player, "cut", computer)
	else:
	    print("That's not a valid play. Check your spelling!")
#button functions
def rocc():
	rpsfunction(computer, "rock")
def paypar():
	rpsfunction(computer, "paper")
def caezar():
	rpsfunction(computer, "scissors")
#creating buttons and showing them
textura = Label(root, text="Rock Paper Scissors!").pack()
rocc = Button(root, text="rock", command=rocc).pack()
paypar = Button(root, text="paper", command=paypar).pack()
caezar = Button(root, text="scissors", command=caezar).pack()

root.mainloop()
