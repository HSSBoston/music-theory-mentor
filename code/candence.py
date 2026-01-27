from music21 import *
import random

cadences = {
    "Perfect Authentic Cadence" :  ["V-I", "V7-I"],
    "Imperfect Authentic Cadence" : ["V6-I", "V-I6", "V64-I", "V64-I6", "viidim6-I", "V7-I", "viihalfdim7-I"],
    "Plagal Cadence" : ["IV-I"],
    "Deceptve Cadence" : ["V-vi"],
    "Half Cadence" : ["IV-V", "ii-V", "ii6-V", "I64-V"],
    "Phrygian Half Cadence" : ["iv6-V"]
    }

cadence = random.choice(list(cadences.keys()))
answer = random.choice(cadences[cadence])
option1c = random.choice(list(cadences.keys()))
while option1c == cadence:
    option1c = random.choice(list(cadences.keys()))
option1 = random.choice(cadences[option1c])
option2c = random.choice(list(cadences.keys()))

while option2c == cadence or option2c == option1c:
    option2c = random.choice(list(cadences.keys()))
option2 = random.choice(cadences[option2c])
option3c = random.choice(list(cadences.keys()))

while option3c == cadence or option3c == option1c or option3c == option2c:
    option3c = random.choice(list(cadences.keys()))
option3 = random.choice(cadences[option3c]) 
    

print("Which would be an example of a "+cadence)
print(answer)
print(option1)
print(option2)
print(option3)