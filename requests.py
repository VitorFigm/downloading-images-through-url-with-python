import requests
import pandas as pd

table= pd.read_csv('datasets_363619_861634_20191226-items.csv')
path = 'imgs/{}.jpg'
for i in enumerate(table['image']):
    prod_asin = table['asin'][ i[0] ] #name of the img
    with open(path.format(prod_asin),'wb') as file:
        file.write( requests.get(i[1]).content  )  #saving file