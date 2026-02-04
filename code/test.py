from music21 import *

scalePitchNames = []
sc = scale.MajorScale("C")

for p in sc.getPitches():
  scalePitchNames.append(p.name)
  
print(scalePitchNames.index("C"))