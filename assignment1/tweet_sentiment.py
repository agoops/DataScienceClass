import sys
import json

def hw():
	print 'Hello, world!'

def lines(fp):
	print str(len(fp.readlines()))
	for line in fp:
		tweet_data = json.loads(line)
		tweet = tweet_data['text']
		tokens = tweet.split(' ')
		score = 0
		for word in tokens:
			score += scores[word]
		print "Score: " + str(score)

def main():
	afinnfile = open("AFINN-111.txt")
	scores = {} # initialize an empty dictionary

	for line in afinnfile:
		term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
		scores[term] = int(score)  # Convert the score to an integer.

	# print scores.items() # Print every (term, score) pair in the dictionary


	sent_file = open(sys.argv[1])
	tweet_file = open(sys.argv[2])
	hw()
	# lines(sent_file)
	lines(tweet_file)




if __name__ == '__main__':
    main()
