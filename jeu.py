from dico import prendreMotRandom
from highScore import *

imgPendu = [
  " ______\n |/   \n |    \n |     \n |    \n/|\_______\n\n",
  " ______\n |/   |\n |    \n |     \n |    \n/|\_______\n\n",
  " ______\n |/   |\n |    O\n |     \n |    \n/|\_______\n\n",
  " ______\n |/   |\n |    O\n |    | \n |    \n/|\_______\n\n",
  " ______\n |/   |\n |    O\n |   /| \n |    \n/|\_______\n\n",
  " ______\n |/   |\n |    O\n |   /|\ \n |     \n/|\_______\n\n",
  " ______\n |/   |\n |    O\n |   /|\ \n |   /  \n/|\_______\n\n",
  " ______\n |/   |\n |    O\n |   /|\ \n |   / \ \n/|\_______\n\n"]

def getLettre(tour):
  print("tour n°", tour, ":")
  lettre = input("")
  lettre = lettre.upper()
  return lettre

def LetterFound(lettre,mot,motAtrouver,lettresTrouvees):
  for i in range(7):
    if lettre == mot[i]:
      motAtrouver[i] = mot[i]
      lettresTrouvees += 1
  return lettresTrouvees, motAtrouver

def strtParty (scoreJoueur,pseudo):
  print("votre score est de : ",scoreJoueur,"\n")
  playerWantPlay = True
  while playerWantPlay == True:
    up = 0
    lettresTrouvees = 0
    tour = 1
    answer = 'o'
    mot = prendreMotRandom()
    motAtrouver = ["_", "_", "_", "_", "_", "_", "_"]
    print(mot) #à supprimer
    for i in range(7):
      print(motAtrouver[i], end="")
    print("\n")
    while up < 7 and lettresTrouvees < 7:
      lettre = getLettre(tour)
      if lettre in mot:
        lettresTrouvees, motAtrouver = LetterFound(lettre,mot,motAtrouver,lettresTrouvees)
      else:
        up += 1
        print(imgPendu[up])
      for i in range(7):
        print(motAtrouver[i], end="")
      print("\n")
      tour +=1
    if up >= 7:
      scoreJoueur = loose(scoreJoueur)
    else:
      scoreJoueur = win(scoreJoueur)
    while answer != 'y' and answer !='n':
      answer = input("Voulez-vous continuer ?(y/n)")
      answer = answer.lower()
    if answer == 'y':
      playerWantPlay = True
    else:
      playerWantPlay = False
      endGame(pseudo, scoreJoueur)
  return