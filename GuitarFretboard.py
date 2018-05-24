import constants as c
from Note import Note
from GuitarString import GuitarString

class GuitarFretboard(object):
	def __init__(self, strings=None, num_frets=21):
		if strings is None:
			e = Note(c.NOTE_E)
			a = Note(c.NOTE_A)
			d = Note(c.NOTE_D)
			g = Note(c.NOTE_G)
			b = Note(c.NOTE_B)

			strings = [
				GuitarString(e), GuitarString(a), GuitarString(d),
				GuitarString(g), GuitarString(b), GuitarString(e)
			]
		self.set_strings(strings)
		self.set_num_frets(num_frets)

	def set_strings(self, strings):
		""" Sets the tuning of the guitar. """
		self.strings = strings

	def get_strings(self):
		return self.strings

	def set_num_frets(self, num_frets):
		self.num_frets = num_frets

	def get_num_frets(self):
		return self.num_frets

	def get_roots(self, note):
		""" Specifies on the fretboard the fret positions of the given note. """
		return [ string.find_note(note) for string in self.get_strings() ]

	def get_notes(self):
		""" Get every note on the fretboard. """
		return [ string.get_notes() for string in self.get_strings() ]

