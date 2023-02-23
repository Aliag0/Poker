import os
from random import *
from player import *

class Game:
      '''
      Nom: Game

      Class qui permet de jouer au poker

      ...

      Attributs: players: pile de joueurs actif
                 sleeping_players: pile de joueurs inactif
                 jar: pot a remporter par le vainqueur  

      Méthodes: start(self): fonction qui permet de recommencer une partie sans problèmes
                next(self): fonction qui permet aux joueurs de faire leur choix pour la suite de la partie
                mise(self, mise): fonction qui permet ajouter la mise au pot
                crea_players(self): fonction qui créer les joueurs
                distribution(self, pack): fonction qui permet de distribuer les cartes au joueurs actif
                show_players(self): fonction qui montre les joueurs actif avec leur nom, main et argent
                value_hand(self): Fonction qui permet de déterminer la valeur de la main des joueur selon leur main
                find_winner(self): Fonction qui permet de savoir quel joueur est le vainqueur
                winner(self, winner): fonction qui défini le gagnant d'une partie
                loser(self): fonction qui défini les perdants
                clean(self): fonction qui efface la console
      '''

      def __init__(self): 
            '''
            Fonction qui construit les attributs: self.players: pile de joueurs actif
                                                  self.sleeping_players: pile de joueur inactif
                                                  self.jar: pot à remporter par le vainqueur
            '''
            self.players = create_pile_or_file_empty()            # Pile de joueurs actif
            self.sleeping_players = create_pile_or_file_empty()   # Pile de joueur qui ne sont plus actif (coucher ou perdu tout leur argents)
            self.jar = 0                                          # Pot de la partie, la valeur final de "jar" sera remporter par un joueur

      def start(self, A: bool) -> list: 
            '''
            Nom: start

            Fonction qui permet de recommencer une partie sans problèmes
            '''
            if A == True:                                               # "A" permet d'eviter l'utilisation de cette fonction au debut de la partie
                  self.jar = 0                                          # Remet le pot a 0 €
                  with_money = create_pile_or_file_empty()              # Créé une liste vide nommé 'with_money
                  for player in self.sleeping_players:                  # Pour chaque joueurs inactif
                        if player.wallet != 0:                          # Si le joueur a de l'argent
                              stack(with_money, player)                 # Ajoute a la pile de jouer actif le joueur a la position correcte selon sa valeur
                              # Si ce joueur n'a pas d'argent alors il n'est pas remis dans la liste des joueurs actifs
                  for player in with_money:                             # Boucle qui se repete pour chaque joueur qu'il y a dans la liste "with_money"
                        enfiler(self.players, player)                   # Comme le joueur a encor de l'argent il retourne dans la pile des joueurs actifs
                  with_money = create_pile_or_file_empty()              # On vide cette liste 
                  self.sleeping_players = create_pile_or_file_empty()   # On vide cette liste 
                  tri_selection_value(self.players)                     # Tri, dans l'ordre croissant, les joueurs actifs selon leurs valeurs
            return self.players                                         # renvoit la pile des joueurs actifs, avec seulement les oueurs pouvant encore jouer

      def next(self): 
            '''
            Nom: next

            Fonction qui permet aux joueurs de faire leur choix pour la suite de la partie
            '''
            players_mise = create_pile_or_file_empty()      # Pile de joueurs qui ont décider de miser
            players_check = create_pile_or_file_empty()     # Pile de joueurs qui ont décider de ne rien faire
            mise_statut = "OFF"                             # Permet de savoir si une mise a été faite ou non
            Mise = 0                                        # Represente la somme de la mise
            nb_players = len(self.players)                  # Represente le nombre de joueur 

            while is_pile_or_file_empty(self.players) == False:                     # Tant que la pile des joueurs actif n'est pas vide on fait:

                  assert lenght(self.players) > 0, "Aucuns joueurs dans la partie"  # Il doit y avoir minimum un joueur parmi les joueurs actif
            
                  if "Bot" in self.players[-1].name:                                # Si le mode de jeu est "solo", alors il y a des bot, si le joueur est un bot on fait:
                        if Mise == 0:                                               # Si aucunes mise n'est faite, on fait:
                              if lenght(self.sleeping_players) == nb_players-1:     # Si il reste un seul Bot ce Bot n'a que le choix de :
                                    for_after = "check"                             # Faire "check"
                              else:                                                 # Si il reste 2 joueurs ou plus
                                    choice_list = ["sleep", "check", "mise"]        # "choice_list" est la liste des choix possible pour les bots
                                    weights = [0.15, 0.425, 0.425]                  # "weights" represente pour chaque choix possible la chance de l'obtenire
                                    for_after = choices(choice_list, weights=weights, k=1)[0] # "for_after" represente le choix fait par le Bot
                              if for_after == "mise":                               # Si le choix est de miser    
                                    Mise = randint(1, self.players[-1].wallet//4)   # "mise" est un nombre aléatoire compris entre 1 et le total d'argent du bot divisé par 4
                                    for_after = Mise
                        elif Mise != 0:                                             # Si une mise a été faite, on fait:
                              if Mise > self.players[-1].wallet:                    # Si la mise faite est supereieure au porte-feuille du joueur alors:
                                    for_after = "sleep"                             # Le Bot ce couche 
                              else:                                                 # Sinon le bot peut miser aussi 
                                    choice_list = ["sleep", "follow"]               # "choice_list" est la liste des choix possible pour les bots
                                    weights = [0.35, 0.65]                          # "weights" represente pour chaque choix possible la chance de l'obtenire
                                    for_after = choices(choice_list, weights=weights, k=1)[0] # "for_after" est le choix du bot est fait aléatoirement parmi la liste "choice_list"
                        print(f"{self.players[-1].name} : {for_after}")             # Ecrit le nom du bot avec son choix

                  else:                                                             # Si le joueur n'est pas un bot, alors on fait:
                        for_after = str(input(f"{self.players[-1].name} : "))       # "for_after" est le choix du joueur pour ce tour
                        if for_after == "sleep" or for_after == "" or for_after == "check": # Si le choix est "sleep" ou "check", alors;
                              Mise = 0                                              # La mise n'a donc pas ete faite, elle est egale a 0

                  if for_after == "sleep":                                          # Si le choix est est "sleep"
                        stack(self.sleeping_players, unstack(self.players))         # Empile a la pile "self.sleeping_players" le joueur, qui est donc enlève de la pile des joueurs actif

                  elif for_after == "check" or for_after == "":                     # Si le choix est de ne rien faire
                        enfiler(players_check, unstack(self.players))               # Empile a la pile "players_check" le joueur, qui est donc enlève de la pile des joueurs actif

                  elif for_after == "follow":                                       # Si le choix est de suivre une mise
                        assert Mise > 0, "Impossible de suivre si aucune mise n'a été faite"
                        assert Mise <= self.players[-1].wallet, f"Somme mise plus été la somme que possède le joueur {self.players[-1].name}"
                        self.players[-1].wallet -= Mise                             # Enlève a la somme d'argent du joueur la somme miser par le joueur précédant
                        Game.mise(self, Mise)                                       # Ajoute au pot la somme miser
                        enfiler(players_mise, unstack(self.players))                # Ajoute a la pile "players_mise" le joueur, qui est donc enlève de la pile des joueurs actif

                  else:                                                             # Si le choix est une valeur int() donc une mise
                        Mise = int(for_after)                                       # "Mise" prend la valeur du choix en int()
                        assert Mise <= self.players[-1].wallet, f"Somme mise plus élever la somme que possède le joueur {self.players[-1].name}"
                        self.players[-1].wallet -= Mise                             # Enlève a la somme d'argent du joueur la somme miser
                        mise_statut = "ON"                                          # Une mise a ete faite alors "mise_statut" égale "ON"
                        Game.mise(self, Mise)                                       # Ajoute au pot la somme miser
                        enfiler(players_mise, unstack(self.players))                # Ajoute a la pile "players_mise" le joueur, qui est donc enlever de la pile des joueurs actif
      

            if mise_statut == "ON":                                                 # Si une mise a ete faite, alors:
                  for _ in range(lenght(players_check)):                            # Pour chaque joueur dans le pile "players_check"
                        enfiler(self.players, unstack(players_check))               # On les empile dans la liste de joueurs actifs
                  while is_pile_or_file_empty(self.players) == False:               # Tant que la pile des joueurs actif n'est pas vide on fait:

                        assert lenght(self.players) > 0, "Aucuns joueurs dans la partie"  # Il doit y avoir minimum un joueur parmi les joueurs actif


                        if "Bot" in self.players[-1].name:                          # Si le mode de jeu est "solo", alors il y a des bot, si le joueur est un bot on fait:
                              if Mise > self.players[-1].wallet:                    # Si la mise faite est plus elevé que le somme du porte-feuille du joueur, alors:
                                    for_after = "sleep"                             # Le Bot n'a que le choix de se coucher
                              else:                                                 # Si le joueur a assez d'argent, alors:
                                    choice_list = ["sleep", "follow"]               # "choice_list" est la liste des choix possible pour les bots
                                    weights = [0.35, 0.65]                          # "weights" represente pour chaque choix possible la chance de l'obtenire
                                    for_after = choices(choice_list, weights=weights, k=1)[0] # "for_after" est le choix du bot est fait aléatoirement parmi la liste "choice_list"
                              print(f"{self.players[-1].name} : {for_after}")       # Ecrit le nom du bot avec son choix

                        else:                                                       # Si le joueur n'est pas un bot, alors on fait:
                              for_after = str(input(f"{self.players[-1].name} : ")) # "for_after" est le choix du joueur pour ce tour

                        if for_after == "sleep":                                    # Si le choix est est "sleep"
                              stack(self.sleeping_players, unstack(self.players))   # Empile a la pile "self.sleeping_players" le joueur, qui est donc enlève de la pile des joueurs actif

                        elif for_after == "check" or for_after == "":               # Si le choix est de ne rien faire
                              enfiler(players_check, unstack(self.players))         # Empile a la pile "players_check" le joueur, qui est donc enlève de la pile des joueurs actif

                        elif for_after == "follow":                                 # Si le choix est de suivre une mise
                              assert Mise > 0, "Impossible de suivre si aucune mise n'a été faite"
                              assert Mise <= self.players[-1].wallet, f"Somme mise plus été la somme que possède le joueur {self.players[-1].name}"
                              self.players[-1].wallet -= Mise                       # Enlève a la somme d'argent du joueur la somme miser par le joueur précédant
                              Game.mise(self, Mise)                                 # Ajoute au pot la somme miser
                              enfiler(players_mise, unstack(self.players))          # Ajoute a la pile "players_mise" le joueur, qui est donc enlève de la pile des joueurs actif

            other_players = create_pile_or_file_empty()           # Créer une file vide "other_players" 
            for _ in range(lenght(players_check)):                # Pour chaque joueurs dans la pile "players_check"
                  enfiler(other_players, defiler(players_check))  # Enfile a la file "other_players" le joueur "players" qui est enlève de la pile players_check
                  # si la pile est vide rien ne se passe

            for _ in range(lenght(players_mise)):                 # Pour chaque joueurs dans la pile "players_mise"
                  enfiler(other_players, defiler(players_mise))   # Enfile a la file "other_players" le joueur "players" qui est enlève de la pile players_mise
                  # si la pile est vide rien ne se passe

            for _ in range(lenght(other_players)):                # Pour chaque joueurs dans la file "other_players"
                  stack(self.players, defiler(other_players))     # Remet dans la pile "self.players" l'élément défiler de la file "other_players"
            tri_selection_value(self.players)                     # Remet les joueurs dans le bon ordre de passage selon leurs valeurs
                  # les joueurs dans la pile "self.players" sont dans l'ordre d'enregistrement au début
      
      def mise(self, mise: int) -> int: 
            '''
            Nom: mise

            Fonction qui permet ajouter la mise au pot

            Paramètre: mise: somme miser par un joueur
            '''
            assert self.jar >= 0, "jar négatif impossible"
            self.jar += int(mise)  # Est ajouter a la valeur self.jar (le pot) la mise faite
            return self.jar

      def crea_players(self, choice: str) -> None:
            '''
            Nom: crea_players

            Fonction qui créé les joueurs
            '''
            if choice == "multiplayers":                                      # Si le choix est de jouer en multijoueur local alors:
                  nb_players = int(input("How many players are there ? "))    # "nb_players" est le nombre de joueurs qui vont s'enregistrer

                  assert nb_players >= 2, "Nombres de joueurs dans la partie trop bas."
                  assert nb_players <= 10, "Nombres de joueurs dans la partie trop élevé."

                  for i in range(nb_players):                                 # Boucle se répétant le nombre de fois qu'il y a de joueurs
                        name = str(input(f"name player {i+1}: "))             # Demande le nom du joueur
                        player = Player(name)                                 # Cree un joueur avec pour nom "name"
                        player.value = i                                      # La valeur du joueur est égale a "i" 
                        stack(self.players, player)                           # Empile a la pile "self.players" le joueur "player"
                  tri_selection_value(self.players)
                        
            elif choice == "solo":                                            # Si le choix est de jouer en solo alors:
                  name = str(input("Name player : "))                         # Demande le nom du joueur
                  player = Player(name)                                       # Cree le joueur avec le nom "name"
                  player.value = 0                                            # La valeur du joueur est 0
                  stack(self.players, player)                                 # Empile a la pile "self.players" le joueur
                  nb_bots = int(input("How many bots do you want ? "))        # Demande contre combien de bot on veut jouer
                  for i in range(nb_bots):                                    # Boucle se répétant "nb_bots" fois
                        bot = Player(str(f"Bot-{i+1}"))                       # Cree un bot
                        bot.value = i+1                                       # La valeur de ce joueur (bot) est i+1 car il y a déjà une valeur égale a 0 (le joueur)
                        stack(self.players, bot)                              # Empile a la pile "self.players" le joueur(bot)
                  tri_selection_value(self.players)

                  assert lenght(self.players) >= 2, "Nombres de joueurs dans la partie trop bas."
                  assert lenght(self.players) <= 10, "Nombres de joueurs dans la partie trop élevé."

      def distribution(self, pack: classmethod) -> None: 
            '''
            Nom: distribution

            Fonction qui permet de distribuer les cartes au joueurs actif

            Paramètre: pack: paquet de carte
            '''
            assert lenght(self.players) > 0, "Aucuns joueurs dans la partie"
            for player in self.players:                                 # Pour chaque joueurs dans la pile "self.players"
                  if is_pile_or_file_empty(player.hand) == False:       # Si le joueur n'a pas de cartes dans sa main
                        player.hand = create_pile_or_file_empty()       # "player.hand" est une pile vide
                  pack.distribute(player, 2)                            # Prend 2 cartes du paquet pour les donner au joueur "player"
            for i in range(lenght(self.players)):                       # Boucle se répétant le nombre de fois qu'il y a de joueurs dans "self.players"
                  player = str(self.players[-(i+1)])                    # "player" est la chaine de caractère de "self.players[i]"
                  if "Bot" not in player:                               # Si le joueur n'est pas un bot
                        print(player)                                   # permet de voir le nom, la main et l'argent du joueur
                        Game().clean()                                  # efface la console pour éviter que les joueurs voient les cartes des autres
                        input()                                         # Il faut appuyer sur la touche "entrer" pour passer au joueur suivant
            
      def show_players(self) -> None: 
            '''
            Nom: show_players

            Fonction qui montre les joueurs actif avec leur nom, main et argent
            '''
            assert lenght(self.players) > 0, "Aucuns joueurs dans la partie"

            for i in range(lenght(self.players)):     # Pour le nombre de fois qu'il y a de joueurs
                  player = str(self.players[-(i+1)])  # "player" est le joueur a la position -(i+1) dans "self.player". Car la liste est de la forme: ["C", "B", "A"]
                  print(f"{str(player)}")             # Affiche le joueur avec son nom, sa main et son argent
      
      def value_hand(self, commune_cards: list) -> None:
            '''
            Nom: value_hand

            Fonction qui permet de déterminer la valeur de la main des joueur selon leur main

            Paramètres: commune_cards: Sont les cartes dévoiler sur la table
            '''
            assert lenght(self.players) > 0, "Aucuns joueurs dans la partie"

            Player.hand_name(self, self.players, commune_cards)   # Fait appel a la fonction hand_name de la classe Player, en prenant en argument "self.player" et les cartes dévoilé dur la tables
            for player in self.players:                           # Pour chaque joueur dans la pile des joueurs actif
                  names = ["carte haute", "paire", "double paire", "brelan", "quinte", "couleur", "full", "carre", "quinte flush", "quinte flush royal"] # Liste des mains possibles pour chaque joueurs
                  for i in range(lenght(names)):                  # Boucle qui se répète le nombre de fois qu'il y a des main possible
                        name = names[i]                           # "name" est l'élément de la liste names a la position "i"
                        if name == player.hand_name_:             # Si "name" est égale a la main du joueur, alors:
                              player.value_hand = i               # La valeur de la main du joueur est "i" 

      def find_winner(self):
            '''
            Nom: find_winner

            Fonction qui permet de savoir quel joueur est le vainqueur

            Fonction a modifier pour eviter les bugs possibles
            '''
            value_hand_players = create_pile_or_file_empty()                  # Créé un pile nommé "value_hand_players"
            potential_win = create_pile_or_file_empty()
            for player in self.players:                                       # Boucle se répétant le nombre de fois qu'il y a de joueurs actifs
                  stack(value_hand_players, player.value_hand)                # Enfile a cette liste la valeur de la main du joueur
            tri_selection(value_hand_players)                                 # Tri les valeur de la pile "value_hand_players" dans l'ordre croissant
            for player in self.players:                                 # Pour chaques joueurs actifs, faire:
                  if player.value_hand == value_hand_players[-1]:       # Si la valeur du joueur est la valeur la plus élevé, alors:
                        player.value_hand = 0
                        stack(potential_win, player)
            if lenght(potential_win) == 1:
                        return potential_win[0]
            for player in potential_win:                 # Boucle se répétant pour chaque valeurs des cartes qu'il a en main 
                  for i in range(lenght(player.value_cards)):
                        card = player.value_cards[i]
                        if player.value_cards.count(card) > 1:
                              player.value_hand += int(card)*player.value_cards.count(card)
            tri_selection_value_hand(potential_win)
            if potential_win[-1].value_hand == potential_win[-2].value_hand:
                  for player in potential_win:
                        player.value_hand = 0
                        for card in player.value_cards:
                              player.value_hand += int(card)
            tri_selection_value_hand(potential_win)
            return potential_win[-1]
                                    
                                    

      def winner(self, commune_cards: list) -> list: 
            '''
            Nom: winner

            Fonction qui défini le gagnant d'une partie

            Paramètre: winner: joueur qui a gagner la partie
            '''
            assert lenght(self.players) > 0, "Aucuns joueurs dans la partie"  

            Game.value_hand(self, commune_cards)                        # Fait appel a la fonction "value_hand"
            winner = Game.find_winner(self)                             # Fait appel a la fonction "find_winner"
            winner.wallet += self.jar                                   # Le gagnant remporte le pot
            print(f"winner is {winner.name} with {winner.hand_name_}")  # Ecrit le nom du gagnant et sa main
            
            tri_selection_value_hand(self.players)                      # Tri les joueurs selon leurs valeur de main
            tri_selection_value(self.players)                           # Tri les joueurs selon leur valeur
            return self.players
                  
      def loser(self) -> list:
            '''
            Nom: loser

            Fonction qui défini les perdants
            '''
            assert lenght(self.players) > 0, "Aucuns joueurs dans la partie"  

            index = 0                                                         # "index" permet de de choisir le joueur dans la pile "self.players"
            for _ in range(lenght(self.players)):                             # Pour le nombre de fois qu'il y a de joueur
                  player = self.players[index]                                # le joueur est égale au joueur de la pile "self.players" a l'index "index"
                  if player.wallet == 0:                                      # si le joueur n'a plus d'argent:
                        q = create_pile_or_file_empty()                       # Créé un pile vide nommé "q"
                        for _ in range(lenght(self.players)-(index+1)):       # Boucle qui se répète le nombre de fois qu'il y a de joueurs actifs moins le numéro de "index"+1
                              stack(q, unstack(self.players))                 # Enfile a "q" l'élément défiler de la liste "self.players"
                        stack(self.sleeping_players, unstack(self.players))   # Le joueur est empiler dans la pile de joueur inactif "self.sleeping_players"
                        # Le joueur est enlever de la liste des joueurs actif donc le joueur a l'index "index" est le joueur suivant
                        while is_pile_or_file_empty(q) == False:              # Tant que la pile "q" n'est pas vide
                              stack(self.players, unstack(q))                 # Enfile a "self.players" l'élément défilé de "q"
                  else:                                                       # sinon
                        index += 1                                            # On passe au joueur suivant
            return self.players
      
      def clean(self) -> None:
            '''
            Nom: clean

            Fonction qui efface la console
            '''
            input()
            os.system("cls")