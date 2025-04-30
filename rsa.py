import math

class Chiffreur:
    def __init__ (self,message,keyright,keyleft,start_keyleft,start_keyright): #initialise les valeures necessaires
        self.__message = list(message)
        self.__keyleft = keyleft
        self.__keyright = keyright
        self.__start_keyright = list(start_keyright)
        self.__start_keyleft = list(start_keyleft)

        
    #getteurs et setteurs
    
    def set_keyright(self,new_value):
        self.__keyright = new_value
    
    def get_keyright(self):
        return self.__keyright
        
    def set_keyleft(self,new_value):
        self.__keyleft = new_value
    
    def get_keyleft(self):
        return self.__keyleft
    
    def get_start_keyright(self):
        return self.__start_keyright
    
    def get_start_keyleft(self):
        return self.__start_keyleft
    
    def get_message(self):
        return self.__message
    
    #fonctions intermedieraires
    
    
    
    #fonctions de chiffrement et de déchiffrement
        
    def chiffrer(self):
        message_chiffrer = []
        self.__keyright = self.__start_keyright
        self.__keyleft = self.__start_keyleft
        for i in range(len(self.__message)):
            for j in range(len(self.__keyright)):
                if self.__keyright[j] == self.__message[i]:
                    
                    #modifications de keyleft :
                    
                    #récupérer l'index
                    index = j

                    message_chiffrer.append(self.__keyleft[index])
                    
                    #inverser la liste
                    dernier = self.__keyleft[index:]
                    reste = self.__keyleft[:index]
                    self.__keyleft = dernier + reste
                    
                    #enlever l'élément et le remmetre en 13ieme position
                    element = self.__keyleft.pop(1)
                    self.__keyleft.insert(13,element)
                    element = []

                    #modifications de keyright pour faire un autre tour de boucle :

                    #permutation circulaire
                    dernier = self.__keyright[index+1:]
                    reste = self.__keyright[:index]
                    self.__keyright = dernier + reste + [self.__keyright[index]]

                    #décallage des elements
                    element = self.__keyright.pop(2)
                    self.__keyright.insert(13,element)
                    element = []
                    break
                    
        return message_chiffrer
    
    def dechiffrer(self,message_chiffrer):
        message_chiffrer = list(message_chiffrer)
        message_dechiffrer = []
        self.__keyright = self.__start_keyright
        self.__keyleft = self.__start_keyleft
        for i in range(len(self.__message)):
            for j in range(len(self.__keyleft)):
                if self.__keyleft[j] == message_chiffrer[i]:
                    
                    #modifications de keyleft :
                    
                    #récupérer l'index
                    index = j

                    message_dechiffrer.append(self.__keyright[index])
                    
                    #inverser la liste
                    dernier = self.__keyleft[index:]
                    reste = self.__keyleft[:index]
                    self.__keyleft = dernier + reste
                    
                    #enlever l'élément et le remmetre en 13ieme position
                    element = self.__keyleft.pop(1)
                    self.__keyleft.insert(13,element)
                    element = []

                    #modifications de keyright pour faire un autre tour de boucle :

                    #permutation circulaire
                    dernier = self.__keyright[index+1:]
                    reste = self.__keyright[:index]
                    self.__keyright = dernier + reste + [self.__keyright[index]]

                    #décallage des elements
                    element = self.__keyright.pop(2)
                    self.__keyright.insert(13,element)
                    element = []
                    break
                    
        return message_dechiffrer
    

#création d'un objet pour utiliser la classe

chiffreur = Chiffreur("SWAY", #message
                      keyright=[],
                      keyleft=[],
                      start_keyleft="OAJTFYLQXCMPEDNVSBRUKHGWIZ", 
                      start_keyright="EWKFTYIQXUHPMABCNJRLDZSGVO")

print(chiffreur.dechiffrer("GOPJ"))
