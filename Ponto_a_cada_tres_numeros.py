def normalizar(dica_nao_normalizada):
            dica_normalizada = ''
            l = len(dica_nao_normalizada) - 1
            while l >= 0:
                
                if l != len(dica_nao_normalizada) - 1  and l == len(dica_nao_normalizada) - 3 or l == len(dica_nao_normalizada) - 6 or l == len(dica_nao_normalizada) - 9 or l == len(dica_nao_normalizada) - 12 or l == len(dica_nao_normalizada) - 15:
                    dica_normalizada += dica_nao_normalizada[l]
                    dica_normalizada += '.'
                else:
                    dica_normalizada += dica_nao_normalizada[l]
                l -= 1
                dica_real = dica_normalizada[::-1]
            if dica_real[0] == '.':
                return dica_real[1:]
            else:
                return dica_real
            
            
def tira_virgula_normaliza(km):
    str_km = str(km)
    km_sem_virgula = ''
    i = 0
    while True:
        if str_km[i] != '.':
            km_sem_virgula += str_km[i]
            i += 1
        if str_km[i] == '.':
            break
        
    km_normalizado = normalizar(km_sem_virgula)
    return km_normalizado