import constants as c

class Note(object):
	def __init__(self, name, accidental=c.TONE_NATURAL, interval=c.INTVL_ROOT):
		self.set_name(name)
		self.set_accidental(accidental)
		self.set_interval(interval)

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

	def set_interval(self, interval):
		""" Sets the interval of this note relative to a root note. """
		self.interval = interval

	def get_interval(self):
		return self.interval

	def up_half(self):
		""" Get the note up one semitone (half step)."""
		new_interval = (self.get_interval() + c.INTVL_MIN_2) % c.INTVL_OCTAVE
		new_note = None
		if self.get_note_name() == c.NOTE_B:	# B -> C
			new_note = Note(c.NOTE_C, c.TONE_NATURAL, new_interval)
		elif self.get_note_name() == c.NOTE_E:	# E -> F
			new_note = Note(c.NOTE_F, c.TONE_NATURAL, new_interval)
		elif self.get_accidental() == c.TONE_NATURAL:	# natural -> sharp
			new_note = Note(self.get_name(), c.TONE_SHARP, new_interval)
		elif self.get_accidental() == c.TONE_FLAT:	# flat -> natural
			new_note = Note(self.get_name(), c.TONE_NATURAL, new_interval)
		else:	# sharp -> natural (note above)
			i = c.NOTES.index(self.get_name())
			new_note = Note(c.NOTES[(i+1) % 7], accidental=c.TONE_NATURAL, interval=new_interval)

		return new_note.alt() if new_note.get_name() == self.get_name() else new_note
			
	def up_whole(self):
		""" Get the note up two semitones (whole step). """
		whole = self.up_half().up_half()
		return whole if self.get_accidental() == c.TONE_FLAT else whole.alt()

	def down_half(self):
		""" Get the note down one semitone (half step). """
		new_interval = (self.get_interval() - c.INTVL_MIN_2) % c.INTVL_OCTAVE
		new_note = None
		if self.get_note_name() == c.NOTE_C:	# C -> B
			new_note =  Note(c.NOTE_B, c.TONE_NATURAL, new_interval)
		elif self.get_note_name() == c.NOTE_F:	# F -> E
			new_note =  Note(c.NOTE_E, c.TONE_NATURAL, new_interval)
		elif self.get_accidental() == c.TONE_NATURAL:	# natural -> flat
			new_note =  Note(self.get_name(), c.TONE_FLAT, new_interval)
		elif self.get_accidental() == c.TONE_SHARP:
			new_note =  Note(self.get_name(), c.TONE_NATURAL, new_interval)
		else:	# flat -> natural (note below)
			i = c.NOTES.index(self.get_name())
			new_note =  Note(c.NOTES[(i-1) % 7], accidental=c.TONE_NATURAL, interval=new_interval)

		return new_note.alt() if new_note.get_name() == self.get_name() else new_note

	def down_whole(self):
		""" Get the note down two semitones (whole step). """
		whole = self.down_half().down_half()
		return whole if self.get_accidental() == c.TONE_FLAT else whole.alt()

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

	def get_note_at_interval(self, interval):
		""" Get the note at a distance specified by the interval. """
		n = self
		for i in xrange(interval):
			n = n.up_half()
		return n




