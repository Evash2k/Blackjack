import random
import time





play_game = input("Start the game? y/n:")

player_current_deck = 0
dealer_current_deck = 0

def reset_player():
  player_current_deck = 0
def reset_dealer():
  dealer_current_deck = 0


current_cash = 10000


while (play_game.lower() == "y"):

  print(format(f"You currently have ${current_cash:,} "))
  time.sleep(2)
  betting_ammount = int(input("How much are you betting?: "))
  while (betting_ammount > current_cash):
    betting_ammount = int(input(f"You can't bet more than {current_cash}"))


  player_current_deck = 0
  dealer_current_deck = 0



  random_card_player = random.randint(1,11)
  random_card_dealer = random.randint(1,11)

  player_current_deck += random_card_player
  dealer_current_deck += random_card_dealer

  print(f"You have {player_current_deck} and the dealer has {dealer_current_deck} ")
  hit_or_stand = input("Hit or stand: ")

  while(hit_or_stand.lower() == "hit"):
    random_card_player = random.randint(1,11)
    player_current_deck += random_card_player
    del random_card_player

    if (player_current_deck > 21):
      print(f"You have {player_current_deck} which is greater than 21!")
      current_cash -= betting_ammount
      print(format(f"You lose! You now have ${current_cash: ,} in your bank account."))
      time.sleep(2)
      play_game = input("Restart the game? y/n:")
      break

    elif (player_current_deck < 21):
      print(f"You have now have {player_current_deck}")
      hit_or_stand = input("Hit or stand: ")
    else:
      print(f"You now have {player_current_deck} so you automatically win!")
      current_cash += betting_ammount
      print(format(f"You now have ${current_cash: ,} in your bank account."))
      play_game = input("Restart the game? y/n:")
      break


  while (hit_or_stand.lower() == "stand"):
    random_card_dealer = random.randint(1,11)
    dealer_current_deck += random_card_dealer


    if (dealer_current_deck > 21):
      print(f"The dealer rolled {random_card_dealer}")
      print(f"The dealer has {dealer_current_deck} and busted! You win!")
      current_cash += betting_ammount
      print(format(f"You now have ${current_cash: ,} in your bank account."))
      play_game = input("Restart the game? y/n:")
      break

    if (dealer_current_deck >= 17 and dealer_current_deck <= 21):

      if (dealer_current_deck > player_current_deck):
        print(f"The dealer rolled {random_card_dealer}")
        print(f"The dealer has {dealer_current_deck} and you have {player_current_deck}, you lose!")
        current_cash -= betting_ammount
        print(format(f"You now have ${current_cash: ,} in your bank account."))
        play_game = input("Restart the game? y/n:")
        break


      elif (dealer_current_deck < player_current_deck):
        print(f"The dealer rolled {random_card_dealer}")
        print(f"The dealer has {dealer_current_deck} and you have {player_current_deck}, you win!")
        current_cash += betting_ammount
        print(format(f"You now have ${current_cash: ,} in your bank account."))
        play_game = input("Restart the game? y/n:")
        break

    else:
      print(f"The dealer rolled {random_card_dealer} and now has {dealer_current_deck}")
    del random_card_dealer
