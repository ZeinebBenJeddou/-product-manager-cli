

def add_product(products):
    nom=input("Nom : ")
    prix=float(input("Prix : "))
    stock=int(input("Stock : "))
    dictionnaire={
    "name": nom,
    "price": prix,
    "stock": stock
}
    products.append(dictionnaire)

def display_products(products):
    nb=0
    for product in products:
        print(nb+1,".", product["name"],"-", product["price"],"DT - Stock",product["stock"])
        nb=nb+1
        



products = [
    {"name": "p1", "price": 520.2, "stock": 5},
    {"name": "p2", "price": 556, "stock": 4}
]
display_products(products)