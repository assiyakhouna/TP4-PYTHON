
from abc import ABC, abstractmethod

class Paiement(ABC):

    def __init__(self, montant):
        if montant <= 0:
            raise ValueError("Le montant doit être positif")

        self._montant = montant

    @abstractmethod
    def payer(self):
        pass


class CarteBancaire(Paiement):

    def __init__(self, montant, numero, cvv):
        super().__init__(montant)

        if not numero.isdigit() or len(numero) != 16:
            raise ValueError("Numéro de carte invalide")

        if not cvv.isdigit() or len(cvv) != 3:
            raise ValueError("CVV invalide")

        self.numero = numero
        self.cvv = cvv

    def payer(self):
        return f"Paiement par Carte Bancaire de {self._montant} DH effectué avec succès."
carte = CarteBancaire(250, "1234567890123456", "123")

print(carte.payer())
carte = CarteBancaire(250, "1234567890123456", "123")
print(carte.payer())

class PayPal(Paiement):

    def __init__(self, montant, email, token):
        super().__init__(montant)

        if "@" not in email or "." not in email:
            raise ValueError("Adresse email invalide")

        if not token:
            raise ValueError("Token API obligatoire")

        self.email = email
        self.token = token

    def payer(self):
        return f"Paiement PayPal de {self._montant} DH effectué avec succès."
paypal = PayPal(300, "test@gmail.com", "TOKEN123")

print(paypal.payer())

class Crypto(Paiement):

    def __init__(self, montant, wallet_id, reseau):
        super().__init__(montant)

        if not wallet_id:
            raise ValueError("Identifiant du portefeuille obligatoire")

        reseaux_valides = ["BTC", "ETH", "BNB"]

        if reseau not in reseaux_valides:
            raise ValueError("Réseau crypto invalide")

        self.wallet_id = wallet_id
        self.reseau = reseau

    def payer(self):
        return f"Paiement Crypto de {self._montant} DH effectué avec succès via le réseau {self.reseau}."
crypto = Crypto(500, "WALLET123", "BTC")

print(crypto.payer())

def traiter_paiements(liste):
    for paiement in liste:
        confirmation = paiement.payer()
        print(confirmation)

paiements = [
    CarteBancaire(250, "1234567890123456", "123"),
    CarteBancaire(150, "9876543210987654", "456"),

    PayPal(300, "test1@gmail.com", "TOKEN123"),
    PayPal(200, "test2@gmail.com", "TOKEN456"),

    Crypto(500, "WALLET123", "BTC"),
    Crypto(700, "WALLET456", "ETH")
]

traiter_paiements(paiements)
