class Product():

    def __init__(self, supermarket, productName, productPrice):
        self.supermarket = supermarket
        self.productName = productName
        self.productPrice = productPrice

    def printProduct(self):
        print(self.supermarket)
        print(self.productName)
        print(self.productPrice)