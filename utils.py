import os
import json

script_dir = os.path.dirname(os.path.abspath(__file__))

def enregistrer_donnees(l, filename):
    # Construire le chemin d'accès complet au fichier
    data_file_path = os.path.join(script_dir, filename)
    # Enregistrer les données dans le fichier JSON
    with open(data_file_path, "w") as f:
        json.dump(l, f, indent=4)

def charger_donnees(filename):
    # Construire le chemin d'accès complet au fichier
    data_file_path = os.path.join(script_dir, filename)
    try:
        # Charger les données depuis le fichier JSON
        with open(data_file_path, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        # Retourner une liste vide si le fichier n'existe pas ou s'il est vide
        return []
 