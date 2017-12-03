from string import punctuation
def first_world(string):
	return string.strip(punctuation).split()[0].strip(punctuation)

if __name__ == '__main__':
	print(first_world("don't be silly"))