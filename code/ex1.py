import streamlit as st
from PIL import Image

st.title("Streamlit Basics")
st.header("This is a header")
st.subheader("This is a subheader")
st.text("This is a simple text")
st.write("This is a write dimension")

st.markdown("[Streamlit](https://www.streamlit.io)")
st.markdown("https://www.streamlit.io")

html_page = """
<div style="background-color:blue;padding:50px">
<p style="color:yellow;font-size:50px">Enjoy Streamlit!</p>
</div>
"""
st.markdown(html_page, unsafe_allow_html=True)

st.success("Success!")
st.info("Information")
st.warning("This is a warning!")
st.error("This is an error!")

#img = Image.open("photo.png")
#st.image(img, width=300, caption="Packt Logo")

st.video("https://www.youtube.com/watch?v=xAWDqdpOlu8")


if st.button("Play"):
    st.text("Hello world!")
    
if st.checkbox("Checkbox"):
    st.text("Checkbox selected")
    
radio_but = st.radio("Your Selection", ["A","B"])
if radio_but == "A":
    st.info("You selected A")
else:
    st.info("You selected B")
    
city = st.selectbox("Your City", ["Bedford", "Lexington", "Burlington"])

occupation = st.multiselect("Your Occupation", ["Programmer", "Data Scientist", "IT Consultant", "DBA"])

Name = st.text_input("Your Name", "Write something...")
st.text(Name)

Age = st.number_input("Input a number")

message = st.text_area("Your Messsage", "Write something...")

select_val = st.slider("Select a Value", 1, 10)

if st.button("Balloons"):
    st.balloons()
    
if 'processed_input' not in st.session_state:
    st.session_state['processed_input'] = ""

def process_input():
    # This function is called when the text input changes
    st.session_state['processed_input'] = st.session_state['current_input']

st.text_input(
    "Enter something",
    key="current_input",
    on_change=process_input
)
st.button("Update Display") # This button forces a rerun after the callback

# This logic only updates when the 'processed_input' state is changed via the callback
if st.session_state['processed_input']:
    st.write(f"Current processed input: {st.session_state['processed_input']}")
