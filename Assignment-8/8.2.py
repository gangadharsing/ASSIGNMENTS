import random
def extract_file():
    with open('words.txt', 'r') as file:
        list=[]
        for line in file:
            for words in line.split():
                # print(words)
                list.append(words)
    return list

def select_randomly():
    list=extract_file()
    word = random.choice(list)
    return word

def game():
    word=select_randomly()
    print("Guess the characters")

    guesses = ''

    turns = 12

    while turns > 0:

        failed = 0

        for char in word:

            if char in guesses:
                print(char, end=" ")

            else:
                print("_")

                failed += 1

        if failed == 0:

            print("You Win")


            print("The word is: ", word)
            break

        guess = input("guess a character:")

        guesses += guess

        if guess not in word:

            turns -= 1

            print("Wrong")

            print("You have", + turns, 'more guesses')

            if turns == 0:
                print("You Loose")

game()