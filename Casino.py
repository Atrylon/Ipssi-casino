from random import randrange
from datetime import datetime, timedelta
import json
import matplotlib.pyplot as plt

name_user = ""
dotation = 10
mise = 0
level = 1
nb_python = 0
nb_coup = 0
nb_user = 0
essais_niveau = []
data_partie = {}


# Fonction des menus de début de jeu et affichant les règles
def start():
    global name_user
    choix = 0

    try:
        choix = int(input('''
                    Bienvenue !  
---------------------------------------------------- 
| Vous pouvez :                                    |
|       - Jouer (1)                                |
|       - Voir les statistiques globales (2)       |
|       - Quitter (3)                              |
----------------------------------------------------
Votre réponse : '''))

        while choix not in (1, 2, 3):
            choix = int(input('''
ENTREE INCORRECTE !   
---------------------------------------------------- 
| Vous pouvez :                                    |
|       - Jouer (1)                                |
|       - Voir les statistiques globales (2)       |
|       - Quitter (3)                              |
----------------------------------------------------
Votre réponse : '''))

    except:
        while choix not in (1, 2, 3):
            try:
                choix = int(input('''
ENTREE INCORRECTE !   
---------------------------------------------------- 
| Vous pouvez :                                    |
|       - Jouer (1)                                |
|       - Voir les statistiques globales (2)       |
|       - Quitter (3)                              |
----------------------------------------------------
Votre réponse : '''))
            except:
                pass

    while choix == 2:
        statistiques_globales()
        choix = int(input('''
---------------------------------------------------- 
| Vous pouvez :                                    |
|       - Jouer (1)                                |
|       - Voir les statistiques globales (2)       |
|       - Quitter (3)                              |
----------------------------------------------------
Votre réponse : '''))

    if choix == 3:
        print('''
                    Au revoir !''')
        exit()

    name_user = input('''
Je suis PYTHON. Quel est votre pseudo ? 
Votre pseudo : ''')

    get_last_dotation_in_json()

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


# Fonction de récupération de la mise du joueur + gestion des erreurs
def get_mise():
    global mise
    global dotation
    mise = 0

    while int(mise) > float(dotation) or int(mise) == 0:
        try:
            mise = int(input('''Le jeu commence, entrez votre mise : 
Votre mise : '''))

            if int(mise) == 0:
                mise = int(input('''
Erreur, votre mise ne peut être nulle.
Entrer une mise inférieure ou égale à %s€
Votre mise : ''' % (str(dotation))))
            elif int(mise) > float(dotation):
                mise = int(input('''
Erreur, votre mise est plus elevé que votre solde.
Entrer une mise inférieure ou égale à %s€
Votre mise : '''%(str(dotation))))
        except:
            while True:
                try:
                    mise = int(input('''
Erreur, format incorrecte.
Entrer une mise inférieure ou égale à %s€
Votre mise : '''%(str(dotation))))
                    break
                except:
                    continue

    print('''
Vous avez choisi de miser %s€'''%(str(mise)))


# Calcul du nombre random pour le jeu
def get_random():
    global nb_python

    stop = int(str(level) + "1")
    limite = str(str(level) + "0")

    nb_python = randrange(1, stop, 1)
    print('''
Ca y est, j\'ai choisi un nombre entre 1 et %s !'''%(limite))


# Fonction centrale du jeu avec gestion déduction nombre + calcul gains
def guess():
    global nb_coup
    global mise
    global nb_python
    global dotation
    global level
    global essais_niveau
    global nb_user

    essais_niveau = []
    nb_coup = 0
    nb_user = 0
    max_tentatives = 5

    if level == 2:
        max_tentatives = 7
    elif level == 3:
        max_tentatives = 10

    # print('psssst le nombre secret est : ' + str(nb_python))

    try:
        debut = datetime.now()
        nb_user = int(input('''
Vous avez %s essais.
Essayez de deviner mon nombre. 
Votre réponse : '''%(str(max_tentatives-nb_coup))))
    except:
        while True:
            try:
                nb_user = int(input('''
Je ne comprends pas votre nombre, entrez SVP un nombre entier.
Votre réponse : '''))
                break
            except:
                continue

    nb_coup += 1

    while nb_user != nb_python and nb_coup <= max_tentatives:
        # On stocke les essais de l'utilisateur
        essais_niveau.append(nb_user)

        if nb_coup + 1 == max_tentatives:
            print('''
Atention, il ne vous reste qu\'une chance !''')
        elif nb_coup == max_tentatives:
            print('''
Vous avez perdu ! Mon nombre est ''' + str(nb_python) + ''' !''')
            break

        if nb_user > nb_python:
            print('''Votre nombre est trop grand !''')
            nb_user = int(input('''
Il vous reste %s essais.
Essayez de deviner mon nombre. 
Votre réponse : '''%(str(max_tentatives-nb_coup))))
        elif nb_user < nb_python:
            print('''Votre nombre est trop petit !''')
            nb_user = int(input('''
Il vous reste %s essais.
Essayez de deviner mon nombre. 
Votre réponse : '''%(str(max_tentatives-nb_coup))))
        nb_coup += 1

    # On ajoute la dernière réponse au tableau
    essais_niveau.append(nb_user)

    if nb_user == nb_python or nb_coup == max_tentatives:
        if nb_coup == 1:
            gain = mise * 2
        elif nb_coup == 2:
            gain = mise * 0.5
        else:
            gain = - mise

        dotation = int(dotation) + gain

        text_win = 'Bingo %s, vous avez gagné en %s coup(s)'%(name_user, str(nb_coup))

        if dotation > 0:
            if gain > 0 :
                text_win = text_win + ' et vous avez emporté %s€ !'%(str(gain))
            else:
                text_win = text_win + ' mais vous avez perdu %s€ !'%(str(-gain))
        else:
            text_win = text_win + ' mais votre solde est null. A la prochaine !'

        fin = datetime.now()

        duree = fin-debut

        data = {
            'date': str(datetime.today()),
            'duree': str(duree),
            'level': str(level),
            'actual_dotation': str(dotation),
            'mise': str(mise),
            'gain': str(gain),
            'nb_coup': str(nb_coup),
            'essais': essais_niveau
                }

        statistiques_niveau(data)

        # On stocke le résultat du niveau
        if name_user not in data_partie:
            data_partie[name_user] = []
        data_partie[name_user].append(data)

        write_stats(data)

        print(text_win)


# "Menu" post partie qui donne le choix de continuer ou non
def menu():
    global dotation
    global level

    if dotation > 0:
        choix = input('''Il vous reste %s€. 
Souhaitez-vous continuer la partie (O/N) ? 
Votre réponse : '''%(str(dotation)))

        while choix not in ('O', 'N'):
            choix = input('''
Je ne comprends pas votre réponse. Souhaitez-vous continuer la partie (O/N) ? 
Votre réponse : ''')

        if choix == 'N':
            print('''
Au revoir ! Vous finissez la partie avec %s€.'''%(str(dotation)))
            return False
        elif choix == 'O':
            if level < 3:
                level += 1
                print('''
Super ! Vous passez au niveau %s.
Rappelez vous, le principe est le même sauf que mon nombre est maintenant entre 1 et %s0 !'''%(str(level), str(level)))
            else:
                print('''
Super ! Vous restez au niveau %s.
Rappelez vous, le principe reste le même : mon nombre est entre 1 et %s0 !'''%(str(level), str(level)))

            return True
    else:
        return False


# On affiche les statistiques du niveau
def statistiques_niveau(data):
    print('''
Statistiques du niveau %s :
Temps de complétion : %s
Nombre d'essais : %s   
Essais : [ %s ]
Gain : %s
Argent à la fin du niveau : %s  
'''%(data['level'], data['duree'], data['nb_coup'], str(data['essais']).strip('[]'), data['gain'],
     data['actual_dotation']))


# Calcul et affichage des differentes statistiques de fin de partie
def statistiques_partie(data_partie):
    essais_cumules = 0
    gain_cumules = 0
    durees = []
    for item in data_partie[name_user]:
        durees.append(datetime.strptime(item['duree'], '%H:%M:%S.%f'))
        essais_cumules += int(item['nb_coup'])
        gain_cumules += float(item['gain'])

    last_duree = durees.pop()
    for duree in durees:
        last_duree = last_duree + timedelta(hours=duree.hour, minutes=duree.minute, seconds=duree.second, microseconds=duree.microsecond)

    dotation_finale = str(data_partie[name_user][-1]['actual_dotation'])

    print('''
Au revoir %s !
Vous avez fini %s partie(s) en %s
Nombre d'essais totaux : %s
Gains totaux : %s€
Argent à la fin de la partie : %s €
'''%(name_user, str(len(data_partie[name_user])), str(last_duree.time()), str(essais_cumules), str(gain_cumules), dotation_finale))


# Calcul et affichage des différentes stats possibles
def statistiques_globales():
    choix_stats = 0

    plt.style.use('ggplot')

    try:
        choix_stats = int(input('''
---------------------------------------------------------
| Vous pouvez :                                         |
|       - Fréquence de réponse au niveau 1 (1)          |
|       - Pourcentage de gagnants (2)                   |
|       - Fréquence du nombre de coup au niveau  (3)    |
|       - Retour au menu (4)                            |
---------------------------------------------------------
Votre réponse : '''))
    except:
        while choix_stats not in (1, 2, 3):
            choix = int(input('''
    ENTREE INCORRECTE !   
---------------------------------------------------------
| Vous pouvez :                                         |
|       - Fréquence de réponse au niveau 1 (1)          |
|       - Pourcentage de gagnants (2)                   |
|       - Fréquence du nombre de coup au niveau  (3)    |
|       - Retour au menu (4)                            |
---------------------------------------------------------
Votre réponse : '''))

    if choix_stats == 4:
        start()
    else:
        with open('stats.json') as json_file:
            json_content = json.load(json_file)

        if choix_stats == 1:
            tab = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            for player in json_content:
                for item in json_content[player]:
                    if item['level'] == '1':
                        for essai in item['essais']:
                            tab[essai-1] += 1
            reponses = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

            plt.bar(reponses, tab)
            plt.ylabel('Nombre d\'occurence')
            plt.xlabel('Réponses possibles')
            plt.title('Fréquences des réponses au niveau 1')

        elif choix_stats == 2:

            slices = [0, 0]
            for player in json_content:
                for item in json_content[player]:

                    if float(item['gain']) > 0:
                        slices[0] += 1
                    elif float(item['gain']) < 0:
                        slices[1] += 1

            activies = ['gagnants', 'perdants']
            colors = ['b', 'r']
            plt.title('Proportions de gagnants')

            plt.pie(slices, labels=activies
                    , colors=colors
                    , startangle=90
                    , shadow=True
                    , explode=(0, 0)
                    , autopct='%1.1f%%'
                    )

        elif choix_stats == 3:
            tab = [0, 0, 0, 0, 0]
            for player in json_content:
                for item in json_content[player]:
                    if item['level'] == '1':
                        # if item['statut'] == 'win':
                            tab[len(item['essais'])-1] += 1
                        # else:
                        #     tab[5] += 1
            reponses = ['1', '2', '3', '4', '5']

            plt.bar(reponses, tab)
            plt.ylabel('Nombre de victoires')
            plt.xlabel('Nombre de coups')
            plt.title('Fréquence du nombre de coup au niveau 1')

    plt.show()


# On sauvegarde les statistiques de chaque niveau dans le json
def write_stats(data):
    with open('stats.json') as json_file:
        json_content = json.load(json_file)

    if name_user not in json_content:
        json_content[name_user] = []

    json_content[name_user].append(data)

    with open('stats.json', 'w') as outfile:
        json.dump(json_content, outfile)


# On vérifie si le joueur existe dans le JSON pour lui redonner sa dernière mise si elle n'est pas nulle
def get_last_dotation_in_json():
    global dotation

    with open('stats.json') as json_file:
        json_content = json.load(json_file)

    if name_user in json_content:
        test = json_content[name_user][-1]

        if test['actual_dotation'] == 0:
            print('''
Welcome back %s !
Vous étiez à sec la dernière fois, cependant vous êtes chanceux : la banque vous fait cadeau de 10€.'''%(name_user))
        else:
            dotation = test['actual_dotation']
            print('''
Welcome back %s !
La dernière fois, vous aviez fini à %s€, la banque vous rend votre argent.'''%(name_user, str(dotation)))


# Fonction globale du jeu
def game():
    boolean_while = True
    global data_partie

    start()
    while boolean_while:
        get_mise()
        get_random()
        guess()
        boolean_while = menu()
    statistiques_partie(data_partie)


game()
