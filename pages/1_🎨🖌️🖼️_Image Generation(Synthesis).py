import streamlit as st
import time
import numpy as np
from utils.generation import get_prompt

def update_status(message, state):
    """
    This is for updating the status
    """
    st.status(message, state = state)

"""
Making the configuration and the structure of the page
"""
#st.set_page_config(page_title="Image Synthesis (Generation)", page_icon="🎨🖌️🖼️")
st.markdown("# Image Generation")
st.sidebar.header("Image Generation is selected")
st.write(
    """Experience the magic of AI as it brings your imagination to life with stunning images! Watch as your prompts come alive with creativity and innovation in just a few moments. Embark on a journey of visual storytelling with Streamlit's powerful image generation capabilities!"""
)

# Taking text input from the user
user_input = st.text_input("Enter description of the image you want to create:", placeholder = "Describe your image here", key = 'submit')
button_status = st.button("Generate Image")
if button_status :

    with st.status("Generating the Image see dropdown to see the status..."):
        st.write("Analysing the prompt............")
        time.sleep(2)
        st.write("Building components according to the prompt.")
        img = get_prompt(user_input)
        st.write("Uploading the Image...")
    
    st.image(img, width = 500)
    #update_status("Image is Generated Please take a look", state='complete')
    

