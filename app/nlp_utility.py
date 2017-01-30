class NlpUtility():
	"""
		Utility methods to get particular parts of speech from a token set
	"""
	def get_nouns(self, tokens):
		nouns = []
		for word, pos in tokens:
			if pos == "NN":
				nouns.push(word)

	def get_verbs(self, tokens):
		verbs = []
		for word, pos in tokens:
			if pos == "VB":
				nouns.push(word)

	def get_adjectives(self, tokens):
		nouns = []
		for word, pos in tokens:
			if pos == "NN":
				nouns.push(word)

	def get_nouns(self, tokens):
		nouns = []
		for word, pos in tokens:
			if pos == "NN":
				nouns.push(word)

	def get_nouns(self, tokens):
		nouns = []
		for word, pos in tokens:
			if pos == "NN":
				nouns.push(word)
