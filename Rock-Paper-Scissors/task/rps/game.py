import random


def draw(option):
    print("There is a draw (" + option + ")")
    return 50


def player_win(option):
    print("Well done. The computer chose " + option + " and failed")
    return 100


def player_loss(option):
    print("Sorry, but the computer chose " + option)
    return 0


def get_rating_for_player(name_to_find):
    rating_file = open("rating.txt")
    ratings = rating_file.readlines()
    rating_file.close()
    for rating in ratings:
        entry = rating.split(' ')
        if entry[0] == name_to_find:
            return int(entry[1])
    return 0


def get_options():
    user_input = input()
    if user_input == "":
        return ["rock", "paper", "scissors"]
    suggested_options = user_input.split(",")
    print("Okay, let's start")
    return suggested_options


name = input("Enter your name:")
print("Hello, " + name)
score = get_rating_for_player(name)


def process_turn(player_choice, ai_choice, options):
    result = decide_result(ai_choice, player_choice, options)

    if result == "win":
        return player_win(ai_choice)
    elif result == "loss":
        return player_loss(ai_choice)
    else:
        return draw(ai_choice)


def decide_result(ai_choice, player_choice, options):
    if player_choice == ai_choice:
        return "draw"

    later_options = options[options.index(ai_choice) + 1:]
    earlier_options = options[:options.index(ai_choice):]
    other_options = later_options + earlier_options
    winners = other_options[:len(other_options)//2]
    return "win" if player_choice in winners else "loss"


global_options = get_options()

while True:
    player_input = input()

    if player_input == "!exit":
        print("Bye!")
        break
    elif player_input == "!rating":
        print("Your rating: " + str(score))
    elif player_input in global_options:
        score += process_turn(player_input, global_options[random.randint(0, 2)], global_options)
    else:
        print("Invalid input")
