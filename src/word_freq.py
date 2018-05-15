# -*- coding: utf-8 -*-
# This for read file and count the frequency of the word.
# fo = open("readme.txt","r")
# text = fo.readline()
# text = text.split(" ")
# print(re.findall(r"[\w']+", text))

from __future__ import division
import re
import urllib2, obo
import test_graph
def MyMain(myurl):
    url = myurl
    response = urllib2.urlopen(url) # Open Url
    html = response.read() # Read Url
    text = obo.stripTags(html).lower() # Strip any html-tag
    fullwordlist = obo.stripNonAlphaNum(text)
    rbwords = obo.rbkarp_stop(fullwordlist)
    wordlist = obo.removeStopwords(fullwordlist)
    dictionary = obo.wordListToFreqDict(rbwords)
    sorteddict = obo.sortFreqDict(dictionary)
    positivew = obo.rbkarp_posit(dictionary) # List of positive words (Use as a keys to get the frequency)
    negativew = obo.rbkarp_negat(dictionary) # List of negative words (Use as a keys to get the frequency)
    neutralw = obo.rbkarp_neutral(dictionary) # List of neutral words (Use as a keys to get the frequency)
    # Get Dictionary for P/N/Ne
    positivew_dic = obo.get_dic(positivew, dictionary)
    negativew_dic = obo.get_dic(negativew, dictionary)
    neutralw_dic = obo.get_dic(neutralw, dictionary)
    # Create a combination of dictionary
    Classified_dic = {
    'Positive': positivew_dic,
    'Negative': negativew_dic,
    'Neutral': neutralw_dic
    }

    results = obo.AnalaysisArticle(positivew, negativew, neutralw, rbwords, dictionary)
    # Printing Analysis
    print "\n\nURL:", url
    obo.printAnalysis(results)
    # Printing Graph.
    print "Printing Graph~"
    test_graph.bar(Classified_dic)
    test_graph.Scattergraph(dictionary)


# To Test out output when running the code. No Need to be in the report.
#print "+++++++++++++++++++++++++++++ fullwordlist after removing stripNonAlphaNum +++++++++++++++++++++++++++++\n", fullwordlist
#print "+++++++++++++++++++++++++++++ WORDLIST after removing stopwords +++++++++++++++++++++++++++++\n", wordlist
#print "+++++++++++++++++++++++++++++ dictionary after wordlist +++++++++++++++++++++++++++++\n", dictionary
#print "+++++++++++++++++++++++++++++ sorteddict after sorting +++++++++++++++++++++++++++++\n", sorteddict
#print "+++++++++++++++++++++++++++++ gWord after filtering words +++++++++++++++++++++++++++++\n", gWord
#print"\n+++++++++++++++++++++++++++++ List of positive words rb +++++++++++++++++++++++++++++\n ", positivew, "\n+++++++++++++++++++++++++++++ List of negative words +++++++++++++++++++++++++++++\n ", negativew, "\n+++++++++++++++++++++++++++++ List of neutral words +++++++++++++++++++++++++++++\n ", neutralw

# Main Function
if __name__ == "__main__":
    while True:
        cmd = raw_input("\nEnter URL ((q)uit): ")
        if cmd == 'q':
            break
        MyMain(cmd)
        # https://www.childhelp.org/child-abuse/
