from music21 import *
import random

keysLettersList = ["C","G","D","A","E","B","F","B-","E-","A-","D-","G-","a","e","b","f#","c#", "g#", "d", "g", "c","f","b-","e-"]
keyLetter = random.choice(keysLettersList)

if keyLetter.isupper():
    ks = key.Key(keyLetter);
    print("What is the parallel minor of " + str(ks))
    print(ks.parallel)
else:
    ks = key.Key(keyLetter);
    print("What is the parallel major of " + str(ks))
    print(ks.parallel)


