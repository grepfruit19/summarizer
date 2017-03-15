# Automatic Summarization Program

Meet Barot, William Kim
NLP: Final Project Proposal
Automatic Summarization

# Proposal:
 A program that, given a body of text, it extracts sentences deemed important, and outputs a list of important sentences and phrases as a summary of the text.

# Methodology:
Automated summarization processes generally rely on either extraction-based summarization, or abstraction-based summarization. Extraction based processes work by outright taking phrases deemed important and returning those sentences without modification. Abstraction-based summarization does the same as extraction, but then paraphrases and processes those sentences to produce a (generally) better summarization, but is more difficult to do, and possibly beyond the scope of what we can accomplish. Thus, this project will rely on extraction-based summarization.
	The steps of automated summarization can be summed up in three steps:
Find the most significant sentences
Remove redundant sentences
Keep the summary under a given length.
The key to this process is being able to weight sentences based on importance and pertinence to the overall article. It's difficult to do this in context; “understanding” the article and then returning important and relevant phrases is probably beyond the scope of what we can accomplish, but by identifying patterns in sentences that readers may determine are “important”, we may be able to produce worthwhile summaries. So the question becomes, how can we determine which sentences are important? What patterns are common in important sentences?
The first step would most likely be to manually go through a number of articles and underline sentences that an annotator declares as “important”. Although the annotations haven't actually been done yet, some important metrics can be imagined. A preliminary list may include traits like the following:
Words appear in sentence that are in the title of the article. (Sans generic words such as articles, prepositions, etc)
A large amount of proper nouns.
A presence of dates and times (Often relating to events that occurred), as well as related terms, 	such as “days”, “months”, “yesterday”, etc.
A presence of numbers, especially numbers that appear to be statistics (percentages can be particularly useful)
Appearance of words that have been manually predetermined to be important.
Comparative words (better, while, but, etc)
The first sentence in a given paragraph
A large amount of active verbs
That list is by far from a final list, as it may include features that turn out not to be useful, or features that would take a prohibitively long time to implement. There may also be other features which have been overlooked which we may include in the future. The list as it is, however, brings up some important considerations.

# Possible Obstacles and Pitfalls, Considerations:
For one, the type of text to be processed will be very important to this project. Some strategies that may work well with news articles (such as comparing words that appear in the title to the article) may not work well for other bodies of text, such as a novel. A collection of words that appear often in important sentences may not work for more specialized documents.
	After these criteria are collected, a formula can be created and tuned to produce results that most closely matched the hand annotated texts. The formula could follow a form such as:
Score: Sum of (Weighting factor w * importance criteria n), where 0<w<1
Where importance criteria is one of the above criteria, and weighting factor is its experimentally determined usefulness in determining if a sentence is “important” or not. The issue with this is of course portability; a tuned system that works for news articles may not quite work well with say, movie scripts, however, the possibility that a tuned system could provide particularly good results for news articles is potentially valuable and interesting enough to warrant such a non-portable system.
	After scoring each sentence using a formula that will be created from either the above criteria or a separate criteria, each sentence will be scored and ranked. The user could request a certain n number of sentences to be returned, and then the program will return the n highest rated sentences, in order of appearance in original document.
	As for removing redundant sentences, this could be done by determining similarity scores in the extracted sentences, and removing sentences whose similarities are too similar (likely keeping the first instance only). This may be more difficult than expected, because given an article about a narrow topic, one may expect that the same words occur often within that article, however this is a problem that must be dealt with as it comes.
    
# Conclusion and Summary:
This program will utilize a more semantic analysis of important sentence in a style of text, rather than an algorithmic approach to article summarization. This program will be tuned to a certain type of text, in the hopes that particularly strong summaries can be written for a specific style of writing. As more features are completed, more may be added to produce a better program, but this will be time dependent. Some potential future features may include things such as a “simplification summary”, that uses a thesaurus to replace more obscure words with understandable words.
    
# Resources:
http://www.aclweb.org/anthology/P11-5003.pdf
