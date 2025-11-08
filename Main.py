from IPython.display import clear_output
import random
import time

play_game = input("Start the game? y/n:")

player_current_deck = 0
dealer_current_deck = 0

def reset_player():
  player_current_deck = 0
def reset_dealer():
  dealer_current_deck = 0

while (play_game.lower() == "y"):
  player_current_deck = 0
  dealer_current_deck = 0
  random_card_player = random.randint(1,11)
  random_card_dealer = random.randint(1,11)

  player_current_deck += random_card_player

  dealer_current_deck += random_card_dealer

  print(f"You have {player_current_deck} and the dealer has {dealer_current_deck} ")
  time.sleep(2)
  hit_or_stand = input("Hit or stand: ")

  while(hit_or_stand.lower() == "hit"):
    random_card_player = random.randint(1,11)
    player_current_deck += random_card_player
    del random_card_player

    if (player_current_deck > 21):
      print(f"You have {player_current_deck} which is greater than 21!")
      print("You lose!")
      play_game = input("Restart the game? y/n:")
      break
          
    else: 
      print(f"You have now have {player_current_deck}")
      time.sleep(2)
      hit_or_stand = input("Hit or stand: ")



  while (hit_or_stand.lower() == "stand"):
    random_card_dealer = random.randint(1,11)
    dealer_current_deck += random_card_dealer
    del random_card_dealer

    if (dealer_current_deck > 21):
      print(f"The dealer has {dealer_current_deck} and busted! You win!")

      play_game = input("Restart the game? y/n:")
      break

    if (dealer_current_deck >= 17 and dealer_current_deck <= 21):

      if (dealer_current_deck > player_current_deck):
        print(f"The dealer has {dealer_current_deck} and you have {player_current_deck}, you lose!")
        play_game = input("Restart the game? y/n:")
        break
        

      elif (dealer_current_deck < player_current_deck):
        print(f"The dealer has {dealer_current_deck} and you have {player_current_deck}, you win!")
        play_game = input("Restart the game? y/n:")
        break
        
    else:
      print(f"The dealer currently has {dealer_current_deck}")
      time.sleep(2)
  clear_output()


















