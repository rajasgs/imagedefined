
'''
Created on 

@author: Raja CSP Raman

source:

    Salesforce blip image captioning base
    https://huggingface.co/Salesforce/blip-image-captioning-base
'''

def startpy():

    print("Tact101")
    

if __name__ == '__main__':
    startpy()

import streamlit as st
from dotenv import find_dotenv, load_dotenv
from transformers import pipeline

# Local
import custom


# from transformers import AutoTokenizer, AutoModelForCausalLM

# st.title("Image to Audio Text Generation")

load_dotenv(find_dotenv())


# print(f'HUGGINGFACEHUB_API_TOKENS : {HUGGINGFACEHUB_API_TOKENS}')

def img2text(url):
    
    image_to_text   = pipeline("image-to-text", model = "Salesforce/blip-image-captioning-base")
    text            = image_to_text(url)[0]['generated_text']
    st.text("Generated Text from Image:")
    st.write(text)

    st.image(url, use_column_width = True)
    return text

# Get the image URL from the user
image_url = st.text_input("Enter the URL of the image:")
if st.button("Generate Text from Image"):

    image_caption   = img2text(image_url)

    print(f'image_caption : {image_caption}')
    
    custom.get_story(image_caption, st)