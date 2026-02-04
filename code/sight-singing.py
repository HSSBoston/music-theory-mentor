# import random, numpy as np
# import os
# import streamlit as st
# from PIL import Image
# import subprocess

from music21 import *
from sight_singing_gen import *

m21Settings = environment.UserSettings()
m21Settings["musescoreDirectPNGPath"] = "/Applications/MuseScore 4.app/Contents/MacOS/mscore"

score = generateSightSingingScore()

# 
# melody.write("musicxml.png", fp = "melody-image.png")
# midiFile= melody.write("midi", fp = "melody.mid")
# 
# museScoreCmd = "/Applications/MuseScore 4.app/Contents/MacOS/mscore"
# cmd = [museScoreCmd, "melody.mid", "-o", "melody.mp3"]
# subprocess.run(cmd, check=True)
# 
# st.title("Sight singing")
# st.image( Image.open("melody-image-1.png") )
# st.audio("melody.mp3")

if __name__ == "__main__":
    score = generateSightSingingScore()
    score.show("text")
    score.show()

    