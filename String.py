from FretboardNote import FretboardNote

class String:
	def __init__(self, open):
		self.set_open(open)

	def __str__(self):
		return str(self.get_open())

	def set_open(self, open):
		self.open = open

	def get_open(self):
		return self.open

	def find_note(self, note, num_frets):
		""" Find note(s) occurences on the string. """
		n = self.open
		matches = []
		for fret in range(num_frets):
			if str(n) == str(note):
				fb_note = FretboardNote(n.get_name(), n.get_accidental(), self, fret)
				matches.append(fb_note)
			n = n.up_half()
		return matches

	def find_roots(self, num_frets):
		""" Find root occurences on the string. """
		return self.find_note(self.open, num_frets)
