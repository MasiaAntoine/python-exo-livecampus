from ip_validator import detect_ip_version, validate_ip_list
from file_utils import replace_letters_in_file, file_to_dict, create_file_if_not_exists
import os

if __name__ == "__main__":
    try:
        path_file = "exo2/file.txt"

        # Créer le fichier s'il n'existe pas
        create_file_if_not_exists(path_file)

        ip = input("Veuillez entrer une adresse IP: ")
        print(f"L'adresse IP {ip} est de type {detect_ip_version(ip)}")
        print("\n")

        # Exemple d'utilisation avec une liste
        ip_list = ["192.168.1.1", "2001:0db8:85a3:0000:0000:8a2e:0370:7334", "invalid_ip"]
        print(validate_ip_list(ip_list))
        print("\n")

        # Exemple d'utilisation avec un dictionnaire
        ip_dict = {"host1": "192.168.1.1", "host2": "2001:0db8:85a3:0000:0000:8a2e:0370:7334", "host3": "invalid_ip"}
        print(validate_ip_list(ip_dict))

        # Remplacer certaines lettres par "x" dans un fichier texte
        replace_letters_in_file(path_file, ["a", "e", "i", "o", "u"])

        # Stocker le contenu d'un fichier texte dans un dictionnaire et l'afficher
        file_dict = file_to_dict(path_file)
        for line_num, content in file_dict.items():
            print(f"Ligne numéro {line_num} : {len(content)} caractères → \"{content}\"")

    except Exception as e:
        print(f"Une erreur est survenue: {e}")
