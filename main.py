from dico import dico
from jeu import strtParty
from highScore import isInNameTxt
from credits import credit
from highScore import highScore
from highScore import joueur

#blabla d'acceuil
print("Bienvenue dans le jeu du PENDU.")
#déclaration
menuBreak = False
#boucle d'appels
while menuBreak == False:
  #blabla
  print("Dans quelle section voulez-vous entrer ?\n1 - Dictionnaire\n2 - High Score\n3 - Jeu\n4 - Credits\n5 - Quitter")
  #demande où le joueur veut aller
  section = int(input(""))
  if section == 1:
    dico()
  elif section == 2:
    highScore()
  elif section == 3:
    print("Quel est votre pseudo ?")
    pseudo = input("")
    pseudo = pseudo.capitalize()
    isInNameTxt(pseudo)
    scoreJoueur = joueur(pseudo)
    menuBreak = strtParty(scoreJoueur, pseudo)
  elif section == 4:
    credit()
  elif section == 5:
    menuBreak = True
    print("à la prochaine !")