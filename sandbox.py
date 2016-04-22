#This is a test program to independently test functions and whatnot.

import re

def number_check(sentence_array):
    #check for keywords such as thousand, hundred, million, billion, trillion, percent
    #Check for numbers that are formatted.
    numbers = re.compile('[0-9]+|(hundred|thousand|million|billion|trillion)|(percent)')
    check = re.search(numbers, sentence_array)
    if check is not None:
        print "True"
        return True
    else:
        print "False"
        return False

test_sentence = "A percent of people used to live here"
number_check(test_sentence)
