import streamlit as st

st.set_page_config(
    page_title="Image Captioning📝and Generation 🖼️",
    page_icon="🖼️",
)

# Header
st.title("Image Captioning📝and Generation 🖼️")
st.sidebar.header("Try one of the options above")
# Description
st.write("""
This Streamlit app allows you to generate captions for images and generate images from text descriptions using machine learning models.

## Image Captioning

To generate a caption for an image, simply upload an image using the "Upload Image" button. Once the image is uploaded, click the "Generate Caption" button. The model will then process the image and provide a caption for it.

## Image Synthesis or Generation

If you want to generate an image from a text description, enter your description in the text input box provided. After entering the description, click the "Generate Image" button. The model will then interpret the text and generate an image based on the description.

### Tips:

- For best results, use clear and descriptive text descriptions when generating images from text.
- For image caption generation, use high-quality images with clear subjects for accurate captions.
- The models used in this app are based on state-of-the-art deep learning techniques, but results may vary depending on the complexity of the input and the model's training data.

Enjoy experimenting with image caption generation and image generation from text!
""")