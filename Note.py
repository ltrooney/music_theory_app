import constants as c

class Note:
	def __init__(self, name, accidental):
		self.name = name
		self.accidental = accidental

	def __str__(self):
		return self.get_name() + self.get_accidental()

	def get_name(self):
		return self.name

	def get_accidental(self):
		return self.accidental

	def up_half(self):
		if self.name == c.NOTE_B:
			return Note(c.NOTE_C, c.TONE_NATURAL)
		elif self.name == c.NOTE_E:
			return Note(c.NOTE_F, c.TONE_NATURAL)
		elif self.accidental == c.TONE_NATURAL:
			return Note(self.name, c.TONE_SHARP)
		elif self.name == c.NOTE_G and self.accidental == c.TONE_SHARP:
			return Note(c.NOTE_A, c.TONE_NATURAL)
		return Note(self.name, c.TONE_SHARP)

	def up_whole(self):
		return self.up_half().up_half()

	def down_half(self):
		if self.name == c.NOTE_C:
			return Note(c.NOTE_B, c.TONE_NATURAL)
		elif self.name == c.NOTE_F:
			return Note(c.NOTE_E, c.TONE_NATURAL)
		elif self.name == c.NOTE_A and self.accidental == c.TONE_FLAT:
			return Note(c.NOTE_G, c.TONE_SHARP)
		return Note(self.name, c.TONE_FLAT)

	def down_whole(self):
		return self.down_half().down_half()

	# def down_whole --> down whole step
	# def alternative --> converts sharp to flat or vice versa