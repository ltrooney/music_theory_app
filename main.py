from Note import Note
from Chord import Chord
from GuitarNote import GuitarNote
from GuitarString import GuitarString
from GuitarChord import GuitarChord
from GuitarFretboard import GuitarFretboard
from Menu import Menu
from Renderer import Renderer
import constants as c
import re
from curses import wrapper

def parse_note(note_str):
	""" Parse the input to determine the note and the accidental. 
	- parse_note("A") -> "A", None
	- parse_note("Ab" [or "A flat" or "A-flat"]) -> "A", "b"
	- parse_note("Abb") -> "A", "bb"
	- parse_note("bA" [or "flat A" or "flat-A"]) -> None, None
	- parse_note("ABb") -> None, None
	- parse_note("Ab#") -> None, None
	"""
	note_str = " ".join(note_str.split())	# remove duplicate whitespace
	# TODO: don't match if '-' not followed by accidental
	m = re.search('(A|B|C|D|E|F|G){1}(-| |)(b|flat|#|sharp){0,2}', note_str)
	if m is None:
		return
	match_str = m.group(0)
	return match_str[0], match_str[1:]

def main(stdscr):
	menu = Menu(stdscr)
	response = None
	key = Key(Note(c.NOTE_C), c.TONALITY_MAJOR)
	menu.set_response("Current key: " + key.get_tonic().get_note_name() + " major")

	while True:
		menu.display(c.MAIN_MENU_DICT)
		
		menu.printstr("Pick an option: ")
		option = int(menu.read_input())

		if option == c.OPTN_EXIT:
			break
		elif option == c.OPTN_CHOOSE_ROOT:
			menu.printstr("New root: ")
			new_root_str = menu.read_input()
			note_str = parse_note(new_root_str)
			if note_str is None:
				menu.set_response(new_root_str + " is not a valid key!")
			else:
				root = Note(note_str[0], note_str[1])
				menu.set_response("Key updated! New key is " + root.get_note_name() + " major")
		elif option == c.OPTN_GET_NOTES_IN_KEY:
			pass
		elif option == c.OPTN_GET_CHORDS_IN_KEY:
			pass
		elif option == c.OPTN_GET_INTERVALS:
			pass
		elif option == c.OPTN_DISPLAY_ROOTS:
			print r.plot(note)
		elif option == c.OPTN_DISPLAY_NOTES_IN_KEY:
			pass
		elif option == c.OPTN_DISPLAY_CHORD:
			pass
		elif option == c.OPTN_DISPLAY_SCALE:
			pass
		else:
			menu.set_response("Invalid input.")

		menu.refresh()

wrapper(main)
'''
note_f = Note(c.NOTE_A)
c = GuitarChord(note_f, c.CHORD_MAJ_7)
r = Renderer()
r.display_intervals()
r.set_num_dashes_per_fret(4)
print r.plot(c)
'''

