from random import randrange
from datetime import datetime
import json
# import Menu

name_user = ""
dotation = 10
mise = 0
level = 1
nb_python = 0
nb_coup = 0
nb_user = 0


# TO USE
# gain = le montant de la mise du joueur !\n
# solde = le montant de la mise du joueur !\n  
# mise moyenne est de "mise_moy"\n


def start():
    global name_user

    name_user = input('Je suis Python. Quel est votre pseudo ? ')

    get_last_dotation_in_json()

    menu = Menu()
    menu.open()
    print('''
---------------------------------------------------------------------------------------------------------------
|                                      Hello ''' + name_user + ''', vous avez '''+ str(dotation) +'''€.                                            |
|                          Très bien ! Installez vous SVP à la table de pari.                                 |
|                                                                                                             |
|                                                                                                             |
| Je vous expliquerai le principe du jeu :                                                                    |
| Je viens de penser à un nombre entre 1 et 10. Devinez lequel ?                                              |
|    - Att : vous avez le droit à trois essais !                                                              |
|    - Si vous devinez mon nombre dès le premier coup, vous gagnez le double de votre mise !                  |
|    - Si vous le devinez au 2è coup, vous gagnez la moitiè de votre mise !                                   |
|    - Si vous le devinez au 3è coup, vous perdez votre mise !                                                |
|    - Si vous ne le devinez pas au troisième coup, vous perdez évidemment votre mise et vous avez le droit : |
|            - de retenter votre chance avec l'argent qu'il vous reste pour reconquérir le level perdu.       |
|            - de quitter le jeu.                                                                             |
|                                                                                                             |
| Dès que vous devinez mon nombre et tant que votre solde est positif : vous avez le droit de quitter le jeu  |
| et de partir avec vos gains OU de continuer le jeu en passant au level supérieur.                           |
---------------------------------------------------------------------------------------------------------------
''')


def get_mise():
    global mise
    global dotation

    try:
        mise = int(input('Le jeu commence, entrez votre mise : '))
    except:
        print('not okay : to do verif input type')

    while int(mise) > dotation:
        mise = input(' Erreur, votre mise est plus elevé que votre solde.'
 'Entrer une mise inférieure ou égale à '+ str(dotation) +'€')

    print('''
Vous avez choisi de miser '''+ str(mise)+'''€''')


def get_random():
    global nb_python

    #     calcul du stop PEUT ETRE A REFAIRE
    stop = int(str(level) + "1")
    limite = str(str(level) + "0")

    nb_python = randrange(1, stop, 1)
    print('Ca y est, j\'ai choisi un nombre entre 1 et', limite)


def guess():
    global nb_coup
    global mise
    global nb_python
    global dotation

    nb_coup = 0
    nb_user = 0

    if level == 1:
        max_tentatives = 5
    elif level == 2:
        max_tentatives = 7
    elif level == 3:
        max_tentatives = 10

    print('psssst le nombre secret est : ' + str(nb_python))


    try:
        nb_user = int(input('''Alors mon nombre est : 
'''))

    except:
        while True:
            try:
                nb_user = int(input('Je ne comprends pas votre nombre. Entrez SVP un nombre entier : '))
                break
            except:
                continue

    nb_coup += 1

    while nb_user != nb_python and nb_coup <= max_tentatives:

        if nb_coup + 1 == max_tentatives:
            print('''Atention, il ne vous reste qu\'une chance !''')
        elif nb_coup == max_tentatives:
            print('''Vous avez perdu ! Mon nombre est ''' + str(nb_python) + ''' !\n
            ''')

        if nb_user > nb_python:
            print('''Votre nombre est trop grand !
            ''')
            nb_user = int(input('Alors mon nombre est : '))
        elif nb_user < nb_python:
            print('''Votre nombre est trop petit !
            ''')
            nb_user = int(input('Alors mon nombre est : '))
        nb_coup += 1

    if nb_user == nb_python:
        if nb_coup == 1:
            gain = mise * 2
        elif nb_coup == 2:
            gain = mise * 0.5
        else:
            gain = 0

        dotation = dotation - mise + gain

        text_win = 'Bingo ' + name_user + ', vous avez gagné en ' + str(nb_coup) + ' coup(s)'

        if dotation > 0:
            text_win = text_win + 'et vous avez emporté ' + str(gain) + '€ !'
        else:
            text_win = text_win + ' mais votre solde est null. A la prochaine !'

        data = {
            'date' : str(datetime.today()),
            'level' : level,
            'actual_dotation' : dotation,
            'mise' :  mise,
            'gain' : gain,
            'nb_coup' : nb_coup
                }

        write_stats(data)

        print(text_win)

def menu():
    global dotation
    global level

    if dotation > 0:
        choix = input('Il vous reste '+ str(dotation)+ '€. Souhaitez-vous continuer la partie (O/N) ? ')

        while choix not in ('O', 'N') :
            choix = input('Je ne comprends pas votre réponse. Souhaitez-vous continuer la partie (O/N) ? ')

        if choix == 'N' :
            print('Au revoir ! Vous finissez la partie avec ' + str(dotation) +'€.')
            return False
        elif choix == 'O':
            if level < 3 :
                level += 1
                print('''Super ! Vous passez au niveau ''' + str(level) +'''.
Rappelez vous, le principe est le même sauf que mon nombre est maintenant entre 1 et ''' + str(level) + '''0 !''')
            else:
                print('''Super ! Vous restez au niveau ''' + str(level) + '''.
Rappelez vous, le principe reste le même : mon nombre est entre 1 et ''' + str(level) + '''0 !''')

            return True
    else:
        return False


def statistiques_partie():
    return True


def statistiques_globales():
    return True


def write_stats(data):
    with open('stats.json') as json_file:
        json_content = json.load(json_file)

    if name_user in json_content:
        json_content[name_user].append(data)
    else:
        json_content[name_user] = []
        json_content[name_user].append(data)

    with open('stats.json', 'w') as outfile:
        json.dump(json_content, outfile)

def get_last_dotation_in_json():
    global dotation

    with open('stats.json') as json_file:
        json_content = json.load(json_file)

    if name_user in json_content:
        test = json_content[name_user][-1]
        dotation = test['actual_dotation']


def game():
    boolean_while = True

    start()
    while boolean_while == True:
        get_mise()
        get_random()
        guess()
        boolean_while = menu()



game()