import constants as c

class Key(object):
	def __init__(self, tonic, tonality=c.TONALITY_MAJOR):
		self.set_tonic(tonic)
		self.set_tonality(tonality)

	def __str__(self):
		return str(self.get_tonic()) + " " + self.get_tonality()

	def set_tonic(self, tonic):
		""" Sets the root note of the key. """
		self.tonic = tonic

	def get_tonic(self):
		""" Get the root note of the key. """
		return self.tonic

	def set_tonality(self, tonality):
		""" Set whether the key is major or minor. """
		self.tonality = tonality

	def get_tonality(self):
		""" Get the tonality of the key. """
		return self.tonality

	def get_notes(self):
		""" Get the notes that make up the key. """
		scale_note = self.get_tonic()
		notes = [ scale_note ]

		if self.get_tonality() == c.TONALITY_MAJOR:
			scale_note = scale_note.up_whole()
			notes.append(scale_note)
			scale_note = scale_note.up_whole()
			notes.append(scale_note)
			scale_note = scale_note.up_half()
			notes.append(scale_note)
			scale_note = scale_note.up_whole()
			notes.append(scale_note)
			scale_note = scale_note.up_whole()
			notes.append(scale_note)
			scale_note = scale_note.up_whole()
			notes.append(scale_note)
			scale_note = scale_note.up_half()
			notes.append(scale_note)
		elif self.get_tonality() == c.TONALITY_MINOR:
			scale_note = scale_note.up_whole()
			notes.append(scale_note)
			scale_note = scale_note.up_half()
			notes.append(scale_note)
			scale_note = scale_note.up_whole()
			notes.append(scale_note)
			scale_note = scale_note.up_whole()
			notes.append(scale_note)
			scale_note = scale_note.up_half()
			notes.append(scale_note)
			scale_note = scale_note.up_whole()
			notes.append(scale_note)
			scale_note = scale_note.up_whole()
			notes.append(scale_note)
		else:
			pass

		return notes
		
