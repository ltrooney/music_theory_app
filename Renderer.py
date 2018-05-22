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
		self.num_dashes_per_fret = num

	def get_num_dashes_per_fret(self):
		""" The number of dashes that appear in a fret when plotted. """
		return self.num_dashes_per_fret

	def plot_empty(self):
		""" Returns an ascii art image of an empty fretboard. """
		return self.plot(pattern=None)

	def plot(self, pattern=None):
		""" Returns an ascii art image of the specified notes on the fretboard. """
		def draw_note_on_string(s, note, string):
			p_string = note.get_string()
			p_fret = note.get_fret()
			print p_fret

			# fill in occupied frets
			if str(p_string) == str(string):
				half_dashes = int(floor(dashes_per_fret/2))
				s[p_fret] = "-"*half_dashes + "X" + "-"*(dashes_per_fret-half_dashes-1) + "|"
			return s
			
		def draw_notes_on_string(s, notes, string):
			for note in notes:
				s = draw_note_on_string(s, note, string)
			return s
	
		fb_str = []
		dashes_per_fret = self.get_num_dashes_per_fret()

		if dashes_per_fret < 1:
			self.set_num_dashes_per_fret(1)
		elif dashes_per_fret > 6:
			self.set_num_dashes_per_fret(6)

		# draw empty board
		fretboard = self.get_fretboard()
		for string in reversed(fretboard.get_strings()):
			# draw empty frets
			s = [ ("-"*dashes_per_fret + "|") for fret in range(fretboard.get_num_frets()) ]

			string_header = str(string)

			# occupy notes on frets
			if isinstance(pattern, GuitarNote):	# display single note
				s = draw_note_on_string(s, pattern, string)
				string_header += "-X||" if (pattern.get_fret() == 0 and pattern.get_string() == string) else "--||"
			elif isinstance(pattern, Note):	# display note at every location it occurs
				notes = string.find_note(pattern)
				s = draw_notes_on_string(s, notes, string)
				string_header += "-X||" if string.get_open() in notes else "--||"
			elif isinstance(pattern, list):		# display array of notes
				if all(type(n) is GuitarNote for n in pattern):
					s = draw_notes_on_string(s, pattern, string)
					string_header += "-X||" if string.get_open() in pattern else "--||"
			#elif isinstance(pattern, GuitarChord):
			# 	TODO
			#	pass

			# prepend string label
			s.insert(0, string_header)
			s = "".join(s)
			fb_str.append(s)

		fb_str = '\n'.join(fb_str)
		
		# add fret markers
		if self.fret_markers_enabled() and self.get_num_dashes_per_fret() > 1:
			marker_str = " "*len(string_header)
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