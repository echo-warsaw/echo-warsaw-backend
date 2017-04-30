def stemmer(word):  # super simple word stemmer
	word = word.lower()
	return word if len(word) <= 3 else word[:-1] if len(word) == 4 else word[:-2]


if __name__ == '__main__':
	import sys
	print(stemmer(str(sys.argv[1])))
