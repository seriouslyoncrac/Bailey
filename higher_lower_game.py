import random
import time

def print_loading_bar():
    print("Processing:", end=" ")
    for _ in range(20):
        time.sleep(random.uniform(0.05, 0.2))  # Simulate sporadic loading delay
        print("█", end="", flush=True)
    print("\n")

def higher_or_lower_game():
    options = ["Lower", "Higher", "Bailey", "Cabbage"]
    bailey_present = random.choice([True, False])
    correct_option = "Bailey" if bailey_present else random.choice(options[:-1])
    
    print("Welcome to the Higher or Lower game!")
    print("Here are your options:", options)

    user_guess = input("Guess: ").lower()

    # Simulate processing with a longer and more sporadic loading bar
    print_loading_bar()

    if user_guess == "higher":
        if correct_option == "Higher":
            print("Correct! You win!")
        else:
            print(f"Wrong! The correct answer was {correct_option}.")
    elif user_guess == "lower":
        print(f"Wrong! The correct answer was {correct_option}.")
    elif user_guess == "bailey":
        bailey_present_guess = input("Is Bailey present? (Yes/No): ").lower()
        if bailey_present_guess == "yes":
            print("Correct! You win!")
        else:
            print("Wrong! The correct answer was Cabbage.")
    elif user_guess == "cabbage":
        bailey_present_guess = input("Is Bailey present? (Yes/No): ").lower()
        if bailey_present_guess == "yes":
            print("Wrong! The correct answer was Bailey. ALWAYS BAILEY.")
        else:
            print("Correct! You win!")
    else:
        print("Invalid input. Please choose from the given options.")

# Main game loop
while True:
    higher_or_lower_game()
    
    play_again = input("Do you want to play again? (Yes/No): ")
    if play_again.lower() != "yes" and play_again.lower() != "y":
        print("Thanks for playing. Goodbye!")
        break
