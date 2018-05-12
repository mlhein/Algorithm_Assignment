
# Python program for Naive Pattern Searching
def search(pat, txt):
	M = len(pat)
	N = len(txt)

	# A loop to slide pat[] one by one
	for i in xrange(N-M + 1):

		# For current index i, check for pattern match
		for j in xrange(M):
			if txt[i + j] != pat[j]:
				break

		if j == M-1: # if pat[0...M-1] = txt[i, i + 1, ...i + M-1]
			print "Pattern found at index " + str(i)

# Driver program to test the above function
txt = "AABAACAADAABAAABAA"
pat = "AABA"
search (pat, txt)

# This code is contributed by Bhavya Jain
