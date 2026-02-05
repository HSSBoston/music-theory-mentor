from music21 import *
import random, numpy as np

RANDOM_SEED_NOTE = None #None or int
rng = np.random.default_rng(seed=RANDOM_SEED_NOTE)

P = np.array([
    [0,   0.4,  0.4, 0.2,  0, 0,    0,    0],
    [0.3, 0,    0.4, 0.3,  0,   0,    0,    0],
    [0.1, 0.4,  0,   0.4,  0.1, 0,    0,    0],
    [0,   0.15, 0.4, 0,    0.4, 0.05, 0,    0],
    [0,   0,    0.2, 0.65, 0,   0.1,  0.05, 0],
    [0,   0,    0,   0.3,  0.5, 0,    0.2,  0],
    [0,   0,    0,   0.1,  0.1, 0.3,  0,    0.5],
    [0,   0,    0,   0,    0.6,   0,  0.4,  0]])

#SIMPLE 4/4
measureOneFF = [
    [1, 1,   0.5, 0.5, 1],
    [1, 1,   1,   0.5, 0.5],
    [1, 0.5, 0.5, 1, 1],
    [1, 1,   1,   1],
    [1, 1,   0.5, 0.5, 0.5, 0.5],
    [1, 0.5, 0.5, 0.5, 0.5, 1]]

measureTwoThreeFF = [
    [0.5, 0.5, 1, 1.5,   0.5],
    [1.5, 0.5, 2],
    [1.5, 0.5, 1,   0.5, 0.5],
    [1,   1,   1.5, 0.5],
    [0.5, 0.5, 0.5, 0.5, 1.5, 0.5],
    [1,   1.5, 0.5, 1],
    [1,   1,   0.5, 0.5, 0.5, 0.5],
    [1,   0.5, 0.5, 0.5, 0.5, 1],
    [1,   1,   0.5, 0.5, 0.5, 0.5],
    [0.5, 0.5, 1,   1,   0.5, 0.5],
    [0.5, 0.5, 0.5, 0.5, 1,   1]]

measureFourFF = [
    [1,   1,   2],
    [0.5, 0.5, 1, 2],
    [1,   0.5, 0.5, 2]]

#SIMPLE 6/8
measureOneSE = [
    [0.5, 0.5, 0.5, 0.5, 0.5, 0.5],
    [0.5, 0.5, 0.5, 1,   0.5],
    [0.5, 0.5, 0.5, 0.5, 1],
    [1,   0.5, 0.5, 0.5, 0.5],
    [0.5, 1,   0.5, 0.5, 0.5],
    [1,   0.5, 1,   0.5],
    [0.5, 1,   0.5, 1],
    [1,   0.5, 0.5, 1]]

measureTwoThreeSE = [
    [0.75, 0.25, 0.5,  0.5,   0.5,  0.5],
    [0.75, 0.25, 0.5,  1,     0.5],
    [0.75, 0.25, 0.5,  0.5,   1],
    [0.5,  0.5,  0.5,  0.75,  0.25, 0.5],
    [0.5,  1,    0.75, 0.25,  0.5],
    [1,    0.5,  0.75, 0.25,  0.5],
    [0.5,  0.5,  0.5,  1,     0.5],
    [0.5,  0.5,  0.5,  0.5,   1],
    [1,    0.5,  0.5,  0.5,   0.5],
    [0.5,  1,    0.5,  0.5,   0.5],
    [1,    0.5,  1,    0.5],
    [0.5,  1,    0.5,  1],
    [1,    0.5,  0.5,  1]]

measureFourSE = [
    [0.5, 0.5, 0.5,  1.5],
    [1,   0.5, 1.5],
    [0.5, 1,   1.5]]


#up to three accidentals only (to keep problems not too hard)
keyLettersList = ["C","G","D","A","F","B-","E-","a","e","b", "d", "g", "c"]
keyLetter = random.choice(keyLettersList)
k = key.Key(keyLetter)

if k.mode == "major":
  sc = scale.MajorScale(keyLetter)
else:
  sc = scale.HarmonicMinorScale(keyLetter)

scalePitchNames = []

randomInt = random.randint(0,1)
if randomInt < 0.5:
    cl = clef.TrebleClef()
    for pitch in sc.getPitches(keyLetter+"4"):
        scalePitchNames.append(pitch.nameWithOctave)
    
else:
    cl = clef.BassClef()
    for pitch in sc.getPitches(keyLetter+"3"):
        scalePitchNames.append(pitch.nameWithOctave)

randomInt = random.randint(0,1)
if randomInt < 0.5:
    timeSig = "4/4"
else:
    timeSig = "6/8"

melody = stream.Part()
m1 = stream.Measure()
m1.append(cl)
m1.insert(0, meter.TimeSignature(timeSig))
m1.keySignature = k
m2 = stream.Measure()
m3 = stream.Measure()
m4 = stream.Measure()
m4.rightBarLine = bar.Barline("final")

if timeSig == "4/4":
    #LIST OF STRINGS
    m1Rhythm = random.choice(measureOneFF)
    m2Rhythm = random.choice(measureTwoThreeFF)
    m3Rhythm = random.choice(measureTwoThreeFF)
    m4Rhythm = random.choice(measureFourFF)
else:
    m1Rhythm = random.choice(measureOneSE)
    m2Rhythm = random.choice(measureTwoThreeSE)
    m3Rhythm = random.choice(measureTwoThreeSE)
    m4Rhythm = random.choice(measureFourSE)

print(m1Rhythm)
print(m2Rhythm)
print(m3Rhythm)
print(m4Rhythm)

prevNote = None

#MEASURE ONE
for index, noteDuration in enumerate(m1Rhythm):
    if index == 0:
        newNote = note.Note(k.tonic)
        newNoteSD = "1"
        if cl == clef.BassClef():
            newNote.octave = 3
        else:
            newNote.octave = 4
        newNote.quarterLength = noteDuration
    else:
        print(prevNote.nameWithOctave)
        newNoteSD = rng.choice(["1", "2", "3", "4", "5", "6", "7", "8"], p=P[scalePitchNames.index(prevNote.nameWithOctave)])
        newNote = note.Note(scalePitchNames[int(newNoteSD)-1])
        
        newNote.octave = m1.notes.first().octave
        if (newNote.pitch.midi - prevNote.pitch.midi) >= 7:
            newNote.octave -= 1
        if (prevNote.pitch.midi - newNote.pitch.midi) >= 7:
            newNote.octave += 1
            
        newNote.quarterLength = noteDuration

    prevNote = newNote
    
    m1.append(newNote)
    
    
    
#MEASURE TWO
for index, noteDuration in enumerate(m2Rhythm):
    print(prevNote.nameWithOctave)
    newNoteSD = rng.choice(["1", "2", "3", "4", "5", "6", "7", "8"], p=P[scalePitchNames.index(prevNote.nameWithOctave)])
    newNote = note.Note(scalePitchNames[int(newNoteSD)-1])
    
    
    newNote.octave = m1.notes.first().octave
#     if (newNote.pitch.midi - prevNote.pitch.midi) > 7:
#         testNewNote = newNote
#         testNewNote.octave -= 1
#         if (testNewNote.pitch.midi - prevNote.pitch.midi) > (newNote.pitch.midi - prevNote.pitch.midi):
#             pass
#         else:
#             newNote.octave -= 1
#     if (prevNote.pitch.midi - newNote.pitch.midi) > 7:
#         testNewNote = newNote
#         testNewNote.octave += 1
#         if (prevNote.pitch.midi - testNewNote.pitch.midi) > (prevNote.pitch.midi - newNote.pitch.midi):
#             pass
#         else:
#             newNote.octave += 1
    if (newNote.pitch.midi - prevNote.pitch.midi) >= 7:
        newNote.octave -= 1
    if (prevNote.pitch.midi - newNote.pitch.midi) >=7:
        newNote.octave += 1
    
    newNote.quarterLength = noteDuration

    prevNote = newNote
    
    m2.append(newNote)
    
#MEASURE THREE
for index, noteDuration in enumerate(m3Rhythm):
    print(prevNote.nameWithOctave)
    newNoteSD = rng.choice(["1", "2", "3", "4", "5", "6", "7", "8"], p=P[scalePitchNames.index(prevNote.nameWithOctave)])
    newNote = note.Note(scalePitchNames[int(newNoteSD)-1])
    
    newNote.octave = m1.notes.first().octave
    if (newNote.pitch.midi - prevNote.pitch.midi) >= 7:
        newNote.octave -= 1
    if (prevNote.pitch.midi - newNote.pitch.midi) >= 7:
        newNote.octave += 1
        
    newNote.quarterLength = noteDuration

    prevNote = newNote
        
    m3.append(newNote)

#MEASURE FOUR
for index, noteDuration in enumerate(m4Rhythm):
    if index == len(m4Rhythm) - 1:
        newNote = note.Note(k.tonic)
        newNoteSD = "1"
        if cl == clef.BassClef():
            newNote.octave = 3
        else:
            newNote.octave = 4
        newNote.quarterLength = noteDuration
    else:
        print(prevNote.nameWithOctave)
        newNoteSD = rng.choice(["1", "2", "3", "4", "5", "6", "7", "8"], p=P[scalePitchNames.index(prevNote.nameWithOctave)])
        newNote = note.Note(scalePitchNames[int(newNoteSD)-1])
                
        newNote.octave = m1.notes.first().octave
        if (newNote.pitch.midi - prevNote.pitch.midi) >= 7:
            newNote.octave -= 1
        if (prevNote.pitch.midi - newNote.pitch.midi) >= 7:
            newNote.octave += 1
            
        newNote.quarterLength = noteDuration

    prevNote = newNote
    
    m4.append(newNote)

melody.append(m1)
melody.append(m2)
melody.append(m3)
melody.append(m4)
melody.show("text")
melody.show()
