import os
from transformers import VisionEncoderDecoderModel, ViTFeatureExtractor, AutoTokenizer
from huggingface_hub import hf_hub_download
import torch

def initialising():
    # Directory to store the downloaded files
    download_dir = "Json_downloads"
    os.makedirs(download_dir, exist_ok=True)

    HUGGING_FACE_API_KEY = os.environ.get("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")
    model_id = "nlpconnect/vit-gpt2-image-captioning"
    filenames = ["README.md",
                "config.json",
                "merges.txt",
                "preprocessor_config.json",
                "pytorch_model.bin",
                "special_tokens_map.json",
                "tokenizer.json",
                "tokenizer_config.json",
                "vocab.json"]
    
    # Check if the files already exist in the download directory, if not, download them
    for filename in filenames:
        file_path = os.path.join(download_dir, filename)
        if not os.path.exists(file_path):
            downloaded_model_path = hf_hub_download(
                repo_id=model_id,
                filename=filename,
                token=HUGGING_FACE_API_KEY,
                cache_dir=download_dir
            )
            print(f"Downloaded {filename} to {downloaded_model_path}")
        else:
            print(f"{filename} already exists locally.")

    # Load the model, feature extractor, and tokenizer from the local directory
    model = VisionEncoderDecoderModel.from_pretrained(download_dir)
    feature_extractor = ViTFeatureExtractor.from_pretrained(download_dir)
    tokenizer = AutoTokenizer.from_pretrained(download_dir)
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model.to(device)
    max_length = 16
    num_beams = 4
    gen_kwargs = {"max_length": max_length, "num_beams": num_beams}
    return model, feature_extractor, tokenizer


