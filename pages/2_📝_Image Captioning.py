import streamlit as st
from PIL import Image
import io
#from utils.caption_generator import initialising
from utils.cap_generation import query
import os
# st.set_page_config(page_title="Image Captioning", page_icon="📝")

st.markdown("# Image Captioning")
st.sidebar.header("Image Captioning is Selected")
st.write(
    """Unleash the power of AI to add context and meaning to your images! With our image caption generation tool, transform ordinary images into captivating stories. Witness how AI effortlessly describes the essence of each image, opening doors to endless possibilities in visual communication. Experience the future of image understanding with ease and precision, only with Streamlit!"""
)
st.title("Image Captioning App")

st.write("Upload an image and let's generate a caption!")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

#model, feature_extractor, tokenizer = initialising()


# def predict_step(image_paths):
#   images = []
#   for image_path in image_paths:
#     i_image = Image.open(image_path)
#     if i_image.mode != "RGB":
#       i_image = i_image.convert(mode="RGB")

#     images.append(i_image)

#   pixel_values = feature_extractor(images=images, return_tensors="pt").pixel_values
#   pixel_values = pixel_values.to(device)

#   output_ids = model.generate(pixel_values, **gen_kwargs)

#   preds = tokenizer.batch_decode(output_ids, skip_special_tokens=True)
#   preds = [pred.strip() for pred in preds]
#   return preds

# def predict_step(images):
#     pixel_values = []

#     # Convert each image to RGB mode if necessary and collect pixel values
#     for img in images:
#         if img.mode != "RGB":
#             img = img.convert(mode="RGB")
#         pixel_values.append(img)

#     # Convert pixel values to PyTorch tensors and move to appropriate device
#     pixel_tensors = feature_extractor(images=pixel_values, return_tensors="pt").pixel_values
#     pixel_tensors = pixel_tensors.to(device)

#     # Generate captions for the images
#     output_ids = model.generate(pixel_tensors, **gen_kwargs)

#     # Decode the generated captions
#     preds = tokenizer.batch_decode(output_ids, skip_special_tokens=True)
#     preds = [pred.strip() for pred in preds]

#     return preds
# Function to process the uploaded image and generate caption
def process_image(image, preds):
    # Display the uploaded image
    st.image(image, caption= preds, use_column_width=True)

    # Here you would typically use your image captioning model to generate the caption
    # For the sake of example, let's just display a placeholder caption
    st.write(f"Caption: {preds}")

def main():
    #model, feature_extractor, tokenizer = initialising()
    if uploaded_file is not None:
        # Read the image file as bytes
        image_bytes = uploaded_file.read()
        
        # Convert the image bytes to PIL Image
        image = Image.open(io.BytesIO(image_bytes))
        image1 = image
        image.save('temp.jpg')
        a = query('temp.jpg')
        pred = a[0]['generated_text']
        process_image(image1, pred)
        file_path = "temp.jpg"  # Example file path

        # Check if the file exists before deleting
        if os.path.exists(file_path):
            os.remove(file_path)
            print(f"File {file_path} deleted successfully.")
        else:
            print(f"File {file_path} does not exist.")

if __name__ == "__main__":
    main()
