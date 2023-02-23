from paramettres import *

class Player:
      '''
      Nom: Player

      Class qui permet de créer un joueur

      ...

      Attributs: name: nom du joueur
                 hand: liste avec les cartes en main du joueur
                 wallet: argent que possède la joueur
                 value: valeur du joueur

      Méthode: receive_card(self, card): Fonction qui ajoute a la main du joueur une carte "card"
               chance_to_win(self): Fonction qui calcule en % le chance qu'un joueur a de gagner
               trad_val(self, lst_value): Fonction qui traduit les figures en valeur
               hand_name(self, all_players, commune_cards): Fonction qui donne le nom de la main des joueurs
      '''

      def __init__(self, name: str) -> None:
            '''
            Fonction que permet de créer un joueur

            Paramètre: name: nom du joueur

            Attributs: self.name: nom du joueur
                       self.hand: liste avec les cartes en main du joueur
                       self.wallet: argent que possède la joueur
                       self.value: valeur du joueur
            '''
            self.name = name                          # Le nom du joueur et "name"
            self.hand = create_pile_or_file_empty()   # créé une liste vide qui correspond a la main du joueur
            self.hand_name_ = None                    # sera le nom de la main du joueur a la fin de la parti
            self.value_hand = None
            self.value_cards = create_pile_or_file_empty()
            self.wallet = 1000                        # Permet de définir l'argent que possède un joueur, au début de la partie chaque joueur a 1000€
            self.value = int()                        # Correspond a la valeur du joueur (permettra plus tard de trier les joueurs)

      def __str__(self) -> str: 
            '''
            Fonction qui renvoi le joueur sous forme de chaine de caractère
            '''
            return f"player : {self.name} \n hand : {self.hand} \n wallet : {self.wallet} €" # Renvoi le nom, la main, et l'argent du joueur
      
      def receive_card(self, card): 
            '''
            Nom: receive_card

            Fonction qui ajoute a la main du joueur une carte "card"

            Paramètre: card: carte du paquet
            '''
            assert lenght(self.hand) <= 2, "Le joueur a déjà reçu des cartes"       # Le joueur ne peut pas avoir plus de 2 cartes

            stack(self.hand, str(card))                                             # Ajoute a la pile "self.hand" une carte
      
      def trad_val(self, lst_value: list) -> list:
            '''
            Nom: trad_val

            Fonction qui traduit les figures en valeur numérique (en chaine de caractère)

            Paramètre: lst_value: Liste que parcoure le programme pour la traduire
            '''
            for i in range(lenght(lst_value)):                  # Boucle qui se répète le nombre de fois qu'il y a d'éléments dans la liste
                value = lst_value[i]                            # "value" prend la valeur de "lst_value" a la position "i"
                if value == "T":                                # Si "value" est un "T", on fait:
                    q = create_pile_or_file_empty()             # Créé une file vide nommé "q"
                    for _ in range(lenght(lst_value)-(i+1)):    # Boucle qui se répète la nombre de fois qu'il y a d'éléments dans "lst_value" moins le nombre "i"+1
                        # Ce qui permettra d'avoir au sommet de la file la valeur a enlever
                        stack(q, unstack(lst_value))            # Enlève une valeur de "lst_value" pour la mètre dans "q" momentanément
                    unstack(lst_value)                          # La valeur au sommet de "lst_value" est enlevé pour être remplacer par sa traduction
                    stack(lst_value, "10")                      # Empile a "lst_value" la traduction a la position de la valeur enlevé
                    while is_pile_or_file_empty(q) == False:    # Tant que la file "q" n'est pas vide:
                        stack(lst_value, unstack(q))            # On enlève les éléments de la file "q" pour les remettes dans "lst_value" dans le même ordre qu'au départ

                elif value == "J":                              # Si "value" est un "J", on fait:
                    q = create_pile_or_file_empty()             # Créé une file vide nommé "q"
                    for _ in range(lenght(lst_value)-(i+1)):    # Boucle qui se répète la nombre de fois qu'il y a d'éléments dans "lst_value" moins le nombre "i"+1
                        # Ce qui permettra d'avoir au sommet de la file la valeur a enlever
                        stack(q, unstack(lst_value))            # Enlève une valeur de "lst_value" pour la mètre dans "q" momentanément
                    unstack(lst_value)                          # La valeur au sommet de "lst_value" est enlevé pour être remplacer par sa traduction
                    stack(lst_value, "11")                      # Empile a "lst_value" la traduction a la position de la valeur enlevé
                    while is_pile_or_file_empty(q) == False:    # Tant que la file "q" n'est pas vide:
                        stack(lst_value, unstack(q))            # On enlève les éléments de la file "q" pour les remettes dans "lst_value" dans le même ordre qu'au départ

                elif value == "Q":                              # Si "value" est un "Q", on fait:
                    q = create_pile_or_file_empty()             # Créé une file vide nommé "q"
                    for _ in range(lenght(lst_value)-(i+1)):    # Boucle qui se répète la nombre de fois qu'il y a d'éléments dans "lst_value" moins le nombre "i"+1
                        # Ce qui permettra d'avoir au sommet de la file la valeur a enlever
                        stack(q, unstack(lst_value))            # Enlève une valeur de "lst_value" pour la mètre dans "q" momentanément
                    unstack(lst_value)                          # La valeur au sommet de "lst_value" est enlevé pour être remplacer par sa traduction
                    stack(lst_value, "12")                      # Empile a "lst_value" la traduction a la position de la valeur enlevé
                    while is_pile_or_file_empty(q) == False:    # Tant que la file "q" n'est pas vide:
                        stack(lst_value, unstack(q))            # On enlève les éléments de la file "q" pour les remettes dans "lst_value" dans le même ordre qu'au départ

                elif value == "K":                              # Si "value" est un "K", on fait:
                    q = create_pile_or_file_empty()             # Créé une file vide nommé "q"
                    for _ in range(lenght(lst_value)-(i+1)):    # Boucle qui se répète la nombre de fois qu'il y a d'éléments dans "lst_value" moins le nombre "i"+1
                        # Ce qui permettra d'avoir au sommet de la file la valeur a enlever
                        stack(q, unstack(lst_value))            # Enlève une valeur de "lst_value" pour la mètre dans "q" momentanément
                    unstack(lst_value)                          # La valeur au sommet de "lst_value" est enlevé pour être remplacer par sa traduction
                    stack(lst_value, "13")                      # Empile a "lst_value" la traduction a la position de la valeur enlevé
                    while is_pile_or_file_empty(q) == False:    # Tant que la file "q" n'est pas vide:
                        stack(lst_value, unstack(q))            # On enlève les éléments de la file "q" pour les remettes dans "lst_value" dans le même ordre qu'au départ

                elif value == "A":                              # Si "value" est un "A", on fait:
                    q = create_pile_or_file_empty()             # Créé une file vide nommé "q"
                    for _ in range(lenght(lst_value)-(i+1)):    # Boucle qui se répète la nombre de fois qu'il y a d'éléments dans "lst_value" moins le nombre "i"+1
                        # Ce qui permettra d'avoir au sommet de la file la valeur a enlever
                        stack(q, unstack(lst_value))            # Enlève une valeur de "lst_value" pour la mètre dans "q" momentanément
                    unstack(lst_value)                          # La valeur au sommet de "lst_value" est enlevé pour être remplacer par sa traduction
                    stack(lst_value, "14")                      # Empile a "lst_value" la traduction a la position de la valeur enlevé
                    while is_pile_or_file_empty(q) == False:    # Tant que la file "q" n'est pas vide:
                        stack(lst_value, unstack(q))            # On enlève les éléments de la file "q" pour les remettes dans "lst_value" dans le même ordre qu'au départ
                        
            return lst_value                                    # Renvoi la liste une fois traduite
      
      def hand_name(self, all_players: list, commune_cards: list) -> None:
            '''
            Nom: name_hand

            Fonction qui donne la nom de la main du joueur après révélation de toutes les cartes communes

            Paramètre: player: Le joueur dont on regardera la main

            Renvoi: le nom de la main
            '''
            for player in all_players:                                      # Boucle qui se répète le nombre de fois qu'il y a de joueurs actifs

                for card in commune_cards:                                  # Pour chaques cartes qu'il y a dans les cartes communes
                    stack(player.hand, card)                                # Empile a la main du joueur les carte communes
                cards = player.hand                                         # "cards" représente la main du joueur

                values = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]      # Liste de valeurs possible pour chaque cartes du paquet
                colors = ["♥️", "♦️", "♣️", "♠️"]                               # Liste des couleurs possible pour les cartes d'un paquet
                player.value_cards = create_pile_or_file_empty()            # Créé une pile vide pour trouver les valeurs des cartes du joueur
                cards_colors = []                                           # Créé une pile vide pour trouver les couleurs des cartes du joueur
                main = []                                                   # Représente le nom de la main du joueur

                for card in cards:                                          # Pour chaque cartes dans cards (main du joueur)
                    for value in values:                                    # Pour chaque valeurs dans la liste des valeurs
                        if value in card:                                   # Si la valeur est écrite dans la carte:
                            stack(player.value_cards, value)                # Enfile dans la pile des valeurs des cartes la valeur correspondant
                    for color in colors:                                    # Pour chaque couleurs dans la liste des couleurs
                        if color in card:                                   # Si la couleur est écrite dans la carte:
                            stack(cards_colors, color)                      # Enfile dans la pile des couleurs des cartes du joueur la couleur correspondant
                            
                player.trad_val(player.value_cards)                         # Traduit les valeurs des cartes du joueur, les figures devienne des valeurs numérique

                for value in player.value_cards:                            # Pour chaques valeur dans la pile des valeurs des cartes du joueur
                    if player.value_cards.count(value) == 2:                # Si parmi la pile des valeurs des cartes du joueur il y a 2 fois la même valeur:
                        stack(main, "paire")                                # Enfile a la main "paire"

                if main.count("paire") >= 4:                                # Si dans la main il y a 4 fois "paire":
                    main = create_pile_or_file_empty()                      # Vide la main
                    stack(main, "double paire")                             # Enfile a "main" "double paire"

                for value in player.value_cards:                            # Pour chaques valeur dans la pile des valeurs des cartes du joueur
                    if player.value_cards.count(value) == 3:                # Si parmi la pile des valeurs des cartes du joueur il y a 3 fois la même valeur:
                        stack(main, "brelan")                               # Enfile a la main "brelan"

                for value in player.value_cards:                            # Pour chaques valeur dans la pile des valeurs des cartes du joueur
                    if str(int(value)+1) in player.value_cards and str(int(value)+2) in player.value_cards and str(int(value)+3) in player.value_cards and str(int(value)+4) in player.value_cards:     # Si il y a dans la main 4 nombres (croissant) qui suivent "value" :
                        suite = create_pile_or_file_empty()                 # Créé une pile vide nommé "suite"
                        stack(main, "quinte")                               # Enfile dans la main "quinte"
                        for i in range(5):                                  # Boucle qui se répète 5 fois
                            stack(suite, str(int(value)+i))                 # Enfile a la pile "suite" les valeurs (sous forme de caractère) correspondant a la suite

                for color in cards_colors:                                  # Pour chaque couleurs dans la liste des couleurs des cartes du joueur
                    if cards_colors.count(color) >= 5:                      # Si il y a 5 fois ou plus la même couleur:
                        stack(main, "couleur")                              # Enfile a la main "couleur"
                        couleur = create_pile_or_file_empty()               # Créé une pile vide nommé "couleur"
                        for card in cards:                                  # Pour chaques cartes dans la main du joueur
                            if color in card:                               # Si la couleur est écrite dans la cartes
                                stack(couleur, card)                        # Enfile dans "couleur" "card"

                if main.count("paire") == 2 and main.count("brelan") == 3:  # Si dans la main il y a a écrit 2 fois paire et 3 fois "brelan":
                    main = create_pile_or_file_empty()                      # Vide la liste "main"
                    stack(main, "full")                                     # Enfile a "main" "full"

                for value in player.value_cards:                            # Pour chaques valeur dans la pile des valeurs des cartes du joueur
                    if player.value_cards.count(value) == 4:                # Si parmi la pile des valeurs des cartes du joueur il y a 3 fois la même valeur:
                        main = create_pile_or_file_empty()                  # Vide la liste "main"
                        stack(main, "carré")                                # Enfile a "main" "carré"

                if "quinte" in main and "couleur" in main:                  # Si dans la main il y a écrit "quinte" et "couleur"
                    verif = 0                                               # Représente le nombre de cartes dans la suite qui ont la même couleur
                    for num_color in couleur:                               # Pour chaque valeur des cartes présent da la liste des cartes formant une couleur
                        for val in suite:                                   # Pour chaque valeur dans la liste des cartes formant une suite(quinte)
                            if val in num_color:                            # Si la valeur de la carte, dans la suite, est écrite dans la valeur de la carte, dans la couleur
                                verif += 1                                  # Une carte en plus de la suite correspond a la carte de la couleur
                    if verif == 5:                                          # Si les 5 cartes de la suite ont la même couleur
                        main = create_pile_or_file_empty()                  # Vide la liste "main"
                        stack(main, "quinte flush")                         # Enfile a "main" "quinte flush"
                        
                if "quinte flush" in main:                                  # Si il y a "quinte flush" dans la main
                    if "A" in suite:                                        # Si il y a un As dans la quinte flush
                        main = create_pile_or_file_empty()                  # Vide la liste "main"
                        stack(main, "quinte flush royal")                   # Enfile a "main" "quinte flush royal"

                if main == []:                                              # Si la main est vide:
                    stack(main, "carte haute")                              # Enfile a "main" "carte haute"
                    
                player.hand_name_ = main[-1]                                # Le nom de la main est le dernier élément dans la liste "main"