class Bibliotheque:
    
    # Constructeur
    def __init__(self,type,nombre,contenu):
        # definition des attributs
        self.type = type
        self.nombre = nombre
        self.contenu = contenu

    # Methodes
    def afficheContenu(self):
        print("Contenu de la bibliotheque : "+ str(self.contenu))
    
