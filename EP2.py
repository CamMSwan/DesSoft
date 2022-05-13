import Normalizando_base as Bp
import Esta_na_lista as El
import Haversine as Dist
import Base_paises
import Adicionando_lista_ordenada as Lo
import Sorteia_Letra_com_Restrições as Sl
import Sorteando_Países as SortPa
import colorir as cor
import random 

lista_vazia = []


iniciar = input('Desejar iniciar? s/n :')
if iniciar == 's':
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
            
            
        print('Bem Vindo ao adivinha paises')
        
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
        area_escolhida_normalizada = ''
        l = 0
        while l < len(area_escolhida):
            if l%3 == 0:
                area_escolhida_normalizada += '.'
            else:
                area_escolhida_normalizada += area_escolhida[l]
            l += 1
            
        lista_dicas_usadas = []
        
        populacao_escolhida = str(dados_pais_escolhido['populacao'])
        populacao_escolhida_normalizada = '' + populacao_escolhida[0]
        f = len(populacao_escolhida) - 1
        
        while f >=  0:
            for letra in populacao_escolhida:
                populacao_escolhida_normalizada += populacao_escolhida
                populacao_escolhida_normalizada += '.'
            
            f -= 3
                    
        continente_escolhido = dados_pais_escolhido['continente']
        
        lista_opcao_dicas = [1,2,3,4,5,0]

            

        
        print(pais_escolhido)
        print(dados_pais_escolhido)
        print (lista_cores_bandeira)
        i = 0
        while i < tentativas:
            print('Numero de tentativas {}'.format(tentativas))
        
            resposta = input('Qual pais voce acha que é? Ou quer uma dica? --> ')
            
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
                    print('Ja tentou esse!')

                elif lista_resposta not in lista_paises_tentados:
                    lista_paises_tentados.append(lista_resposta)
                    
                tentativas -= 1

            if resposta == 'dica':
                #Menu de opções:
                if tentativas > 7 and len(lista_dicas_usadas) == 0:
                    dica = int(input('Escolha a opção [0|1|2|3|4|5]: '))
                elif tentativas > 7 and 3 in lista_dicas_usadas and 4 not in lista_dicas_usadas and 5 not in lista_dicas_usadas:
                    dica = int(input('Escolha a opção [0|1|2|4|5]: '))
                elif tentativas > 7 and 4 in lista_dicas_usadas and 3 not in lista_dicas_usadas and 5 not in lista_dicas_usadas:
                    dica = int(input('Escolha a opção [0|1|2|3|5]: '))
                elif tentativas > 5 and 5 in lista_dicas_usadas and 4 not in lista_dicas_usadas and 3 not in lista_dicas_usadas:
                    dica = int(input('Escolha a opção [0|1|2|3|4]: '))
                elif tentativas > 7 and 3 in lista_dicas_usadas and 4 in lista_dicas_usadas:
                    dica = int(input('Escolha a opção [0|1|2|5]: '))
                elif tentativas > 5 and 3 in lista_dicas_usadas and 5 in lista_dicas_usadas:
                    dica = int(input('Escolha a opção [0|1|2|4]: '))
                elif tentativas > 6 and 4 in lista_dicas_usadas and 5 in lista_dicas_usadas:
                    dica = int(input('Escolha a opção [0|1|2|3]: '))
                elif tentativas > 4:
                    dica = int(input('Escolha a opção [0|1|2]: '))
                elif tentativas > 3:
                    dica = int(input('Escolha a opção [0|2]: '))
                elif tentativas < 3:
                    print('Não consegue comprar dicas!')
                    dica = 0
                    
                if dica == 0:
                    print('Numero de tentativas {}'.format(tentativas))
        
                    resposta = input('Qual pais voce acha que é? Ou quer uma dica? --> ')

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
                        print('Dica já usada!')
                        
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
                    print('Opção Inválida')
                    dica = 0
                    

            if resposta  == pais_escolhido:
                i = 100      
            
            if resposta not in lista_paises and resposta != 'dica':
                print('Resposta Invalida')

        if i == 100:
            print("PARABENS, VOCE ACERTOU!")
            iniciar = input('Desejar jogar novamente? s/n :')
            if iniciar not in ('s','n'):
                    print("Resposta Invalida")
            if iniciar == 'n':
                print('Até Logo!')
                break
        
        if tentativas <= 0: 
            acabou = input('Suas tentativas acabaram, gosteria de reiniciar o jogo? s/n')
            if acabou == 's':
                print (resposta)
            else: 
                print('Obrigada, volte sempre!')
                break
                

    
        
