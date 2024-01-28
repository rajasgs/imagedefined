

'''
Created on 

@author: Raja CSP Raman

source:

    Salesforce blip image captioning base
    https://huggingface.co/Salesforce/blip-image-captioning-base
'''

from transformers import pipeline

def img2text(url):
    
    image_to_text   = pipeline("image-to-text", model = "Salesforce/blip-image-captioning-base")
    text            = image_to_text(url)[0]['generated_text']
    
    return text