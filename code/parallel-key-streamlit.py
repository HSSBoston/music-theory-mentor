from music21 import *
import random
import streamlit as st

with st.form(key="my_form"):
    keysLettersList = ["C","G","D","A","E","B","F","B-","E-","A-","D-","G-","a","e","b","f#","c#", "g#", "d", "g", "c","f","b-","e-"]
    keyLetter = random.choice(keysLettersList)

    st.title("Parallel Key")

    if keyLetter.isupper():
        ks = key.Key(keyLetter);
        
        optionsList = [ks.parallel, ks.relative, ks.relative.parallel, ks.parallel.relative]
        optionsOrderList = []
        
        for x in range(len(optionsList)):
            o = random.choice(optionsList)
            optionsOrderList.append(o)
            optionsList.remove(o)
        
        ksOption = st.radio("What is the parallel minor of " + str(ks), optionsOrderList)
        if ksOption == ks.parallel:
            st.success("You are correct!")
        else:
            st.warning("You are incorrect.")

    else:
        ks = key.Key(keyLetter);
        
        optionsList = [ks.parallel, ks.relative, ks.relative.parallel, ks.parallel.relative]
        optionsOrderList = []
        
        for x in range(len(optionsList)):
            o = random.choice(optionsList)
            optionsOrderList.append(o)
            optionsList.remove(o)
        
        ksOption = st.radio("What is the parallel major of " + str(ks), optionsOrderList)

        if ksOption == ks.parallel:
            st.success("You are correct!")
        else:
            st.warning("You are incorrect. The correct answer is "+ ks.parallel.name)
    
        doneOption = st.radio("Are you done?", ["Yes", "No"])
        if doneOption == "Yes":
            st.success("Ok")
        else:
            st.warning("Ok")
        
        submit_button = st.form_submit_button(label="submit")








