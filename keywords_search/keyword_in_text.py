import sys

sys.path.append('..')
from keywords_search.stemmer import stemmer

def keyword_in_text(keyword, text, synonyms):
	text = text.lower()
	keyword_found = stemmer(keyword) in text
	synonyms_found = []
	for syn in synonyms:
		if ' ' in syn:  # if synonym is a phrase, eg. 'stróż prawa'
			s = syn.split(' ')
			syn_found = all(stemmer(syn) in text for syn in s)
			synonyms_found.append(syn_found)
		else:
			syn_found = stemmer(syn) in text
			synonyms_found.append(syn_found)
	synonyms_found = any(synonyms_found)
	return keyword_found or synonyms_found
