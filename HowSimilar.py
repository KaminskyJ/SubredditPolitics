import praw
import collections
reddit = praw.Reddit(client_id = 'os7m34NXJFkr0g',
					 client_secret = '0oJVizuj3K3XGFEIUPCw_t9D23M',
					 username = 'justTestingStuffyeah',
					 password = 'justTestingStuffyeah',
					 user_agent = 'testBotv1')

#subreddits you would like to test
subreddits = ['politics','the_donald','neutralpolitics']
#comments over 2,000 characters are often spam that ruin the data
LENGTH_THRESHOLD = 2000

"""
the main objective of this script is to take in frequencies and compare them to the
politicized data.

The result should be two numbers that is the average politiczed index of a word in the subreddit.
First one is democrat, second, republican.
So if it prints:
[subreddit]
.3245
.724
Then the subreddit, on average, uses words that are used .3245 times more often by r/politics than r/all.
and .724 for r/the_donald.

Valid outputs are anywhere from 0 to the largest political index (this would mean the subreddit only uses
the most political word and no others)
"""
def main():
	for subs in subreddits:
		compute(reddit.subreddit(subs))

#computes the values stated above for a given subreddit
def compute(subreddit):
	demData = importData("DemsData.txt")
	repubData = importData("RepubsData.txt")
	democratSim = parseSubmissions(subreddit, demData)
	republicanSim = parseSubmissions(subreddit, repubData)
	"""
	IMPORTANT. If you are going to use this code for large ammounts
	of data, you should rewrite this code so it checks dem and repub data
	together, instead of two different method calls. This would reduce the
	ammount of time to calculate by half
	"""
	print(subreddit)
	print(democratSim)
	print(republicanSim)

#similar to prev
def importData(fileToImport):
	file = open(fileToImport, "r")
	lines = file.readlines()
	file.close
	return collections.Counter(eval(lines[0][7:]))

"""
similar to prev with a modification to the return value
shoudld return a num which represent that described above
main
"""
def parseSubmissions(subreddit, freqToCompare):
	count = 0
	totalVal = 0
	total = 0
	for submission in subreddit.top(limit = 200):
		if not submission.stickied:
			result = process_submission(submission, freqToCompare)
			count+=1
			totalVal +=result[0] # total number of words
			total += result[1] # either value of key or 0
	return totalVal/total

"""
returns a tuple which contains the sum of political index and the
total number of words

rest is similar to prev
"""
def process_submission(submission, freqToCompare):
	sum = 0
	total = 0
	submission.comments.replace_more(limit=0)
	for top_level_comment in submission.comments:
		if len(top_level_comment.body) <LENGTH_THRESHOLD:
			for words in top_level_comment.body.lower().split():
				if words in freqToCompare:
					sum += freqToCompare[words]
				total += 1
	return (sum, total)

if __name__ == '__main__':
	main()
