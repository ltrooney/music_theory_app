from constants import TONALITY_MAJOR, TONALITY_MINOR, CHORD_MIN, CHORD_DIM
from Chord import Chord

class Key(object):
	def __init__(self, tonic, tonality=TONALITY_MAJOR):
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
		if tonality != TONALITY_MAJOR and tonality != TONALITY_MINOR:
			raise ValueError("tonality must be 'major' or 'minor'")
		self.tonality = tonality

	def get_tonality(self):
		""" Get the tonality of the key. """
		return self.tonality

	def get_notes(self):
		""" Get the notes that make up the key. """
		scale_note = self.get_tonic()
		notes = [ scale_note ]

		if self.get_tonality() == TONALITY_MAJOR:
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
		elif self.get_tonality() == TONALITY_MINOR:
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

		return notes
		
	def get_chords(self):
		""" Get the chords in the key. """
		notes = self.get_notes()
		chords = [ Chord(n) for n in notes ]

		if self.get_tonality() == TONALITY_MAJOR:
			chords[1].set_chord_type(CHORD_MIN)
			chords[2].set_chord_type(CHORD_MIN)
			chords[5].set_chord_type(CHORD_MIN)
			chords[6].set_chord_type(CHORD_DIM)
		elif self.get_tonality() == TONALITY_MINOR:
			chords[0].set_chord_type(CHORD_MIN)
			chords[1].set_chord_type(CHORD_DIM)
			chords[3].set_chord_type(CHORD_MIN)
			chords[4].set_chord_type(CHORD_MIN)

		return chords

	def get_chord_numerals(self):
		numerals = ["i","ii","iii","iv","v","vi","vii"]
		return ' '.join(numerals)






