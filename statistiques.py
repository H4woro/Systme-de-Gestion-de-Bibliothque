from utils import *
from tabulate import tabulate

def nbr_recherche(nom):
    # Charge les statistiques depuis le fichier JSON
    stat = charger_donnees("Statistiques.json")
    if nom in stat:
        # Incrémente le nombre de recherches pour le livre donné s'il est déjà présent dans les statistiques
        stat[nom]["nb_recherche"] += 1
    else:
        # Ajoute une nouvelle entrée pour le livre avec un nombre de recherches initial de 1 s'il n'est pas déjà présent
        stat[nom] = {"nb_recherche": 1}
    # Enregistre les statistiques mises à jour dans le fichier JSON
    enregistrer_donnees(stat, "Statistiques.json")

def Afficher_nbr_recherche():
    # Charge les statistiques depuis le fichier JSON
    stat = charger_donnees("Statistiques.json")
    tab = []
    # Trie les livres en fonction du nombre de recherches, du plus grand au plus petit
    livres_plus_recherche = sorted(stat.items(), key=lambda x: x[1]["nb_recherche"], reverse=True)

    # Formatte les données des livres pour les afficher dans un tableau
    i=0
    for livre, infos in livres_plus_recherche:
        i+=1
        tab.append([i,livre, infos["nb_recherche"]])

    # Affiche le tableau des livres triés par nombre de recherches
    print(tabulate(tab, headers=["Classement","Livre", "Nombre de recherches"], tablefmt="fancy_grid"))
