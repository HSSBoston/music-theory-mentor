from music21 import *
import random

keysLettersList = ["C","G","D","A","E","B","F","B-","E-","A-","D-","G-","a","e","b","f#","c#", "g#", "d", "g", "c","f","b-","e-"]
keyLetter = random.choice(keysLettersList)

if keyLetter.isupper():
    ks = key.Key(keyLetter);
    print("What is the relative minor of " + str(ks))
    print(ks.relative)
else:
    ks = key.Key(keyLetter);
    print("What is the relative major of " + str(ks))
    print(ks.relative)