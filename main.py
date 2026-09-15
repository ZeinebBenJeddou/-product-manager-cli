

def add_product(products):
    nom=input("Nom : ")
    if nom.strip() == "":
        print("Nom invalide")
        return False
    try:

        prix=float(input("Prix : "))
        stock=int(input("Stock : "))
    except ValueError:
        print("Prix ou stock invalide") 
        return False
    if prix <= 0:
        print("Le prix doit être supérieur à 0.")
        return False

    if stock < 0:
        print("Le stock ne peut pas être négatif.")
        return False
    dictionnaire={
    "name": nom,
    "price": prix,
    "stock": stock
}
    products.append(dictionnaire)
    return True

def display_products(products):
    nb=0
    for product in products:
        print(nb+1,".", product["name"],"-", product["price"],"DT - Stock",product["stock"])
        nb=nb+1

def search_product(products,name):
    for p in products:
        if p["name"]==name:
            return p
    return None

def update_stock(products, name, new_stock):
    produit=search_product(products,name)
    if produit!=None:
        if new_stock>=0:
            produit["stock"]=new_stock
            return True
    return False

def delete_product(products, name):
    produit=search_product(products,name)
    if produit!=None:
        del products[products.index(produit)]
        return True

    return False

def calculate_inventory_value(products):
    val=0
    for p in products:
        val= val+(p["price"]*p["stock"])
    return val

products = [
]

add_product(products)

display_products(products)

print(calculate_inventory_value(products))