'''
Created on 

@author: Raja CSP Raman

source:

    https://dev.to/cihankoseoglu_84/an-easy-way-to-scrape-public-domain-images-from-pixabay-5eeb

    https://pixabay.com/service/about/api/

    https://pixabay.com/api/docs/

    https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_csv.html
'''

import requests
import pandas as pd

# Local
import constants

API_KEY         = constants.PIXABAY_KEY
URL_ENDPOINT    = "https://pixabay.com/api/"
query           = "istanbul"
PER_PAGE        = 200

# location        = "boy standing"

PARAMS          = {'q': query, 'per_page': PER_PAGE, 'page': 1}
ENDPOINT        = URL_ENDPOINT + "?key=" + API_KEY

print(f'ENDPOINT : {ENDPOINT}')

def startpy():

    print("Tact101")

    url_links = []

    req = requests.get(url = ENDPOINT, params = PARAMS)
    data = req.json()

    # num_pages = (data["totalHits"] // PER_PAGE) + 1

    for image in data["hits"]:
        url_links.append(image["webformatURL"])

    # print(f'url_links : {url_links}')
        
    # df = pd.DataFrame(columns = ['image_url'])
    # df = df.append({
    #     'image_url': url_links
    #     }, 
    #     ignore_index = True
    # )
        
    df = pd.DataFrame({
        'image_url': url_links,
        # 'mask': ['red', 'purple'],
        # 'weapon': ['sai', 'bo staff']
    })

    # pd.to_csv(df)

    df.to_csv('images.csv', index = False)  


    # for page in range(2, num_pages + 1):
    #     time.sleep(3)
    #     PARAMS['page'] = page
    #     req = requests.get(url=ENDPOINT, params=PARAMS)
    #     data = req.json()
    #     for image in data["hits"]:
    #         url_links.append(image["webformatURL"])

if __name__ == '__main__':
    startpy()
