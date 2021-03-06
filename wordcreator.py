#!/usr/bin/python
#Combines all wordlists into one file (wordlist.txt) without 
#duplicates. 
#
# by ..:: crazyjunkie ::.. 2015

import sys, os, sets

def getwords(wordlist):
	try:
  		file = open(wordlist, "r")
		words = file.readlines()
		file.close()
	except(IOError),msg:
		words = "" 
  		print "Error:",msg
  		pass
	return words

if len(sys.argv) != 2:
	print "Usage: ./wordcreator.py <wordlist dir>"
	sys.exit(1)

wordlists = os.listdir(sys.argv[1])

print "\n wordcreator v0.1 by ..:: crazyjunkie ::.."
print "--------------------------------------------"

print "[+] Wordlists Loaded:",len(wordlists)

final = []

for lst in wordlists:
	words = getwords(os.path.join(sys.argv[1],lst))
	print "[+] List:",lst,"  Length:",len(words),"loaded"
	for word in words:
		final.append(word.replace("\n",""))
	print "[+] Length:",len(final)
final = list(sets.Set(final))
print "\n[!!!] FINAL LENGTH:",len(final)
master = open("wordlist.txt", "a")
for w in final:
	master.writelines(w+"\n")
master.close()
print "\n[-] Done\n"
