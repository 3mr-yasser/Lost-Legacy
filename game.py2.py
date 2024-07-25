import time
import random

# Initialize global score
score = 0


# Define a function to pause and print messages
def print_pause(message):
    print(message)
    time.sleep(1.6)


# Update the score and print it
def total_score(points):
    global score
    score += points
    print(f"Player's score: {score}")
    return score


# Function to handle random outcomes
def random_outcome(outcome1, pts1, outcome2, pts2):
    outcome = random.choice([outcome1, outcome2])
    print_pause(outcome)
    if outcome == outcome1:
        total_score(pts1)
    elif outcome == outcome2:
        total_score(pts2)


# Main function to control the game flow
def game():
    global score
    score = 0
    while True:
        # function to get the user name
        while True:
            name = input("What is your name?")
            if name.isalpha():
                break
            else:
                print("invaild input please enter a name ")
        print_pause(f"You are {name}, a skilled adventurer.")
        print_pause("One day, you receive a letter with an old map and a message.")
        print_pause("You are the one who can find the Lost Kingdom.")
        print_pause("Follow the map to uncover its secrets.")
        print_pause("Excited, you decide to go on this adventure.")
        print_pause("Your journey begins at the edge of an ancient forest")
        print_pause("said to be the entrance to the Lost Kingdom.")
        print_pause("You feel a mix of excitement and nerves. The adventure awaits.")
        print_pause("The Forest Path. You stand at the edge of the forest.")
        print_pause("Enter 1 to enter the forest")
        print_pause("Enter 2 to search for another path")
        choice = input("What would you like to do? (Please enter 1 or 2): ")
        if choice == "1":
            enter_the_forest()
            total_score(10)
        elif choice == "2":
            search_for_another_path()
        else:
            print("Invalid input. Please enter 1 or 2.")


# Function for entering the forest path
def enter_the_forest():
    print_pause("You find a hidden trail. Suddenly, you hear a noise behind you.")
    print_pause("Enter 1 to investigate the noise")
    print_pause("Enter 2 to ignore it and move forward")
    choice = input("What would you like to do? (Please enter 1 or 2): ")
    if choice == "1":
        investigate_the_noise()
        total_score(10)
    elif choice == "2":
        ignore_it_and_move_forward()
    else:
        print("Invalid input. Please enter 1 or 2.")
        enter_the_forest()


# Function for searching another path
def search_for_another_path():
    print_pause("You find a river with a small boat.")
    print_pause("Enter 1 to take the boat")
    print_pause("Enter 2 to walk along the riverbank")
    choice = input("What would you like to do? (Please enter 1 or 2): ")
    if choice == "1":
        take_the_boat()
        total_score(10)
    elif choice == "2":
        walk_along_the_riverbank()
        total_score(10)
    else:
        print("Invalid input. Please enter 1 or 2.")
        search_for_another_path()


# Function for investigating the noise in the forest
def investigate_the_noise():
    random_outcome(
        "You find a hidden cave filled with valuable artifacts, transforming a potentially dangerous moment into a fortunate discovery.",
        50,
        "While following the noise, you suddenly fall into a pit and hurt yourself.",
        -50,
    )
    print_pause("You meet an old hermit named Sayed. He offers to help.")
    print_pause("Enter 1 to accept his help")
    print_pause("Enter 2 to decline his help")
    choice = input("What would you like to do? (Please enter 1 or 2): ")
    if choice == "1":
        accept_his_help()
        total_score(10)
    elif choice == "2":
        decline_his_help()
    else:
        print("Invalid input. Please enter 1 or 2.")
        investigate_the_noise()


# Function for ignoring the noise and moving forward in the forest
def ignore_it_and_move_forward():
    print_pause("You come to a fork in the path.")
    print_pause("Enter 1 to take the left path")
    print_pause("Enter 2 to take the right path")
    choice = input("What would you like to do? (Please enter 1 or 2): ")
    if choice == "1":
        the_left_path()
        total_score(10)
    elif choice == "2":
        the_right_path()
        total_score(10)
    else:
        print("Invalid input. Please enter 1 or 2.")
        ignore_it_and_move_forward()


# Function for taking the left path
def the_left_path():
    print_pause("You find a sage in a clearing.")
    print_pause("Enter 1 to ask the sage for help")
    print_pause("Enter 2 to continue by yourself")
    choice = input("What would you like to do? (Please enter 1 or 2): ")
    if choice == "1":
        ask_the_sage_for_help()
        total_score(100)
        pass
    elif choice == "2":
        continue_by_yourself()
        total_score(-50)
        pass
    else:
        print("Invalid input. Please enter 1 or 2.")
        the_left_path()


# Function for taking the right path
def the_right_path():
    print_pause("You encounter a wild beast.")
    print_pause("Enter 1 to fight the beast")
    print_pause("Enter 2 to run away")
    choice = input("What would you like to do? (Please enter 1 or 2): ")
    if choice == "1":
        print_pause(
            "You defeat the beast and find a hidden path to the Lost Kingdom. You win!"
        )
        total_score(100)
        end_the_game()
    elif choice == "2":
        print_pause("You get lost. You lose.")
        total_score(-50)
        end_the_game()
    else:
        print("Invalid input. Please enter 1 or 2.")
        the_right_path()


# Function for accepting help from the hermit
def accept_his_help():
    print_pause("Enter 1 to follow the map")
    print_pause("Enter 2 to trust Sayed's instincts")
    choice = input("What would you like to do? (Please enter 1 or 2): ")
    if choice == "1":
        print_pause("You find the Lost Kingdom and its secrets. You win!")
        total_score(100)
        end_the_game()
    elif choice == "2":
        print_pause("Sayed betrays you, and you get lost. You lose.")
        total_score(-50)
        end_the_game()
    else:
        print("Invalid input. Please enter 1 or 2.")
        accept_his_help()


# Function for declining help from the hermit
def decline_his_help():
    print_pause("You get lost and find an ancient ruin.")
    print_pause("Enter 1 to explore the ruin")
    print_pause("Enter 2 to find a way around it")
    choice = input("What would you like to do? (Please enter 1 or 2): ")
    if choice == "1":
        print_pause("You find clues but are trapped by a curse. You lose.")
        total_score(-100)
        end_the_game()
    elif choice == "2":
        print_pause("You avoid the ruin and find the Lost Kingdom. You win!")
        total_score(100)
        end_the_game()
    else:
        print("Invalid input. Please enter 1 or 2.")
        decline_his_help()


# Function for taking the boat
def take_the_boat():
    random_outcome(
        "You find a paddle floating on the water and use it to arrive faster.",
        50,
        "Your boat gets attacked by piranhas, but you paddle away as fast as you can and manage to survive with a hole in your boat.",
        -50,
    )
    print_pause("You meet a river guardian who offers guidance.")
    print_pause("Enter 1 to trust the guardian")
    print_pause("Enter 2 to continue alone")
    choice = input("What would you like to do? (Please enter 1 or 2): ")
    if choice == "1":
        trust_the_guardian()
        total_score(10)
    elif choice == "2":
        continue_alone()
    else:
        print("Invalid input. Please enter 1 or 2.")
        take_the_boat()


# Function for walking along the riverbank
def walk_along_the_riverbank():
    print_pause("You find a small village.")
    print_pause("Enter 1 to ask the villagers for help")
    print_pause("Enter 2 to sneak through the village")
    choice = input("What would you like to do? (Please enter 1 or 2): ")
    if choice == "1":
        ask_the_villager()
    elif choice == "2":
        sneak_through_the_village()
    else:
        print("Invalid input. Please enter 1 or 2.")
        walk_along_the_riverbank()


# Function for trusting the guardian
def trust_the_guardian():
    print_pause("The guardian takes you to a secret entrance.")
    print_pause("Enter 1 to enter the entrance")
    print_pause("Enter 2 to camp by the waterfall")
    choice = input("What would you like to do? (Please enter 1 or 2): ")
    if choice == "1":
        enter_the_entrance()
    elif choice == "2":
        camp_by_the_waterfall()
    else:
        print("Invalid input. Please enter 1 or 2.")
        trust_the_guardian()


# Function for continuing alone
def continue_alone():
    print_pause("You face dangerous rapids and get lost. You lose.")
    total_score(-100)
    end_the_game()


# Function for entering the entrance
def enter_the_entrance():
    print_pause("You reach the Lost Kingdom. You win!")
    total_score(100)
    end_the_game()


# Function for camping by the waterfall
def camp_by_the_waterfall():
    print_pause("You are attacked by bandits. You lose.")
    total_score(-50)
    end_the_game()


# Function for asking the villagers
def ask_the_villager():
    print_pause("The villagers guide you to the Lost Kingdom. You win!")
    total_score(100)
    end_the_game()


# Function for sneaking through the village
def sneak_through_the_village():
    print_pause("You are caught and mistaken for a spy. You lose.")
    total_score(-50)
    end_the_game()


# function for asking the sage for help
def ask_the_sage_for_help():
    print_pause("The sage guides you to the Lost Kingdom. You win!")
    total_score(100)
    end_the_game()


# function for continue by yourself
def continue_by_yourself():
    print_pause("You get lost. You lose")
    total_score(-50)
    end_the_game()
    game()


# Function to end the game and provide options to restart or exit
def end_the_game():
    print_pause("Enter 1 to restart the game")
    print_pause("Enter 2 to exit the game")
    while True:
        retry = input("What would you like to do? (Please enter 1 or 2): ")
        if retry == "1":
            return
        elif retry == "2":
            print("Thank you for playing our old-fashioned text-based adventure game.")
            exit()
        else:
            print("Invalid input. Please enter 1 or 2.")


# Start the game loop
while True:
    # start_game()
    game()
    if end_the_game():
        break
