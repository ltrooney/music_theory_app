from Note import Note
from GuitarNote import GuitarNote
from math import floor

class Renderer(object):
	def __init__(self, fretboard):
		self.set_fretboard(fretboard)
		self.show_fret_markers()
		self.set_num_dashes_per_fret(3)

	def set_fretboard(self, fretboard):
		self.fretboard = fretboard

	def get_fretboard(self):
		return self.fretboard

	def show_fret_markers(self, val=True):
		""" Choose whether or not the fret numbers will be displayed. """
		self.show_fret_markers = val

	def fret_markers_enabled(self):
		""" Determines if fret numbers will be displayed. """
		return self.show_fret_markers

	def set_num_dashes_per_fret(self, num):
		""" Sets the number of dashes that appear in a fret when plotted. """
		if num < 1:
			self.num_dashes_per_fret = 1
		elif num > 6:
			self.num_dashes_per_fret = 6
		else:
			self.num_dashes_per_fret = num

	def get_num_dashes_per_fret(self):
		""" The number of dashes that appear in a fret when plotted. """
		return self.num_dashes_per_fret

	def plot_empty(self):
		""" Returns an ascii art image of an empty fretboard. """
		return self.plot(pattern=None)

	def plot(self, pattern=None):
		""" Returns an ascii art image of the specified notes on the fretboard. """
		
		dashes_per_fret = self.get_num_dashes_per_fret()
		
		def draw_note_on_string(s, note, string):
			# exit if note is on another string
			if note.get_string() != string:
				return s
			# fill in occupied frets
			half_dashes = int(floor(dashes_per_fret/2))
			fret = note.get_fret()
			s[fret] = "-X||" if fret == 0 else "-"*half_dashes + "X" + "-"*(dashes_per_fret-half_dashes-1) + "|"
			return s

		# draw empty board
		fb_str = []
		fretboard = self.get_fretboard()
		for string in reversed(fretboard.get_strings()):
			# draw empty frets, treating root as special case
			s = [ "--||" if fret == 0 else "-"*dashes_per_fret + "|" for fret in range(fretboard.get_num_frets()+1) ]

			# occupy notes on frets
			if isinstance(pattern, GuitarNote):	# display single note
				s = draw_note_on_string(s, pattern, string)
			elif isinstance(pattern, Note):	# display note at every location it occurs
				notes = string.find_note(pattern)
				for note in notes:
					s = draw_note_on_string(s, note, string)
			elif isinstance(pattern, list):		# display array of notes
				if all(type(n) is GuitarNote for n in pattern):
					for note in pattern:
						s = draw_note_on_string(s, note, string)
			#elif isinstance(pattern, GuitarChord):
			# 	TODO
			#	pass

			# prepend string label
			s.insert(0, str(string))
			s = "".join(s)
			fb_str.append(s)

		fb_str = '\n'.join(fb_str)

		# add fret markers
		if self.fret_markers_enabled() and dashes_per_fret > 1:
			marker_str = " "*5
			fret_markers = [3, 5, 7, 9, 12, 15, 17, 19, 21, 24]
			i = 0
			k = 1
			for i, fret in enumerate(fret_markers):
				if fret > fretboard.get_num_frets():
					break

				while k != fret:
					marker_str += " "*(dashes_per_fret+1)
					k += 1

				half_dashes = int(floor(dashes_per_fret/2))
				if k > 9:
					marker_str += " "*(half_dashes-1) + str(k) + " "*(dashes_per_fret-half_dashes)
				else:
					marker_str += " "*half_dashes + str(k) + " "*(dashes_per_fret-half_dashes)
				k += 1

			return fb_str + "\n" + marker_str

		return fb_str
