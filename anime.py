from representation import Representation

# Classe Anime étendue de representation
class Anime(Representation): 
    
    # Constructeur
    def __init__(self, id, nom, rang, date_debut, date_fin, episodes, score):
        # Appel au constructeur de la classe mère ( Representation )
        # pour attribuer la valeur 'nom' et 'rang' de la classe mère.
        super().__init__(nom)
        super().__init__(rang)

        self.id = id 
        self.date_debut = date_debut
        self.date_fin = date_fin
        self.episodes = episodes
        self.score = score
    
    # Méthodes 
    # Remplace de la classe mère
    def afficheRep(self):
        print ("Nom du Manga : " + str(self.nom))
        print ("Rang : " + str(self.rang))
        print ("Score : " + str(self.score))
        print ("Date de debut : " + str(self.date_debut))
        print ("Date de fin : " + str(self.date_fin))
        print ("Episodes : " + str(self.episodes))
        