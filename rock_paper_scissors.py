import random

comm = ["r","s","p"]
score_user = 0
score_machine = 0

def game_result(user_input):
    global score_user
    global score_machine
    
    machine = random.choice(comm)

    if user_input == machine:
        return "It's a draw!"
    elif user_input == "r" and machine == "s":
        score_user += 1
        return "You chose rock and the computer chose scissors. You win!"
    elif user_input == "r" and machine == "p":
        score_machine += 1
        return "You chose rock and the computer chose paper. You lose!"
    elif user_input == "s" and machine == "p":
        score_user += 1
        return "You chose scissors and the computer chose paper. You win!"
    elif user_input == "s" and machine == "r":
        score_machine += 1
        return "You chose scissors and the computer chose rock. You lose!"
    elif user_input == "p" and machine == "s":
        score_user += 1
        return "You chose paper and the computer chose scissors. You win!"
    elif user_input == "p" and machine == "r":
        score_machine += 1
        return "You chose paper and the computer chose rock. You lose!"


while True:
    print("Make a move!(r/s/p - r for rock, s for scissors, p for paper")
    user_input = input()

    if user_input in comm:
        print(game_result(user_input))
    elif user_input == "sc":
        print("human: " + str(score_user) + ", computer: " + str(score_machine))

    print("Do you want to play again? (y/n)")

    if input() == "n":
        break
