import collections

def main():
	data = processData("google-books-common-words.txt")
	print(data, file = open("genWordFreq.txt", "a"))

def processData(fileToImport):
	data = collections.Counter()
	file = open(fileToImport, "r")
	lines = file.readlines()
	sum = 0
	count = 0
	for line in lines:
		index = line.index("\t")
		sum += int(line[index:])
		count += 1
	
	for line in lines:
		index = line.index("\t")
		data[line[0:index].lower()] = int(line[index:]) / sum
		
	return data
	file.close
	print("Summary: " + str(count) + " unique words, used " + str(sum) + " total number of times, for an average of " + str(count/sum) + " frequency.")
	return 4
if __name__ == '__main__':
	main()