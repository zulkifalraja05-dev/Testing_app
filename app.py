# ==============================
# 📌 Import Libraries
# ==============================
import streamlit as st
import numpy as np
import pandas as pd

# ==============================
# 🎯 App Title
# ==============================
st.title('My First Testing App')

# ==============================
# 📝 Simple Text
# ==============================
st.write('Here is a simple text')

# ==============================
# 🎚️ Slider Input
# ==============================
number = st.slider('Pick a number', 0, 100)
st.write(f'You selected: {number}')

# ==============================
# 🎬 Radio Button (Movie Genre)
# ==============================
st.header("Select Your Favorite Movie Genre")

genre = st.radio(
    "What's your favorite movie genre",
    ('Comedy', 'Drama', 'Documentary')
)

st.write("You selected:", genre)

# ==============================
# 📂 Sidebar Inputs
# ==============================
option = st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone')
)

# ✅ Only ONE text input (with key)
whatsapp = st.sidebar.text_input(
    'Enter your WhatsApp number',
    key='whatsapp_input'
)

# ✅ Only ONE file uploader (with key)
uploaded_file = st.sidebar.file_uploader(
    "Choose a CSV file",
    type="csv",
    key='file_upload'
)

# ==============================
# 📊 Line Chart
# ==============================
data = pd.DataFrame({
    'first column': list(range(1, 11)),
    'second column': np.arange(number, number + 10)
})

st.line_chart(data)