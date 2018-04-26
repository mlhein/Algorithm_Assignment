# obo.py
import re
def stripTags(pageContents):
    startLoc = pageContents.find("<p>")
    endLoc = pageContents.rfind("<br/>")
    pageContents = pageContents[startLoc:endLoc]
    inside = 0
    text = ''
    for char in pageContents:
        if char == '<':
            inside = 1
        elif (inside == 1 and char == '>'):
            inside = 0
        elif inside == 1:
            continue
        else:
            text += char
    return text

# Given a text string, remove all non-alphanumeric
# characters (using Unicode definition of alphanumeric).
def stripNonAlphaNum(text):
    return re.compile(r'\W+', re.UNICODE).split(text)

# Given a list of words, return a dictionary of
# word-frequency pairs.
def wordListToFreqDict(wordlist):
    wordfreq = [wordlist.count(p) for p in wordlist]
    return dict(zip(wordlist, wordfreq))

# Sort a dictionary of word-frequency pairs in
# order of descending frequency.
def sortFreqDict(freqdict):
    aux = [(freqdict[key], key) for key in freqdict]
    aux.sort()
    aux.reverse()
    return aux

# Given a list of words, remove any that are
# in a list of stop words.
def removeStopwords(wordlist):
    fo = open("resources/stopwordlist.txt")
    stopwords = fo.read()
    stopwords = stopwords.split("\n")
    fo.close()
    # print("List of stop words", stopwords)
    return [w for w in wordlist if w not in stopwords]
