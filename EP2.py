import Base_de_paises as Bp
import Esta_na_lista as El
import Haversine as Dist
import Base_paises
import math 
import random 


tentativas = 0
lista_paises_tentados = []
vitoria = 0
dados_normalizados = Bp.normaliza(Base_paises.continentes)

def escolher_pais(comando):
    lista_paises = []
    if comando != '':
        for paises in dados_normalizados.keys():
            if paises not in lista_paises:
                lista_paises.append(paises)
    
        pais_escolhido = random.choice(lista_paises)
        return pais_escolhido
            
iniciar_jogo = input('Iniciar? S/N: ')
if iniciar_jogo == 'S':
    pais_escolhido = escolher_pais(iniciar_jogo)
    
print(pais_escolhido)
