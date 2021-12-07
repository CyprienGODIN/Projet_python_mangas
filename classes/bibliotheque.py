import itertools

# Création de la classe Bibliotheque qui contient une liste de manga ainsi que des actions à effectuer dessus
class Bibliotheque:
    newid = itertools.count().next
    # Initialisation des variables de la classe
    def __init__(self, id=int, proprietaire="", date_creation="", liste_manga=dict()):
        self.id = Bibliotheque.newid()   
        self.proprietaire = proprietaire 
        self.date_creation = date_creation
        self.liste_manga = liste_manga

    # Représentaion d'une bibliothèque
    def __repr__(self) -> str:
        return f"Id : {self.id}\tPropriétaire : {self.proprietaire}\tDate de création : {self.date_creation}\tListe des mangas : {self.liste_manga}\t"
