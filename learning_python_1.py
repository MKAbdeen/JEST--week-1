#__author__ = Mohammad Abdin
import random
import itertools

print(0.1+0.2==0.3)

#############################
#Write a function that takes two strings, and prints them interlaced in one another.
def get_strings():
    first = input("enter your first string:\n")
    second = input("enter your second string:\n")
    result = first + second
    print(''.join(random.sample(result, len(result))))

########################################################
#Write an implementation to two string functions you’ve learned in class:
def use_upper():
    return (input("enter string:\n")).upper()

def use_split():
    return (input("enter string with spaces between words:\n")).split()

###################################################
#Complete the function biggerIsGreater(s) to create and return the new
#string meeting the criteria. If it is not possible, return no answer.

from itertools import permutations
def biggerIsGreater(s):
    a=s
    user_input = sorted(list(a))
    print(a)

    # Get all permutations of [1, 2, 3]
    perm = permutations(user_input)

    # Print the obtained permutations
    # for i in list(perm):
    #     print(i)
    # print("*********")


    for i in list(perm):
        if tuple(a) == i:
            print("YES")

##################################################################
# hangman game
def hangman():
    print("WELCOME TO HANGMAN !\n")

    secret_word = input("please enter a word: \n")
    secret_word_list = list(secret_word)
    lives = len(secret_word_list) * 2
    user_guessing = []

    for i in range(len(secret_word)):
        user_guessing.append('_')

    for i in range(0, lives):
        print(' '.join(user_guessing))
        guessed_char = input("please enter a character: \n")
        for j in range(len(secret_word_list)):
            if guessed_char == secret_word_list[j]:
                user_guessing[j] = guessed_char

            else:
                continue

        print("you have {} lives left\n".format(lives - i - 1))

        for k in range(len(secret_word)):
            if secret_word_list == user_guessing:
                print(secret_word)
                print("YOU WON!.. bye bye")
                exit(0)

    if secret_word_list != user_guessing:
        print("YOU LOST :(")


                ###################
def main():
   get_strings()
   print(use_upper())
   print(use_split())
   biggerIsGreater('word')
   hangman()

if __name__ == '__main__':
    main()
