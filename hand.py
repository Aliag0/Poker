from paramettres import *

def trad_val(lst_value):
    '''
    Nom: trad_val

    Fonction qui traduit les figures en valeur numérique (en chaine de caractère)

    Paramètre: lst_value: Liste que parcours le programme pour la traduire
    '''
    for i in range(lenght(lst_value)):
        value = lst_value[i]
        if value == "T":
            q = create_pile_or_file_empty()
            for _ in range(lenght(lst_value)-(i+1)):
                stack(q, unstack(lst_value))
            unstack(lst_value)
            stack(lst_value, "10")
            while is_pile_or_file_empty(q) == False:
                stack(lst_value, unstack(q))

        elif value == "J":
            q = create_pile_or_file_empty()
            for _ in range(lenght(lst_value)-(i+1)):
                stack(q, unstack(lst_value))
            unstack(lst_value)
            stack(lst_value, "11")
            while is_pile_or_file_empty(q) == False:
                stack(lst_value, unstack(q))

        elif value == "Q":
            q = create_pile_or_file_empty()
            for _ in range(lenght(lst_value)-(i+1)):
                stack(q, unstack(lst_value))
            unstack(lst_value)
            stack(lst_value, "12")
            while is_pile_or_file_empty(q) == False:
                stack(lst_value, unstack(q))

        elif value == "K":
            q = create_pile_or_file_empty()
            for _ in range(lenght(lst_value)-(i+1)):
                stack(q, unstack(lst_value))
            unstack(lst_value)
            stack(lst_value, "13")
            while is_pile_or_file_empty(q) == False:
                stack(lst_value, unstack(q))

        elif value == "A":
            q = create_pile_or_file_empty()
            for _ in range(lenght(lst_value)-(i+1)):
                stack(q, unstack(lst_value))
            unstack(lst_value)
            stack(lst_value, "14")
            while is_pile_or_file_empty(q) == False:
                stack(lst_value, unstack(q))
                
    return lst_value

def poker_hand(cards):

    values = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
    colors = ["♥️", "♦️", "♣️", "♠️"]
    cards_values = []
    cards_colors = []
    main = []

    for card in cards:
        for value in values:
            if value in card:
                cards_values.append(value)
        for color in colors:
            if color in card:
                cards_colors.append(color)
                
    for value in cards_values:
        if cards_values.count(value) == 2:
            stack(main, "paire")

    if main.count("paire") >= 4:
        main = create_pile_or_file_empty()
        stack(main, "double paire")

    for value in cards_values:
        if cards_values.count(value) == 3:
            stack(main, "brelan")

    for value in cards_values:
        trad_val(cards_values, 1)
        if str(int(value)+1) in cards_values and str(int(value)+2) in cards_values and str(int(value)+3) in cards_values and str(int(value)+4) in cards_values:
            suite = create_pile_or_file_empty()
            stack(main, "quinte")
            for i in range(5):
                stack(suite, str(int(value)+i))

    for color in cards_colors:
        if cards_colors.count(color) >= 5:
            stack(main, "couleur")
            couleur = create_pile_or_file_empty()
            for card in cards:
                if color in card:
                    stack(couleur, card)

    if main.count("paire") == 2 and main.count("brelan") == 3:
        main = create_pile_or_file_empty()
        stack(main, "full")

    for value in cards_values:
        if cards_values.count(value) == 4:
            main = create_pile_or_file_empty()
            stack(main, "carré")

    if "quinte" in main and "couleur" in main:
        trad_val(suite, 2)
        verif = 0
        for num_color in couleur:
            for val in suite:
                if val in num_color:
                    verif += 1
        if verif == 5:
            main = create_pile_or_file_empty()
            stack(main, "quinte flush")

    if "quinte flush" in main:
        if "A" in suite:
            main = create_pile_or_file_empty()
            stack(main, "quinte flush royal")
    
    if main == []:
        stack(main, "carte haute")

    return main[-1]

cards = ["3", "A", "Q", "8", "2", "9", "K"]
print(trad_val(cards))