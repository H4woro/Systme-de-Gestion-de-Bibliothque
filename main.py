from gestion_livres import *
from gestion_emprunteurs import *
from recherche_avancee import *
from statistiques import *

def menu_principal():# Boucle principale du menu
    while True:
        print("\n==========Menu principal========== ")
        print("1. Menu des livres")
        print("2. Menu des emprunteurs")
        print("3. statistiques")
        choix = input("\nEntrez votre choix (1-3) :")

        if choix == "1":
            menu_livres()
        elif choix == "2":
            menu_emprunteurs()
        elif choix == "3":
            menu_statistiques()
        else:
            print("Choix invalide. Veuillez réessayer.")

def menu_livres():
    while True:
        print("\n==========Menu des livres========== ")
        print("1. Ajouter un livre")
        print("2. Supprimer un livre")
        print("3. Modifier un livre")
        print("4. Rechercher un livre")
        print("5. Afficher la liste des livres triés")
        print("6. Retour au menu principal")

        choix = input("\nEntrez votre choix (1-6) : ")

        if choix == "1":
            Ajouter()
        elif choix == "2":
            supprimer()
        elif choix == "3":
            modifier()
        elif choix == "4":
            menu_recherche()
        elif choix == "5":
            Afficher_triés()
        elif choix == "6":
            break
        else:
            print("Choix invalide. Veuillez réessayer.")

def menu_emprunteurs():
    while True:
        print("\n==========Menu des emprunteurs========== ")
        print("1. Ajouter un emprunteur")
        print("2. Supprimer un emprunteur")
        print("3. Modifier un emprunteur")
        print("4. Rechercher un emprunteur")
        print("5. Afficher la liste des emprunteurs triés")
        print("6. Retour au menu principal")

        choix = input("\nEntrez votre choix (1-6) : ")

        if choix == "1":
            Ajouter_emp()
        elif choix == "2":
            supprimer_emp()
        elif choix == "3":
            modifier_emp()
        elif choix == "4":
            Rechercher_emprunteurs()
        elif choix == "5":
            Afficher_emp_triés()
        elif choix == "6":
            break
        else:
            print("Choix invalide. Veuillez réessayer.")
def menu_statistiques():
    while True:
        print("\n==========Menu des statistiques========== ")
        print("1. Afficher la liste des livres les plus recherchés ")
        print("2. Retour au menu principal")
        

        choix = input("\nEntrez votre choix  : ")

        if choix == "1":
            Afficher_nbr_recherche()
        elif choix == "2":
            menu_principal()
        else:
            print("Choix invalide. Veuillez réessayer.")

def menu_recherche():
    print("\n==========Menu de recherche========== ")
    print("1. Recherche simple")
    print("2. Recherche avancée")
    print("3. Retour au menu précédent")

    choix = input("\nEntrez votre choix (1-3) : ")

    if choix == "1":
        Rechercher()
    elif choix == "2":
        recherche_annee()
    elif choix == "3":
        return
    else:
        print("Choix invalide. Veuillez réessayer.")


menu_principal() # Appel de la fonction principale pour démarrer le programme
