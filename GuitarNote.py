from Note import Note
import constants as c

class GuitarNote(Note):
	def __init__(self, string, fret, interval=c.INTVL_ROOT):
		self.set_string(string)
		self.set_fret(fret)

		note = string.get_note_at_fret(fret)
		Note.__init__(self, note.get_name(), note.get_accidental(), interval)

	def __str__(self):
		return Note.__str__(self) + " on " + str(self.get_string()) + "[" + str(self.get_fret()) + "]"

	def __eq__(self, other):
		return self.__dict__ == other.__dict__

	def set_string(self, string):
		self.string = string

	def get_string(self):
		return self.string

	def set_fret(self, fret):
		self.fret = fret

	def get_fret(self):
		return self.fret

	def up_half(self):
		""" Get the note up one semitone (half step)."""
		new_fret = self.fret+1
		if new_fret > self.get_string().get_num_frets():
			return None

		note = super(GuitarNote, self).up_half()
		return GuitarNote(self.string, new_fret)

	def up_whole(self):
		""" Get the note up two semitones (whole step). """
		up = self.up_half()
		if up:
			return up.up_half()
		return None

	def down_half(self):
		""" Get the note down one semitone (half step). """
		new_fret = self.fret-1
		if new_fret < 0:
			return None

		note = super(GuitarNote, self).down_half()
		return GuitarNote(self.string, new_fret)

	def down_whole(self):
		""" Get the note down two semitones (whole step). """
		down = self.down_half()
		if down:
			return down.down_half()
		return None

	def alt(self):
		""" Turn flat note into relative sharp and vice versa. """
		note = super(GuitarNote, self).alt()
		return GuitarNote(note.get_note_name(), self.get_string())
	
	def get_note_at_interval(self, interval, fretboard=None):
		""" Get the note at a distance specified by the interval. """
		note = super(GuitarNote, self).interval(interval)
		if fretboard == None:
			return note
		# get all instances of interval on the fretboard
		return fretboard.get_roots(note)

