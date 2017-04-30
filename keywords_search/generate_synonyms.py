from nltk.corpus import wordnet as wn


def generate_synonyms(word, lang='pol'):
	"""
	Uses synsets from nltk to generate synonyms and terms similar to the given word.
	Defaults to polish language.
	"""
	word = word.replace(' ', '_')  # sysnets require '_' instead of spaces
	synonyms = [syn.lemma_names(lang) for syn in wn.synsets(word, lang=lang)]
	synonyms = [syn for syn in synonyms if syn != []]  # filer out empty []
	if not synonyms:  # if there are no synonyms
		d = set()
		d.add(word.replace('_', ' '))
		return d
	else:  # flatten list, remove '_' and convert to set() to get rid of repetitions
		d = set()
		for syn in synonyms:
			if isinstance(syn, type(list())):
				[d.add(i) for i in syn]
			else:
				d.add(syn)
		d = map(lambda x: x.replace('_', ' '), d)
		return set(syn for syn in d)


#can be run as a script with: python generate_synonyms.py word_to_find_synonyms_for
if __name__ == '__main__':
	import sys
	print(generate_synonyms(' '.join(sys.argv[1:])))
