import random

def sorteia_letra(palavra,lista_restritiva):
    caracteres_especiais = ['.', ',', '-', ';', ' ']
    restricao = ','.join(lista_restritiva)
    restriction = restricao.lower()
    lista_restritiva2 = restriction.split(',')
    palavra_m = palavra.lower()
    
    lista_pode = []
    for letra in palavra_m:
        if letra not in lista_restritiva2:
            if letra not in caracteres_especiais:
                lista_pode.append(letra)
                
    if lista_pode == []:
        retorno = ''
        
    else:
        retorno = random.choice(lista_pode)
        
    return retorno
                
palavra = 'Andorra a-Velha'
lista_restritiva =  ['a', 'r']  
print(sorteia_letra(palavra,lista_restritiva))
            