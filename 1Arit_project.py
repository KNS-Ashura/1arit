import math

class Chiffreur:
    def __init__ (self,keyright,keyleft,start_keyleft,start_keyright): #initialise les valeures necessaires
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
    
    def Keyleft_permutation(self,index):
        dernier = self.__keyleft[index:]
        reste = self.__keyleft[:index]
        self.__keyleft = dernier + reste
        
    def Keyright_permutation(self,index):
        dernier = self.__keyright[index+1:]
        reste = self.__keyright[:index]
        self.__keyright = dernier + reste + [self.__keyright[index]]
        
    def move_element(self,position,key):
        element = key.pop(position)
        key.insert(13,element)
        element = []
    
    #fonctions de chiffrement et de déchiffrement
        
    def chiffrer(self,message):
        message = list(message)
        message_chiffrer = []
        self.__keyright = self.__start_keyright
        self.__keyleft = self.__start_keyleft
        for i in range(len(message)):
            for j in range(len(self.__keyright)):
                if self.__keyright[j] == message[i]:
                    
                    #récupérer l'index
                    index = j
                    
                    #ajouter la lettre trouver au message chiffrer
                    message_chiffrer.append(self.__keyleft[index])
                                    
                    #modifications de keyleft :
                    
                    #permutation circulaire de keyleft
                    self.Keyleft_permutation(index)
                    
                    #enlever l'élément position 1 et le remmetre en 13ieme position
                    self.move_element(1,self.__keyleft)
                    
                    
                    #modifications de keyright :

                    #permutation circulaire de keyright
                    self.Keyright_permutation(index)

                    #enlever l'élément position 2 et le remmetre en 13ieme position
                    self.move_element(2,self.__keyright)
                    break
                    
        return message_chiffrer
    
    def dechiffrer(self,message_chiffrer):
        message_chiffrer = list(message_chiffrer)
        message_dechiffrer = []
        self.__keyright = self.__start_keyright
        self.__keyleft = self.__start_keyleft
        for i in range(len(message_chiffrer)):
            for j in range(len(self.__keyleft)):
                if self.__keyleft[j] == message_chiffrer[i]:
                    
                    #récupérer l'index
                    index = j
                    
                    #ajouter la lettre trouver au message dechiffrer
                    message_dechiffrer.append(self.__keyright[index])
                    
                    #modifications de keyleft :
                    
                    #permutation circulaire de keyleft
                    self.Keyleft_permutation(index)
                    
                    #enlever l'élément position 1 et le remmetre en 13ieme position
                    self.move_element(1,self.__keyleft)
                    
                    #modifications de keyright :

                    #permutation circulaire de keyright
                    self.Keyright_permutation(index)

                    #enlever l'élément position 2 et le remmetre en 13ieme position
                    self.move_element(2,self.__keyright)
                    break
                    
        return message_dechiffrer
    

#création d'un objet pour utiliser la classe

chiffreur = Chiffreur(keyright=[],
                      keyleft=[],
                      start_keyleft="OAJTFYLQXCMPEDNVSBRUKHGWIZ", 
                      start_keyright="EWKFTYIQXUHPMABCNJRLDZSGVO")

print(chiffreur.dechiffrer("GOPJ"))
print(chiffreur.chiffrer("SWAY"))
