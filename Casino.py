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


# TO USE
# gain = le montant de la mise du joueur !\n
# solde = le montant de la mise du joueur !\n  
# mise moyenne est de "mise_moy"\n


def start():
    global name_user

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
    except:
        while choix not in (1,2,3):
            choix = int(input('''
ENTREE INCORRECTE !   
---------------------------------------------------- 
| Vous pouvez :                                    |
|       - Jouer (1)                                |
|       - Voir les statistiques globales (2)       |
|       - Quitter (3)                              |
----------------------------------------------------
Votre réponse : '''))

    while choix == 2 :
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


def get_mise():
    global mise
    global dotation

    try:
        mise = int(input('''Le jeu commence, entrez votre mise : 
Votre mise : '''))
    except:
        print('not okay : to do verif input type')

    while int(mise) > dotation or int(mise) == 0:
        if int(mise) == 0 :
            mise = int(input('''
Erreur, votre mise ne peut être nulle.
Entrer une mise inférieure ou égale à %s€
Votre mise : ''' % (str(dotation))))
        else:
            mise = int(input('''
Erreur, votre mise est plus elevé que votre solde.
Entrer une mise inférieure ou égale à %s€
Votre mise : '''%(str(dotation))))

    print('''
Vous avez choisi de miser %s€'''%(str(mise)))


def get_random():
    global nb_python

    #     calcul du stop PEUT ETRE A REFAIRE
    stop = int(str(level) + "1")
    limite = str(str(level) + "0")

    nb_python = randrange(1, stop, 1)
    print('''
Ca y est, j\'ai choisi un nombre entre 1 et %s !'''%(limite))


def guess():
    global nb_coup
    global mise
    global nb_python
    global dotation
    global level
    global essais_niveau

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

        dotation = dotation + gain

        text_win = 'Bingo ' + name_user + ', vous avez gagné en ' + str(nb_coup) + ' coup(s)'

        if dotation > 0:
            if gain > 0 :
                text_win = text_win + ' et vous avez emporté ' + str(gain) + '€ !'
            else:
                text_win = text_win + ' mais vous avez perdu ' + str(-gain) + '€ !'
        else:
            text_win = text_win + ' mais votre solde est null. A la prochaine !'

        fin = datetime.now()

        duree = fin-debut

        data = {
            'date' : str(datetime.today()),
            'duree' : str(duree),
            'level' : str(level),
            'actual_dotation' : str(dotation),
            'mise' : str(mise),
            'gain' : str(gain),
            'nb_coup' : str(nb_coup),
            'essais' : essais_niveau
                }

        statistiques_niveau(data)

        # On stocke le résultat du niveau
        if name_user not in data_partie:
            data_partie[name_user] = []
        data_partie[name_user].append(data)

        write_stats(data)

        print(text_win)

def menu():
    global dotation
    global level

    if dotation > 0:
        choix = input('''Il vous reste '+ str(dotation)+ '€. 
Souhaitez-vous continuer la partie (O/N) ? 
Votre réponse : ''')

        while choix not in ('O', 'N') :
            choix = input('''
Je ne comprends pas votre réponse. Souhaitez-vous continuer la partie (O/N) ? 
Votre réponse : ''')

        if choix == 'N' :
            print('Au revoir ! Vous finissez la partie avec ' + str(dotation) +'€.')
            return False
        elif choix == 'O':
            if level < 3 :
                level += 1
                print('''
Super ! Vous passez au niveau ''' + str(level) +'''.
Rappelez vous, le principe est le même sauf que mon nombre est maintenant entre 1 et ''' + str(level) + '''0 !''')
            else:
                print('''
Super ! Vous restez au niveau ''' + str(level) + '''.
Rappelez vous, le principe reste le même : mon nombre est entre 1 et ''' + str(level) + '''0 !''')

            return True
    else:
        return False

# On affiche les statistiques du niveau
def statistiques_niveau(data):
    print('''
Statistiques du niveau ''' + data['level'] + ''' :
Temps de complétion : ''' + data['duree'] + '''
Nombre d'essais : ''' + data['nb_coup'] + '''   
Essais : '''+ str(data['essais']).strip('[]') + '''   
Gain : ''' + data['gain'] + ''' 
Argent à la fin du niveau : ''' + data['actual_dotation'] + '''   
''')


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


def statistiques_globales():
    plt.style.use('ggplot')

    choix_stats = 0

    try:
        choix_stats = int(input('''
---------------------------------------------------- 
| Vous pouvez :                                    |
|       - Fréquence de réponse au niveau 1 (1)     |
|       - Pourcentage de gagnants (2)              |
|       - Retour au menu (3)                       |
----------------------------------------------------
Votre réponse : '''))
    except:
        while choix_stats not in (1, 2, 3):
            choix = int(input('''
    ENTREE INCORRECTE !   
---------------------------------------------------- 
| Vous pouvez :                                    |
|       - Fréquence de réponse au niveau 1 (1)     |
|       - Pourcentage de gagnants (2)              |
|       - Retour au menu (3)                       |
----------------------------------------------------
Votre réponse : '''))

    if choix_stats == 3 :
        start()
    elif choix_stats == 1:
        with open('stats.json') as json_file:
            json_content = json.load(json_file)

        list_essais_1 = []
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
        with open('stats.json') as json_file:
            json_content = json.load(json_file)

        slices = [0, 0]
        for player in json_content:
            for item in json_content[player]:

                if float(item['gain']) > 0:
                   slices[0] += 1
                elif float(item['gain']) < 0:
                    slices[1]+=1

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
Vous étiez à sec la dernière fois, cependant vous êtes chanceux : la banque vous fait cadeau de 10€.''')
        else:
            dotation = test['actual_dotation']
            print('''
La dernière fois, vous aviez fini à '+ str(dotation) +'€, la banque vous rend votre argent.''')


def game():
    boolean_while = True
    global data_partie

    start()
    while boolean_while == True:
        get_mise()
        get_random()
        guess()
        boolean_while = menu()
    statistiques_partie(data_partie)




game()