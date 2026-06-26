import streamlit as st

# Set up the browser tab
st.set_page_config(page_title="Do Not Enter", page_icon="👁️")

# Inject custom CSS to make it dark and creepy
st.markdown("""
    <style>
    .stApp {
        background-color: #000000;
    }
    h1 {
        color: #8B0000;
        text-align: center;
        font-family: 'Courier New', Courier, monospace;
        letter-spacing: 5px;
    }
    p {
        color: #A9A9A9;
        text-align: center;
        font-family: 'Courier New', Courier, monospace;
    }
    .stButton>button {
        display: block;
        margin: 0 auto;
        color: red;
        background-color: black;
        border: 1px solid red;
    }
    </style>
""", unsafe_allow_html=True)

# Add the title
st.markdown("<h1>THE ORDER AWAITS</h1>", unsafe_allow_html=True)

# Display your logo
try:
    st.image("image_a0643d.png", use_container_width=True)
except Exception as e:
    st.error("The Eye is closed. (Make sure 'image_a0643d.png' is inside your Mywebsite.py folder!)")

# Add creepy text
st.markdown("<p>We have been watching you.</p>", unsafe_allow_html=True)
st.markdown("<p>Do you accept the truth?</p>", unsafe_allow_html=True)

# Add a spooky interactive button
if st.button("I Accept"):
    st.markdown("<h1>IT IS TOO LATE TO TURN BACK NOW.</h1>", unsafe_allow_html=True)
    st.snow()