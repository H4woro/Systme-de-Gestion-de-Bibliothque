from utils import *  # Importe les fonctions utilitaires pour charger et enregistrer des données
from tabulate import tabulate  # Importe la fonction tabulate pour afficher les données sous forme de tableau

emprunteurs = []  # Initialise une liste vide pour stocker les emprunteurs

def Ajouter_emp():
    # Charge les données des emprunteurs depuis le fichier JSON
    emprunteurs = charger_donnees("donnees_emprunteurs.json")

    # Saisie des informations sur l'emprunteur
    nom = input("\nEntrez le nom de l'emprunteur : ")
    numero_didentification = input("Entrez le numéro d'identification de l'emprunteur : ")
    contact = input("Entrez le contact de l'emprunteur : ")
    
    # Crée un dictionnaire pour le nouvel emprunteur
    nouvel_emprunteur = {
        "nom": nom,
        "numero_didentification": numero_didentification,
        "contact": contact,
    }
   
    # Vérifie si l'emprunteur est déjà dans la liste des emprunteurs
    for existing_emprunteur in  emprunteurs :
        if existing_emprunteur["nom"] == nouvel_emprunteur["nom"]:
            print("\nCet emprunteur est déjà sur la liste.")
            return
    
    print(f"\nL'emprunteur {nouvel_emprunteur['nom']} a été ajouté avec succès.")
    # Ajoute l'emprunteur à la liste des emprunteurs
    emprunteurs.append(nouvel_emprunteur)
    # Enregistre les données mises à jour dans le fichier JSON
    enregistrer_donnees(emprunteurs, "donnees_emprunteurs.json")

def supprimer_emp():    
    # Charge les données des emprunteurs depuis le fichier JSON
    emprunteurs = charger_donnees("donnees_emprunteurs.json")

    # Saisie du nom de l'emprunteur à supprimer
    choix = input("\nEntrez le nom de l'emprunteur que vous souhaitez supprimer :")
    
    emprunteur_trouve = False
    nouveaux_emprunteurs = []

    # Parcourt la liste des emprunteurs et supprime l'emprunteur trouvé avec le nom spécifié
    for emprunteur in emprunteurs:
        if emprunteur['nom'].lower() == choix.lower():
            emprunteur_trouve = True
            print(f"\nEmprunteur trouvé : '{emprunteur['nom']}'")
        else:
            nouveaux_emprunteurs.append(emprunteur)

    # Vérifie si l'emprunteur à supprimer a été trouvé
    if emprunteur_trouve:
        # Enregistre les données mises à jour dans le fichier JSON (sans l'emprunteur supprimé)
        enregistrer_donnees(nouveaux_emprunteurs, "donnees_emprunteurs.json")
        print(f"\nL'emprunteur '{choix}' a été supprimé.")
    else:
        print(f"\nL'emprunteur '{choix}' n'a pas été trouvé dans la liste.")

def modifier_emp():
    # Charge les données des emprunteurs depuis le fichier JSON
    emprunteurs = charger_donnees("donnees_emprunteurs.json")

    # Saisie du nom de l'emprunteur à modifier
    choix = input("\nSaisissez le nom de l'emprunteur dont vous souhaitez modifier les informations :")
    emprunteur_trouve = False

    # Modifie les informations de l'emprunteur spécifié s'il est trouvé
    for emprunteur in emprunteurs:
        if emprunteur["nom"].lower() == choix.lower():
            emprunteur_trouve = True
            print(f"\nModification de l'emprunteur '{choix}':")
            emprunteur["nom"] = input("Entrez le nouveau nom : ")
            emprunteur["numero_didentification"] = input("Entrez le nouveau numéro d'identification : ")
            emprunteur["contact"] = input("Entrez le nouveau contact : ")
            print("\nLes informations de l'emprunteur ont été modifiées avec succès.")
            break

    # Vérifie si l'emprunteur à modifier a été trouvé
    if not emprunteur_trouve:
        print(f"\nL'emprunteur '{choix}' n'a pas été trouvé.")
    
    # Enregistre les données mises à jour dans le fichier JSON
    enregistrer_donnees(emprunteurs, "donnees_emprunteurs.json")

def Afficher_emp_triés():
    # Affiche les options de tri disponibles
    print("\n1. Afficher la liste des emprunteurs par nom")
    print("2. Afficher une liste de emprunteurs par numéro d'identifications")

    # Saisie du choix de tri
    methode = input("\nEntrez votre choix (1-2) : ")

    # Charge les données des emprunteurs depuis le fichier JSON
    emprunteurs = charger_donnees("donnees_emprunteurs.json")

    if methode == "1":
        choix = "nom"
    elif methode == "2":
        choix = "numero_didentification"
    else:
        print("Choix invalide, veuillez réessayer.")
        return

    # Trie les emprunteurs en fonction de la méthode de tri choisie
    emprunteurs_tries = sorted(emprunteurs, key=lambda x: x[choix])

    # Affiche les emprunteurs triés sous forme de tableau
    print(f"\nEmprunteurs triés par {choix}:")
    table = []

    for emprunteur in emprunteurs_tries:
        table.append([emprunteur["nom"], emprunteur["numero_didentification"], emprunteur["contact"]])

    print(tabulate(table, headers=["Nom", "Numéro d'identification", "Contact"], tablefmt="fancy_grid"))

def Rechercher_emprunteurs() :
    print("\nla méthode de recherche :")
    print("1.recherche par nom")
    print("2.recherche par numéro d'identification")
    print("3.recherche par contact")
    print("4.Retour au menu emprunteurs")

    # Saisie de la méthode de recherche
    while True:
        méthode = input("entrez votre choix (1-3) :")
        if méthode == "1":
            méthode = "nom"
            break
        elif méthode == "2":
            méthode = "numero_didentification"
            break
        elif méthode == "3" :
            méthode = "contact"
            break
        elif méthode == "4":
            return
        else:
            print("\nChoix invalide, veuillez réessayer.")
    
    # Saisie de la valeur à rechercher
    choix = input(f"Entrez le {méthode} :")

    # Charge les données des emprunteurs depuis le fichier JSON
    emprunteurs = charger_donnees("donnees_emprunteurs.json")

    résultats = False
    tab = []
    for emprunteur in emprunteurs:
        if choix.lower() in str(emprunteur[méthode]).lower():
            tab.append([emprunteur["nom"], emprunteur["numero_didentification"], emprunteur["contact"]])
            résultats = True
        
            print(f"le {méthode} invalide")
    if résultats:
        print(f"\nEmprunteur trouvé :")
        print(tabulate(tab, headers=["Nom", "Numéro d'identification", "Contact"], tablefmt="fancy_grid"))
    else:
        print(f"\nAucun emprunteur trouvé pour {méthode}")