import sys
import simplejson
import pygraphviz as pgv

from_users_arr = []
sub_users_arr = []
dict = {}
															
def getTweets ():
   	      
   outfile = open("data_out", "w")
   #infile = open("data", "r")			
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
   for user in from_users_arr:
      if user not in dict:
         dict[user]=0
      

   G = pgv.AGraph("MERGED.dot")
   for user in from_users_arr:
      sub_users_arr = G.predecessors(user)
      for user_1 in sub_users_arr:
         if user_1 in dict:
            dict[user_1] += 1
         else:
            dict[user_1] = 1   
   print "The values of the dictionary are : "
   for user in dict:
      String = ""
      string = user," : ", dict[user]
      print>>outfile, string
      print string
 			 

def main():
	getTweets ()

if __name__ == '__main__':
    main()
