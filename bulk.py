'''
Created on 

@author: Raja CSP Raman

source:

    Salesforce blip image captioning base
    https://huggingface.co/Salesforce/blip-image-captioning-base

    https://www.golinuxcloud.com/pandas-add-row-to-existing-dataframe/
'''

import pandas as pd
import time

# Local
import util

def append_row():

    df1 = pd.read_csv("images.csv")

    df = pd.read_csv("images1.csv")

    for index, row in df1.iterrows():
        image_url = row['image_url']

        c_text = util.img2text(image_url, index)

        new_row = {
            "image_url"     : image_url,
            "definition"    : c_text
        }

        df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)

        # print(df)

    df.to_csv('images1.csv', index = False)


def startpy():

    print("Tact101")

    start = time.time()
    append_row()
    end = time.time()
    time_taken = end - start
    print(f'time_taken : {time_taken}')

if __name__ == '__main__':
    startpy()