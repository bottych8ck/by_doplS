import streamlit as st
import pyperclip

def replace_eszett(text):
    return text.replace('ß', 'ss')

st.title('ß to ss Converter')

# Text input area
input_text = st.text_area('Paste your text here:', height=200)

# Convert button
if st.button('Replace ß'):
    if input_text:
        # Convert the text
        converted_text = replace_eszett(input_text)
        
        # Copy to clipboard
        pyperclip.copy(converted_text)
        
        # Show the converted text
        st.text_area('Converted text (copied to clipboard):', converted_text, height=200)
        st.success('Text converted and copied to clipboard!')
    else:
        st.warning('Please enter some text first.')
