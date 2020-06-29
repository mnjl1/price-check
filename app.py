import sys
from getProduct import getProductByEan
from supermarketLink import supermarkeNames, links
from product import Product

def main():
    ean = sys.argv[1]
    products = getProductByEan(supermarkeNames, links, ean)
    
    for product in products:
        print(product.printProduct())
    
main()