from Note import Note

class FretboardNote(Note):
	def __init__(self, name, accidental, string, fret):
		Note.__init__(self, name, accidental)
		self.set_string(string)
		self.set_fret(fret)

	def __str__(self):
		return Note.__str__(self) + " on " + str(self.get_string()) + "[" + str(self.get_fret()) + "]"

	def set_string(self, string):
		self.string = string

	def get_string(self):
		return self.string

	def set_fret(self, fret):
		self.fret = fret

	def get_fret(self):
		return self.fret