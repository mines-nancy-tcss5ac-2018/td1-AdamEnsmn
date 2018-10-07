def solve(n) :
    assert type(n) == int
    somme_chiffres = 0
    nombre = n
    while nombre >= 1 :
        somme_chiffres += nombre%10 #on prend le chiffre des unites
        nombre = nombre//10 #on garde 'enl�ve' le chiffre des unit�s
    return somme_chiffres

assert solve(2**1000) == 1366

print(solve(2**1000))


# Mon programme �tait faux parce que int(nombre/10) != nombre//10 pour des chiffres grands !!! 
# alors que normalement c'EST LA M�ME CHOSE !!!


# 8/3 = 2.66666...
# int(8/3) = 2 
# 8//3     = 2