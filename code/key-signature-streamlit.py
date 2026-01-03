import random
from music21 import *
import streamlit as st

listNumOfAccidentals = [0,1,2,3,4,5,6,7]
listSharpOrFlat = ["sharps", "flats"]

accidentals = random.choice(listNumOfAccidentals)
sharpOrFlat = random.choice(listSharpOrFlat)

print("What is the name of the key signature with " + str(accidentals) + " " + sharpOrFlat)

if sharpOrFlat == "sharps":
    ks = key.KeySignature(accidentals)
    key = ks.asKey()
    option1ks = key.KeySignature(accidentals-1)
    option1 = option1ks.asKey()
    option2ks = key.KeySignature(accidentals+1)
    option2 = option2ks.asKey()
    option3ks = key.KeySignature(accidentals+1)
    option3 = option3ks.asKey()
    
else:
    ks = key.KeySignature(-accidentals);
    key = ks.asKey()
    option1ks = key.KeySignature(accidentals+1)
    option1 = option1ks.asKey()
    option2ks = key.KeySignature(accidentals+1)
    option2 = option2ks.asKey()
    option3ks = key.KeySignature(accidentals+1)
    option3 = option3ks.asKey()
    
optionsList = [key, option1, option2, option3]
optionsInOrderList = []
for x in range(len(optionsList)):
    o = random.choice(optionsList)
    optionsInOrder.append(o)
    optionsList.remove(o)

st.title("Key Signature")


ksOption = st.radio("What is the name of the key signature with " + str(accidentals) + " " + sharpOrFlat, [key, "A"])
if ksOption == key:
    st.info("You are correct!")
else:
    st.info("You are incorrect.")


