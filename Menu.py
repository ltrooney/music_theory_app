import curses
import constants as c

class Menu():
	def __init__(self):
		self.w = curses.initscr()
		self.response = None

	def __del__(self):
		""" Reset the console."""
		self.refresh()
		curses.endwin()

	def get_window(self):
		""" Get the curses window instance."""
		return self.w

	def set_response(self, response):
		self.response = response

	def get_response(self):
		""" Get response from previous input."""
		return self.response

	def has_response(self):
		return self.response != None

	def print_response(self):
		if self.has_response():
			self.printstr("RESPONSE: ")
			self.printstr_ln(self.get_response())

	'''
	---------------------
	|	I/O operations	|
	---------------------
	'''

	def read_input(self):
		""" Get input from the user."""
		return self.w.getstr()
	
	def printstr(self, text):
		""" Print text to the console without a newline character. """
		self.w.addstr(text)

	def printstr_ln(self, text):
		""" Print text to the console with a newline character. """
		self.printstr(text)
		self.printstr('\n')

	def print_option(self, option_num, text):
		""" Print an option with related text to the console. """
		self.printstr_ln(str(option_num) + ". " + text)

	def display(self):
		""" Show menu options. """
		self.print_response()
		self.printstr_ln("-"*10 + "Music Theory" + "-"*10)
		self.print_option(c.OPTN_CHOOSE_ROOT, "set root")
		self.print_option(c.OPTN_CALC_INTVL, "calculate interval")	
		self.print_option(c.OPTN_GET_NOTES, "get notes")
		self.print_option(c.OPTN_GET_CHORDS, "get chords")

	'''
	---------------------
	|	Housekeeping	|
	---------------------
	'''

	def refresh(self):
		""" Clear the console. """
		self.w.clear()
		self.w.refresh()

	
