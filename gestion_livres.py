from utils import *  # Importe les fonctions utilitaires pour charger et enregistrer des données
from tabulate import tabulate  # Importe la fonction tabulate pour afficher les données sous forme de tableau


Livres = []  # Initialise une liste vide pour stocker les livres

def Ajouter():
    
    # Charge les données des livres depuis le fichier JSON
    Livres = charger_donnees("donnees_livres.json")

    # Saisie des informations sur le livre
    

    titre = input("\nEntrez le titre du livre : ")
    auteur = input("Entrez l'auteur du livre : ")
    while True:
        annee_publication = input("Entrez l'année de publication du livre : ")
        if annee_publication.isdigit():
            break
        else:
            print("L'année de publication doit être un nombre. Veuillez réessayer.")

    # Crée un dictionnaire pour le nouveau livre
    

    livre = {
        
        "titre": titre,
        "auteur": auteur,
        "annee_publication": annee_publication,
    }
    # Vérifie si le livre est déjà dans la liste des livres
    for  existing_book  in Livres :
        if existing_book["titre"] == livre["titre"]:
            print("\nCe livre est déjà sur la liste des livres")
            return
    
    print(f"\nLe livre '{livre['titre']}' a été ajouté avec succès")

    # Ajoute le livre à la liste des livres
    Livres.append(livre)

    # Enregistre les données mises à jour dans le fichier JSON
    enregistrer_donnees(Livres, "donnees_livres.json")

def supprimer():
    # Charge les données des livres depuis le fichier JSON
    Livres = charger_donnees("donnees_livres.json")

    # Saisie du nom du livre à supprimer
    choix = input("\nEntrez le nom du livre que vous souhaitez supprimer :")

    livre_trouve = False

    # Liste pour stocker les livres filtrés (ceux à conserver)
    livres_filtrés = []
    for livre in Livres:
        if livre['titre'].lower() == choix.lower():
            livre_trouve = True
            print(f"\nLivre trouvé : '{livre['titre']}'")
        else:
            livres_filtrés.append(livre)

    # Vérifie si le livre à supprimer a été trouvé
    if livre_trouve:
        # Enregistre les données mises à jour dans le fichier JSON (sans le livre supprimé)
        enregistrer_donnees(livres_filtrés, "donnees_livres.json")
        print(f"\nLe livre '{choix}' a été supprimé.")
    else:
        print(f"\nLe livre '{choix}' n'a pas été trouvé dans la liste des livres.")

def modifier():
    # Charge les données des livres depuis le fichier JSON
    Livres = charger_donnees("donnees_livres.json")

    # Saisie du nom du livre à modifier
    choix = input("\nSaisissez le nom du livre dont vous souhaitez modifier les informations :")
    livre_trouve = False
    for livre in Livres:
        if livre["titre"].lower() == choix.lower():
            livre_trouve = True
            print(f"\nModification du livre '{choix}':")
            # Modification des informations du livre spécifié
            livre["titre"] = input("Entrez le nouveau titre : ")
            livre["auteur"] = input("Entrez le nouvel auteur : ")
            while True:
                annee_publication = input("Entrez la nouvelle année de publication : ")
                if annee_publication.isdigit():
                    livre["annee_publication"] = annee_publication
                    break
                print("\nL'année de publication doit être un nombre. Veuillez réessayer.")
            print("\nLes informations du livre ont été modifiées avec succès")
            break
    # Vérifie si le livre à modifier a été trouvé
    if livre_trouve:
        # Enregistre les données mises à jour dans le fichier JSON
        enregistrer_donnees(Livres, "donnees_livres.json")
    else:
        print(f"\nLe livre '{choix}' n'a pas été trouvé.")

def Afficher_triés():
    # Affiche les options de tri disponibles
    print("\n1. Afficher la liste des livres par titre")
    print("2. Afficher une liste de livres par auteurs")
    print("3. Afficher une liste de livres par année de publication")

    # Saisie du choix de tri
    méthode = input("\nEntrez votre choix (1-3) : ")

    # Charge les données des livres depuis le fichier JSON
    Livres = charger_donnees("donnees_livres.json")

    while True:
        if méthode == "1":
            choix = "titre"
            break
        elif méthode == "2":
            choix = "auteur"
            break
        elif méthode == "3":
            choix = "annee_publication"
            break
        else:
            print("Choix invalide, veuillez réessayer.")
            return

    # Trie les livres en fonction de la méthode de tri choisie
    Livre_trie = sorted(Livres, key=lambda x: x[choix])
    if choix == "annee_publication":
        Livre_trie.reverse()

    # Affiche les livres triés sous forme de tableau
    print(f"\nLivres triés par {choix}:")
    table = []
    for livre in Livre_trie:
        table.append([livre["titre"], livre["auteur"], livre["annee_publication"]])

    print(tabulate(table, headers=["Titre", "Auteur", "Année de publication"], tablefmt="fancy_grid"))

