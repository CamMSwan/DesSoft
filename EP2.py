import Base_de_paises as Bp
import Esta_na_lista as El
import Haversine as Dist
import Base_paises
import math 
import random 

#NInanogitkekek
iniciar = input('Desejar iniciar? s/n :')
if iniciar == 's':
    Jogo = 0
    while Jogo == 0:
        tentativas = 20
        lista_paises_tentados = []
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
            
        def lista_pais(comando):
            lista_paises = []
            if comando != '':
                for paises in dados_normalizados.keys():
                    if paises not in lista_paises:
                        lista_paises.append(paises)

                return lista_paises
            
            
        print('Bem Vindo ao adivinha paises')
        
        lista_paises = lista_pais(Jogo)
        pais_escolhido = escolher_pais(Jogo)
        dados_pais_escolhido = dados_normalizados[pais_escolhido]
        coordenadas_pais_escolhido = dados_pais_escolhido['geo']
        latidude_pe = coordenadas_pais_escolhido['latitude']
        longitude_pe = coordenadas_pais_escolhido['longitude']
        
        print(pais_escolhido)
        
        i = 0
        while i < tentativas:
            print('Numero de tentativas {}'.format(tentativas))
            resposta = input('Qual pais voce acha que é? --> ')
            if resposta in lista_paises:
                dados_resposta = dados_normalizados[resposta]
                coordenadas_resposta = dados_resposta['geo']
                latidude_re = coordenadas_resposta['latitude']
                longitude_re = coordenadas_resposta['longitude']
                distancia_eles = Dist.haversine(r,latidude_pe,longitude_pe,latidude_re,longitude_re)
                lista_resposta = [resposta,distancia_eles]
                if lista_resposta in lista_paises_tentados:
                    print('Ja tentou esse!')
                elif lista_resposta not in lista_paises_tentados:
                    lista_paises_tentados.append(lista_resposta)
                    
                tentativas -= 1
            
            if resposta  == pais_escolhido:
                i = 100      
            
            if resposta not in lista_paises:
                print('Resposta Invalida')

        if i == 100:
            print("PARABENS, VOCE ACERTOU!")
            iniciar = input('Desejar jogar novamente? s/n :')
            if iniciar not in ('s','n'):
                    print("Resposta Invalida")
            if iniciar == 'n':
                print('Até Logo!')
                break
                
                        
    
        
