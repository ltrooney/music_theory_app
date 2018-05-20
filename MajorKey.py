class MajorKey(Key):
	def __init__(self, tonic):
		Key.__init__(tonic)
		
	def get_notes(self):
		notes = []
		notes.append(tonic.interval(c.INTVL_MAJ_2))
		notes.append(tonic.interval(c.INTVL_MAJ_3))
		notes.append(tonic.interval(c.INTVL_PER_4))
		notes.append(tonic.interval(c.INTVL_PER_5))
		notes.append(tonic.interval(c.INTVL_MAJ_6))
		notes.append(tonic.interval(c.INTVL_MAJ_7))

	def get_chords(self):
		pass

	def relative_minor(self):
		pass