from ip_validator import detect_ip_version, validate_ip_list

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
