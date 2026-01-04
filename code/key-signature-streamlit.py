import random
from music21 import *
import streamlit as st

with st.form(key="my_form"):
    listNumOfAccidentals = [0,1,2,3,4,5,6,7]
    listSharpOrFlat = ["sharps", "flats"]

    accidentals = random.choice(listNumOfAccidentals)
    sharpOrFlat = random.choice(listSharpOrFlat)



    if sharpOrFlat == "sharps":
        ks = key.KeySignature(accidentals)
        ksKey = ks.asKey()
        option1ks = key.KeySignature(accidentals-1)
        option1 = option1ks.asKey()
        option2ks = key.KeySignature(accidentals+1)
        option2 = option2ks.asKey()
        option3ks = key.KeySignature(-(accidentals+1))
        option3 = option3ks.asKey()
        
    else:
        ks = key.KeySignature(-accidentals);
        ksKey = ks.asKey()
        option1ks = key.KeySignature(-(accidentals-1))
        option1 = option1ks.asKey()
        option2ks = key.KeySignature(-(accidentals+1))
        option2 = option2ks.asKey()
        option3ks = key.KeySignature(accidentals+1)
        option3 = option3ks.asKey()
        
    optionsList = [option1.name, ksKey.name, option2.name, option3.name]
    # optionsInOrder = [None]
    # for x in range(len(optionsList)):
    #     o = random.choice(optionsList)
    #     optionsInOrder.append(o)
    #     optionsList.remove(o)

    st.title("Key Signature")


    ksOption = st.radio("What is the name of the key signature with " + str(accidentals) + " " + sharpOrFlat, optionsList)


    if ksOption == ksKey.name:
        st.success("You are correct!")
    else:
        st.warning("You are incorrect. The correct answer is "+ksKey.name)
        
        
    doneOption = st.radio("Are you done?", ["Yes", "No"])
    if doneOption == "Yes":
        st.success("Ok")
    else:
        st.warning("Ok")
    
    submit_button = st.form_submit_button(label="submit")
    







