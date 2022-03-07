from random import randint

def prendreMotRandom():
  with open("dico.txt", 'r') as dicoFile:
    dico = dicoFile.readlines()
    mot = dico[randint(0, len(dico)-1)]
    dicoFile.close()
  return mot

def isWordInAlphabet(word):
  alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  for i in range(len(word)):
    if word[i] not in alphabet:
      return False
  return True

def dicoAjout(newMot):
  with open("dico.txt", 'r+') as dicoFile:
    dico = dicoFile.readlines()
    for i in range(len(dico)):
      dico[i] =dico[i].replace("\n", "")
    if newMot in dico:
      print("Le mot existe déjà.")
    elif len(newMot) != 7 :
      print("Le mot n'est pas à la bonne taille. \nIl faut uniquement des mots de 7 lettres.\n")  
    elif isWordInAlphabet(newMot)==False:
      print("Les caractères spéciaux ne sont pas acceptés.\n")
    else:
      dicoFile.seek(0,0)
      dico.append(newMot)
      dico.sort()
      dicoFile.write("\n".join(dico))
      dicoFile.close()
      print("nouveau mot ajouté :",newMot)

def dicoLire():
  with open("dico.txt", 'r') as dicoFile:
    dico = dicoFile.readlines()
    dicoFile.close()
    for i in range(len(dico)):
      print(dico[i])

def dico():
  #déclarations
  ShouldBreak = False
  direction = 0
  #boucle d'appels
  while ShouldBreak == False:
    #blabla
    print("Que souhaitez vous faire ?\n1 - voir tous les mots\n2 - Ajouter un mot\n3 - voir un mot au hasard\n4 - Retourner au menu")
    #demande où le joueur veut aller
    direction = int(input(""))
    if direction == 1:
      dicoLire()
    elif direction == 2:
      newMot = input("quel est le nouveau mot ?")
      newMot = newMot.upper()
      dicoAjout(newMot)
    elif direction == 3:
      print(prendreMotRandom())
    elif direction == 4:
      ShouldBreak = True