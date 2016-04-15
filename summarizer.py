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


