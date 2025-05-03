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
                    
        return "".join(message_chiffrer)
    
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
                    
        return "". join(message_dechiffrer)
    

#création d'un objet pour utiliser la classe

#chiffreur = Algo1(keyright=[], keyleft=[], start_keyleft="QWERTYUIOPASDFGHJKLZXCVBNM", start_keyright="MNBVCXZLKJHGFDSAPOIUYTREWQ")

#print(chiffreur.dechiffrer("QVCLPLBGUNKYLAOLSJJRONAODIZQAMKYGT"))
#print(chiffreur.chiffrer("MEET ME AT MIDNIGHT BY THE OLD CLOCK TOWER"))


class Algo2:
    def __init__(self, n, offset):
        self.__n = n
        self.__offset = offset
        self.__error = f"Erreur : l'offset doit être compris entre 0 et {2*self.__n - 3}"


    #fonctions intermaidiaires

    def verif(self):
        if self.__offset < 0 or self.__offset > 2*self.__n - 3:
            return False
        return True
    
    def creer_tableau(self, i, j):
        tableau = []
        for ligne in range(i):
            tableau.append([0] * j)
        return tableau

    #fonction principales
    def vagues(self,tableau):
        for i in range(len(tableau)):
            for j in range(len(tableau[i])):
                if tableau[i][j] == 0 :
                    print(" ", end=" ")
                else :
                    print(tableau[i][j], end=" ")
            print("\n")
                    
                    
    def chiffrer(self, message):
        
        #mise en forme du message pour qu'il n'y ait pas d'espaces et que tout soit en majuscule 
        # + transformation en liste

        message = list(message)
        
        
        if self.verif() is False :
            return self.__error     
        
        tableau = self.creer_tableau(self.__n, len(message))
        
        if self.__offset < self.__n:
            ligne_actuelle = self.__offset
            direction = 1 #descente
        else:
            ligne_actuelle = 2 * self.__n - 2 - self.__offset
            direction = -1 #remontée
        
        #création du tableau
        for i in range(len(message)):
            tableau[ligne_actuelle][i] = message[i]
            if ligne_actuelle == 0:
                direction = 1
            if ligne_actuelle == self.__n - 1:
                direction = -1
            ligne_actuelle += direction
            
        #appelle de la fonction d'affichage
        self.vagues(tableau)
            
        #recuperation du message chiffrer en parcourant les lignes
        message_chiffrer = []
        for i in range(len(tableau)) :
            for j in range(len(tableau[i])):
                if tableau[i][j] != 0:
                    message_chiffrer.append(tableau[i][j])
        
        return "".join(message_chiffrer)
    
#/////////////////////////////////////////////////

   
    def dechiffrer(self, message_chiffre):
        
        #transformation en liste
        message_chiffre = list(message_chiffre)
        
        if self.verif() is False :
            return self.__error 
        
        #calcul de la longueur nécessaire pour le tableau
        #on doit déterminer combien de colonnes seraient nécessaires pour le message original
        
        positions = []
        longueur_colonne = 0
        
        if self.__offset < self.__n:
            ligne_actuelle = self.__offset
            direction = 1 #descente
        else:
            ligne_actuelle = 2 * self.__n - 2 - self.__offset
            direction = -1 #remontée
            
        #simulation du parcours pour déterminer les positions
        while longueur_colonne < len(message_chiffre):
            positions.append((ligne_actuelle, longueur_colonne))
            longueur_colonne += 1
            
            if ligne_actuelle == 0:
                direction = 1
            if ligne_actuelle == self.__n - 1:
                direction = -1
            ligne_actuelle += direction
        
        #création du tableau vide
        tableau = self.creer_tableau(self.__n, longueur_colonne)
        
        #remplissage du tableau avec le message chiffré
        indice_message = 0
        for i in range(len(tableau)):
            for j in range(len(tableau[i])):
                for position in positions:
                    if position == (i, j):
                        if indice_message < len(message_chiffre):
                            tableau[i][j] = message_chiffre[indice_message]
                            indice_message += 1
        
        #appelle de la fonction d'affichage
        self.vagues(tableau)
        
        #lecture du message original en suivant les colonnes
        message_original = []
        for j in range(len(tableau[0])):
            for i in range(len(tableau)):
                if tableau[i][j] != 0:
                    message_original.append(tableau[i][j])
        
        return "".join(message_original)
            
        

        
        
chiffreur2 = Algo2(n=7, offset=8)
#print(chiffreur2.chiffrer("DIDYOUEVERWAKEUPTOFINDADAYTHATBROKEUPYOURMIND"))
# on doit obtenir "ETTPUVPOYHUYOEUFAAEODYREIDTKUNDDWKNABORIIADRM"
print(chiffreur2.dechiffrer("HANHARYMTPTLAYNCIPSITTITNOWRIOEFHOAEALOWIDIIGTNOSATTNSDOATNSSOEGSHLEFTTAMTODAGGITHSGTIDYTGEETSSSTETMOILJINNWGSNIEEISNAISTKNUELIYSYENNAUAAEILGYLTMUGNMUOASOGRNBTENMGNSWFIRBAJIJMEIGHIOTR"))
# on doit obtenir "DIDYOUEVERWAKEUPTOFINDADAYTHATBROKEUPYOURMIND"
