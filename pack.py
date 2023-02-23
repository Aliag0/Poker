from random import *
from paramettres import *
from card import *

class Pack:
      '''
      Nom: Pack

      Class qui permet de créer un paquet de cartes avec 52 cartes

      ...

      Attributs: cards: sont les 52 cartes du paquet

      Méthodes: mix(self): mélange le paquet
                pick(self): donne la carte au sommet de la pile self.cards
                distributes(self, player, nb_cards): distribue au joueur "player" le nombre de carte "nb_cards"
      '''

      def __init__(self) -> None: 
            '''
            Fonction qui permet de créer un paquet de carte avec 52 cartes différentes
            '''
            self.cards = create_pile_or_file_empty()              # self.cards est une pile comportant toutes les cartes d'un paquet de carte
            for color in COLORS:                                  # Boucle qui parcoure toutes les couleurs de la liste COLORS

                  assert lenght(COLORS) == 4, "Il manque une ou plusieurs valeurs dans la liste"           # Pour que la fonction marche il faut les 4 couleurs soit enregistrer dans la liste COLORS

                  for value in VALUES:                            # Boucle parcourant chaque valeur de la liste VALUE
                        assert lenght(VALUES) == 13, "Il manque une ou plusieurs couleurs dans la liste"  # Pour que la fonction marche il faut les 13 valeurs soit enregistrer dans la liste COLORS
                        stack(self.cards, Card(color, value))     # Ajoute au paquet de cartes la carte prenant pour valeur "color" et "value"

      def __str__(self) -> str: 
            '''
            Fonction qui renvoi le paquet de carte sous forme de chaine de caractère
            '''
            pack = str()                        # pack sera la forme str de self.cards

            assert lenght(self.cards) == 52, "Nombres de cartes dans le paquet incorrecte"      # Pour que cela fonctionne il faute 52 cartes dans le paquet

            for card in self.cards:             # Boucle qui parcourt chaque carte de la pile "self.cards"
                  pack += str(card) + " - "     # Ajoute a "pack" une carte

            return pack + "\n"                  # Renvoi le paquet contenant toutes les cartes

      def mix(self) -> list: 
            '''
            Nom: mix

            Fonction qui mélange le paquet de carte

            Renvoi: le paquet de cartes mélangé
            '''
            assert lenght(self.cards) == 52, "Nombres de cartes dans le paquet incorrecte"      # Pour que cela fonctionne il faut les 52 cartes dans le paquet

            return shuffle(self.cards)                                                          # Renvoi le paquet de cartes avec chaque cartes de "self.cards" dans un nouvel ordre aléatoire

      def pick(self) -> list:
            '''
            Nom: pick

            Fonction qui permet de piocher une carte

            Renvoi: la carte au sommet de la pile
            '''
            assert lenght(self.cards) > 0, "Nombres de cartes dans le paquet incorrecte"  # Pour que cela fonctionne il faut 1 carte ou plus dans le paquet
            
            return unstack(self.cards)                                                    # Renvoi la carte au sommet de la pile "self.cards" qui est enlever de cette pile

      def distribute(self, player, nb_cards: int):
            '''
            Nom: distribute

            Fonction qui ajoute a un joueur "player" un nombre de cartes "nb_cards"

            Paramètres: player: joueur dans la partie
                         nb_cards: nombres de cartes a distribuer
            '''
            for _ in range(nb_cards):                 # Boucle qui se répète "nb_cards" fois
                  player.receive_card(self.pick())    # Ajoute au joueur "player" une carte piocher du paquet