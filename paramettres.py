def stack(tab: list, val: int or float or list) -> list:
      '''
      Nom: stack

      Fonction ajoutant au sommet de la pile une valeur "val" 

      Paramètres: tab: une pile 
                   val: une valeur

      Renvoi: la pile tab avec cette nouvelle valeur
      '''
      tab += [val]      # La valeur "val" est ajouter a la pile "tab" 

      return tab        # Renvoi la liste avec la nouvelle valeur au sommet de la pile

def unstack(tab: list) -> int or float or str:
      '''
      Nom: unstack

      Fonction qui enlève la valeur au sommet de la pile

      Paramètres: tab: une pile 

      Renvoi: cette pile avec la valeur au sommet de la pile en moins
      '''
      assert len(tab) > 0, "La fonction ne peut pas marcher si la liste est vide" 

      return tab.pop()        # Renvoi la liste avec la valeur au sommet de la liste en moins

def enfiler(tab: list, val: int or float or list) -> list: 
      '''
      Nom: enfiler

      Fonction qui ajoute une valeur "val" au début de la file

      Paramètres: tab: une pile
                   val: une valeur

      Renvoi: cette file avec la valeur ajouter a la file
      '''
      tab.insert(0, val)      # La valeur "val" est ajouter au début de la file "tab"

      return tab              # Renvoi la file "tab" avec la valeur "val" en plus
      
def defiler(tab: list) -> int or float or str: 
      '''
      Nom: défiler

      Fonction qui enlève a la droite de la file "tab" une valeur

      Paramètres: tab: une file 

      Renvoi: cette file avec la valeur a droite de la file en moins
      '''
      assert lenght(tab) > 0, "La fonction ne peut pas marcher si la liste est vide"

      return tab.pop() # Enlève la valeur

def lenght(tab: list) -> int: 
      '''
      Nom: lenght

      Fonction qui calcule la longueur d'une pile ou file sans utiliser len() 

      Paramètres: tab: une pile ou file

      Renvoi: la longueur de la pile/file
      '''
      q = create_pile_or_file_empty()                 # Cree une pile "q" vide qui permettra de déplacer la valeur de la pile/file "tab" puis de les remettre
      len = 0                                         # La valeur len est égale au nombre éléments de "tab" donc la longueur de "tab"
      while is_pile_or_file_empty(tab) == False:      # Tant que "tab" n'est pas vide on fait:
            stack(q, unstack(tab))                    # Ajoute a la pile "q" une valeur de "tab"
            len += 1                                  # la valeur len prend plus 1
      while is_pile_or_file_empty(q) == False:        # Tant que la pile "q" n'est pas vide on fait:
            stack(tab, unstack(q))                    # déplace les valeurs de "q" dans "tab" pour que "tab" reste inchangé

      return len                                      # Renvoi "tab" dans le même état qu'avant changement

def tri_selection(tab: list) -> list:  
      '''
      Nom: tri_selection

      Fonction de tri sélection qui permet de remettre les joueurs d'une liste dans le bon ordre selon leurs valeur 

      Paramètres: tab: une pile ou file

      Renvoi: la liste une fois trie
      '''
      for i in range(lenght(tab) -1, 0, -1):          # Boucle qui parcoure chaques élément de la liste 
            Imax = 0                                  # La valeur "Imax" est égale a la plus grande valeur de la liste, on commence avec "Imax" égale a 0
            for j in range(1, i+1):                   # Boucle permettant de comparer la première valeur de la liste avec les autre
                  if tab[j] > tab[Imax]:              # Si la valeur du joueur tab[j] est inferieur a la valeur du joueur tab[Imax]
                        Imax = j                      # Imax prend la valeur de j
            tab[Imax], tab[i] = tab[i], tab[Imax]     # Dans la liste on change les positions des joueur tab[j] et tab[Imax]

      return tab                                      # Renvoie la liste avec les joueurs dans le bon ordre, selon leurs valeur


def tri_selection_value(tab: list) -> list:  
      '''
      Nom: tri_selection

      Fonction de tri sélection qui permet de remettre les joueurs d'une liste dans le bon ordre selon leurs valeur 

      Paramètres: tab: une pile ou file

      Renvoi: la liste une fois trie
      '''
      for i in range(lenght(tab) -1, 0, -1):          # Boucle qui parcoure chaques élément de la liste 
            Imax = 0                                  # La valeur "Imax" est égale a la plus grande valeur de la liste, on commence avec "Imax" égale a 0
            for j in range(1, i+1):                   # Boucle permettant de comparer la première valeur de la liste avec les autre
                  if tab[j].value < tab[Imax].value:  # Si la valeur du joueur tab[j] est inferieur a la valeur du joueur tab[Imax]
                        Imax = j                      # Imax prend la valeur de j
            tab[Imax], tab[i] = tab[i], tab[Imax]     # Dans la liste on change les positions des joueur tab[j] et tab[Imax]

      return tab                                      # Renvoi la liste avec les joueurs dans le bon ordre, selon leurs valeur

def tri_selection_value_hand(tab: list) -> list: 
      '''
      Nom: tri_selection

      Fonction de tri sélection qui permet de remettre les joueurs d'une liste dans le bon ordre selon leurs valeur 

      Paramètres: tab: une pile ou file

      Renvoi: la liste une fois trie
      '''
      for i in range(lenght(tab) -1, 0, -1):          # Boucle qui parcoure chaques élément de la liste 
            Imax = 0                                  # La valeur "Imax" est égale a la plus grande valeur de la liste, on commence avec "Imax" égale a 0
            for j in range(1, i+1):                   # Boucle permettant de comparer la première valeur de la liste avec les autre
                  if tab[j].value_hand > tab[Imax].value_hand:  # Si la valeur du joueur tab[j] est inferieur a la valeur du joueur tab[Imax]
                        Imax = j                      # Imax prend la valeur de j
            tab[Imax], tab[i] = tab[i], tab[Imax]     # Dans la liste on change les positions des joueur tab[j] et tab[Imax]

      return tab                                      # Renvoi la liste avec les joueurs dans le bon ordre, selon leurs valeur

def create_pile_or_file_empty() -> list: 
      '''
      Nom: create_pile_or_file_empty

      Fonction qui créé une pile ou un file vide

      Renvoi: cette pile ou file vide
      '''
      return [] 

def is_pile_or_file_empty(tab: list) -> bool: 
      '''
      Nom: is_pile_or_file_empty

      Fonction qui permet de savoir si une pile ou une file est vide ou non 

      Paramètres: tab: une pile ou file

      Renvoi: True si elle est vide et False si non
      '''
      if tab == []:           # si la pile ou file "tab" est vide
            return True       # Renvoi True
      
      return False            # Si la pile n'est pas vide Renvoi False                                 