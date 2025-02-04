import os
import json
import csv

def file_to_dict(file_path):
    """
    Stocke le contenu d'un fichier texte dans un dictionnaire.

    Args:
        file_path (str): Le chemin du fichier texte.

    Returns:
        dict: Dictionnaire avec les numéros de ligne comme clés et le contenu des lignes comme valeurs.
    """
    file_dict = {}
    try:
        with open(file_path, 'r') as file:
            for i, line in enumerate(file, 1):
                file_dict[i] = line.strip()
    except Exception as e:
        print(f"Erreur lors de la lecture du fichier: {e}")
    return file_dict

def export_dict_to_json(data, output_file_path):
    """
    Exporte un dictionnaire dans un fichier JSON.

    Args:
        data (dict): Dictionnaire à exporter.
        output_file_path (str): Le chemin du fichier JSON de sortie.
    """
    if not data:
        print("Le dictionnaire est vide, rien à exporter.")
        return

    try:
        with open(output_file_path, 'w') as json_file:
            json.dump(data, json_file, indent=4)
    except Exception as e:
        print(f"Erreur lors de l'exportation du fichier JSON: {e}")

def export_dict_to_csv(data, output_file_path):
    """
    Exporte un dictionnaire dans un fichier CSV.

    Args:
        data (dict): Dictionnaire à exporter.
        output_file_path (str): Le chemin du fichier CSV de sortie.
    """
    if not data:
        print("Le dictionnaire est vide, rien à exporter.")
        return

    try:
        with open(output_file_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Line Number", "Content"])
            for line_num, content in data.items():
                writer.writerow([line_num, content])
    except Exception as e:
        print(f"Erreur lors de l'exportation du fichier CSV: {e}")
