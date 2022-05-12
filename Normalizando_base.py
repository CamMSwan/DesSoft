def normaliza(continentes):
    dic_novo = {}
    for continente, paises in continentes.items():
        for pais, info in paises.items():
            info['continente'] = continente
            dic_novo[pais] = info
    return dic_novo       