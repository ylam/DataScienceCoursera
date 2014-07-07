import sys
import json
import operator;

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def main():
    #sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[1])
    #hw()
    #lines(sent_file)
    #lines(tweet_file)

    #save tweet files
    myData = {}
    #save tweet and sentiment results
    Result = {}

    #i = 1;    
 
    for line in tweet_file:
    	#Save every line into myData
	myData = json.loads(line)
	#print "Line " + str(i)
	#print myData
	#print myData.keys()
	if "entities" in myData and "lang" in myData:
		if myData["lang"] == 'en':
			
			entity = myData["entities"];
			hashtag = entity["hashtags"];
			if hashtag:
				#print hashtag[0]["text"];
				#if hashtag exists
				if hashtag[0]["text"] in Result:				
					Result[hashtag[0]["text"]] = Result[hashtag[0]["text"]] + 1;
				#if hashtag does not exits
				else:
					Result[hashtag[0]["text"]] = 1;
			#Split each word found in the text and sum the value of sentiment.
			#tweet = myData["text"]
			#tweet = tweet.lower()
			#words = tweet.split()

			#runningCount = 0;				
			#for word in words:
			#	if word in scores:				
			#		runningCount = runningCount + scores[word];
			#	elif word not in scores:
			#		runningCount = runningCount + 0;
			#print "Text Running Count " + str(runningCount);
			#Result[i] = runningCount;
			#print runningCount;
		#elif myData["lang"] != 'en':
			#Result[i] = 0;
			#print 0;
	
	#i = i + 1;   
    #Output to standard out of tweet # and its sentiment score
    #print Result.items()

    #Output = sorted(Result);
    #sortedResult = sorted(Result.values(), reverse=True);
    
    #for term in Result:
    #	print term + " " + str(Result[term])
    z = 0;
    for w in sorted(Result, key=Result.get, reverse=True):
	if (z < 10):	
		print w, Result[w];
		z = z + 1;
    #top10 = {};
    #y = 0;
    #for y in range(0,10):
#	top10[y] = sortedResult[y];
      
 #   print top10;

    #print sortedResult;
  #  for x in Result:
	#if (Result[x]     	
	#for z in range (0,10):
	#	if (Result[x] == top10[z]):
	#		print x + " " + str(Result[x]);

if __name__ == '__main__':
    main()
