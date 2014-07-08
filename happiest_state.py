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

    #i = 1;    
    
    states = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
	}
    

    for line in tweet_file:
    	#Save every line into myData
	myData = json.loads(line)
	#print "Line " + str(i)
	#print myData
	#print myData.keys()
	if "text" in myData and "lang" in myData and "place" in myData:
		#print myData.keys()
		#if myData["place"] is :		
		location = myData["place"]
		
		if location is None:
			location;
		elif location["country_code"] == "US":
			#print location["full_name"];
			#We now know it is a tweet from US. Need to determine which state is the tweet from.

			var1, var2 = location["full_name"].split(', ')
			#print var1 + " " + var2;
			
			stateAbbr = '';

			if var2 == 'USA':
				#print "State Code: " + var1;
				for abbr, state in states.items():
					if (state == var1):
						stateAbbr = abbr;
			else:
				#print "State Code: " + var2;
				if var2 in states:
					stateAbbr = var2;

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
			#Result[i] = runningCount;
			#print runningCount;

			if stateAbbr in Result:
				Result[stateAbbr] = Result[stateAbbr] + runningCount;
			else:
				Result[stateAbbr] = runningCount;
		#elif myData["lang"] != 'en':
			#Result[i] = 0;
			#print 0;
	
	#i = i + 1;   
    #Output to standard out of tweet # and its sentiment score
    highestSentiment = 0;
    highestState = '';

    for term in Result:
	if (Result[term] > highestSentiment):
		highestSentiment = Result[term];	
		highestState = term;
    
    print highestState;

if __name__ == '__main__':
    main()
