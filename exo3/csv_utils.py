import csv
import os

def create_csv_if_not_exists(file_path, fieldnames):
    """
    Crée un fichier CSV avec des en-têtes s'il n'existe pas.

    Args:
        file_path (str): Le chemin du fichier CSV.
        fieldnames (list): Liste des noms de colonnes pour le fichier CSV.
    """
    if not os.path.exists(file_path):
        try:
            with open(file_path, mode='w', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
        except Exception as e:
            print(f"Erreur lors de la création du fichier CSV: {e}")

def import_csv(file_path):
    """
    Importe le contenu d'un fichier CSV.

    Args:
        file_path (str): Le chemin du fichier CSV.

    Returns:
        list: Liste de dictionnaires représentant les lignes du fichier CSV.
    """
    data = []
    try:
        with open(file_path, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                data.append(row)
    except Exception as e:
        print(f"Erreur lors de l'importation du fichier CSV: {e}")
    return data

def modify_csv_data(data):
    """
    Modifie le contenu des données CSV.

    Args:
        data (list): Liste de dictionnaires représentant les lignes du fichier CSV.

    Returns:
        list: Liste modifiée de dictionnaires.
    """
    # Exemple de modification: ajouter un champ "modified" à chaque ligne
    for row in data:
        row['modified'] = 'yes'
    return data

def save_csv(data, output_file_path):
    """
    Sauvegarde le contenu modifié dans un nouveau fichier CSV.

    Args:
        data (list): Liste de dictionnaires représentant les lignes du fichier CSV.
        output_file_path (str): Le chemin du fichier CSV de sortie.
    """
    if not data:
        print("Aucune donnée à sauvegarder.")
        return

    try:
        with open(output_file_path, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)
    except Exception as e:
        print(f"Erreur lors de la sauvegarde du fichier CSV: {e}")
