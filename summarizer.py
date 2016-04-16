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
