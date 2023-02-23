from game import *
from pack import *

def game_poker(game: classmethod) -> None: 
      '''
      Nom: game_poker

      Fonction pour jouer au poker

      Paramètres: game: crée une partie de poker
      '''
      pack = Pack()                                         # pack est le paquet de cartes
      burn = create_pile_or_file_empty()                    # Pile comportant les cartes bruler
      common_cards = create_pile_or_file_empty()            # Pile comportant les cartes communes
      game.clean()                                          # Efface la console
      pack.mix()                                            # Mélange le paquet
      game.distribution(pack)                               # Distribue les cartes
      stack(burn, pack.pick())                              # Brule une carte
      for _ in range(3):                                    # Ajoute 3 cartes au cartes communes
            stack(common_cards, str(pack.pick()))           # ajoute une cartes piocher a la pile "common_cards"
      if lenght(game.players) != 1:
            print(common_cards, "jar : ", game.jar, "€")    # Affiche les cartes commune et le pot

      if lenght(game.players) != 1:
            game.next()                                     # Demande a chaque joueur leur choix pour après
            game.clean()                                    # Efface la console
      for _ in range(2):
            stack(burn, pack.pick())                        # Brule une cartes, empile a la pile "burn" une carte piocher
            stack(common_cards, str(pack.pick()))           # Empile a la pile "common_cards" une cartes piocher
            if lenght(game.players) != 1:
                  print(common_cards, "jar : ", game.jar, "€") # Affiche les cartes commune et la pot
            if lenght(game.players) != 1:
                  game.next()                               # Demande a chaque joueur leur choix pour après
                  game.clean()                              # efface ce qui est affiché dans la console
      print(common_cards, "jar : ", game.jar, "€")          # Affiche les cartes commune et le pot

      game.show_players()                                   # Affiche tous les joueurs actif avec leur nom, main et argent
      game.winner(common_cards)                             # Fait gagner au gagnant le pot
      game.loser()                                          # Permet d'identifier qui sont les joueurs

game = print("")      
poker = Game()                       # Cree la partie de poker
choice = str(input("mode ? "))       # Demande a quel mode on veut jouer

if choice == "multiplayers" or choice == "solo":      # Si on veut jouer alors
      print("Explications:")                          # explications sur la partie
      print("Sur cette partie de poker il est impossible de faire des relances.\nPour jouer vous devez faire votre choix entre 'sleep', 'checked', faire une mise ou 'follow'")
      poker.crea_players(choice)                      # Cree les joueurs
      A = False

      while game != "0":                              # Tant que on écrit pas 0 
            poker.start(A)                            # permet de commencer une partie sans qu'il n'y est de problèmes
            game_poker(poker)                         # Lance la fonction pour jouer au poker
            poker.clean()                             # Efface la console
            game = str(input("CONTINUE ?"))           # Demande si on veut continuer de jouer au poker, si on écrit "0" la partie se termine
            A = True