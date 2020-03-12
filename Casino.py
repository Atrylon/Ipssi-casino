#!/usr/bin/env python
# coding: utf-8

# In[59]:


from random import randrange

pseudo = ''
argent = 10
mise = 0
niveau = 1
nombre_random = 0
nb_tentatives = 0
nombre_joueur = 0

def start() :
    pseudo = str(input('Je suis Python. Quel est votre pseudo ? '))
    print('''
Hello ''' + pseudo + ''', vous avez''', argent ,'''€. 
Très bien ! Installez vous SVP à la table de pari.
    
Je vous expliquerai le principe du jeu :
Je viens de penser à un nombre entre 1 et 10. Devinez lequel ?
    - Att : vous avez le droit à trois essais !
    - Si vous devinez mon nombre dès le premier coup, vous gagnez le double de votre mise !
    - Si vous le devinez au 2è coup, vous gagnez la moitiè de votre mise !
    - Si vous le devinez au 3è coup, vous perdez votre mise !
    - Si vous ne le devinez pas au troisième coup, vous perdez évidemment votre mise et vous avez le droit :
            - de retenter votre chance avec l'argent qu'il vous reste pour reconquérir le level perdu.
            - de quitter le jeu. 
            
Dès que vous devinez mon nombre et tant que votre solde est positif : vous avez le droit de quitter le jeu et 
de partir avec vos gains OU de continuer le jeu en passant au level supérieur.
''')
    

def get_mise() :
    try:
        mise = int(input('Le jeu commence, entrez votre mise : '))
    except:
        print('not okay : to do verif input type')
    
    
    while mise > argent:
        mise=input('Le mise doit être inférieure à votre réserve totale. Entrer SVP un montant entre 1 et ', argent,' € :  ?')

       
    print('''
Vous avez choisi de miser''', mise,'''€''')
    
    
def get_random():
#     calcul du stop PEUT ETRE A REFAIRE
    stop = int(str(niveau)+"1")
    
    nombre_random = randrange (0, stop, 1)
#     print("mon nombre est : ",nombre_random)
    print('Ca y est, j\'ai choisi un nombre entre 1 et', stop)
    
def guess():
    if niveau == 1 :
        max_tentatives = 5
    elif niveau == 2 :
        max_tentatives = 7
    elif niveau == 3 :
        max_tentatives = 10
        
    nombre_joueur=input('Alors mon nombre est : ')
    print(nb_tentatives)
    nb_tentatives = nb_tentatives + 1
    
    while nombre_joueur != nombre_random and nb_tentatives <= max_tentatives:
        
        if nombre_joueur > nombre_random :
            print('Votre nombre est trop grand !')
            nombre_joueur=input('Alors mon nombre est : ')
        elif nombre_joueur < nombre_random :
            print('Votre nombre est trop petit !')
            nombre_joueur=input('Alors mon nombre est : ')
        
        nb_tentatives += 1
        
        if nb_tentatives + 1 == max_tentatives:
            print('Attention, il ne vous reste qu\'une chance !')

            
#     TODO
# 	\t- Je ne comprends pas votre nombre. Entrez SVP un nombre entier :  ?\n
# 	\t- Vous avez dépassé le délai de 5 secondes" ! Vous perdez l'essai courant\n\t\t\t et il vous reste "E" essai(s) !\n
    
    
def game():
    start()
    get_mise()
    get_random()
    guess()
        
    

game()


# In[ ]:





# In[ ]:




