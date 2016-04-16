#I just like to have a "sandbox" where I can test code independently

import re

test_sentence = "The pope will arrive on June 24th, "

def date_present(sentence):
    months = ["January", "February", "March", "April", "May", "June", "July", "August",
    "September", "October","November", "December", "Jan", "Feb", "Mar", "Apr", "Jun", "Jul",
    "Aug", "Sept", "Oct", "Nov", "Dec"]
    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
