import sys
import json
"""name = "MERGED.dot"
infile = open(name, 'r')
data = infile.read()
print(data)
"""

sents = []
tweetsText = []
sentDict = {}
																
resultDic = {}
hashtagsFound = {} 		

def getTweets ():
       
        outfile = open("data_out", "w")
			
	with open("data") as myfile:
	   head=[myfile.next() for x in xrange(100000)]
        
	for line in all_lines:
	
           try:
              tweet = simplejson.loads(line)
	      print tweet

def main():
	getTweets ()

if __name__ == '__main__':
    main()


