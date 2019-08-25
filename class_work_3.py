#__author__ = Mohammad Abdin

############# 1 ####################
### a #####
#Find all the numbers between 1 and 1000 that are divisible by 7.
import random
from queue import Queue


def find_nums():
    return [x for x in range(1000) if x%7 ==0]

### b ####
#Find all of the numbers from 1-1000 that have a 3 in them
def contain_three():
    return [ x for x in range(1000) if '3' in str(x)]

### c ####
#Remove all of the vowels in a string
def remove_vowels(mystring):
    return [x for x in mystring if x not in ['a', 'e', 'i', 'o', 'u']]

### d ####
#Find all of the words in a string that are less than 4 letters
def find_words(mystring):
    return [x for x in mystring if len(mystring) < 4]

### e ####
#Find all the numbers between 1 and 1000 that are divisible by any digit besides 1 (2-9)
def find_numbers():
    return [num for num in range(1000) if [i for i in range(2,10) if num % i == 0]]

############# a2 ###############################
#Write a function that takes a string and returns
# a dictionary that contains all the words in the string as keys, and their length as values
def dict_of_word(mystring):
  return  {word: len(word) for word in mystring.split()}

########## 2 #############################
#Write a function that takes two numbers and
#randomly performs one of these functions between them
def operator(num1,num2):
    switch_dict = {
        1 : "num1 + num2",
        2 : "num1 * num2",
        3 : "num1 % num2",
        4 : "num1 / num2"
    }
    operation = random.choice(list(switch_dict.values()))
    return eval(operation)

######### 3 ###############
def cal_fibonacci(n):
    if n < 0:
        print("invalid input")
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        # recursive call
        return cal_fibonacci(n - 1) + cal_fibonacci(n - 2)

######### 4 #################
#Given a value N, if we want
# to make change for N cents, and we have an
# infinite supply of each of S = { S1, S2, .. , Sm} valued coins,
def money_change(S, m, n):
    if n < 0:
        return 0;
    if n == 0:
        return 1

    if m <= 0 and n >= 1:
        return 0
    #recirsive call
    return money_change(S, m - 1, n) + money_change(S, m, n - S[m - 1])

################# 5 ###############################
def legal_path():

    # doesn't work

    matrix = [[0,0,0,1],
              [1,7,7,2],
              [5,0,5,0]
              ]
    numrows, numcols = len(matrix), len(matrix[0])
    q = Queue()
    for row in range(len(matrix)):
       for col in range(len(matrix[0])):

        if col + 1 < numcols and matrix[row][col + 1] == "0":
            q.put((row, col + 1))

        if row + 1 < numrows and matrix[row + 1][col] == "0":
            q.put((row + 1, col))

        if 0 <= col - 1 and matrix[row][col - 1] == "0":
            q.put((row, col - 1))

        if 0 <= row - 1 and matrix[row - 1][col] == "0":
            q.put((row - 1, col))

    row, col = numrows - 1, numcols - 1

    if row ==0 and col == 0:
        print("There is no path")
        exit()
    else:
        print("There is a path")

def main():

    print(money_change([1,2,3,4],4,6))

if __name__ == '__main__':
    main()