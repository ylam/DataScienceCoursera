import sys
import json

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])

    #Store all the words with affinity
    scores = {} #initialize an empty dictionary

    for line in sent_file:
	term, score = line.split("\t") # The file is tab-delimited. "\t" means tab character
	scores[term] = int(score) #Convert the score to an integer

    #for score in scores:
    #	print score + " " + str(scores[score]);

    noSentimentValue = {};
    noSentimentTweetCount = {};

    #Collect all the words from tweets
    for line in tweet_file:
    	#Save every line into myData
	myData = json.loads(line)

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

			for word in words:
				if word not in scores and word not in noSentimentValue:
					noSentimentValue[word] = runningCount;
					noSentimentTweetCount[word] = 1;
				elif word not in scores and word in noSentimentValue:
					noSentimentValue[word] = noSentimentValue[word] + runningCount;	
					noSentimentTweetCount[word] = noSentimentTweetCount[word] + 1;		

    for word in noSentimentValue:
	wordValue = noSentimentValue[word] / (noSentimentTweetCount[word] * 1.0);	
	print word + " " + str(wordValue);	
	#print word + " " + str(noSentimentValue[word]);

if __name__ == '__main__':
    main()
