from Chord import Chord
from GuitarFretboard import GuitarFretboard

class GuitarChord(Chord):
	def __init__(self, root, intervals, fretboard=GuitarFretboard()):
		Chord.__init__(self, root, intervals)	
		notes = self.get_notes()
		self.notes = []
		for note in notes:
			self.notes += fretboard.get_roots(note) 
