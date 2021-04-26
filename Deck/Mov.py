def extrai_valor(x):
    c = x[0 : len(x) - 1]
    return c

def extrai_naipe(x):
    j = x[-1]
    return j


def lista_movimentos_possiveis(x):
    dev = []
    z = 0
    e = 1
    i = 1
    for e in x:    
        v = extrai_valor(e)
        n = extrai_naipe(e)
        for i in range(len(e)):
            if e[i - 1] == e[i]:
                dev.append(z)
                z += 1
            elif e[i - 1] != e[i]:
                if v(e[i]) == v(e[i - 1]):
                    dev.append(z)
                    z += 1
                elif n(e[i]) == n(e[i - 1]):
                    dev.append(z)
                    z += 1
    
    return dev


x = ['Q♠', 'A♦', 'K♣', 'K♥', '3♦', 'A♥', 'Q♦', '10♠', '7♦', 'A♠', '7♥', 'J♦', '8♣', '9♣', 'A♣', 'K♦', 'J♥', '4♦', '4♥', '2♦', '10♥', '8♦', '8♥', '6♠', '2♠', '3♠', 'J♠', '10♦', '7♠', '3♥', '5♠', '4♣', '2♥', '2♣', '9♠', '7♣', '4♠', 'K♠', '10♣', '9♦', '3♣', '5♦', '5♣', '6♥', 'Q♣', '5♥', '9♥', '6♦', 'J♣', '8♠', 'Q♥', '6♣']
print(lista_movimentos_possiveis(x))