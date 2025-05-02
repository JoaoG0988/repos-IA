def check_rainhas(rainhas, nova_rainha):
    #Faca seu codigo aqui
    for i in range(len(rainhas)):
        l = rainhas[i][0]
        c = rainhas[i][1]
        if nova_rainha[0] == l or nova_rainha[1] == c:
            return False
        elif (l-c) == (nova_rainha[0]-nova_rainha[1]):
            return False
        elif (l+c) == (nova_rainha[0]+nova_rainha[1]):
            return False
    return True


print(check_rainhas([(2, 2)], (4, 4)))
