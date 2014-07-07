import sys
import json

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def main():
    tweet_file = open(sys.argv[1])
    #hw()
    #lines(sent_file)
    #lines(tweet_file)

    #save tweet files
    myData = {}
    #save tweet counts
    Result = {}
    #save frequency
    Frequency = {}

    CountAllTerms = 0;

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

			for word in words:
				if word not in Result:
					Result[word] = 1;			
				elif word in Result:				
					Result[word] = Result[word] + 1;
				CountAllTerms = CountAllTerms + 1;
				
    #Output to standard out of tweet # and its sentiment score
    #print Result.items()
    print "Occurence of all terms " + str(CountAllTerms);
    
    for term in Result:
	Frequency[term] = Result[term] / (CountAllTerms * 1.0)

    print Frequency.items()
if __name__ == '__main__':
    main()
