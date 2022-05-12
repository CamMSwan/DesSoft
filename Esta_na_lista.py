def esta_na_lista(pais,lista_pais):
    for paises in lista_pais:
        for Pais in paises:
            if pais == Pais:
                return True
        
    else:
        return False
        