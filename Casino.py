#!/usr/bin/env python
# coding: utf-8

# In[15]:


pseudo = ''
mise = 10

def start():
    pseudo = input('Je suis Python. Quel est votre pseudo ? ')
    print('''
Hello ''' + pseudo + ''', vous avec''', mise ,'''€. 
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
            
Dès que vous devinez mon nombre et tant que votre solde est positif : vous avez le droit de quitter
le jeu et de partir avec vos gains OU de continuer le jeu en passant au level supérieur.''')
        
    

start()

