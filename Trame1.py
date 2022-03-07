from random import randint

def mot():
  with open("dico.txt", 'r') as filin:
    dico = filin.readlines()
    mot = dico[randint(0, len(dico)-1)]

imgPendu = [
  " ______\n |/   \n |    \n |     \n |    \n/|\_______",
  " ______\n |/   |\n |    \n |     \n |    \n/|\_______",
  " ______\n |/   |\n |    O\n |     \n |    \n/|\_______",
  " ______\n |/   |\n |    O\n |    | \n |    \n/|\_______",
  " ______\n |/   |\n |    O\n |   /| \n |    \n/|\_______",
  " ______\n |/   |\n |    O\n |   /|\ \n |     \n/|\_______",
  " ______\n |/   |\n |    O\n |   /|\ \n |   /  \n/|\_______",
  " ______\n |/   |\n |    O\n |   /|\ \n |   / \ \n/|\_______"]

print("Bonjour, nous allons jouer au Pendu.")
print("Mais avant ça, voulez-vous accéder au dictionnaire ? (y/n)")
dico = ["ABATTRA","ABEILLE","ABETIES","ABONDER"]
score = 0
name = "Horo"
"""ici il va falloir coder :
    - la condition y ou n
    - la partie dico
        + ajout
        + suppr
        + modif
        + lire
"""
print("avez-vous déjà jouer ? (y/n)")
""" à l'ordre du jour :
    - condition y ou n
    - si y :
        + quel est votre pseudo ?
            => lire name et score
    - si n :
        + quel est va être votre pseudo ?
            => verif : pas 2 scores diff
"""
print("début du jeu. Trouvez le mot en indiquant une lettre. \nSi celle-ci est dans le mot, c'est bon. \nSi elle n'est pas dans le mot, un morceau sera ajouté à votre potence.")
"""pour commencer, il va falloir :
    - définir le mot
    - donner 7 chances au joueur
    - 
"""

def strtParty (score,name):
  #score = profil.score
  playerWantPlay = True
  while playerWantPlay == True:
    up = 0
    lettresTrouvees = 0
    tour = 1
    answer = 'o'
    
    mot()
    motAtrouver = ["_", "_", "_", "_", "_", "_", "_"]
    print(mot)
    for i in range(7):
      print(motAtrouver[i], end="")
    print("\n")
    while up < 7 and lettresTrouvees < 7:
      print("tour n°", tour, ":")
      lettre = input("")
      lettre = lettre.upper()
      if lettre in mot:
        for i in range(7):
          if lettre == mot[i]:
            motAtrouver[i] = mot[i]
            lettresTrouvees += 1
      else:
        up += 1
        print(imgPendu[up])
      for i in range(7):
        print(motAtrouver[i], end="")
      print("\n")
      tour +=1
    if up >= 7:
      score -= 7
      print("Tu as perdu. Voici ton score :",score)
    else:
      score += 7
      print("Bravo ! Voici ton score :",score)
    while answer != 'y' and answer !='n':
      answer = input("Voulez-vous continuer ?(y/n)")
      answer = answer.lower()
    if answer == 'y':
      playerWantPlay = True
    else:
      print("à la prochaine !")
      playerWantPlay = False
  return score

"""fonctionnement du score :
    - compteurLettreTrouvee
    - win = Score + lettreTrouvée - rounds
    - loose = Score - lettreTrouvée -7 - rounds
"""
score = strtParty(score, name)