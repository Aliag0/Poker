VALUES = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K"]   # La liste VALUES comporte toutes les valeurs possible des cartes
COLORS = ["♥️", "♦️", "♣️", "♠️"]   # La liste COLORS comporte toutes les couleurs possible des cartes

class Card:
      """
      Nom: Card

      Class qui permet de crée une carte comportant une valeur est une couleur

      ...

      Attributs: color: couleur de carte
                 value: valeur de carte
      """

      def __init__(self, color: str, value: str) -> None: 
            '''
            Fonction qui permet de donner des caractéristiques aux carte

            Paramètres: color: couleur de carte
                         value: valeur de carte
            '''
            assert color in COLORS, "La couleur ne peut être autre chose que le propositions dans la liste 'COLORS' "
            assert value in VALUES, "La valeur ne peut être autre chose que le propositions dans la liste 'VALUES' "

            self.color = color      # La couleur de la carte est égale a la valeur "color"
            self.value = value      # La valeur de la carte est égale a la valeur "value"

      def __str__(self) -> str: 
            '''
            Fonction qui renvoi la carte sous forme de chaine de caractère

            Renvoi: une valeur avec une couleur en str
            '''
            assert f"{self.value}{self.color}" != "", "La chaine de carractere ne peut pas etre vide"
            
            return f"{self.value}{self.color}" # renvoi en str la valeur de la carte suivi de la couleur