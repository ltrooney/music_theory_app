from Note import Note
import constants as c

n1 = Note(c.NOTE_G, c.TONE_SHARP)
print n1
n2 = n1.up_half()
print n2
print n2.down_whole()