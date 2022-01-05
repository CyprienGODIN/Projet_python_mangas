class Representation:  

    # Constructeur
    def __init__(self, nom, rang):
        # Attributs de la classe representation
        self.nom = nom
        self.rang = rang 
    
    # Methodes :
    def afficheRep(self):
        print ("Représentation : " + self.nom + "\n" + "Rang : " + self.rang)
        