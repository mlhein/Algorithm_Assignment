# This for read file and count the frequency of the word.
# fo = open("readme.txt","r")
# text = fo.readline()
# text = text.split(" ")
# print(re.findall(r"[\w']+", text))


import re
import urllib2, obo

url = 'http://www.oldbaileyonline.org/browse.jsp?id=t17800628-33&div=t17800628-33'

response = urllib2.urlopen(url) # Open Url
html = response.read() # Read Url
text = obo.stripTags(html).lower() # Strip any html-tag
fullwordlist = obo.stripNonAlphaNum(text)
wordlist = obo.removeStopwords(fullwordlist)
dictionary = obo.wordListToFreqDict(wordlist)
sorteddict = obo.sortFreqDict(dictionary)

for w in dictionary:
    print(str(w))

#for s in sorteddict:
#    print(str(s))
