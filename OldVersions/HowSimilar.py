import praw
import collections
reddit = praw.Reddit(client_id = 'os7m34NXJFkr0g',
					 client_secret = '0oJVizuj3K3XGFEIUPCw_t9D23M',
					 username = 'justTestingStuffyeah',
					 password = 'justTestingStuffyeah',
					 user_agent = 'testBotv1')


LENGTH_THRESHOLD = 1000

def main():
	compute(reddit.subreddit('politics'))
	compute(reddit.subreddit('conservative'))
	compute(reddit.subreddit('the_donald'))
	compute(reddit.subreddit('latestagecapitalism'))
	compute(reddit.subreddit('cringeanarchy'))
	compute(reddit.subreddit('sandersforpresident'))
	compute(reddit.subreddit('thealtright'))
	compute(reddit.subreddit('the_mueller'))
	compute(reddit.subreddit('neutralpolitics'))
	compute(reddit.subreddit('news'))
	compute(reddit.subreddit('worldnews'))
	compute(reddit.subreddit('askreddit'))
	compute(reddit.subreddit('me_irl'))

	
def compute(subreddit):
	demData = importData("DemocratWords6.txt")
	repubData = importData("RepublicanWords6.txt")
	democratSim = parseSubmissions(subreddit, demData)
	republicanSim = parseSubmissions(subreddit, repubData)
	#need to normalize
	demIndex = democratSim #/ sum(demData.values()) # REMEMBER TO NOT DIVIDE IF YOU MULTIPLY FREQ IN POL
	repubIndex = republicanSim #/ sum(repubData.values())
	print(subreddit)
	print(demIndex)
	print(repubIndex)

def importData(fileToImport):
	file = open(fileToImport, "r")
	lines = file.readlines()
	file.close
	return collections.Counter(eval(lines[0][7:]))

def parseSubmissions(subreddit, freqToCompare):
	count = 0
	totalVal = 0
	total = 0
	for submission in subreddit.top(limit = 50):
		if not submission.stickied:
			result = process_submission(submission, freqToCompare)
			count+=1
			totalVal +=result[0] # total number of words
			total += result[1] # either value of key or 0
	return totalVal/total
	
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

def find_differential(a,b):
	a.subtract(b)
	return a

if __name__ == '__main__':
	main()
