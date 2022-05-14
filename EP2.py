import Normalizando_base as Bp
import Esta_na_lista as El
import Haversine as Dist
import Base_paises
import Adicionando_lista_ordenada as Lo
import Sorteia_Letra_com_Restrições as Sl
import Sorteando_Países as SortPa
import Ponto_a_cada_tres_numeros as norm
import random 
import time

lista_vazia = []


iniciar = input('\033[1;36mDesejar iniciar o jogo? \033[32msim\033[m/\033[31mnao\033[m:')
if iniciar == 'sim':
    Jogo = 0
    while Jogo == 0:
        tentativas = 20
        lista_paises_tentados = []
        dados_normalizados = Bp.normaliza(Base_paises.continentes)
        lista_paises_por_distancia = []
        r = 6371
        
        def lista_pais(comando):
            lista_paises = []
            if comando != '':
                for paises in dados_normalizados.keys():
                    if paises not in lista_paises:
                        lista_paises.append(paises)

                return lista_paises
            
        print(' ===============================')
        print('|                               |')
        print('| \033[1;32mBem Vindo ao Adivinha Paises!\033[m |')
        print('|             \033[32m2022\033[m              |')
        print(' ====== Desing de Software ===== ')

        time.sleep(0.5)

        print('')
        
        print('Comandos:')
        print('     dica        --> entra no mercado de dicas')
        print('     desisto     --> desiste da rodada')
        print('     inventário  --> exibe sua posição')
        time.sleep(0.5)

        print('')

        print('Um \033[35mpaís\033[m foi escolhido, tente adivinhar!')
        time.sleep(1)

        
        

        print('')
        
        lista_paises = lista_pais(Jogo)
        pais_escolhido = SortPa.sorteia_pais(dados_normalizados)
        dados_pais_escolhido = dados_normalizados[pais_escolhido]
        coordenadas_pais_escolhido = dados_pais_escolhido['geo']
        latidude_pe = coordenadas_pais_escolhido['latitude']
        longitude_pe = coordenadas_pais_escolhido['longitude']
        cor_bandeira = dados_pais_escolhido['bandeira']
        lista_impressa_cores = []
        lista_cores_bandeira = []
        capital = dados_pais_escolhido['capital']
        lista_letras_capital = []
        letras_escolhidas = []
        for cores , num in cor_bandeira.items():
            if num!= 0 and cores != 'outras':
                lista_cores_bandeira.append(cores)
        area_escolhida = str(dados_pais_escolhido['area'])
        area_escolhida_normalizada = norm.normalizar(area_escolhida)
        
        lista_dicas_usadas = []
        
        populacao_escolhida = str(dados_pais_escolhido['populacao'])
        populacao_escolhida_normalizada = norm.normalizar(populacao_escolhida)
        
                    
        continente_escolhido = dados_pais_escolhido['continente']
        
        lista_opcao_dicas = [1,2,3,4,5,0]

            

        
        print(pais_escolhido)
        print(dados_pais_escolhido)
        print (lista_cores_bandeira)
        
        i = 0
        while i < tentativas:
            z = 0 
            print('')
            if lista_paises_por_distancia != []:
                while z < len(lista_paises_por_distancia):
                    distancia_normalizada = norm.tira_virgula_normaliza(lista_paises_por_distancia[z][1])
                    print('{0} km ----> {1}'.format(distancia_normalizada,lista_paises_por_distancia[z][0]))
                    z += 1
            print('')
            print('Você tem \033[33m{}\033[m tentativas'.format(tentativas))
            resposta = input('Você quer \033[1;31;43mchutar um país\033[m ou quer uma \033[1;45mdica\033[m? ')
            
            if resposta in lista_paises:
                dados_resposta = dados_normalizados[resposta]
                coordenadas_resposta = dados_resposta['geo']
                latidude_re = coordenadas_resposta['latitude']
                longitude_re = coordenadas_resposta['longitude']
                distancia_eles = Dist.haversine(r,latidude_pe,longitude_pe,latidude_re,longitude_re)
                lista_resposta = [resposta,distancia_eles]

                lista_paises_por_distancia = Lo.adiciona_em_ordem(resposta,distancia_eles,lista_paises_por_distancia)
                #ainda tem que printar coloido os valores acima 

                if lista_resposta in lista_paises_tentados:
                    print('\033[1;41mVocê ja chutou este pais!\033[m')

                elif lista_resposta not in lista_paises_tentados:
                    lista_paises_tentados.append(lista_resposta)
                    
                tentativas -= 1

            if resposta == 'dica':
                print('')
                print('Processando...')
                time.sleep(0.5)
                print('')
                print('Mercado de Dicas:')
                print('----------------------------------------------')
                print(' [\033[31m0\033[m] Sem dica')
                print(' [\033[32m1\033[m] Cor da bandeira     \033[32m->\033[m custa 4 tentativas')
                print(' [\033[33m2\033[m] Letra da capital    \33[33m->\033[m custa 3 tentativas')
                print(' [\033[34m3\033[m] Área                \033[34m->\033[m custa 6 tentavis')
                print(' [\033[35m4\033[m] Populeção           \033[35m->\033[m custa 5 tentativas')
                print(' [\033[36m5\033[m] COntinente          \033[36m->\033[m custa 7 tentativas')
                print('----------------------------------------------')
                print ('')
                #Menu de opções:
                if tentativas > 7 and len(lista_dicas_usadas) == 0:
                    dica = int(input('Escolha a opção [\033[31m0\033[m|\033[32m1\033[m|\033[33m2\033[m|\033[34m3\033[m|\033[35m4\033[m|\033[36m5\033[m]: '))
                elif tentativas > 7 and 3 in lista_dicas_usadas and 4 not in lista_dicas_usadas and 5 not in lista_dicas_usadas:
                    dica = int(input('Escolha a opção [\033[31m0\033[m|\033[32m1\033[m|\033[33m2\033[m|\033[35m4\033[m|\033[36m5\033[m]: '))
                elif tentativas > 7 and 4 in lista_dicas_usadas and 3 not in lista_dicas_usadas and 5 not in lista_dicas_usadas:
                    dica = int(input('Escolha a opção [\033[31m0\033[m|\033[32m1\033[m|\033[33m2\033[m|\033[34m3\033[m|\033[36m5\033[m]: '))
                elif tentativas > 5 and 5 in lista_dicas_usadas and 4 not in lista_dicas_usadas and 3 not in lista_dicas_usadas:
                    dica = int(input('Escolha a opção [\033[31m0\033[m|\033[32m1\033[m|\033[33m2\033[m|\033[34m3\033[m|\033[35m4\033[m]: '))
                elif tentativas > 7 and 3 in lista_dicas_usadas and 4 in lista_dicas_usadas:
                    dica = int(input('Escolha a opção [\033[31m0\033[m|\033[32m1\033[m|\033[33m2\033[m|\033[36m5\033[m]: '))
                elif tentativas > 5 and 3 in lista_dicas_usadas and 5 in lista_dicas_usadas:
                    dica = int(input('Escolha a opção [\033[31m0\033[m|\033[32m1\033[m|\033[33m2\033[m|\033[35m4\033[m]: '))
                elif tentativas > 6 and 4 in lista_dicas_usadas and 5 in lista_dicas_usadas:
                    dica = int(input('Escolha a opção [\033[31m0\033[m|\033[32m1\033[m|\033[33m2\033[m|\033[34m3\033[m]: '))
                elif tentativas > 4:
                    dica = int(input('Escolha a opção [\033[31m0\033[m|\033[32m1\033[m|\033[33m2\033[m]: '))
                elif tentativas > 3:
                    dica = int(input('Escolha a opção [\033[31m0\033[m|\033[33m2\033[m]: '))
                elif tentativas < 3:
                    print('\033[1;35mVocê não consegue mais comprar nenhuma dica! :( \033[m')
                    dica = 0
                    
                if dica == 0:
                    print('Numero de tentativas \033[1;33m{}\033[m'.format(tentativas))
        
                    resposta = input('Você quer \033[1;31;43mchutar um país\033[m ou quer uma \033[1;45mdica\033[m? ')

                if dica == 1:
                    while True:
                        cor = random.choice(lista_cores_bandeira)
                        if cor not in lista_impressa_cores:
                            lista_impressa_cores.append(cor)
                            tentativas -= 4
                            break
                    print ('Cores da bandeira: {}'.format(lista_impressa_cores))

                if dica == 2:
                    while True:
                        letra_printada = Sl.sorteia_letra(capital, lista_vazia)
                        if letra_printada not in letras_escolhidas:
                            letras_escolhidas.append(letra_printada)
                            print(letra_printada)
                            tentativas -= 3
                            break
                
                if dica == 3:
                    if dica not in lista_dicas_usadas:
                        lista_dicas_usadas.append(3)
                        print ('Area: {} Km2'.format(area_escolhida_normalizada))
                        tentativas -= 6
                    else:
                        print('\033[1;41mEstá dica já foi usada!\033[m')
                        
                if dica == 4:
                    if dica not in lista_dicas_usadas:
                        lista_dicas_usadas.append(4)
                        print ('População = {} Habitantes'.format(populacao_escolhida_normalizada))
                        tentativas -= 5

                if dica == 5:
                     if dica not in lista_dicas_usadas:
                        lista_dicas_usadas.append(5)
                        print ('Continente: {}'.format(continente_escolhido))
                        tentativas -= 7
                        
                if dica not in lista_opcao_dicas:
                    print('\033[1;33mOpção Inválida\033[m')
                    dica = 0
                    

            if resposta  == pais_escolhido:
                i = 100      
            
            if resposta == 'desisto':
                i = 50
            
            if resposta not in lista_paises and resposta != 'dica' and resposta != 'desisto' :
                print('\033[33mResposta Invalida\033[m')

        if i == 100:
            print("\033[1;30;42mPARABENS, VOCE ADIVINHOU O PAÍS QUE FOI ESCOLHIDO! :) \033[m")
            iniciar = input('\033[1;36mDesejar reiniciar o jogo? \033[32msim\033[m/\033[31mnao\033[m:')
            if iniciar not in ('sim','nao'):
                    print("\033[31mResposta Invalida\033[m")
            if iniciar == 'nao':
                print('\033[35mAté Logo!\033[m')
                break
        
        if i == 50:
            print("\033[1;30;42mFRACO!, o país era {}) \033[m".format(pais_escolhido))
            desistencia = input('\033[1;36mTem certeza que quer desistir? \033[32msim\033[m/\033[31mnao\033[m:')
            if desistencia not in ('sim','nao'):
                    print("\033[31mResposta Invalida\033[m")
            if desistencia == 'sim':
                time.sleep(0.5)
                print('\033[35mAté Logo!\033[m')
                break
            if desistencia == 'nao':
                time.sleep(0.5)
                iniciar = input('\033[1;36mDesejar reiniciar o jogo? \033[32msim\033[m/\033[31mnao\033[m:')
        
        if tentativas <= 0: 
            acabou = input('Suas \033[33mtentativas\033[m acabaram, gostaria de \033[44mreiniciar o jogo?\033[m \033[32msim\033[m/\033[31mnao\033[m :')
            if acabou == 'sim':
                time.sleep(0.5)
                print (resposta)
            else: 
                time.sleep(0.5)
                print('\033[1;30;46mObrigada, volte sempre!\033[m')
                break
                

    
        
