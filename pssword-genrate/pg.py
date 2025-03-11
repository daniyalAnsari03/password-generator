import streamlit as st
import random
import string

def password_generator(lenght, use_digits, use_special):
    characters = string.ascii_letters

    if use_digits:
        characters += string.digits # Adds number character (0-9) if selected

    if use_special:
        characters += string.punctuation # Add special characters (!,#,&,@,^,%,*,.,;,)

    return ''.join(random.choice(characters) for _ in range(lenght))
        
st.title("Password Generator")
lenght = st.slider("Select Password length", min_value=6, max_value=32, value=12)
use_digits = st.checkbox("Include Digits")
use_special = st.checkbox("Include Special characters")

if st.button("Generate Password"):
    password = password_generator(lenght, use_digits, use_special)
    st.write(f"Generated Password: `{password}`")

