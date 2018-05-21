from Note import Note
from GuitarNote import GuitarNote
from GuitarString import GuitarString
from Menu import Menu
from Fretboard import Fretboard
import constants as c
import re
from curses import wrapper

response = None
root = Note(c.NOTE_C, c.TONE_NATURAL)

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
	return m.group(0)

def main(stdscr):
	menu = Menu(stdscr)

	while True:
		menu.display()
		
		menu.printstr("Choose: ")
		option = int(menu.read_input())

		menu.refresh()

		if option == c.OPTN_EXIT:
			break
		elif option == c.OPTN_CHOOSE_ROOT:
			menu.printstr("New root: ")
			new_root_str = menu.read_input()

			menu.set_response(parse_note(new_root_str))

			# TODO

		else:
			menu.set_response("Invalid input.")

#wrapper(main)

e_n = Note(c.NOTE_E)
string = GuitarString(e_n, 21)
n = GuitarNote(c.NOTE_E, c.TONE_NATURAL, string, 0)

print string.get_notes()



