import sys
import json

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    #hw()
    #lines(sent_file)
    #lines(tweet_file)

    scores = {} #initialize an empty dictionary

    for line in sent_file:
	term, score = line.split("\t") # The file is tab-delimited. "\t" means tab character
	scores[term] = int(score) #Convert the score to an integer

    #print scores.items() #Print every (term, score) pair in the dictionary
    
    #save tweet files
    myData = {}
    #save tweet and sentiment results
    Result = {}

    i = 1;    
 
    for line in tweet_file:
    	#Save every line into myData
	myData = json.loads(line)
	#print "Line " + str(i)
	#print myData
	#print myData.keys()
	if "text" in myData and "lang" in myData:
		if myData["lang"] == 'en':
			#Split each word found in the text and sum the value of sentiment.
			tweet = myData["text"]
			tweet = tweet.lower()
			words = tweet.split()

			runningCount = 0;				
			for word in words:
				if word in scores:				
					runningCount = runningCount + scores[word];
				elif word not in scores:
					runningCount = runningCount + 0;
			#print "Text Running Count " + str(runningCount);
			Result[i] = runningCount;
		elif myData["lang"] != 'en':
			Result[i] = 0;
	else: 
		#print "No Text Running Count: " + str(runningCount)
		Result[i] = 0;
	
	i = i + 1;   
    #Output to standard out of tweet # and its sentiment score
    print Result.items()

if __name__ == '__main__':
    main()
