import nltk
import re
import sys

def sentenceScore(sentence, wordlist):
    score = 0
    for word in sentence.split(' '):
        if word in wordlist:
            score += wordlist[word]
    return score

#Input: Unparsed sentence string
#Processing: Runs a regex to check for presence of "number keywords", or numbers.
#Output: Boolean True if keywords are found, else False.
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

#Input: Unparsed sentence string
#Processing: Runs a regex to check for presence of months or days of the week, as well
#as words like "Today", "Yesterday", "Tomorrow". Assumes proper capitalization,
#given that these are edited articles.
#Output: Boolean True if keywords are found, else False.
def check_dates(sentence):
    #months
    #weekdays
    #yesterday, today, tomorrow
    month2 = re.compile('[Tt]oday|[Yy]esterday|[Tt]omorrow|Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday|Jan(uary)?|Feb(ruary)?|Mar(ch)?|Apr(il)?|May|June|July|Aug(ust)?|Sept(ember)?|Oct(ober)?|Nov(ember)?|Dec(ember)?')
    check = re.search(month2, sentence_array)
    if check is not None:
        return True
    else:
        return False

with open(sys.argv[1], 'r') as input_file:
    content = input_file.read()
    paragraphs = content.split('\n')
    i = 0
    importantwords = {'shall': 1, 'pay': 1, 'war': 1, 'crimes': 1, 'genocide': 1, 'immigration': 1, 'emigrants': 1, 'immigrants': 1}
    ps = []
    for paragraph in paragraphs:
        currpara = {}
        for sentence in paragraph.split('.'):
            currsent = []
            for word in sentence.split(' '):
                currsent.append(word)
            currpara[sentence] = sentenceScore(sentence,importantwords)
            if(currpara[sentence] > 0):
                print(sentence)
        ps.append(currpara)
        i += 1


#Everything below this line is stuff I've done, we can pick out what we want to keep later -Will

#How will we attach scores to each sentence?
#List of lists that are related to the layout of the original?

paragraphlist = []

for pindex, paragraph in enumerate(file):
    for sindex, sentence in enumerate(paragraph):
        paragraphlist[pindex][sindex]=rank(sentence)
        if (sindex==0):
            paragraphlist[pindex][sindex]+=5 #weights first sentence more heavily

for qindex, qvector in enumerate(query_vectors):

for paragraph in file:
    paragraph[0]

def rank(sentence):
    output = 0

    return output

def date_present(sentence):
