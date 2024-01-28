

import os
import requests
from IPython.display import Audio

HUGGINGFACEHUB_API_TOKENS = os.getenv("api_token")

def get_story(image_caption, st):

    API_URL         = "https://api-inference.huggingface.co/models/HuggingFaceH4/zephyr-7b-beta"
    headers         = {"Authorization": "Bearer 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"}

    def query(prompt, max_new_tokens = 200):
        payload = {
            "inputs": prompt,
            "parameters": {
                "max_new_tokens": max_new_tokens
            }
        }
        response = requests.post(API_URL, headers = headers, json = payload)
        return response.json()
    
    print(f'image_caption : {image_caption}')

    data            = query(image_caption, max_new_tokens = 250)
    generated_text  = data[0].get("generated_text", "")
    st.text("Generated Text:")
    st.write(generated_text)

    API_URL = "https://api-inference.huggingface.co/models/espnet/kan-bayashi_ljspeech_vits"
    headers = {"Authorization": f"Bearer {HUGGINGFACEHUB_API_TOKENS}"}

    def generate_and_play_audio(text, sampling_rate = 22050):
        payload     = {"inputs": text}
        response    = requests.post(API_URL, headers = headers, json = payload)
        audio       = response.content

        # Create an Audio object to play the binary audio data
        return Audio(audio, rate = sampling_rate)
