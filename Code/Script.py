import sys
import simplejson
import pygraphviz as pgv
#import codecs
#from collections import OrderedDict

from_users_arr = []
															
def getTweets ():
   	      
   outfile = open("data_out", "w")
   infile = open("data", "r")			
   with open("data") as myfile:
      head=[myfile.next() for x in xrange(10000)]
   #while True:
   #   s=infile.readline()

 
  


   for line in head:
      tweet = simplejson.loads(line)
      if 'doc' in tweet:
         doc = tweet["doc"]
         from_user=doc["from_user"]
	 from_users_arr.append(from_user)
   print "The users names are"	 
   print from_users_arr
   G = pgv.AGraph("MERGED.dot")
   print "Friends of taxg are : "
   print G.predecessors("taxg")
  # print G.predecessors("acalvani")			 

def main():
	getTweets ()

if __name__ == '__main__':
    main()
