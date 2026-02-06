from music21 import *
from sight_singing_gen import *
from PIL import Image
import subprocess, streamlit as st

MUSESCORE_PATH = "/Applications/MuseScore 4.app/Contents/MacOS/mscore"

m21Settings = environment.UserSettings()
m21Settings["musescoreDirectPNGPath"] = MUSESCORE_PATH

def score2imgMidi():
    score.write("musicxml.png", fp = "melody-image.png")
    score.write("midi",         fp = "melody.mid")

def score2mp3():    
    subprocess.run(
        [MUSESCORE_PATH, "melody.mid", "-o", "melody.mp3"],
        check=True)

score = generateSightSingingScore()
score2imgMidi(score)
score2mp3(score)

st.title("Section 2B: Sight-singing")
st.image(Image.open("melody-image-1.png"))
st.audio("melody.mp3")
