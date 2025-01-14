import streamlit as st
from streamlit.components.v1 import html

def replace_eszett(text):
    return text.replace('ß', 'ss')

def generate_html_with_js(text):
    return f"""
    <div>
        <textarea id='text_area' style='position: absolute; left: -9999px;'>{text}</textarea>
        <button onclick="copyToClipboard()" style="padding: 5px 10px; border-radius: 4px; border: 1px solid #ccc; background: white; cursor: pointer;">
            Copy to clipboard
        </button>
        <script>
            function copyToClipboard() {{
                var copyText = document.getElementById('text_area');
                copyText.style.opacity = 1;
                copyText.select();
                navigator.clipboard.writeText(copyText.value).then(function() {{
                    alert('Text copied to clipboard!');
                }}, function(err) {{
                    console.error('Could not copy text: ', err);
                }});
                copyText.style.opacity = 0;
            }}
        </script>
    </div>
    """

st.title('ß to ss Converter')

# Text input area
input_text = st.text_area('Paste your text here:', height=200)

# Convert button
if st.button('Replace ß'):
    if input_text:
        # Convert the text
        converted_text = replace_eszett(input_text)
        
        # Show the converted text
        st.text_area('Converted text:', converted_text, height=200)
        # Add copy to clipboard button
        html(generate_html_with_js(converted_text))
    else:
        st.warning('Please enter some text first.')
