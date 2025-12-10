import random

ran_num = random.randint(1, 50)

print(
    "welcome to the guessing game! I have selected a number between 1 and 50. Can you guess it?"
)
user_num = int(input("Enter your guess: "))
while user_num != ran_num:
    if user_num < ran_num:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")
    user_num = int(input("Enter your guess: "))
print("Congratulations! You've guessed the correct number:", ran_num)
print("THANK YOU FOR PLAYING THE GUESSING GAME")
