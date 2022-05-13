#Para representar uma cor em python:
#\033[style;text;backm
#Exemplo:
    #\033[0;33;44m

#Style:
    # 0 : estilo nenhum  
    # 1 : coloca em negrito
    # 4 : sublinhado
    # 7 : o que vc colocou para a letra vai p fundo e vs

#Text / cores:
    # 30 : branco (padrao)
    # 31 : vermelho 
    # 32 : verde
    # 33 : amarelo
    # 34 : azul
    # 35 : magenta
    # 36 : ciano 
    # 37 : cinza 

#Back gound:
    # 40 : branco (padrao)
    # 41 : vermelho 
    # 42 : verde
    # 43 : amarelo
    # 44 : azul
    # 45 : magenta
    # 46 : ciano 
    # 47 : cinza 

#Teste 1: fundo vermelho com letra branca
    #\033[0;30;41m

#Teste  2: fundo azul com letra amarela sublinhado
    #\033[4;33;44m

#Teste 3: fundo amarelo com letra roxa em negrito
    #\033[1;35;43m

print('\033[4;30;40mOlá Mundo\033[m')