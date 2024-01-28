
'''
Created on 

@author: Raja CSP Raman

source:

    ?
'''


import streamlit as st
from dotenv import find_dotenv, load_dotenv


# Local
import custom
import util


# from transformers import AutoTokenizer, AutoModelForCausalLM

# st.title("Image to Audio Text Generation")

load_dotenv(find_dotenv())


# print(f'HUGGINGFACEHUB_API_TOKENS : {HUGGINGFACEHUB_API_TOKENS}')


# Get the image URL from the user
image_url = st.text_input("Enter the URL of the image:")
if st.button("Generate Text from Image"):

    image_caption   = util.img2text(image_url)

    st.text("Generated Text from Image:")
    st.write(image_caption)

    st.image(image_url, use_column_width = True)

    print(f'image_caption : {image_caption}')
    
    custom.get_story(image_caption, st)