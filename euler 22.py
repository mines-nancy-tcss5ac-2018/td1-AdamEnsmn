import os
os.chdir("U:\Documents\Informatique\Prog1A S5\TD1_projet Euler")

def tri(liste) : 
    f = open(liste, "r")
    fichier = f.read()
    fichier = fichier.split('","')			#creer une liste a partir du fichier
    element_premier = fichier[0].split('"') 
    element_dernier = fichier[-1].split('"')
    fichier[0] = element_premier[1]
    fichier[-1] = element_dernier[0]
    fichier.append(None)					#on rajoute None qui sera en premier elmt apres le tri
										#ca permet d'avoir le premier prenom indice par 1
    return sorted(fichier)					#sorted() trie la liste



liste_triee = tri("noms.txt")		#a partir d'ici on a un tableau trie, less autres fonctions sont prevues pour travailler avec

def valeur_lettre(lettre) :
    alphabet = (None,'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z')
    for k in range(1,27) :
        if lettre == alphabet[k] :
            return k
    return "Lettre non trouvée, écrivez en majuscules"

def valeur_prenom(prenom) : 
    somme = 0
    for lettre in prenom :
        somme += valeur_lettre(lettre)
    return somme

def position_liste(prenom,liste) : 
    prenom1 = prenom
    for k in range(0,len(liste)) : 
	if prenom1 == liste[k] :
	    return k
    return "Prénom non trouve"

def score_prenom(prenom,liste):
    return position_liste( prenom,liste)*valeur_prenom(prenom)

def solve(liste) :
    somme_score = 0
    for k in range(1, len(liste)): 
	somme_score += score_prenom(liste[k],liste)
    return somme_score

resultat = solve(liste_triee)

assert 871198282 == resultat

#print("Valeur COLIN =",valeur_prenom("COLIN"))
#print("Position COLIN =",position_liste("COLIN", liste_triee))
#print("Score COLIN =",score_prenom("COLIN", liste_triee))
print("Somme totale de tous les scores =", resultat)
print("Programme non optimise : dans solve, on recherche a chaque fois la position dans la liste, alors qu'on la connait. Ce programme marche aussi avec une liste non triee, meme si alors le resultat n'est pas le meme.")
