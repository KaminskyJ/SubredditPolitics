import praw
import collections
reddit = praw.Reddit(client_id = 'os7m34NXJFkr0g',
					 client_secret = '0oJVizuj3K3XGFEIUPCw_t9D23M',
					 username = 'justTestingStuffyeah',
					 password = 'justTestingStuffyeah',
					 user_agent = 'testBotv1')

subreddit1 = reddit.subreddit('politics')
subreddit2 = reddit.subreddit('conservative')

THRESHOLD_VALUE = 5



def main():
	a = parseSubmissions(subreddit1)
	b = parseSubmissions(subreddit2)

	convertToFrequency(a)
	convertToFrequency(b)
	difference = find_differential(a,b)
	cleanUp = collections.Counter()
	for key in difference:
		if difference[key] != 0:
			cleanUp[key] = difference[key]
		
	
	print(cleanUp, file=open("DifferentialOutput2.txt", "a"))

def parseSubmissions(subreddit):
	frequencies = collections.Counter()
	count = 1
	for submission in subreddit.top(limit = 1000):
		if not submission.stickied:
			process_submission(submission,frequencies)
			count += 1
			print("new post " + str(count))
	return frequencies
	
def process_submission(submission, frequencies):
	
	print(submission.title)
	
	submission.comments.replace_more(limit=0)
	for top_level_comment in submission.comments:
		print(top_level_comment.body)
		frequencies.update(top_level_comment.body.lower().split())

def convertToFrequency(counter):
	total = sum(counter.values())
	for key in counter:
		if ( counter[key] >THRESHOLD_VALUE):
			counter[key] = counter[key]/total
		else: counter[key] = 0
		
def find_differential(a,b):
	a.subtract(b)
	return a

if __name__ == '__main__':
	main()
