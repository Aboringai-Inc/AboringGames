# Copyright 2024 Aboringai Inc. All Rughts Reserved.

import os, random, time

def nextline(times) -> str: return "\n"*times

print("AboringGames 1.8")
print(nextline(2))

# Game 1: Guess the Number
def guess_the_number():
    print("Welcome to Guess the Number!")
    number = random.randint(1, 100)
    attempts = 0
    while True:
        guess = int(input("Guess a number between 1 and 100: "))
        attempts += 1
        if guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")
        else:
            print(f"Congratulations! You guessed it in {attempts} attempts.")
            break

# Game 2: Rock, Paper, Scissors
def rock_paper_scissors():
    print("Welcome to Rock, Paper, Scissors!")
    choices = ["rock", "paper", "scissors"]
    while True:
        user_choice = input("Choose rock, paper, or scissors (or 'quit' to exit): ").lower()
        if user_choice == "quit":
            break
        if user_choice not in choices:
            print("Invalid choice. Try again.")
            continue
        computer_choice = random.choice(choices)
        print(f"Computer chose {computer_choice}.")
        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissors" and computer_choice == "paper"):
            print("You win!")
        else:
            print("You lose!")

# Game 3: Hangman
def hangman():
    print("Welcome to Hangman!")
    word_list = ["python", "hangman", "programming", "developer", "game"]
    word = random.choice(word_list)
    guessed = "_" * len(word)
    attempts = 6
    guessed_letters = set()

    while attempts > 0 and "_" in guessed:
        print(f"Word: {guessed}")
        print(f"Attempts remaining: {attempts}")
        guess = input("Guess a letter: ").lower()
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue
        guessed_letters.add(guess)
        if guess in word:
            guessed = "".join([guess if guess == word[i] else guessed[i] for i in range(len(word))])
        else:
            attempts -= 1
            print(f"Wrong guess! You lost an attempt.")

    if "_" not in guessed:
        print(f"Congratulations! You guessed the word: {word}")
    else:
        print(f"Game over! The word was: {word}")

# Game 4: Dice Roller
def dice_roller():
    print("Welcome to Dice Roller!")
    while True:
        input("Press Enter to roll the dice (or 'q' to quit): ")
        dice = random.randint(1, 6)
        print(f"You rolled a {dice}!")
        if input("Roll again? (y/n): ").lower() != 'y':
            break

# Game 5: Word Scramble
def word_scramble():
    print("Welcome to Word Scramble!")
    words = ["python", "scramble", "developer", "challenge", "project"]
    word = random.choice(words)
    scrambled = ''.join(random.sample(word, len(word)))
    print(f"Scrambled word: {scrambled}")
    guess = input("Unscramble the word: ")
    if guess == word:
        print("Correct! You win!")
    else:
        print(f"Wrong! The correct word was: {word}")

# Game 6: Simple Quiz
def simple_quiz():
    print("Welcome to Simple Quiz!")
    questions = {
        "What is the capital of France?": "paris",
        "What is 5 + 7?": "12",
        "Who wrote 'To Kill a Mockingbird'?": "harper lee",
    }
    score = 0
    for question, answer in questions.items():
        user_answer = input(question + " ").lower()
        if user_answer == answer:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer was: {answer}")
    print(f"Your total score: {score}/{len(questions)}")

# Game 7: Typing Speed Test
def typing_speed_test():
    print("Welcome to Typing Speed Test!")
    sentence = "The quick brown fox jumps over the lazy dog."
    print(f"Type the following sentence as fast as you can:")
    print(sentence)
    input("Press Enter when ready...")
    start_time = time.time()
    typed = input("Type here: ")
    end_time = time.time()
    if typed == sentence:
        print(f"Correct! You took {end_time - start_time:.2f} seconds.")
    else:
        print("You made a mistake. Try again!")

# Game 8: Memory Game
def memory_game():
    print("Welcome to Memory Game!")
    numbers = [random.randint(1, 9) for _ in range(5)]
    print(f"Memorize this sequence: {numbers}")
    time.sleep(3)
    print("\033c", end="")  # Clear the screen
    guess = input("Enter the sequence: ").split()
    if [int(num) for num in guess] == numbers:
        print("Correct! You have a great memory!")
    else:
        print(f"Wrong! The sequence was: {numbers}")

# Game 9: Coin Toss
def coin_toss():
    print("Welcome to Coin Toss!")
    while True:
        input("Press Enter to toss the coin (or 'q' to quit): ")
        result = random.choice(["Heads", "Tails"])
        print(f"The coin landed on: {result}")
        if input("Toss again? (y/n): ").lower() != 'y':
            break

# Game 10: Math Challenge
def math_challenge():
    print("Welcome to Math Challenge!")
    score = 0
    for _ in range(5):
        num1, num2 = random.randint(1, 10), random.randint(1, 10)
        print(f"What is {num1} x {num2}?")
        answer = int(input("Your answer: "))
        if answer == num1 * num2:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer was: {num1 * num2}")
    print(f"Your final score: {score}/5")

# Menu to play games
def main():
    games = {
        1: guess_the_number,
        2: rock_paper_scissors,
        3: hangman,
        4: dice_roller,
        5: word_scramble,
        6: simple_quiz,
        7: typing_speed_test,
        8: memory_game,
        9: coin_toss,
        10: math_challenge,
    }
    while True:
        print("\nChoose a game to play (or -1 to make own game or -2 to run game):")
        for i in range(1, 11):
            print(f"{i}: {games[i].__name__.replace('_', ' ').title()}")
        print("0: Exit")
        choice = int(input("Enter your choice: "))
        if choice == 0:
            break
        if choice == -2:
            choice4 = input("name for the file: ")
            os.system(f"python user_game_{choice4}.py")
        if choice == -1:
            choice2 = input("what name will the file be? ")
            os.system(f"nano user_game_{choice2}.py")
            choice3 = input("run game? (y/n): ")
            if choice3 == "y":
                os.system(f"python user_game_{choice2}.py")
        if choice in games:
            games[choice]()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
