import praw
import collections
#our reddit instance. You can thank me for the free account information
reddit = praw.Reddit(client_id = 'os7m34NXJFkr0g',
					 client_secret = '0oJVizuj3K3XGFEIUPCw_t9D23M',
					 username = 'justTestingStuffyeah',
					 password = 'justTestingStuffyeah',
					 user_agent = 'testBotv1')

#we are looking at r/all
reddit = reddit.subreddit('all')
#comments over 2000 chars are often spam
MAX_LENGTH = 2000
#words that occur less than 10 times are not worth the space and usually typos
MIN_OCCURANCE = 10

"""
The main objective of this script is to produce a txt document "RedditFrequency.txt"
which contains a dictionary of "words" and their frequencies in r/all.
The words do NOT have to be valid english words.
"""
def main():
	count = parseSubmissions()
	frequency = convertToFrequency(count)
	print(frequency, file = open("RedditFrequency.txt", "a"))

#iterates over the top 1000 comments of r/all
def parseSubmissions():
	occurances = collections.Counter()
	count = 0
	for submission in reddit.top(limit = 1000):
		if not submission.stickied:
			processSubmission(submission,occurances)
			count += 1
			print("new post " + str(count) + " " + submission.title)
	
	return occurances

#processes each submission and checks words for a few errors
#submission is a valid submission. Occurances is a dictionary to compare
def processSubmission(submission, occurances):
	submission.comments.replace_more(limit=0)
	for comment in submission.comments.list():
		if len(comment.body) < MAX_LENGTH and not comment.stickied:
			words = comment.body.lower().split()
			checkWords(words)
			occurances.update(words)

#converts words that occur over 10 times into frequencies
#count is a dictionary of occurances
def convertToFrequency(count):
	totalCount = sum(count.values())
	print(totalCount)
	frequency = collections.Counter()
	for word in count:
		if count[word] > MIN_OCCURANCE:
			frequency[word] = count[word] / totalCount
	return frequency

#recursively gets rid of !?, end characters
def checkWords(words):
	for word in words:
				if word[len(word)-1] == "!" or word[len(word)-1] == "?" or word[len(word)-1] == "," or word[len(word)-1] == ".":
					word = word[:len(word)-1]

if __name__ == '__main__':
	main()