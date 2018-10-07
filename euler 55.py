def est_un_palyndrome(n) :
    nombre = str(n)
    for k in range(0,len(nombre)) :
	    if nombre[k] != nombre[-k-1] :
		return False
    return True

def renverser_nombre(n) :
    nombre  = str(n)
    annexe = ""
    for k in range(0,len(nombre)) :
	annexe += nombre[-k-1]
    return int(annexe)

def est_un_nombre_de_Lychrel(n) :
    nombre = n
    for k in range(1,51) : 
	nombre = nombre + renverser_nombre(nombre)
	if est_un_palyndrome(nombre) == True :
	    return False
    return True

def solve(n): 
    somme = 0
    for k in range(0,n) :
	if est_un_nombre_de_Lychrel(k) :
	    somme += 1
    return somme


reponse = solve(10000)
assert solve(10000) == reponse
print("Il y a %f nombres de Lychrel avant 10000" %reponse)