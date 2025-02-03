import fileinput
import os

def create_file_if_not_exists(file_path):
    """
    Crée le fichier s'il n'existe pas.

    Args:
        file_path (str): Le chemin du fichier texte.
    """
    if not os.path.exists(file_path):
        try:
            with open(file_path, 'w') as file:
                file.write("Ceci est un exemple de contenu.\nUne autre ligne de texte.")
        except Exception as e:
            print(f"Erreur lors de la création du fichier: {e}")

def replace_letters_in_file(file_path, letters):
    """
    Remplace certaines lettres par "x" dans un fichier texte.

    Args:
        file_path (str): Le chemin du fichier texte.
        letters (list): Liste des lettres à remplacer par "x".
    """
    try:
        for line in fileinput.input(file_path, inplace=True):
            for letter in letters:
                line = line.replace(letter, 'x')
            print(line, end='')
    except Exception as e:
        print(f"Erreur lors du traitement du fichier: {e}")

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
