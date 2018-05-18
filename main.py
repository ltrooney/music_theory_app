from Note import Note
import constants as c
import curses

w = curses.initscr()

def print_option(option_num, text):
	w.addstr(str(option_num) + ". " + text + "\n")

def display_menu():
	w.addstr("-"*10 + "Music Theory" + "-"*10 + "\n")
	print_option(1, "set root")
	print_option(2, "calculate interval")	

response = None

while True:
	display_menu()
	
	if response != None:
		w.addstr("RESPONSE: ")
		w.addstr(response)
		w.addstr("\n")
	
	w.addstr("Choose: ")
	option = w.getstr()

	w.clear()
	w.refresh()

	if int(option) == c.OPTION_EXIT:
		w.addstr("Goodbye!\n")
		break
	else:
		response = "Invalid"

curses.endwin()