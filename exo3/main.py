from api_utils import fetch_commune_data
from csv_utils import import_csv, modify_csv_data, save_csv, create_csv_if_not_exists
import os

if __name__ == "__main__":
    try:
        # Utilisation de l'API pour récupérer les données des communes
        postal_code = "31400"
        commune_data = fetch_commune_data(postal_code)
        print(f"Données des communes pour le code postal {postal_code}: {commune_data}")

        # Vérifier si le fichier CSV d'entrée existe, sinon le créer
        input_csv_path = "exo3/input.csv"
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
        output_csv_path = "exo3/output.csv"
        save_csv(modified_data, output_csv_path)
        print(f"Données sauvegardées dans le fichier: {output_csv_path}")

    except Exception as e:
        print(f"Une erreur est survenue: {e}")
