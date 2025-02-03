import re

def is_valid_ipv4(ip):
    """
    Vérifie si l'adresse IP donnée est une IPv4 valide.

    Args:
        ip (str): L'adresse IPv4 à vérifier.

    Returns:
        bool: True si l'adresse est valide, False sinon.
    """
    pattern = re.compile(r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")
    if pattern.match(ip):
        return all(0 <= int(num) <= 255 for num in ip.split('.'))
    return False

def is_valid_ipv6(ip):
    """
    Vérifie si l'adresse IP donnée est une IPv6 valide.

    Args:
        ip (str): L'adresse IPv6 à vérifier.

    Returns:
        bool: True si l'adresse est valide, False sinon.
    """
    pattern = re.compile(r"^([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$")
    return bool(pattern.match(ip))

def detect_ip_version(ip):
    """
    Détecte si l'adresse IP est une IPv4 ou une IPv6 et renvoie la version.

    Args:
        ip (str): L'adresse IP à vérifier.

    Returns:
        str: "IPv4" si l'adresse est une IPv4, "IPv6" si l'adresse est une IPv6, "Invalid IP" sinon.
    """
    if is_valid_ipv4(ip):
        return "IPv4"
    elif is_valid_ipv6(ip):
        return "IPv6"
    else:
        return "Invalid IP"

def validate_ip_list(ip_list):
    """
    Valide une liste ou un dictionnaire d'adresses IP et renvoie leur version.

    Args:
        ip_list (list ou dict): Liste ou dictionnaire d'adresses IP à vérifier.

    Returns:
        dict: Dictionnaire avec les adresses IP et leur version.
    """
    if isinstance(ip_list, dict):
        return {host: detect_ip_version(ip) for host, ip in ip_list.items()}
    else:
        return {ip: detect_ip_version(ip) for ip in ip_list}

def validate_ip_dict(ip_dict):
    """
    Valide un dictionnaire d'adresses IP et renvoie leur version.

    Args:
        ip_dict (dict): Dictionnaire d'adresses IP à vérifier.

    Returns:
        dict: Dictionnaire avec les adresses IP et leur version.
    """
    return {host: detect_ip_version(ip) for host, ip in ip_dict.items()}

if __name__ == "__main__":
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
