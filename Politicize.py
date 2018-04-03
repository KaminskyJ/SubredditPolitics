import praw
import collections
reddit = praw.Reddit(client_id = 'os7m34NXJFkr0g',
					 client_secret = '0oJVizuj3K3XGFEIUPCw_t9D23M',
					 username = 'justTestingStuffyeah',
					 password = 'justTestingStuffyeah',
					 user_agent = 'testBotv1')

#subreddits of interest, can be changed
subreddit1 = reddit.subreddit('politics')
subreddit2 = reddit.subreddit('the_donald')

MIN_OCCURANCE = 20
MAX_LENGTH = 2000

"""
The main objective of this script is to "politicize" words. That is:
freq(subreddit)-freq(all)/freq(all) yields the percent difference between
the subreddit and r/all. ie. if a particular subreddit yields a dictionary
of 'dog' : 50.4, it means that subreddit uses the word 'dog' 50.4 times
the average.

The results of this script are printed into the txt documents "DemsData.txt"
and "RepubsData.txt".

NOTE: many of the procedures of this script are not commented because they are
similar to that of RedditWordFrequencies.py. If you are confused, go check that
out.
"""
def main():
	demsOccurances = parseSubmissions(subreddit1)
	repubsOccurances = parseSubmissions(subreddit2)
	demsFrequency = convertToFrequency(demsOccurances)
	repubsFrequency = convertToFrequency(repubsOccurances)
	redditData = importData("RedditFrequency.txt")
	demsPoliticized = politicize(demsFrequency, redditData)
	repubsPoliticized = politicize(repubsFrequency, redditData)
	print(demsPoliticized, file = open("DemsData.txt", "a"))
	print(repubsPoliticized, file = open("RepubsData.txt", "a"))
	
#politicizes the data as described above the main() method
def politicize(freq, data):
	mostPolitical = collections.Counter()
	for word in freq:
		if word in data:
			if freq[word] - data[word] > 0:
				mostPolitical[word] = (freq[word] - data[word])/data[word]

	return mostPolitical

#same as
def parseSubmissions(subreddit):
	occurances = collections.Counter()
	count = 0
	for submission in subreddit.top(limit = 1000):
		if not submission.stickied:
			processSubmission(submission,occurances)
			count += 1
	
	return occurances

#similar to
def processSubmission(submission, occurances):
	submission.comments.replace_more(limit=0)
	for comment in submission.comments.list():
		if len(comment.body) < MAX_LENGTH and not comment.stickied:
			words = comment.body.lower().split()
			for word in words:
				checkWord(word)
				word  = isLowercaseLetter(word)
			occurances.update(words)

#same as
def convertToFrequency(count):
	totalCount = sum(count.values())
	print(totalCount)
	frequency = collections.Counter()
	for word in count:
		if count[word] > MIN_OCCURANCE:
			frequency[word] = count[word] / totalCount
	return frequency

#similar to
def checkWord(word):
		if len(word) > 0:
			if word[len(word)-1] == "!" or word[len(word)-1] == "?" or word[len(word)-1] == "," or word[len(word)-1] == ".":
				word = word[:len(word)-1]
				checkWord(word)

#import data. Data should be in form of a printed dictionary.
def importData(fileToImport):
	file = open(fileToImport, "r")
	lines = file.readlines()
	file.close
	return collections.Counter(eval(lines[0][7:]))

#checks if string is lowercase (or ""), returns string that will be used for data
def isLowercaseLetter(stringInput):
	for character in stringInput:
		if character not in string.ascii_lowercase:
			return stringInput
	return ""

if __name__ == '__main__':
	main()