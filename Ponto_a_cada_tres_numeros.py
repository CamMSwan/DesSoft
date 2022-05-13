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
            return dica_real