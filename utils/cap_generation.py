import requests
from PIL import Image
API_URL = "https://api-inference.huggingface.co/models/nlpconnect/vit-gpt2-image-captioning"
headers = {"Authorization": "Bearer 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"}



def query(filename):
    with open(filename, "rb") as f:
        data = f.read()
    response = requests.post(API_URL, headers=headers, data=data)
    return response.json()


#def get_caption(image)

