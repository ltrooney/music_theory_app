import constants as c

class Key:
	def __init__(self, tonic):
		self.tonic = tonic

	def get_notes(self):
		notes = []
		notes.append(tonic.interval(c.INTVL_MAJ_2))
		notes.append(tonic.interval(c.INTVL_MAJ_3))
		notes.append(tonic.interval(c.INTVL_PER_4))
		notes.append(tonic.interval(c.INTVL_PER_5))
		notes.append(tonic.interval(c.INTVL_MAJ_6))
		notes.append(tonic.interval(c.INTVL_MAJ_7))

	# get chords