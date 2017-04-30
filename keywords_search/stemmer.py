def stemmer(word):  # super simple word stemmer
	word = word.lower()
	def stem(word):
		return word if len(word) <= 3 else word[:-1] if len(word) == 4 else word[:-2]
	if ' ' in word:
		word = word.split(' ')
		word = ' '.join(stem(w) for w in word)
		return word
	else:
		return stem(word)


if __name__ == '__main__':
	import sys
	print(stemmer(str(sys.argv[1])))
