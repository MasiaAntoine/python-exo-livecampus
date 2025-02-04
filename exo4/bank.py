class _ClientIdentity:
    """
    Classe pour représenter l'identité d'un client.

    Attributs:
        name (str): Le nom du client.
        address (str): L'adresse du client.
        phone (str): Le numéro de téléphone du client.
    """
    def __init__(self, name, address, phone):
        self.name = name
        self.address = address
        self.phone = phone

class _BankAccount:
    """
    Classe pour représenter un compte en banque.

    Attributs:
        account_number (str): Le numéro de compte.
        balance (float): Le solde du compte.
    """
    def __init__(self, account_number, balance=0.0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        """
        Dépose un montant sur le compte.

        Args:
            amount (float): Le montant à déposer.
        """
        if amount > 0:
            self.balance += amount
            print(f"{amount} a été déposé. Nouveau solde: {self.balance}")
        else:
            print("Le montant doit être positif.")

    def withdraw(self, amount):
        """
        Retire un montant du compte.

        Args:
            amount (float): Le montant à retirer.
        """
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"{amount} a été retiré. Nouveau solde: {self.balance}")
        else:
            print("Montant invalide ou solde insuffisant.")

class PersonalBankAccount(_BankAccount, _ClientIdentity):
    """
    Classe pour la gestion d’un compte bancaire pour un particulier.

    Hérite de:
        _BankAccount: Pour les opérations bancaires.
        _ClientIdentity: Pour l'identité du client.
    """
    def __init__(self, name, address, phone, account_number, balance=0.0):
        _BankAccount.__init__(self, account_number, balance)
        _ClientIdentity.__init__(self, name, address, phone)

    def display_account_info(self):
        """
        Affiche les informations du compte et du client.
        """
        print(f"Nom: {self.name}")
        print(f"Adresse: {self.address}")
        print(f"Téléphone: {self.phone}")
        print(f"Numéro de compte: {self.account_number}")
        print(f"Solde: {self.balance}")
