from GuitarNote import GuitarNote

class GuitarString(object):
	def __init__(self, open, num_frets=21):
		""" Populate string with notes. """
		self.open = open
		self.set_num_frets(num_frets)

		note = open
		self.notes = []
		for fret in range(num_frets+1):
			self.notes.append(note)
			note = note.up_half()

	def __str__(self):
		return str(self.get_open())

	def __eq__(self, other):
		return self.get_open().__dict__ == other.get_open().__dict__

	def set_open(self, open):
		""" Identify the string's open note value. """
		self.__init__(open, self.get_num_frets())

	def get_open(self):
		""" Get the string's root note. """
		return self.open

	def set_num_frets(self, num_frets):
		""" Set the number of frets on the string. """
		self.num_frets = num_frets

	def get_num_frets(self):
		""" Get the number of frets on the string. """
		return self.num_frets

	def get_note_at_fret(self, fret):
		""" Get the note at the specified fret on the string. """
		return self.get_notes()[fret]

	def get_notes(self):
		""" Get the notes at each fret on the string. """
		return self.notes

	def find_note(self, note):
		""" Find note(s) occurences on the string. """
		matches = []
		for fret, n in enumerate(self.get_notes()):
			if n.get_note_name() == note.get_note_name():
				fb_note = GuitarNote(self, fret)
				matches.append(fb_note)
		return matches

	def find_roots(self, num_frets):
		""" Find root occurences on the string. """
		return self.find_note(self.open, num_frets)

