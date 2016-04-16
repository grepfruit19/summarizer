import nltk
import re
import sys

def sentenceScore(sentence, wordlist):
    score = 0
    for word in sentence.split(' '):
        if word in wordlist:
            score += wordlist[word]
    return score


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
    
