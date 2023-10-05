from random import randint
easy_levl_turns=10
hard_level_turns=5

def check_answer(guess,answer,turns):
    if guess>answer:
        print("Too high")
        return turns - 1
    elif guess<answer:
        print("Too low")
        return turns -1 
    else:
        print("Wohoo correct answer!")

def set_difficulty():
    level= input("Choose level of game .Type 'easy' or 'difficult' . ")
    if level == "easy":
        return easy_levl_turns
    else:
        return hard_level_turns

def game():
    print ("""
  _____                       _   _                                  _               
  / ____|                     | | | |                                | |              
 | |  __ _   _  ___  ___ ___  | |_| |__   ___   _ __  _   _ _ __ ___ | |__   ___ _ __ 
 | | |_ | | | |/ _ \/ __/ __| | __| '_ \ / _ \ | '_ \| | | | '_ ` _ \| '_ \ / _ \ '__|
 | |__| | |_| |  __/\__ \__ \ | |_| | | |  __/ | | | | |_| | | | | | | |_) |  __/ |   
  \_____|\__,_|\___||___/___/  \__|_| |_|\___| |_| |_|\__,_|_| |_| |_|_.__/ \___|_|   
    """)

    print("Welcome to number guessing game!!!!!!!!")
    print("Guess a number between 1 and 200")
    answer=randint(1,200)

    turns=set_difficulty()
    guess=0
    while guess!=answer:
        print(f"You have {turns} remaining to guess the number")

        guess= int(input("Make a guess: "))

        turns = check_answer(guess,answer,turns)
        if turns==0:
            print(f"You've run out of guesses,you lose. The correct answer was {answer}")    
            return
        elif guess!=answer:
            print("Guess again!")

game()