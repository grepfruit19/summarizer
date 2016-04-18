#This is a test program to independently test functions and whatnot.

import re

test_sentence = "The pope will arrive on June 24th, and he will bring with him a herd of cattle."

def date_present(sentence_array):
    months = ["January", "February", "March", "April", "May", "June", "July", "August",
    "September", "October","November", "December", "Jan", "Feb", "Mar", "Apr", "Jun", "Jul",
    "Aug", "Sept", "Oct", "Nov", "Dec"]
    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    month = re.compile(?:Jan(?:uary)?|Feb(?:ruary)|Mar(?:ch)?|Apr(?:il)?|May|June|July|Aug(?:ust)?|Sept(?:ember)|Oct(?:ober)|Nov(?:ember))
    #This isn't working, siqq
    if test_sentence.search():
        print "True"
    return True
