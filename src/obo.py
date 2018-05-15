# -*- coding: utf-8 -*-
# obo.py
from __future__ import division
from test_RabinKarp import search
import operator
import re
import string
from tabulate import *

#############################
#   Function to strip html  #
#############################
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
    text = filter(lambda x: x in set(string.printable), text)
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


#########################################
#   Function to get list of stop words  #
#########################################
def getListStopwords():
    fo = open("resources/stopwordlist.txt")
    stopwords = fo.read()
    stopwords = stopwords.split('\n')
    fo.close()
    return stopwords

######################################################
#   Function to get list of positive/negative words  #
######################################################
def getListPositivewords():
    fo = open("resources/positive.txt")
    pword = str.lower(fo.read())
    pword = filter(lambda x: x in set(string.printable), pword)
    pword = pword.split("\n")
    fo.close()
    return pword
def getListNegativewords():
    fo = open("resources/negative.txt")
    pword = str.lower(fo.read())
    pword = filter(lambda x: x in set(string.printable), pword)
    pword = pword.split("\n")
    fo.close()
    return pword

##########################################################
#       Function to classify words using rabin karp      #
##########################################################
# remove stopword
def rbkarp_stop(pattern):
    text = getListStopwords()
    NoStopWord = []
    for i in pattern:
        for n in text:
            found = search(i, n)
            if found == True:
                break
        if found == False:
            NoStopWord.append(i)
    return NoStopWord

def rbkarp_negat(pattern):
    text = getListNegativewords()
    negativew = []
    for i in pattern:
        for n in text:
            found = search(i, n)
            if found == True:
                negativew.append(i)
                break
        #if found == True:
    return negativew

def rbkarp_posit(pattern):
    text = getListPositivewords()
    positivew = []
    for i in pattern:
        for n in text:
            found = search(i, n)
            if found == True:
                positivew.append(i)
                break
        #if found == True:
    return positivew

def rbkarp_neutral(pattern):
    pword = getListPositivewords()
    nword = getListNegativewords()
    set1 = []
    neutralw = []
    for i in pattern:
        for n in pword:
            found = search(i, n)
            if found == True:
                # neutralw.append(i)
                break
        if found == False:
            set1.append(i)
    for i in set1:
        for n in nword:
            found = search(i, n)
            found = search(i, n)
            if found == True:
                # neutralw.append(i)
                break
        if found == False:
            neutralw.append(i)
    return neutralw

##########################
#    Analysis Function   #
##########################
def AnalaysisArticle(positive, negative, neutral, fullword, dic):
    freq = getFreq(positive, negative, neutral, fullword, dic)
    percent = getPercent(freq["Positive"], freq["Negative"], freq["Neutral"], freq["Full"])
    results = {"freq": freq, "percent": percent}
    return results

def AnalysisFreq(percent):
    print "Article is", max(percent, key=lambda i: percent[i])

def getPercent(fpositive, fnegative, fneutral, ffullword):
    ratio = 100/ffullword
    percent = {"Positive": fpositive*ratio,
    "Negative": fnegative*ratio,
    "Neutral": fneutral*ratio}
    return percent

def getFreq(positive, negative, neutral, fullword, dic):
    fpositive = 0
    fnegative = 0
    fneutral = 0
    ffullword = 0
    for i in positive:
        fpositive += dic[i]
    for i in negative:
        fnegative += dic[i]
    for i in neutral:
        fneutral += dic[i]
    for i in dic.keys():
        ffullword += dic[i]
    freq = {"Positive": fpositive, "Negative": fnegative,
    "Neutral": fneutral, "Full": ffullword}
    return freq

def get_dic(keys, ori_dic):
    new_dic = {}
    for i in keys:
        new_dic[i] = ori_dic[i]
    return new_dic

def printAnalysis(results):
    table_header = ["Type","Total Words", "Percentage (%)"]
    table_body = [
    ["Positive", results["freq"]["Positive"], "%.1f" % results["percent"]["Positive"]],
    ["Negative", results["freq"]["Negative"], "%.1f" % results["percent"]["Negative"]],
    ["Neutral", results["freq"]["Neutral"], "%.1f" % results["percent"]["Neutral"]]
    ]

    print tabulate(table_body, table_header), "\n\nTotal Words: ", results["freq"]["Full"]
    AnalysisFreq(results["percent"])



############################################################################
#   Below function is not using Rabin Karp Algorithm & Unused function.    #
#                       No need to be in the report                        #
############################################################################
# Given a list of words, remove any that are
# in a list of stop words.
def removeStopwords(wordlist):
    stopwords = getListStopwords()
    return [w for w in wordlist if w not in stopwords]
# Classify into positive
def classifypositive(wordlist):
    pword = getListPositivewords()
    return [w for w in wordlist if w in pword]
# Classify into negative
def classifynegative(wordlist):
    pword = getListNegativewords()
    return [w for w in wordlist if w in pword]
# Classify into neutral
def classifyneutral(wordlist):
    fo = open("resources/negative.txt")
    pword = str.lower(fo.read())
    pword = filter(lambda x: x in set(string.printable), pword)
    pword = pword.split("\n")
    fo.close()
    positivew, negativew = classifypositive(wordlist), classifynegative(wordlist)
    return [w for w in wordlist if w not in (positivew and negativew)]
# Sort a dictionary of word-frequency pairs in
# order of descending frequency.
def sortFreqDict(freqdict):
    aux = [[freqdict[key], key] for key in freqdict]
    aux.sort()
    aux.reverse()
    return aux
# Get words only from the list
def getWord(wordlist):
    gWord = [item[1] for item in wordlist]
    return gWord
# Get number only from the list
def getNum(wordlist):
    nWord = [item[0] for item in wordlist]
    return nWord
