import random
word_bank = []
fh = open("words5.txt")
for word in fh:
    word_bank.append(word.strip())


def listEditor(lis, char, pos, boolean):
    new_list =[]
    if boolean:
        for words in lis:
            if words[pos] == char:
                new_list.append(words)
        return new_list
    else:
        for words in lis:
            if char in words:
                new_list.append(words)
        return new_list


def ListRemover(lis, char, pos, boolean):
    new_list = []
    if boolean:
        lis = listEditor(lis, char, pos, False)
        for words in lis:
            if not words[pos] == char:
                new_list.append(words)
        return new_list
    else:
        for words in lis:
            if char not in words:
                new_list.append(words)
        return new_list


i = 1
guess = random.choice(word_bank)
print("This is a wordle game solver.\nThe encoding format is '-' for yellow letters, '*' for black/ash letters and just type the actual letter if it is green coloured.")
while i < 6:
    print("\nEnter {} as guess".format(guess))
    out = input("Please enter the resulting output: ")
    if len(out) != 5:
        out = input("Please enter the resulting output correctly: ")
    out = out.strip().lower()
    if out == guess:
        print("Yay! We did it.")
        break
    for i, cha in enumerate(out):
        if cha == guess[i]:
            word_bank = listEditor(word_bank, cha, i, True)
        elif cha == "-":
            word_bank = ListRemover(word_bank, guess[i], i, True)
        elif cha == "*" and guess[i] in out:
            word_bank = ListRemover(word_bank, guess[i], i, True)
        elif cha == "*":
            word_bank = ListRemover(word_bank, guess[i], i, False)
        else:
            print("Enter using the valid encoding format only.")
            i = i -1
    i = i + 1
    if len(word_bank) == 0:
        print("Sorry, the answer is not in our bank of words.")
        break
    guess = random.choice(word_bank)
    if i == 6:
        print("Sorry I failed you :-(")