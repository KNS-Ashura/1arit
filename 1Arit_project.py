class Algo1:
    def __init__ (self,keyright,keyleft,start_keyleft,start_keyright): #initialise les valeures necessaires
        self.__keyleft = keyleft
        self.__keyright = keyright
        self.__start_keyright = list(start_keyright)
        self.__start_keyleft = list(start_keyleft)
    
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

#chiffreur = Algo1(keyright=[], keyleft=[], start_keyleft="QWERTYUIOPASDFGHJKLZXCVBNM", start_keyright="MNBVCXZLKJHGFDSAPOIUYTREWQ")

#print(chiffreur.dechiffrer("QVCLPLBGUNKYLAOLSJJRONAODIZQAMKYGT"))
#print(chiffreur.chiffrer("MEET ME AT MIDNIGHT BY THE OLD CLOCK TOWER"))


class Algo2:
    def __init__ (self, n, offset):
        self.__n = n
        self.__offset = offset
        self.__error_msg = f"Erreur : l'offset doit être compris entre 0 et {2*self.__n - 3}"

    #vérification de l'offset pour quand on essaye avec un n et un offest différent du sujet
    def verif(self):
        if self.__offset < 0 and self.__offset > 2*self.__n - 3:
            return False
        return True
    def chiffrer(self,message):
        if self.verif() == False:
            return self.__erreur

        #préparation du message
        message = message.replace(" ", "").upper()

        #cycle de vague
        longueur_cycle = 2 * self.__n - 2

        #création des lignes
        lignes = []
        for i in range(self.__n):
            lignes.append([])

        #choix de la ligne de départ
        if self.__offset < self.__n:
            ligne_actuelle = self.__offset
            direction = 1 #descente
        else:
            ligne_actuelle = longueur_cycle - self.__offset
            direction = -1 #remontée

        #remplissage d'une ligne
        for i in range(len(message)):
            lignes[ligne_actuelle].append(message[i])

            #chagement de direction si on touche les bords
            if ligne_actuelle == 0:
                direction = 1
            elif ligne_actuelle == self.__n - 1:
                direction = -1
            
            ligne_actuelle += direction

        #collage des lignes
        message_chiffrer = []
        for i in range(len(lignes)):
            for j in range(len(lignes[i])):
                message_chiffrer.append(lignes[i][j])

        return ''.join(message_chiffrer)
        
chiffreur2 = Algo2(n=6, offset=4)
print(chiffreur2.chiffrer("DIDYOUEVERWAKEUPTOFINDADAYTHATBROKEUPYOURMIND"))