# ask the user for their name
name = input("What is your name?: ")

# ask the user for their age
age = input("What is your age?: ")

# check if the user is old enough to play
if int(age) >= 18:
  print(f"Greetings {name}! Welcome to your adventure game!")

  # ask the user what they would like to do
  start = input(
      "Would you rather perish or play the game? (type 'play' or 'perish'): ")

  # if the user wants to play, start the game
  if start == "play":
    print("Great, let's play the game!")
    setting = input(
        "Would you like to go to the jungle or the desert? (type 'jungle' or 'desert'): "
    )

    # if the user wants to go to the jungle, start the jungle adventure
    if setting == "jungle":
      print(
          "Welcome to the Amazon Rainforest! Your tour guide told you to wait here..."
      )

      response = input(
          "But the tour guide has been gone for a long time... Do you want to follow him or wait here? (type 'follow' or 'wait'): "
      )

      if response == "follow":
        print("You follow the tour guide and he leads you to a waterfall.")

        response2 = input(
            "Do you want to go to the waterfall or go back? (type 'waterfall' or 'go back'): "
        )

        if response2 == "waterfall":
          print(
              "You go to the waterfall and you see a group of monkeys. The monkeys start to attack you."
          )

          response3 = input(
              "Do you want to fight the monkeys or run away? (type 'fight' or 'run away'): "
          )
          if response3 == "fight":
            print(
                "You fight the monkeys and you win! You are now the king of the jungle."
            )
          elif response3 == "run away":
            print("You run away and the monkeys catch you. You lose!")
            quit()
          else:
            print("Invalid response. You lose.")
            quit()

        elif response2 == "go back":
          print(
              "You go back and the tour guide is nowhere to be found. You lose."
          )
          quit()

        else:
          print("Invalid response. You lose.")
          quit()

        response4 = input(
            "Do you want to enter the cave or admire the waterfall? (type 'enter' or 'admire'): "
        )

        if response4 == "enter":
          print(
              "You enter the cave and find a chest full of treasure. Congratulations, you've won the jungle adventure!"
          )
          quit()

        elif response4 == "admire":
          print(
              "You admire the waterfall, feeling at peace. The tour guide eventually returns, and you both leave the jungle together."
          )
          quit()

      elif response == "wait":
        print(
            "You wait another 10 minutes, and the tour guide still isn't here."
        )
        print("Impatient, you decide to explore on your own.")

        response4 = input(
            "You come across a mysterious cave. Do you want to enter the cave or continue waiting? (type 'enter' or 'continue waiting'): "
        )

        if response4 == "enter":
          print(
              "You enter the cave and discover hidden treasures. Congratulations, you've won the jungle adventure!"
          )
          quit()
        elif response4 == "continue waiting":
          print(
              "You continue waiting, but the tour guide never returns. You lose."
          )
          quit()
        else:
          print("Invalid response. You lose.")
          quit()
      else:
        print("Invalid response. You lose.")
        quit()

    # if the user wants to go to the desert, start the desert adventure
    elif setting == "desert":
      print(
          "Welcome to the Sahara Desert! Your tour guide told you to wait here..."
      )

      response = input(
          "But the tour guide has been gone for a long time... Do you want to follow him or wait here? (type 'follow' or 'wait'): "
      )

      if response == "follow":
        print("You follow the tour guide and he leads you to the dunes...")

        response2 = input(
            "Do you want to climb the highest dune or go back? (type 'climb' or 'go back'): "
        )

        if response2 == "climb":
          print(
              "You climb the highest dune and spot an oasis in the distance.")

          response3 = input(
              "Do you want to head towards the oasis or descend the dune? (type 'oasis' or 'descend'): "
          )

          if response3 == "oasis":
            print(
                "You reach the oasis and find a hidden paradise. Congratulations, you've won the desert adventure!"
            )
            quit()
          elif response3 == "descend":
            print(
                "As you descend, a sandstorm approaches. You barely escape, and the tour guide returns to guide you back."
            )
            quit()
          else:
            print("Invalid response. You lose.")
            quit()

        response2 = input(
            "Do you want to go to the dunes or go back? (type 'dunes' or 'go back'): "
        )

        if response2 == "dunes":
          print(
              "You go to the dunes and you see a group of camels. The camels start to attack you."
          )

          response3 = input(
              "Do you want to fight the camels or run away? (type 'fight' or 'run away'): "
          )

          if response3 == "fight":
            print(
                "You fight the camels and you win! You are now the king of the desert."
            )
            quit()
          elif response3 == "run away":
            print(f"You run away and the camels catch you. You lose, {name}.")
            quit()
          else:
            print("Invalid response. You lose.")
            quit()

        elif response2 == "go back":
          print(
              "You go back and the tour guide is nowhere to be found. You lose."
          )
          quit()

      elif response == "wait":
        print(
            "You wait another 10 minutes, and the tour guide still isn't here."
        )
        print("Impatient, you decide to explore on your own.")

        response4 = input(
            "You find gold in the sand. Do you want to take it or leave it? (type 'take' or 'leave'): "
        )

        if response4 == "take":
          print(
              f"You take the gold and the tour guide is nowhere to be found. You lose, {name}."
          )
          quit()

        elif response4 == "leave":
          print(
              f"You leave the gold and the tour guide is nowhere to be found. You lose, {name}."
          )
          quit()

        else:
          print("Invalid response. You lose.")
          quit()

      else:
        print("Invalid response. You lose.")
        quit()

    else:
      print("Invalid response. You lose.")
      quit()

  # if the user does not want to play, end the game
  else:
    print(f"Okay {name}, you have perished. Game over.")

# if the user is not old enough to play, tell them to come back when they are 18
else:
  print(f"Sorry {name}, you are not old enough to play this game. Come back when you are 18 or older.")