import random

word_bank = []
fh = open("words5.txt")
for word in fh:
    word_bank.append(word.strip())

print("Welcome to Wordle!")
i = 0
out = ""
word = random.choice(word_bank)
guesses = []
invalid = []
while i < 6:
    guess = input("\nEnter your guess: ")
    if len(guess) != 5:
        guess = input("Please enter a five letter word as guess: ")
    if guess not in word_bank:
        guess = input("Please enter a valid 5-letter word as guess: ")
    guess = guess.lower().strip()
    p = 0
    out = ""
    # To create the output that guides the user on the precision of their guess
    for char in guess:
        if char == word[p]:
            out += char
            if char not in guesses:
                guesses.append(char)
        elif char in word:
            out += "-"
        else:
            out += "*"
        p += 1
    # For correct answer,
    if out == word:
        print(out)
        print("Congratulations! You have guessed correctly.")
        break
    # For answers that have a letter correct but in wrong position
    elif "-" in out:
        i += 1
        k = 0
        l = 0
        letters = []
        if i == 6:
            print("End of game. You lose.\nThe correct answer was {}".format(word))
            break
        for k, char in enumerate(out):
            if char == "-" and guess[k] not in letters:
                letters.append(guess[k])
            if char == "*" and guess[k] not in invalid:
                invalid.append(guess[k])
        for letter in letters:
            if letter not in guesses:
                guesses.append(letter)
        print(out)
        print(
            "You guessed letter(s) {a} correctly but in wrong position(s)\nLetters guessed so far that are not valid include:".format(
                a=letters) + str(
                invalid) + ".\nLetters you have guessed correctly so far: {c}\nYou have {b} guesses left".format(
                b=6 - i, c=guesses))
    else:
        i += 1
        if i == 6:
            print("End of game. You lose.\nThe correct answer was {}".format(word))
            break
        l = 0
        for l, char in enumerate(out):
            if char == "*" and guess[l] not in invalid:
                invalid.append(guess[l])
        print(out)
        print("Wrong guess.\nLetters guessed so far that are not valid include:" + str(
            invalid) + ".\nLetters you have guessed correctly so far:{a}\nYou have {b} guesses left \nTry Again.".format(
            a=guesses, b=6 - i))