from constants import CHORD_INTVL_DICT, CHORD_MAJ

class Chord(object):
	def __init__(self, root, chord_type=CHORD_MAJ):
		""" Construct a chord given the root and the chord type. """
		self.set_root(root)
		self.set_chord_type(chord_type)
			
		notes = [ root ]
		notes += [ root.get_note_at_interval(interval) for interval in CHORD_INTVL_DICT[chord_type] ]
		self.set_notes(notes)

	def __str__(self):
		return str(self.get_root()) + self.get_chord_type()

	def set_root(self, root):
		self.root = root

	def get_root(self):
		return self.root

	def set_chord_type(self, chord_type):
		self.chord_type = chord_type

	def get_chord_type(self):
		return self.chord_type

	def set_notes(self, notes):
		self.notes = notes

	def get_notes(self):
		return self.notes
