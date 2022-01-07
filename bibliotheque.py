import itertools

class Bibliotheque:
    # Iteration de l'id des bibliotheques
    newid = itertools.count().next

    # Constructeur
    def __init__(self,id=int,type="",nombre=int,contenu=dict()):
        # definition des attributs
        self.id = Bibliotheque.newid()
        self.type = type
        self.nombre = nombre
        self.contenu = contenu

    # Methodes
    def afficheContenu(self):
        print("Contenu de la bibliotheque : "+ str(self.contenu))
    
