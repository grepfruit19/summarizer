#summarizer
Automatic Summarization Program


1. Take only first sentence of every paragraph: Articles naturally include important information in the first sentence.
Additionally, the first sentence of the entire article should probably be an auto-include.

2. Take sentences that have a score above a certain threshold. The score will be determined by if the sentence uses the words:
    - shall not
    - shall
    - pay
    - war
    - [institutions]
    - crimes
    - genocide
    - immigration
    - emigrants
    - immigrants

3. List of "important words"
This should actually be put into categories. There can be several different types of categories:
arguments = ["agree", "disagree", "argue", "said", "lack"]
changes = ["began"]
importantwords = ["priority", "important"]

4. List of "ignorable words": uses a basis of stop words given by www.lextek.com/manuals/onix/stopwords1.html
Right now it's a plain text list, I'll figure out how to deal with that later.

5. Inclusion of numbers: Figures are often indications of important facts that articles are getting across.
Regex to find numbers, include words like million, billion, thousand, percent.

6. Dates are often important sentences, indicating when something is occurring.
Regex to find dates. Months, days of week, "yesterday", "tomorrow", etc.

7. Sentences that contain words in the title of the article (minus stop words)
