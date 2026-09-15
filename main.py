

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

def main():
    products = []
    choix = 0

    while choix != 7:
        print("\n===== PRODUCT MANAGER CLI =====")
        print("1. Ajouter un produit")
        print("2. Afficher les produits")
        print("3. Rechercher un produit")
        print("4. Modifier le stock")
        print("5. Supprimer un produit")
        print("6. Calculer la valeur du stock")
        print("7. Quitter")

        choix = int(input("Votre choix : "))

        match choix:
            case 1:
                if add_product(products)==True:
                    print("Produit ajouté avec succès !")
                else:
                    print("Produit non ajouté")
            case 2:
                display_products(products)
            case 3:
                produit = search_product(products, name)

                if produit != None:
                    print("Produit recherché :")
                    print(produit)
                else:
                    print("Produit introuvable")
            case 4:
                    name = input("Nom à chercher : ")

                    try:
                        stock = int(input("Stock : "))
                    except ValueError:
                        print("Stock invalide")
                        continue

                    if stock < 0:
                        print("Le stock ne peut pas être négatif.")
                        continue

                    resultat = update_stock(products, name, stock)

                    if resultat:
                        print("Produit modifié")
                    else:
                        print("Produit introuvable")
            case 5:
                name = input("Nom à supprimer : ")
                
                resultat = delete_product(products, name)
                
                if resultat:
                    print("Produit supprimé")
                else:
                    print("Produit introuvable")
            case 6:
                print("La valeur du stock est ", calculate_inventory_value(products))
            case 7:
                print("Au revoir !")
                break
            case _:
                print("Choix invalide")

main()