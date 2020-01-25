#__author__ = Mohammad Abdin
#Write a function that takes a string and returns a dictionary that counts how many times
#each character appears in the string.
from collections import Counter
import itertools
from urllib.parse import urlparse
import pprint

def count_char_in_string():

    user_input = input("please enter your string: \n")
    user_input = list(user_input)
    counter = Counter(user_input)
    print(counter)

##################################################################
#Write a function that takes a list that can have nested lists in it and returns a flat list. A
#flat list is a list without any nested lists in it.

def nested_list(s):
    my_list = list(itertools.chain(*s))
    print(my_list)

##################################################
#Write a simple URL parser. The parser takes a full string of url and returns a dictionary
#that contains 3 values: “scheme”, which is the URL scheme specifier, “netloc” which is
#the net location of the website, and “path” which is the Hierarchical path.

def url_parser(entered_url):
    my_parser = urlparse(entered_url)
    print(my_parser.scheme)
    print(my_parser.netloc)
    print(my_parser.path)
#######################################################
def day_schedule():
	
	# deosn"t work 

    #input_filename =  input("please enter the input file name:")
    #output_filename = input("please enter the output file name:")

    dic ={}
    input_filename = 'C.W2_input.txt'
    output_filename ='C.W2_output.txt'

    #with open(output_filename, 'w') as f2:
    with open(input_filename) as f:
        for line in f:
            key, value = line.strip().split(' ', 1)
            dic[key] = value

            print(dic)
            # key, val = line.split(" ",1)
            # dic[key] = val
            # print(dic)

           #dict(zip(line.split(" ")))


#######################################################
def main():
    count_char_in_string()
    nested_list([[1,2,3],[4,5,6], [7], [8,9]])
    url_parser('http://google.com/ProjectRails/KISS/')
    #day_schedule()


if __name__ == '__main__':
    main()
