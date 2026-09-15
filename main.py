

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


products = []
add_product(products)
add_product(products)
print(products)