from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
from product import Product
from supermarketLink import supermarkeNames, links

def getProductByEan(supermarketNames, links, ean):
    results = []
    for name in supermarketNames:
        data = links[name]
        linkByEan = urlopen(f'{data[0]}\/{ean}')
        try:
            bs = BeautifulSoup(linkByEan, 'html.parser')
        except HTTPError as e:
            return None
        else:        
            supermarket = name
            productName = bs.find(data[1][0], data[1][1]).get_text()
            productPrice = bs.find(data[2][0], data[2][1]).get_text()
            product = Product(supermarket, productName, productPrice)
            results.append(product)
    return results