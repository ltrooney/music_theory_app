import constants as c
from Note import Note
from GuitarString import GuitarString
from GuitarNote import GuitarNote
from math import floor

class Fretboard:
	def __init__(self, strings=None, num_frets=None):
		if strings is None:
			e = Note(c.NOTE_E)
			a = Note(c.NOTE_A)
			d = Note(c.NOTE_D)
			g = Note(c.NOTE_G)
			b = Note(c.NOTE_B)

			strings = [
				GuitarString(e), GuitarString(a), GuitarString(d),
				GuitarString(g), GuitarString(b), GuitarString(e)
			]
		self.set_strings(strings)

		if num_frets is None:
			self.set_num_frets(21)
		else:
			self.set_num_frets(num_frets)

		self.show_fret_markers()
		self.set_num_dashes_per_fret(3)

	def set_strings(self, strings):
		""" Sets the tuning of the guitar. """
		self.strings = strings

	def get_strings(self):
		return self.strings

	def set_num_frets(self, num_frets):
		self.num_frets = num_frets

	def get_num_frets(self):
		return self.num_frets

	def get_roots(self, note):
		""" Specifies on the fretboard the fret positions of the given note. """
		roots = []
		for string in self.get_strings():
			s_root = string.find_note(note, self.get_num_frets())
			roots.append(s_root)
		return roots

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
			# fill in occupied frets
			if str(p_string) == str(string):
				half_dashes = int(floor(dashes_per_fret/2))
				s[p_fret-1] = "-"*half_dashes + "X" + "-"*(dashes_per_fret-half_dashes-1) + "|"
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
		for string in reversed(self.get_strings()):
			s = []
			for fret in range(self.get_num_frets()):
				s.append("-"*dashes_per_fret + "|")

			if isinstance(pattern, GuitarNote):	# display single note
				s = draw_note_on_string(s, pattern, string)
				s = "".join(s)
				fb_str.append(s)
			elif isinstance(pattern, Note):	# display note at every location it occurs
				notes = string.find_note(pattern, self.get_num_frets())
				s = draw_notes_on_string(s, notes, string)
				s = "".join(s)
				fb_str.append(s)
			elif isinstance(pattern, list):		# display array of notes
				if isinstance(pattern[0], GuitarNote):
					s = draw_note_on_string(s, pattern, string)
					s = "".join(s)
					fb_str.append(s)
		#elif isinstance(pattern, GuitarChord):
		# 	TODO
		#	pass

		# string label fretboard
		string_header = ""
		for i, string in enumerate(reversed(self.get_strings())):
			string_header = str(string) + "--||"
			fb_str[i] = string_header + fb_str[i]	# prepend string name
		fb_str = '\n'.join(fb_str)
		
		# add fret markers
		if self.fret_markers_enabled() and self.get_num_dashes_per_fret() > 1:
			marker_str = " "*len(string_header)
			fret_markers = [3, 5, 7, 9, 12, 15, 17, 19, 21, 24]
			i = 0
			k = 1
			for i, fret in enumerate(fret_markers):
				if fret > self.get_num_frets():
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


e_n = Note(c.NOTE_E)
string = GuitarString(e_n)
n = GuitarNote(c.NOTE_E, c.TONE_NATURAL, string, 3)
f = Fretboard()
print f.plot(e_n)
