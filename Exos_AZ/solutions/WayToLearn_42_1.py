# Définir la classe ProduitElectronique
class ProduitElectronique:
    # Iniatialiser l'ID, le nom et le prix du produit
    def __init__(self, produit_id, nom, prix):
        self.produit_id = produit_id  # ID du produit
        self.nom = nom  # Nom du produit
        self.prix = prix  # Prix du produit

    # Méthode pour appliquer une réduction au prix du produit
    def appliquer_remise(self, pourcentage_remise):
        # Calculer le montant de la remise
        montant_remise = self.prix * pourcentage_remise / 100
        # Soustraire le montant de la remise du prix initial
        self.prix -= montant_remise

    # Méthode de calcul du prix final après remise
    def get_prix_final(self):
        # Retourner le prix actuel qui peut avoir été réduit
        return self.prix

    # Méthode pour récupérer l'ID du produit
    def get_produit_id(self):
        return self.produit_id

    # Méthode pour récupérer le nom du produit
    def get_nom(self):
        return self.nom

    # Méthode pour récupérer le prix du produit
    def get_prix(self):
        return self.prix


# Définir la classe fille Refrigerateur qui hérite de ProduitElectronique
class Refrigerateur(ProduitElectronique):
    # Attribut supplémentaire pour la période de garantie
    def __init__(self, produit_id, nom, prix, periode_garantie):
        # Appeler le constructeur de la classe mère pour initialiser 
        # les attributs communs
        super().__init__(produit_id, nom, prix)
		# Période de garantie en mois
        self.periode_garantie = periode_garantie  

    # Méthode pour prolonger la période de garantie
    def prolonger_garantie(self, additional_months):
        # Ajouter les mois supplémentaires à la période de garantie 
        # actuelle
        self.periode_garantie += additional_months

    # Méthode pour récupérer la période de garantie
    def get_periode_garantie(self):
        return self.periode_garantie

    # Surcharger la méthode d'application de remise pour inclure un 
    # Smessage
    def appliquer_remise(self, pourcentage_remise):
        # Appeler la méthode de la classe mère pour appliquer la 
        # Sréduction
        super().appliquer_remise(pourcentage_remise)
        # Afficher un message indiquant que la réduction a été 
        # appliquée
        print("Remise appliquée au réfrigérateur:", self.get_nom())


# Code pour tester la classe ProduitElectronique
if __name__ == "__main__":
    # Créer un objet ProduitElectronique
    p = ProduitElectronique("P123", "Lave-vaisselle", 500.00)
    # Appliquer une réduction et afficher le prix final
    p.appliquer_remise(15)
    print("ID du produit:", p.get_produit_id())
    print("Nom:", p.get_nom())
    print("Prix après réduction:", p.get_prix_final(), "€")
    print()

    # Créer un objet Refrigerateur
    r = Refrigerateur("P789", "Réfrigérateur Samsung", 900.00, 12)
    # Appliquer une réduction et afficher le prix final
    r.appliquer_remise(15)
    print("ID du produit:", r.get_produit_id())
    print("Nom:", r.get_nom())
    print("Prix après réduction:", r.get_prix_final(), "€")
    # Afficher la période de garantie
    print("Période de garantie:", r.get_periode_garantie(), "mois")

    # Prolonger la période de garantie et afficher la nouvelle 
    # période
    r.prolonger_garantie(12)
    print("Période de garantie après prolongation:", r.get_periode_garantie(), "mois")
