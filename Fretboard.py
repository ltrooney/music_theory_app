import constants as c
from Note import Note
from String import String

class Fretboard:
	def __init__(self, strings, num_frets=None):
		self.set_strings(strings)
		if num_frets is None:
			self.set_num_frets(21)
		else:
			self.set_num_frets(num_frets)

	def set_strings(self, strings):
		""" Sets the tuning of the guitar. """
		self.strings = strings

	def get_strings(self):
		return self.strings

	def set_num_frets(self, num_frets):
		self.num_frets = num_frets

	def get_roots(self, note):
		""" Specifies on the fretboard the fret positions of the given note. """
		roots = []
		for s in self.strings:
			s_root = s.find_note(note, self.num_frets)
			#dic = {str(note): s_root}
			roots.append(s_root)
		return roots

	# def show_chord

	# def show_scale

	def display(self, notes):
		""" Returns an ascii art image of the specified notes on the fretboard. 
			Expects input in array form with dimension string-by-# notes"""
		fretboard = ""


e = Note(c.NOTE_E)
a = Note(c.NOTE_A)
d = Note(c.NOTE_D)
g = Note(c.NOTE_G)
b = Note(c.NOTE_B)

strings = [
	String(e), String(a), String(d),
	String(g), String(b), String(e)
]

f = Fretboard(strings)

r = f.get_roots(e)

for i in r:
	for j in i:
		print j