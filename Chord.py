class Chord(object):
	def __init__(self, root, intervals):
		self.root = root
		self.type = intervals
			
		self.notes = [ root ]
		self.notes += [ root.interval(interval) for interval in intervals ]

	def get_notes(self):
		return self.notes
