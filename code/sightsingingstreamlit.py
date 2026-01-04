import streamlit as st
from PIL import Image

midiFilePath = "melody.mid"
melody.write("midi", fp = midiFilePath)

img = Image.open("melodyImage.png")
st.image(img)

audioFile = open("melody.wav", "rb")
audioBytes = audioFile.read()
st.audio(audioBytes, format="audio/wav")

