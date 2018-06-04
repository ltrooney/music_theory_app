from Note import Note
from Chord import Chord
from Key import Key
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
	key = Key(Note(c.NOTE_C))
	menu.set_response("Current key: " + str(key))

	while True:
		menu.display(c.MAIN_MENU_DICT)
		
		menu.printstr("Pick an option: ")
		option = int(menu.read_input())

		if option == c.OPTN_EXIT:
			break
		elif option == c.OPTN_CHOOSE_KEY:
			menu.printstr("New key: ")
			new_key_str = menu.read_input()
			note_str = parse_note(new_key_str)
			if note_str is None:
				menu.set_response(new_key_str + " is not a valid key!")
			else:
				root = Note(note_str[0], note_str[1])
				key.set_tonic(root)

				# check if key is minor
				if ("minor" in new_key_str) or ("min" in new_key_str):
					key.set_tonality(c.TONALITY_MINOR)
				else:
					key.set_tonality(c.TONALITY_MAJOR)

				menu.set_response("Key updated! New key is " + str(key))
		elif option == c.OPTN_GET_NOTES_IN_KEY:
			s = ""
			for n in key.get_notes():
				s += str(n) + " "
			menu.set_response(s)
		elif option == c.OPTN_GET_CHORDS_IN_KEY:
			s = ""
			for chord in key.get_chords():
				s += str(chord) + " "
			s += "\n" + key.get_chord_numerals()
			menu.set_response(s)
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

