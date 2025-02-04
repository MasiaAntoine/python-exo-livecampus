from ip_validator import IPValidator
from bank import PersonalBankAccount

def main():
    # Simulation des fonctionnalités de validation d'IP
    validator = IPValidator()
    ip = input("Veuillez entrer une adresse IP: ")
    print(f"L'adresse IP {ip} est de type {validator.detect_ip_version(ip)}")
    print("\n")

    # Exemple d'utilisation avec une liste
    ip_list = ["192.168.1.1", "2001:0db8:85a3:0000:0000:8a2e:0370:7334", "invalid_ip"]
    print(validator.validate_ip_list(ip_list))
    print("\n")

    # Exemple d'utilisation avec un dictionnaire
    ip_dict = {"host1": "192.168.1.1", "host2": "2001:0db8:85a3:0000:0000:8a2e:0370:7334", "host3": "invalid_ip"}
    print(validator.validate_ip_list(ip_dict))
    print("\n")

    # Simulation des fonctionnalités de gestion de compte bancaire
    account = PersonalBankAccount(name="John Doe", address="123 Main St", phone="555-1234", account_number="123456789")
    account.display_account_info()
    account.deposit(1000)
    account.withdraw(500)
    account.display_account_info()

if __name__ == "__main__":
    main()
