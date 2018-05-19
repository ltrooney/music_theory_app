from Note import Note
from Menu import Menu
import constants as c

response = None
root = Note(c.NOTE_C, c.TONE_NATURAL)
menu = Menu()

while True:
	menu.display()
	
	menu.printstr("Choose: ")
	option = int(menu.read_input())

	menu.refresh()

	if option == c.OPTN_EXIT:
		break
	elif option == c.OPTN_CHOOSE_ROOT:
		menu.printstr("New root: ")
		new_root = menu.read_input()
		for n in c.NOTES:
			if new_root == n:
				root = Note(new_root, c.TONE_NATURAL)
				break
	else:
		menu.set_response("Invalid")

del menu






