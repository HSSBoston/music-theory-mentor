import random
from music21 import *

listNumOfAccidentals = [0,1,2,3,4,5,6,7]
listSharpOrFlat = ["sharps", "flats"]

accidentals = random.choice(listNumOfAccidentals)
sharpOrFlat = random.choice(listSharpOrFlat)

print("What is the name of the key signature with " + str(accidentals) + " " + sharpOrFlat)

if sharpOrFlat == "sharps":
    ks = key.KeySignature(accidentals);
    key = ks.asKey()
    print(key)
else:
    ks = key.KeySignature(-accidentals);
    key = ks.asKey()
    print(key)
    
print("What is the relative minor of " + str(key))
print(key.relative)

print("What is the parallel minor of " + str(key))
print(key.parallel)






