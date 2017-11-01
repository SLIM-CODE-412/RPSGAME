#RPS_GAME
"""-prompt user for choice of rock,paper,scissors
	-have "computer" randomly pick rock paper or scissors
	-compare choices to dictate who wins, if there is a winner
	-tell em who won
	-import randint
	-import sleep [simulating computer "thinking"..]"""



from random import randint
from time import sleep

options=["R","P","S"]
WIN_MES= "WINNER, WINNER, CHICKEN DINNER!"
LOSS_MES= "YOU LOSE"
STUPID_MES="INVALID SELF DESCRUCT IN... /n 5 /n 4 /n 3/n 2/n 1/n"


def decide_winner(user_choice,computer_choice):
  print ("You selected %s" % user_choice)
  print ("Computer selecting..") #EDIT THIS FOR BETTER EFFECT. eeney meeney minny moe?
  sleep (1)
  print ("The computer selected %s" % computer_choice)
  user_choice_index= options.index(user_choice)
  computer_choice_index=options.index(computer_choice)
  if user_choice_index==0 and computer_choice_index==2:
	  print(WIN_MES)
	  replay_game=input("Wanna try again(Y/N)")
	  replay_game=replay_game.upper()
	  if replay_game == "Y":
	    play_RPS()
	  else:
	    print("Thank you for playing! Goodbye")
  elif user_choice_index==1 and computer_choice_index==0:
	  print(WIN_MES)
	  replay_game=input("Wanna try again(Y/N)")
	  replay_game=replay_game.upper()
	  if replay_game == "Y":
	    play_RPS()
	  else:
	    print("Thank you for playing! Goodbye")
  elif user_choice_index==2 and computer_choice_index==1:
	  print(WIN_MES)
	  replay_game=input("Wanna try again(Y/N)")
	  replay_game=replay_game.upper()
	  if replay_game == "Y":
	    play_RPS()
	  else:
	    print("Thank you for playing! Goodbye")
  elif user_choice_index==computer_choice_index:
	  print("How about that! A tie! ")
	  replay_game=input("Wanna try again(Y/N)")
	  replay_game=replay_game.upper()
	  if replay_game == "Y":
	    play_RPS()
	  else:
	    print("Thank you for playing! Goodbye")
  elif user_choice_index != "R" or user_choice_index != "P" or user_choice_index != "S":
	    print(STUPID_MES)
  else:
	  print(LOSS_MES)
	  replay_game=input("Wanna try again(Y/N)")
	  replay_game=replay_game.upper()
	  if replay_game == "Y":
	    play_RPS()
	  else:
	    print("Thank you for playing! Goodbye")
		
		
def play_RPS():
	print("Welcome to Rock Paper Scissors")
	user_choice=input("Pick either Rock (R), Paper (P) or Scissors(S):")
	user_choice=user_choice.upper()
	sleep (1)
	computer_choice=options[randint(0,2)]
	decide_winner(user_choice,computer_choice)
	
	
play_RPS()