import sys
import simplejson

emotions = (":)",":-)","=)",";)",":D","(:",":(",":-(",";(","=(",":/",":-/","):")

def getEmoticonsTweets(argfile):
    fil = open(argfile,"r")
    outfile = open("nyc.trim.emoticons", "w")
    all_lines = fil.readlines()
    for line in all_lines:
	
        try:
            tweet = simplejson.loads(line)
            if 'doc' in tweet:
                doc = tweet["doc"]
                text_=doc["text"]
                for el in emotions:
		    print "in for loop"
                    index = text_.find(el)
                    if (index > 0):
                        if(el == ":/"):
                            if(text_[index-1] == 'p'):
				print "In If loop"
                                continue
                        simplejson.dump(tweet,outfile)
                        outfile.write("\n")
        except ValueError:
            pass
            print "Error Occured"
    fil.close()
    outfile.close()    

def main():
    getEmoticonsTweets(sys.argv[1])

if __name__ == '__main__':
    main()   
