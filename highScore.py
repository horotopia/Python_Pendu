def profil():
  with open("scores.txt", 'r') as scoresFile:
    scores = scoresFile.readlines()
    for i in range (len(scores)):
	    scores[i] =int(scores[i].replace("\n", ""))
    scoresFile.close()
  with open("name.txt", 'r') as nameFile:
    name = nameFile.readlines()
    for i in range (len(name)):
	    name[i] = name[i].replace("\n", "")
    nameFile.close()
  return scores, name

def joueur(pseudo):
  scores, name = profil()
  for i in range(len(pseudo)):
    if name[i] == pseudo:
      scoreJoueur = scores[i]
      i = len(pseudo)
  return scoreJoueur
  
def ajout(pseudo):
  pseudo = "\n"+pseudo
  with open("scores.txt", 'a') as scoresFile:
    scoresFile.write("\n0")
    scoresFile.close()
  with open("name.txt", 'a') as nameFile:
    nameFile.write(pseudo)
    nameFile.close()

def modif(names, scores):
  with open("scores.txt", 'w') as scoresFile:
    scoresFile.write("\n".join(scores))
    scoresFile.close()
  with open("name.txt", 'w') as nameFile:
    nameFile.write("\n".join(names))
    nameFile.close()

def tri_bulle():
  scores, names = profil()
  n = len(scores)
  # Traverser tous les éléments du tableau
  for i in range(n):
    for j in range(0, n-i-1):
      # échanger si l'élément trouvé est plus grand que le suivant
      if scores[j] < scores[j+1] :
        scores[j], scores[j+1] = scores[j+1], scores[j]
        names[j], names[j+1] = names[j+1], names[j]
  return scores, names

def isInNameTxt(pseudo):
  scores, name = profil()
  count = 0
  for i in range(len(name)):
    if name[i] == pseudo:
      count += 1
  if count >= 1:
    print("Te revoilà ",pseudo," !")
  else:
    print("Oh ! Un nouveau.")
    ajout(pseudo)
    print("Pseudo : ",pseudo,"\nScore : 0")  

#highScore
def highScore():
  scores, names = tri_bulle()
  for i in range(len(scores)):
    print(names[i],".....",scores[i])
  
def win(scoreJoueur,tour):
  scoreJoueur += 7+13-tour
  print("Comme dirait le gars dans Code Quantum : Oh bravo !")
  return scoreJoueur

def loose(scoreJoueur,tour):
  scoreJoueur -= 7+13-tour
  print("Dommage ! Potasse un peu et reviens ;p")
  return scoreJoueur

def endGame(pseudo, score):
  scores, name = profil()
  for i in range(len(name)):
    if name[i] == pseudo:
      scores[i] = str(score)
    else:
      scores[i] = str(scores[i])
  modif(name,scores)