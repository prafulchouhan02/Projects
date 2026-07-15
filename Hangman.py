import random

words = (
    "apple", "orange", "banana", "grapes", "mango",
    "peach", "pear", "lemon", "melon", "cherry",
    "coconut", "pineapple", "papaya", "guava", "kiwi",
    "tomato", "potato", "carrot", "onion", "garlic"
)

#dictionary of key:()
hungman_art = {0: ("   ",
                   "   ",
                   "   "),
               1: (" o ",
                   "   ",
                   "   "),
               2: (" o ",
                   " | ",
                   "   "),
               3: (" o ",
                   "/| ",
                   "  "),
               4: (" o ",
                   "/|\\",
                   "  "),
               5: (" o ",
                   "/|\\",
                   "/ "),
               6: (" o ",
                   "/|\\",
                   "/ \\")}

def display_man(wrong_guesses):
    print("****************")
    for line in hungman_art[wrong_guesses]:
        print(line)
    print("****************")

def display_hint(hint):
    print(" ".join(hint))

def display_answer(answer):
    print(" ".join(answer))

def main():
    answer = random.choice(words)
    hint = ["_"] * len(answer)
    wrong_guesses = 0
    guessed_letters = set()
    

    while True:
        display_man(wrong_guesses)
        display_hint(hint)
        print("Guessed letters:", " ".join(sorted(guessed_letters)))

        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input! Enter a single letter.\n")
            continue

        if guess in guessed_letters:
            print(f"{guess} is already guessed")
            continue

        guessed_letters.add(guess)

        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess
                    print("Correct! ")
                    
        else:
            wrong_guesses += 1
            print("Wrong Guess! ")

        if "_" not in hint:
            display_man(wrong_guesses)
            display_answer(answer)
            print("YOU WIN!")
            break

        elif wrong_guesses == len(hungman_art) - 1:
            display_man(wrong_guesses)
            display_answer(answer)
            print("Game Over! YOU LOSE!")
            break
        

if __name__ == "__main__":
    main()