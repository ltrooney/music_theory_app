from GuitarNote import GuitarNote

class GuitarString(object):
	def __init__(self, open, num_frets=21):
		""" Populate string with notes. """
		self.open = open
		self.set_num_frets(num_frets)

		self.notes = []
		guitar_note = GuitarNote(open.get_name(), open.get_accidental(), self, 0)
		self.notes.append(guitar_note)
		for fret in range(1,num_frets+1):
			note = guitar_note.up_half()
			guitar_note = GuitarNote(note.get_name(), note.get_accidental(), self, fret)
			self.notes.append(guitar_note)

	def __str__(self):
		return str(self.get_open())

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

	def get_notes(self):
		""" Get the notes at each fret on the string. """
		return self.notes

	def find_note(self, note):
		""" Find note(s) occurences on the string. """
		matches = []
		for fret, n in enumerate(self.get_notes()):
			if n.get_note_name() == note.get_note_name():
				fb_note = GuitarNote(n.get_name(), n.get_accidental(), self, fret)
				matches.append(fb_note)
		return matches

	def find_roots(self, num_frets):
		""" Find root occurences on the string. """
		return self.find_note(self.open, num_frets)

