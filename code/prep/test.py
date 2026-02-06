from music21 import *

# scalePitchNames = []
# sc = scale.MajorScale("C")
# 
# for p in sc.getPitches("C4","C5"):
#   scalePitchNames.append(p.nameWithOctave)
#   
# print(scalePitchNames)
# 
# sc1 = scale.MajorScale('a')
# print([str(p) for p in sc1.getPitches('g2', 'g4')])

# sharp = pitch.Accidental('flat')
# print(sharp.alter)
# 
# sharp.alter + 1
# print(sharp.name)

newNote = note.Note("D")

if "-" in newNote.name:
    newNote.pitch.accidental = pitch.Accidental('natural')
elif "#" in newNote.name:
    newNote.pitch.accidental = pitch.Accidental('double-sharp')
else:
    newNote.pitch.accidental = pitch.Accidental('sharp')

print(newNote.name)

# if "-" in newNote.name:
#     newNote.
# 
# print(newNote.transpose(1))
    
