import praw
import collections
import string
reddit = praw.Reddit(client_id = 'os7m34NXJFkr0g',
					 client_secret = '0oJVizuj3K3XGFEIUPCw_t9D23M',
					 username = 'justTestingStuffyeah',
					 password = 'justTestingStuffyeah',
					 user_agent = 'testBotv1')

subreddit1 = reddit.subreddit('politics')
subreddit2 = reddit.subreddit('the_donald')

THRESHOLD_VALUE = 5
MAX_LENGTH = 1000


def main():
	a = parseSubmissions(subreddit1)
	b = parseSubmissions(subreddit2)
	dems2 = politicize2(convertToFrequency(a))
	repubs2 = politicize2(convertToFrequency(b))
	print(dems2, file = open("DemocratWords7.txt", "a"))
	print(repubs2, file = open("RepublicanWords7.txt", "a"))

def politicize(frequencies):
	mostPolitical = collections.Counter()
	genFreq = importData("genWordFreq.txt")
	for word in frequencies:
		if word in genFreq:
			if frequencies[word] - genFreq[word] > 0:
				mostPolitical[word] = (frequencies[word] - genFreq[word])/genFreq[word]
		elif frequencies[word] - 1.3116344469e-7 > 0:
			mostPolitical[word] = (frequencies[word] - 1.3116344469e-7)/1.3116344469e-7
	
	return mostPolitical

def politicize2(frequencies):
	mostPolitical = collections.Counter()
	genFreq = importData("genWordFreq.txt")
	for word in frequencies:
		if word in genFreq:
			if frequencies[word] - genFreq[word] > 0:
				mostPolitical[word] = (frequencies[word] - genFreq[word])/(genFreq[word]*frequencies[word])
		elif frequencies[word] - 1.3116344469e-7 > 0:
			mostPolitical[word] = (frequencies[word] - 1.3116344469e-7)/(1.3116344469e-7*frequencies[word])
	
	return mostPolitical

def importData(fileToImport):
	file = open(fileToImport, "r")
	lines = file.readlines()
	file.close
	return collections.Counter(eval(lines[0][7:]))

def parseSubmissions(subreddit):
	instances = collections.Counter()
	count = 0
	for submission in subreddit.top(limit = 1000):
		if not submission.stickied:
			process_submission(submission,instances)
			count += 1
			print("new post " + str(count))
	
	return instances
	
def process_submission(submission, instances):
	
	submission.comments.replace_more(limit=0)
	for top_level_comment in submission.comments:
		if len(top_level_comment.body) < MAX_LENGTH and not top_level_comment.stickied:
			words = top_level_comment.body.lower().split()
			#filter spam
			isNotSpam = True
			for index in range(0,len(words) - 1):
				if(words[index] == words[index+1]):
					isNotSpam = False
			if isNotSpam:
				instances.update(words)

def convertToFrequency(counter):
	#CLEAN UP
	fix = collections.Counter()
	for word in counter: 
		if(word.find(".") == len(word)-1 or word.find("?") == len(word)-1 or word.find("!") == len(word)-1 or word.find(",") == len(word)-1 or word.find(":") == len(word)-1): #catches end characters
			if(isLowercaseLetter(word[:len(word) -1])): #gets rid of contractions and the like
				fix[word[:len(word)-1]] = counter[word]
		elif isLowercaseLetter(word):
			fix[word] = counter[word]

	total = sum(fix.values())
	fixedFreq = collections.Counter()
	for key in fix:
		if ( fix[key] >THRESHOLD_VALUE):
			fixedFreq[key] = fix[key]/total
	return fixedFreq

def isLowercaseLetter(stringInput):
	for character in stringInput:
		if character not in string.ascii_lowercase:
			return False
	return True

if __name__ == '__main__':
	main()
