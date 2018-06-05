from Note import Note
from Chord import Chord
from GuitarNote import GuitarNote
from GuitarChord import GuitarChord
from GuitarFretboard import GuitarFretboard
from math import floor, ceil
import constants as c

class Renderer(object):
	def __init__(self, fretboard=GuitarFretboard()):
		self.set_fretboard(fretboard)
		self.show_fret_markers()
		self.set_num_dashes_per_fret(3)
		self.display_intervals(False)
		self.display_note_name(False)

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

	def display_intervals(self, val=True):
		""" Determines whether to show the interval number on the fretboard. """
		self.show_intervals = val

	def display_note_name(self, val=True):
		""" Determines wheter to show the note name on the fretboard. """
		self.show_note_name = val

	def plot_empty(self):
		""" Returns an ascii art image of an empty fretboard. """
		return self.plot(pattern=None)

	def plot(self, pattern=None):
		""" Returns an ascii art image of the specified notes on the fretboard. """
		dashes_per_fret = self.get_num_dashes_per_fret()

		def get_fret_pattern(note):
			marker = ""
			if self.show_note_name:
				marker = note.get_note_name()
			elif self.show_intervals:
				marker = c.INTVL_DICT[note.get_interval()]
			else:
				marker = "R" if note.get_interval() == 0 else "X"
			root_fret_pattern = "*"*(2-len(marker)) + marker + "||"
			dashes_buffer = float(dashes_per_fret - len(marker))
			return root_fret_pattern if note.get_fret() == 0 else "-"*int(ceil(dashes_buffer/2)) + marker + "-"*int(floor(dashes_buffer/2)) + "|"
		 
		def draw_note_on_string(s, note, string):
			# if GuitarNote ...
			if type(note) is GuitarNote:	
				note_buf = [note]	# display single note
			elif type(note) is Note:
				note_buf = string.find_note(note)  # display note at every location it occurs
			elif type(note) is Chord:
				note_buf = note.get_notes()	# display chord
			else:
				raise ValueError("input 'note' must be of instance Note, [Note], or Chord")

			for n in note_buf:
				# skip note if on another string
				if n.get_string() != string:
					continue
				# fill in occupied frets
				s[n.get_fret()] = get_fret_pattern(n)
			return s

		# draw empty board
		fb_str = []
		fretboard = self.get_fretboard()
		for string in reversed(fretboard.get_strings()):
			# draw empty frets, treating root as special case
			s = [ "--||" if fret == 0 else "-"*dashes_per_fret + "|" for fret in range(fretboard.get_num_frets()+1) ]
			
			if isinstance(pattern, list):		# display array of notes
				for note in pattern:
					s = draw_note_on_string(s, note, string)
			elif isinstance(pattern, Chord):
				for note in pattern.get_notes():
					s = draw_note_on_string(s, note, string)
			else:
				s = draw_note_on_string(s, pattern, string)

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
