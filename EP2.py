import Base_de_paises as Bp
import Esta_na_lista as El
import Haversine as Dist
import Base_paises
import math 
import random 

iniciar = input('Desejar iniciar? s/n :')
if iniciar == 's':
    Jogo = 0
    while Jogo == 0:
        tentativas = 20
        lista_paises_tentados = []
        vitoria = 0
        dados_normalizados = Bp.normaliza(Base_paises.continentes)
        r = 6371
        def escolher_pais(comando):
            lista_paises = []
            if comando != '':
                for paises in dados_normalizados.keys():
                    if paises not in lista_paises:
                        lista_paises.append(paises)
            
                pais_escolhido = random.choice(lista_paises)
                return pais_escolhido
        print('Bem Vindo ao adivinha paises')
        pais_escolhido = escolher_pais(Jogo)
        dados_pais_escolhido = dados_normalizados[pais_escolhido]
        print(pais_escolhido)
                
        i = 0
        while i < tentativas:
            print('Numero de tentativas {}'.format(tentativas))
            resposta = input('Qual pais voce acha que é? --> ')
            if resposta  == pais_escolhido:
                i = 100      
            tentativas -= 1

        if i == 100:
            print("PARABENS, VOCE ACERTOU!")
            iniciar = input('Desejar jogar novamente? s/n :')
            if iniciar not in ('s','n'):
                    print("Resposta Invalida")
            if iniciar == 'n':
                print('Até Logo!')
                break
                
                        
    
        
