import random

print("🎮 ROCK - PAPER - SCISSORS GAME")
print("--------------------------------")
print("Rules:")
print("• Rock beats Scissors")
print("• Scissors beats Paper")
print("• Paper beats Rock")
print("--------------------------------\n")

choices = ["rock", "paper", "scissors"]

user_score = 0
computer_score = 0

while True:
    # User input
    user_choice = input("Enter rock, paper, or scissors: ").lower()

    if user_choice not in choices:
        print("❌ Invalid choice. Please enter rock, paper, or scissors.\n")
        continue

    # Computer choice
    computer_choice = random.choice(choices)

    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    # Game logic
    if user_choice == computer_choice:
        print("🤝 Result: It's a tie!")
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "scissors" and computer_choice == "paper") or
        (user_choice == "paper" and computer_choice == "rock")
    ):
        print("🎉 Result: You win!")
        user_score += 1
    else:
        print("😞 Result: You lose!")
        computer_score += 1

    # Display score
    print(f"\nScore → You: {user_score} | Computer: {computer_score}")

    # Play again
    play_again = input("\nDo you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("\nThanks for playing! 👋")
        break
