from music21 import *
import random, numpy as np

RANDOM_SEED_NOTE = None #None or int
rng = np.random.default_rng(seed=RANDOM_SEED_NOTE)

P = np.array(
    [[0, 0.4, 0.4, 0.1, 0.1, 0, 0, 0],
     [0.3, 0, 0.4, 0.3, 0, 0, 0, 0],
     [0.1, 0.4, 0, 0.4, 0.1, 0, 0, 0],
     [0, 0.1, 0.4, 0, 0.4, 0.1, 0, 0],
     [0, 0, 0.2, 0.65, 0, 0.1, 0.05, 0],
     [0, 0, 0, 0.3, 0.5, 0, 0.2, 0],
     [0, 0, 0, 0.1, 0.1, 0.3, 0, 0.5],
     [0, 0, 0, 0, 0, 0.5, 0.5, 0]
     ])

measureOneSE = [" T8 8 8 8 8 8 ",
                " T8 8 8 4 8 ",
                " T8 8 8 8 4 ",
                " T4 8 8 8 8 ",
                " T8 4 8 8 8 ",
                " T4 8 4 8 ",
                " T8 4 8 4 ",
                " T4 8 8 4 "
                ]

measureTwoThreeSE = [" 8. 16 8 8 8 8 " ,
                     " 8. 16 8 4 8 ",
                     " 8. 16 8 8 4 ",
                     " 8 8 8 8. 16 8 ",
                     " 8 4 8. 16 8 ",
                     " 4 8 8. 16 8 ",
                     " 8 8 8 4 8 ",
                     " 8 8 8 8 4 ",
                     " 4 8 8 8 8 ",
                     " 8 4 8 8 8 ",
                     " 4 8 4 8 ",
                     " 8 4 8 4 ",
                     " 4 8 8 4 "
                    ]

measureFourSE = [" 8 8 8 T4. ",
                " 4 8 T4. ",
                " 8 4 T4. "]

#up to four accidentals only (to keep problems not too hard)
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

#randomInt = random.randint(0,1)
#
# if randomInt < 0.5:
#     timeSig == "4/4"
# else:
#     timeSig == "6/8"

randomInt = random.randint(0,1)
if randomInt < 0.5:
    cl = clef.TrebleClef()
else:
    cl = clef.BassClef()

cl = clef.TrebleClef()

randomInt = random.randint(0,1)
if randomInt < 0.5:
    timeSig = "4/4"
else:
    timeSig = "6/8"

timeSig = "6/8"

if timeSig == "4/4":
        
    rhythmString = random.choice(measureOneFF)+random.choice(measureTwoThreeFF)+random.choice(measureTwoThreeFF)+random.choice(measureFourFF)
    print(rhythmString)
    melodyString = "tinyNotation: 4/4"  
    for num in rhythmString.split():
        if "T" in num:
            newNote = note.Note(k.tonic)
            num = num[-1]
            newNoteSD = "1"
            noteName = newNote.name.lower()
        else:
            newNoteSD = rng.choice(["1", "2", "3", "4", "5", "6", "7", "8"], p=P[scalePitchNames.index(temp.name)])
            newNote = note.Note(scalePitchNames[int(newNoteSD)-1])
            
            if newNote.name == k.getLeadingTone().name and keyLetter.islower():
                newNote.pitch.accidental("sharp")
                
            if cl == clef.TrebleClef():
                s = converter.parse("tinyNotation: " + newNote.name.lower() + tempNoteString)

                if abs(s.recurse().notes.first().pitch.midi - s.flatten().notes[1].pitch.midi) > 7:
                    if len(newNote.name) > 1:
                        noteName = newNote.name[0].lower() + "'"
                    else:
                        noteName = newNote.name[0].lower() + "'" + newNote.name[1:]
                else:
                    noteName = newNote.name.lower()
            else:
                s = converter.parse("tinyNotation: " + newNote.name.upper() + tempNoteString)
                
                if abs(s.recurse().notes.first().pitch.midi - s.flatten().notes[1].pitch.midi) > 5:
                    noteName = newNote.name.lower()
                else:
                    noteName = newNote.name.upper()
            
        noteString = " " + noteName + num + " "
        melodyString += noteString
        temp = newNote
        tempNoteString = noteString

else:
    rhythmString = random.choice(measureOneSE)+random.choice(measureTwoThreeSE)+random.choice(measureTwoThreeSE)+random.choice(measureFourSE)
    print(rhythmString)
    melodyString = "tinyNotation: 6/8"  
    for num in rhythmString.split():
        if "T" in num:
            newNote = note.Note(k.tonic)
            if "." in num:
                num = num[-2:]
            else:
                num = num[-1:]
            newNoteSD = "1"
            if cl == clef.TrebleClef():
                noteName = newNote.name.lower()
            else:
#                 if keyLetter.lower() == "g" or keyLetter.lower() == "b" or keyLetter.lower() == "a":
#                     noteName = newNote.name.upper() + newNote.name.upper()
#                 else:
                noteName = newNote.name.upper()
        else:
            newNoteSD = rng.choice(["1", "2", "3", "4", "5", "6", "7", "8"], p=P[scalePitchNames.index(temp.name)])
            newNote = note.Note(scalePitchNames[int(newNoteSD)-1])
            
            if newNote.name == k.getLeadingTone().name and keyLetter.islower():
                newNote.pitch.accidental("sharp")
                
            if cl == clef.TrebleClef():
                print(newNote.pitch.midi)
                print(temp.pitch.midi)
                if newNote.pitch.midi > temp.pitch.midi:
                    if (newNote.pitch.midi - temp.pitch.midi) >= 7:
                        noteName = newNote.name.lower()
                    else:
                        noteName = newNote.name.lower()
                else:
                    if (temp.pitch.midi - newNote.pitch.midi) >= 7:
                        noteName = newNote.name.lower() + "'"
                    else:
                        noteName = newNote.name.upper()
            else:
                if newNote.pitch.midi > temp.pitch.midi:
                    if (newNote.pitch.midi - temp.pitch.midi) >= 7:
                        noteName = newNote.name.upper()[0]+newNote.name.upper()[0]+newNote.name[1:]
                    else:
                        noteName = newNote.name.upper()
                else:
                    if (temp.pitch.midi - newNote.pitch.midi) >= 7:
                        noteName = newNote.name.lower()
                    else:
                        noteName = newNote.name.upper()
                    
            
        noteString = " " + noteName + num + " "
        melodyString += noteString
        temp = newNote
        tempNoteString = noteString

print(melodyString)
melody = converter.parse(melodyString)
melody.measure(1).keySignature = key.Key(keyLetter)
melody.insert(0.0, tempo.MetronomeMark(60))
melody.show()