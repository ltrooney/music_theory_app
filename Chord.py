class Chord(object):
	def __init__(self, root, intervals):
		self.root = root
		self.type = intervals
			
		self.notes = [ root ]
		self.notes += [ root.get_note_at_interval(interval) for interval in intervals ]

	def get_notes(self):
		return self.notes
