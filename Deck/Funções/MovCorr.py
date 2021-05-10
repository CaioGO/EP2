def extrai_valor(x):
    c = x[0 : len(x) - 1]
    return c

def extrai_naipe(x):
    j = x[-1]
    return j


def lista_movimentos_possiveis(x, y):
    dev = []
    z = 0
    i = y
    while z < len(x):
        if x[y - i] == x[y]:
            dev.append(z)
            z += 1
            i -= 1
        elif x[y - i] != x[y]:
            if extrai_valor(x[y - i]) == extrai_valor(x[y]):
                dev.append(z)
                z += 1
                i -= 1
            elif extrai_naipe(x[y - i]) == extrai_naipe(x[y]):
                dev.append(z)
                z += 1
                i -= 1
            else:
                z += 1
                i -= 1
        else:
            z += 1
            i -= 1
    
    return dev

x = ['6♥', 'J♥', '9♣', '9♥']
y = 2
print(lista_movimentos_possiveis(x, y))