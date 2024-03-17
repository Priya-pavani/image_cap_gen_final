import requests
import streamlit as st
from PIL import Image
API_URL = "https://api-inference.huggingface.co/models/Salesforce/blip-image-captioning-large"
api_token =  st.secrets["api_token"]
headers = {"Authorization": api_token}



def query(filename):
    with open(filename, "rb") as f:
        data = f.read()
    response = requests.post(API_URL, headers=headers, data=data)
    return response.json()


#def get_caption(image)

