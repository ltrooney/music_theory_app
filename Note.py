import constants as c

class Note(object):
	def __init__(self, name, accidental=None):
		self.name = name
		if accidental is None:
			self.accidental = c.TONE_NATURAL
		else:
			self.accidental = accidental

	def __str__(self):
		return self.get_note_name()

	def get_note_name(self):
		return self.get_name() + self.get_accidental()

	def get_name(self):
		return self.name

	def get_accidental(self):
		return self.accidental

	def set_note_name(self, name, accidental):
		self.set_name(name)
		self.set_accidental(accidental)

	def set_name(self, name):
		self.name = name

	def set_accidental(self, accidental):
		self.accidental = accidental

	def up_half(self):
		""" Get the note up one semitone (half step)."""
		if self.name == c.NOTE_B:
			return Note(c.NOTE_C, c.TONE_NATURAL)
		elif self.name == c.NOTE_E:
			return Note(c.NOTE_F, c.TONE_NATURAL)
		elif self.accidental == c.TONE_NATURAL:
			return Note(self.name, c.TONE_SHARP)

		i = c.NOTES.index(self.name)
		return Note(c.NOTES[(i+1) % 7], c.TONE_NATURAL)

	def up_whole(self):
		""" Get the note up two semitones (whole step). """
		return self.up_half().up_half()

	def down_half(self):
		""" Get the note down one semitone (half step). """
		if self.name == c.NOTE_C:
			return Note(c.NOTE_B, c.TONE_NATURAL)
		elif self.name == c.NOTE_F:
			return Note(c.NOTE_E, c.TONE_NATURAL)
		elif self.accidental == c.TONE_NATURAL:
			return Note(self.name, c.TONE_FLAT)

		i = c.NOTES.index(self.name)
		return Note(c.NOTES[(i-1) % 7], c.TONE_NATURAL)

	def down_whole(self):
		""" Get the note down two semitones (whole step). """
		return self.down_half().down_half()

	def alt(self):
		""" Turn flat note into relative sharp and vice versa. """
		if self.accidental == c.TONE_SHARP:
			n = self.up_half()
			n.set_accidental(c.TONE_FLAT)
			return n
		elif self.accidental == c.TONE_FLAT:
			n = self.down_half()
			n.set_accidental(c.TONE_SHARP)
			return n
		return self

	def interval(self, interval):
		""" Get the note at a distance specified by the interval. """
		n = self
		for i in xrange(interval):
			n = n.up_half()
		return n





