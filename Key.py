import constants as c

class Key(object):
	def __init__(self, tonic, tonality=c.TONALITY_MAJOR):
		self.set_tonic(tonic)
		self.set_tonality(tonality)

	def set_tonic(self, tonic):
		""" Sets the root note of the key. """
		self.tonic = tonic

	def get_tonic(self):
		""" Get the root note of the key. """
		return self.tonic

	def set_tonality(self, tonality):
		""" Set whether the key is major or minor. """
		self.tonality = type

	def get_tonality(self):
		""" Get the tonality of the key. """
		return self.tonality
