import random

def sorteia_pais(dicionario):
    lista =[]
    for p in dicionario.keys():
        if p not in lista:
            lista.append(p)
    
    pais = random.choice(lista)
    return pais