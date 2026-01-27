from music21 import *
import random, numpy as np

RANDOM_SEED_NOTE = None #None or int
rng = np.random.default_rng(seed=RANDOM_SEED_NOTE)

P = np.array(
    [[0, 0.4, 0.4, 0.1, 0.1, 0, 0, 0],
     [0.3, 0, 0.4, 0.3, 0, 0, 0, 0],
     [0.1, 0.4, 0, 0.4, 0.1, 0, 0, 0],
     [0, 0.15, 0.4, 0, 0.4, 0.05, 0, 0],
     [0, 0, 0.2, 0.65, 0, 0.1, 0.05, 0],
     [0, 0, 0, 0.3, 0.5, 0, 0.2, 0],
     [0, 0, 0, 0.1, 0.1, 0.3, 0, 0.5],
     [0, 0, 0, 0, 0, 0.5, 0.5, 0]
     ])

#SIMPLE 4/4
measureOneFF = [" T1 1 0.5 0.5 1 ",
                " T1 1 1 0.5 0.5 ",
                " T1 0.5 0.5 1 1 ",
                " T1 1 1 1 ",
                " T1 1 0.5 0.5 0.5 0.5 ",
                " T1 0.5 0.5 0.5 0.5 1 "]

measureTwoThreeFF = [" 0.5 0.5 1 1.5 0.5 ",
                    " 1.5 0.5 2 ",
                    " 1.5 0.5 1 0.5 0.5 ",
                    " 1 1 1.5 0.5 ",
                    " 0.5 0.5 0.5 0.5 1.5 0.5 ",
                    " 1 1.5 0.5 1 ",
                    " 1 1 0.5 0.5 0.5 0.5 ",
                    " 1 0.5 0.5 0.5 0.5 1 ",
                    " 1 1 0.5 0.5 0.5 0.5 ",
                    " 0.5 0.5 1 1 0.5 0.5 ",
                    " 0.5 0.5 0.5 0.5 1 1 "]

measureFourFF = [" 1 1 T2 ",
                " 0.5 0.5 1 T2 ",
                " 1 0.5 0.5 T2 "]

#SIMPLE 6/8
measureOneSE = [" T0.5 0.5 0.5 0.5 0.5 0.5 ",
                " T0.5 0.5 0.5 1 0.5 ",
                " T0.5 0.5 0.5 0.5 1 ",
                " T1 0.5 0.5 0.5 0.5 ",
                " T0.5 1 0.5 0.5 0.5 ",
                " T1 0.5 1 0.5 ",
                " T0.5 1 0.5 1 ",
                " T1 0.5 0.5 1 "
                ]

measureTwoThreeSE = [" 0.75 0.25 0.5 0.5 0.5 0.5 " ,
                     " 0.75 0.25 0.5 1 0.5 ",
                     " 0.75 0.25 0.5 0.5 1 ",
                     " 0.5 0.5 0.5 0.75 0.25 0.5 ",
                     " 0.5 1 0.75 0.25 0.5 ",
                     " 1 0.5 0.75 0.25 0.5 ",
                     " 0.5 0.5 0.5 1 0.5 ",
                     " 0.5 0.5 0.5 0.5 1 ",
                     " 1 0.5 0.5 0.5 0.5 ",
                     " 0.5 1 0.5 0.5 0.5 ",
                     " 1 0.5 1 0.5 ",
                     " 0.5 1 0.5 1 ",
                     " 1 0.5 0.5 1 "
                    ]

measureFourSE = [" 0.5 0.5 0.5 T1.5 ",
                " 1 0.5 T1.5 ",
                " 0.5 1 T1.5 "]


#up to three accidentals only (to keep problems not too hard)
keysLettersList = ["C","G","D","A","F","B-","E-","a","e","b", "d", "g", "c"]
keyLetter = random.choice(keysLettersList)
k = key.Key(keyLetter)

if k.mode == "major":
  sc = scale.MajorScale(keyLetter)
else:
  sc = scale.MinorScale(keyLetter)

scalePitchNames = []
scaleMidi = []

for p in sc.getPitches():
  scalePitchNames.append(p.name)
  scaleMidi.append(p.midi)      

randomInt = random.randint(0,1)
if randomInt < 0.5:
    cl = clef.TrebleClef()
else:
    cl = clef.BassClef()

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

temp = None

#MEASURE ONE
for num in m1Rhythm.split():
    if "T" in num:
        newNote = note.Note(k.tonic)
        if cl == clef.BassClef():
            newNote.octave = 3
        else:
            newNote.octave = 4
        newNote.quarterLength = float(num[1:])
    else:
        newNoteSD = rng.choice(["1", "2", "3", "4", "5", "6", "7", "8"], p=P[scalePitchNames.index(temp.name)])
        newNote = note.Note(scalePitchNames[int(newNoteSD)-1])
        
        newNote.octave = m1.notes.first().octave
        print(newNote.pitch.midi)
        print(newNote.pitch.octave)
        print(temp.pitch.midi)
        print(temp.pitch.octave)
        if (newNote.pitch.midi - temp.pitch.midi) >= 7:
            newNote.octave -= 1
        if (temp.pitch.midi - newNote.pitch.midi) >= 7:
            newNote.octave += 1
            
        newNote.quarterLength = float(num)
    
    m1.append(newNote)
    
    temp = newNote
    
#MEASURE TWO
for num in m2Rhythm.split():
    
    newNoteSD = rng.choice(["1", "2", "3", "4", "5", "6", "7", "8"], p=P[scalePitchNames.index(temp.name)])
    newNote = note.Note(scalePitchNames[int(newNoteSD)-1])
    
    if newNote.name == k.getLeadingTone().name and keyLetter.islower():
            newNote.pitch.accidental("sharp")
    
    newNote.octave = m1.notes.first().octave
    if (newNote.pitch.midi - temp.pitch.midi) >= 7:
        newNote.octave -= 1
    if (temp.pitch.midi - newNote.pitch.midi) >= 7:
        newNote.octave += 1
    
    newNote.quarterLength = float(num)
    
    m2.append(newNote)
    
    temp = newNote
    
#MEASURE THREE
for num in m3Rhythm.split():
    
    newNoteSD = rng.choice(["1", "2", "3", "4", "5", "6", "7", "8"], p=P[scalePitchNames.index(temp.name)])
    newNote = note.Note(scalePitchNames[int(newNoteSD)-1])
    
    if newNote.name == k.getLeadingTone().name and keyLetter.islower():
            newNote.pitch.accidental("sharp")
    
    newNote.octave = m1.notes.first().octave
    if (newNote.pitch.midi - temp.pitch.midi) >= 7:
        newNote.octave -= 1
    if (temp.pitch.midi - newNote.pitch.midi) >= 7:
        newNote.octave += 1
        
    newNote.quarterLength = float(num)
    
    m3.append(newNote)
    
    temp = newNote

#MEASURE FOUR
for num in m4Rhythm.split():
    if "T" in num:
        newNote = note.Note(k.tonic)
        newNoteSD = "1"
        if cl == clef.BassClef():
            newNote.octave = 3
        else:
            newNote.octave = 4
        newNote.quarterLength = float(num[1:])
    else:
        newNoteSD = rng.choice(["1", "2", "3", "4", "5", "6", "7", "8"], p=P[scalePitchNames.index(temp.name)])
        newNote = note.Note(scalePitchNames[int(newNoteSD)-1])
        
        if newNote.name == k.getLeadingTone().name and keyLetter.islower():
                newNote.pitch.accidental("sharp")
                
        newNote.octave = m1.notes.first().octave
        if (newNote.pitch.midi - temp.pitch.midi) >= 7:
            newNote.octave -= 1
        if (temp.pitch.midi - newNote.pitch.midi) >= 7:
            newNote.octave += 1
            
        newNote.quarterLength = float(num)
    
    m4.append(newNote)
    
    temp = newNote

melody.append(m1)
melody.append(m2)
melody.append(m3)
melody.append(m4)
melody.show("text")
melody.show()
