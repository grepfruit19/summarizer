import nltk
import re
import sys
from sklearn.decomposition import LatentDirichletAllocation
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
import numpy as np
import nltk.data

def sentenceScore(sentence, wordlist, index):
    score = 0
    for word in sentence.split(' '):
        if word in wordlist:
            score += .2
    #score += .2*(1/(index+1))
    return score

def top_topics(model, feature_names, n_top_words):
    topics = []
    for topic_idx, topic in enumerate(model.components_):
        topics.append([feature_names[i]
                        for i in topic.argsort()[:-n_top_words - 1:-1]])
    i = 1
    for topic in topics:
        print(i)
        print(topic)
        i += 1
    return topics

def latdirall(content):
    lda = LatentDirichletAllocation(n_topics=5) 
    tf_vectorizer = TfidfVectorizer(max_df=0.95, min_df=2,
                                stop_words='english')
    tf = tf_vectorizer.fit_transform(content)
    lolz = lda.fit_transform(tf)
    tfidf_feature_names = tf_vectorizer.get_feature_names()
    return top_topics(lda, tfidf_feature_names, 10)

#Input: Unparsed sentence string
#Processing: Runs a regex to check for presence of "number keywords", or numbers.
#Output: Boolean True if keywords are found, else False.
def number_check(sentence_array):
    #check for keywords such as thousand, hundred, million, billion, trillion, percent
    #Check for numbers that are formatted.
    numbers = re.compile('[0-9]+|(hundred|thousand|million|billion|trillion)|(percent)')
    check = re.search(numbers, sentence_array)
    if check is not None:
        print("True")
        return True
    else:
        print("False")
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
    fil = input_file.read()
    sent_detector = nltk.data.load('tokenizers/punkt/english.pickle')
    importantwords = latdirall(fil.split('\n'))
    paragraphs = fil.split('\n')
    i = 0
    ps = []
    for i in range(0,len(paragraphs)):
        paragraph = sent_detector.tokenize(paragraphs[i].strip())
        currpara = {}
        for j in range(0,len(paragraph)):
            currsent = []
            sentence = paragraph[j]
            for word in sentence.split(' '):
                currsent.append(word)
            currpara[sentence] = sentenceScore(sentence,importantwords,j)
            if(currpara[sentence] > 0):
                print(sentence)
                print(currpara[sentence])
        ps.append(currpara)
        i += 1
    

#Everything below this line is stuff I've done, we can pick out what we want to keep later -Will

#How will we attach scores to each sentence?
#List of lists that are related to the layout of the original?
def lolz():
    paragraphlist = []
    for pindex, paragraph in enumerate(file):
        for sindex, sentence in enumerate(paragraph):
            paragraphlist[pindex][sindex]=rank(sentence)
            if (sindex==0):
                paragraphlist[pindex][sindex]+=5 #weights first sentence more heavily

    for paragraph in file:
        paragraph[0]

def rank(sentence):
    output = 0

    return output

