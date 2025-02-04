from api_utils import fetch_commune_data
from csv_utils import import_csv, modify_csv_data, save_csv, create_csv_if_not_exists
from file_utils import file_to_dict, export_dict_to_json, export_dict_to_csv
import os

if __name__ == "__main__":
    try:
        # Utilisation de l'API pour récupérer les données des communes
        postal_code = "31400"
        commune_data = fetch_commune_data(postal_code)
        print(f"Données des communes pour le code postal {postal_code}: {commune_data}")

        # Vérifier si le fichier CSV d'entrée existe, sinon le créer
        input_csv_path = "exo3/resources/input.csv"
        if not os.path.exists(input_csv_path):
            fieldnames = ["nom", "code", "codeDepartement", "siren", "codeEpci", "codeRegion", "codesPostaux", "population"]
            create_csv_if_not_exists(input_csv_path, fieldnames)

        # Importer le fichier CSV
        csv_data = import_csv(input_csv_path)
        print(f"Données importées du fichier CSV: {csv_data}")

        # Ajouter les données de l'API au CSV
        for commune in commune_data:
            csv_data.append(commune)

        # Modifier les données CSV
        modified_data = modify_csv_data(csv_data)
        print(f"Données modifiées: {modified_data}")

        # Sauvegarder les données modifiées dans un nouveau fichier CSV
        output_csv_path = "exo3/resources/output.csv"
        save_csv(modified_data, output_csv_path)
        print(f"Données sauvegardées dans le fichier: {output_csv_path}")

        # Exporter le contenu d'un fichier texte dans un dictionnaire
        text_file_path = "exo3/resources/input.txt"
        file_dict = file_to_dict(text_file_path)
        print(f"Dictionnaire du fichier texte: {file_dict}")

        # Exporter le dictionnaire dans un fichier JSON
        json_output_path = "exo3/resources/output.json"
        export_dict_to_json(file_dict, json_output_path)
        print(f"Données exportées dans le fichier JSON: {json_output_path}")

        # Exporter le dictionnaire dans un fichier CSV
        csv_output_path = "exo3/resources/output_dict.csv"
        export_dict_to_csv(file_dict, csv_output_path)
        print(f"Données exportées dans le fichier CSV: {csv_output_path}")

        # Valider et exporter la liste des IP
        ip_dict = {"host1": "192.168.1.1", "host2": "2001:0db8:85a3:0000:0000:8a2e:0370:7334", "host3": "invalid_ip"}
        print(f"Validation des IPs: {ip_dict}")

        # Exporter les IP validées dans un fichier JSON
        json_ip_output_path = "exo3/resources/ip_dict.json"
        export_dict_to_json(ip_dict, json_ip_output_path)
        print(f"IPs validées exportées dans le fichier JSON: {json_ip_output_path}")

        # Exporter les IP validées dans un fichier CSV
        csv_ip_output_path = "exo3/resources/ip_dict.csv"
        export_dict_to_csv(ip_dict, csv_ip_output_path)
        print(f"IPs validées exportées dans le fichier CSV: {csv_ip_output_path}")

    except Exception as e:
        print(f"Une erreur est survenue: {e}")
