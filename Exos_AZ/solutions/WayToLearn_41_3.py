# Définir la classe Vehicule
class Vehicule:  
    def __init__(self, marque, model, an):
        # Initialiser la marque du véhicule
        self.marque = marque
        # Initialiser le modèle du véhicule		
        self.model = model  
        # Initialiser l'année du véhicule
        self.an = an  

    # Méthode pour afficher les détails du véhicule
    def afficher_details(self):
        print("Les détails du véhicule:")
        print(f"Marque: {self.marque}")
        print(f"Modèle: {self.model}")
        print(f"Année: {self.an}")

    # Méthode Getter pour la marque du véhicule
    def get_marque(self):
        return self.marque

    # Méthode Getter pour le modèle du véhicule
    def get_model(self):
        return self.model

    # Méthode Getter pour l'année du véhicule
    def get_an(self):
        return self.an


# Définir la classe Voiture qui hérite de Vehicule
class Voiture(Vehicule):
    def __init__(self, marque, model, an, taille_coffre):
        # Appeler le constructeur de la classe mère
        super().__init__(marque, model, an)  
        # Initialiser la taille du coffre
        self.taille_coffre = taille_coffre  

    # Surcharger la méthode afficher_details pour inclure la taille 
    # du coffre
    def afficher_details(self):
        # Appeler la méthode de la classe mère
        super().afficher_details()  
        print(f"Taille du coffre: {self.taille_coffre} mètres cubes")

    # Méthode pour récupérer la taille du coffre
    def get_taille_coffre(self):
        return self.taille_coffre

    # Méthode pour définir la taille du coffre
    def set_taille_coffre(self, taille_coffre):
        if taille_coffre > 0:
            self.taille_coffre = taille_coffre
        else:
            print("La taille du coffre doit être positive.")


# Définir la classe Camion qui hérite de Vehicule
class Camion(Vehicule):
    def __init__(self, marque, model, an, capacit_charge):
        # Appeler le constructeur de la classe mère
        super().__init__(marque, model, an)  
        # Initialiser la capacité de charge
        self.capacit_charge = capacit_charge  

    # Surcharger la méthode afficher_details pour inclure la capacité 
    # de charge
    def afficher_details(self):
        # Appeler la méthode de la classe mère
        super().afficher_details()  
        print(f"Capacité de charge: {self.capacit_charge} tons")

    # Méthode pour récupérer la capacité de charge
    def get_capacit_charge(self):
        return self.capacit_charge

    # Méthode pour définir la capacité de charge
    def set_capacit_charge(self, capacit_charge):
        if capacit_charge > 0:
            self.capacit_charge = capacit_charge
        else:
            print("La capacité de charge doit être positive.")


# Définir la classe Main
if __name__ == "__main__":
    # Créer un objet Voiture
    v = Voiture("BMW", "Série 6", 2014, 16.15)
    v.afficher_details()  # Afficher les détails de la voiture

    # Créer un objet Camion
    c = Camion("Mercedes", "Arocs", 2024, 4.5)
    c.afficher_details()  # Afficher les détails du camion
