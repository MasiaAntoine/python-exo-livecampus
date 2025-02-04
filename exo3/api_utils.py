try:
    import requests
except ImportError:
    import os
    os.system('pip install requests')
    import requests

def fetch_commune_data(postal_code):
    """
    Exécute une requête API GET pour récupérer les données des communes par code postal.

    Args:
        postal_code (str): Le code postal pour lequel récupérer les données.

    Returns:
        dict: Dictionnaire contenant les données des communes.
    """
    url = f"https://geo.api.gouv.fr/communes?codePostal={postal_code}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        print(f"Erreur HTTP: {http_err}")
    except Exception as err:
        print(f"Erreur: {err}")
    return {}
