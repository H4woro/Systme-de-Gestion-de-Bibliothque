from utils import *
from gestion_livres import *
from tabulate import tabulate
from statistiques import *


def Rechercher():
    # Affiche les options de recherche disponibles
    print("\nLa méthode de recherche :")
    print("1. Recherche par titre")
    print("2. Recherche par auteur")
    print("3. Recherche par année de publication")

    # Saisie du choix de méthode de recherche
    while True:
        méthode = input("Entrez votre choix (1-3) : ")
        if méthode in ["1", "2", "3"]:
            break
        else:
            print("\nChoix invalide, veuillez réessayer.")

    # Sélectionne le critère de recherche en fonction du choix
    choix = ["titre", "auteur", "annee_publication"][int(méthode) - 1]

    # Saisie de la valeur à rechercher
    choix2 = input(f"Entrez le {choix} du livre : ")

    # Charge les données des livres depuis le fichier JSON
    Livres = charger_donnees("donnees_livres.json")

    résultats = False
    tab = []
    # Parcourt les livres pour trouver ceux correspondant au critère de recherche
    for Livre in Livres:
        if choix2.lower() in str(Livre[choix]).lower():
            tab.append([Livre["titre"], Livre["auteur"], Livre["annee_publication"]])
            résultats = True

    # Affiche les résultats de la recherche sous forme de tableau
    if résultats:
        print("\nLivres trouvés :")
        print(tabulate(tab, headers=["Titre", "Auteur", "Année de publication"], tablefmt="fancy_grid"))
        # Compte le nombre de livres correspondants
        k = len(tab)
        print(f"Il y a {k} livres correspondants.")

        # Si plusieurs livres sont trouvés, demande à l'utilisateur de choisir un livre
        if k > 1:
            nom = input("\nEntrez le nom complet du livre que vous souhaitez emprunter : ")
            for livre in tab:
                if nom.lower() == livre[0].lower():  
                    # Vérifie si le nom entré correspond à l'un des titres dans la liste
                    nbr_recherche(nom)
                    print("Le livre a été ajouté")
                    break
            else:
                print("Erreur : Le nom du livre n'a pas été trouvé.")
        # Si un seul livre est trouvé, met à jour le nombre de recherches pour ce livre
        elif k == 1:
            nbr_recherche(tab[0][0])  
        else:
            print(f"\nAucun livre trouvé pour {choix}.")
            
def recherche_annee():
    tab = []
    print("Recherchez tous les livres publiés avant ou après l'année de votre choix.")
    print("1. Recherchez tous les livres publiés après l'année de votre choix.")
    print("2. Recherchez tous les livres publiés avant l'année de votre choix.")

    # Saisie du choix de recherche par année
    choix = input("\nEntrez votre choix (1-2) : ")

    while choix not in ("1", "2"):
        print("Choix invalide. Veuillez entrer 1 ou 2.")
        choix = input("\nEntrez votre choix (1-2) : ")

    # Sélectionne le critère de recherche en fonction du choix
    if choix == "1":
        k = 1
        print("Tous les livres publiés après l'année spécifiée.")
    elif choix == "2":
        k = 2
        print("Tous les livres publiés avant l'année spécifiée.")

    # Saisie de l'année à rechercher
    annee = input("Saisissez l'année : ")

    # Charge les données des livres depuis le fichier JSON
    Livres = charger_donnees("donnees_livres.json")

    # Parcourt les livres pour trouver ceux correspondant au critère de recherche
    for Livre in Livres:
        if (k == 1 and int(Livre["annee_publication"]) > int(annee)) or \
           (k == 2 and int(Livre["annee_publication"]) < int(annee)):
            tab.append([Livre["titre"], Livre["auteur"], Livre["annee_publication"]])

    # Affiche les résultats de la recherche sous forme de tableau
    print(tabulate(tab, headers=["Titre", "Auteur", "Année de publication"], tablefmt="fancy_grid"))
    # Compte le nombre de livres correspondants
    c = len(tab)
    titre_livre = Livre["titre"]
    nbr_recherche(titre_livre)
    print(f"Il y a {len(tab)} livres correspondants.")

    # Si plusieurs livres sont trouvés, demande à l'utilisateur de choisir un livre
    if c > 1:
        nom = input("\nEntrez le nom complet du livre que vous souhaitez emprunter : ")
        for livre in tab:
            if nom.lower() == livre[0].lower():  
                # Vérifie si le nom entré correspond à l'un des titres dans la liste
                nbr_recherche(nom)
                print("Le livre a été ajouté")
                break
        else:
            print("Erreur : Le nom du livre n'a pas été trouvé.")
    # Si un seul livre est trouvé, met à jour le nombre de recherches pour ce livre
    elif c == 1:
        nbr_recherche(tab[0][0])  
    else:
        print("Aucun livre trouvé.")
