import curses
from curses import wrapper
import constants as c

class Menu(object):
	def __init__(self, stdscr=curses.initscr()):
		self.w = stdscr
		self.response = None
		self.configure()
		stdscr.keypad(1)

	def __del__(self):
		""" Reset the console."""
		self.configure()
		curses.endwin()

	def configure(self):
		""" Configure the console settings. """
		self.w.keypad(0)
		curses.echo()
		curses.nocbreak()

	def get_window(self):
		""" Get the curses window instance."""
		return self.w

	def set_response(self, response):
		""" Set the response that will appear on next console refresh. """
		if isinstance(response, str):
			self.response = response
		else:
			raise ValueError("Invalid parameter. '%s' must be of type 'str'." % text)
		

	def get_response(self):
		""" Get response from previous input."""
		return self.response

	def has_response(self):
		return self.response != None

	# -------------------
	# |	I/O operations	|
	# -------------------

	def read_input(self):
		""" Get input from the user."""
		return self.w.getstr()
	
	def printstr(self, text):
		""" Print text to the console without a newline character. """
		if isinstance(text, str):
			self.w.addstr(text)
		else:
			raise ValueError("Invalid parameter. '%s' must be of type 'str'." % text)

	def printstr_ln(self, text):
		""" Print text to the console with a newline character. """
		self.printstr(text + "\n")

	def print_option(self, option_num, text):
		""" Print an option with related text to the console. """
		self.printstr_ln(str(option_num) + ". " + text)

	def print_response(self):
		if self.has_response():
			self.printstr_ln(self.get_response())

	def display(self, options_dict, header=None):
		""" Show menu options. """
		self.refresh()
		self.print_response()
		# print the header
		if header != None:
			tot_header_len = 30
			half_dashes = (tot_header_len - len(header)) / 2
			self.printstr_ln("-"*half_dashes + header + "-"*half_dashes)
		# print the menu options
		for option in options_dict:
			self.print_option(option, options_dict[option])

	def is_left_arrow(self, user_input):
		return user_input == curses.KEY_LEFT

	def is_right_arrow(self, user_input):
		return user_input == curses.KEY_RIGHT
	
	# -----------------
	# |	Housekeeping  |
	# -----------------

	def refresh(self):
		""" Clear the console. """
		self.w.clear()
		self.w.refresh()

	
