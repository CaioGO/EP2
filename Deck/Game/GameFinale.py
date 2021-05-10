import random

#Cores
Vermelho   = "\033[1;31m"  
Azul  = "\033[1;34m"
MC = "\033[0;0m"

# Extrai o valor 
def extrai_valor(x):
    c = x[0 : len(x) - 1]
    return c

# Extrai o naipe
def extrai_naipe(x):
    j = x[-1]
    return j

#Criando Deck
def cria_baralho():
    cart = []
    let = ['J', 'Q', 'K', 'A']
    naipes = ['♠', '♥', '♦', '♣']
    baralho = []

    for i in range(2, 11):
        cart.append(str(i))
    
    for j in range(4):
        cart.append(let[j])

    for w in range (4):
        for k in range(13):
            carta = (cart[k] + naipes[w])
            baralho.append(carta)

    random.shuffle(baralho)
    
    for n in range(52):
        print(baralho[n])

    return baralho

print(cria_baralho())
# Movimentos possíveis
def lista_movimentos_possiveis(x, y):
    dev = []
    i = 1

    while i <= 4:
        if x[y - i] == x[y]:
            dev.append(i)
            i += 2
        elif y == 0:
            break

        elif x[y - i] != x[y]:
            if y - i < 0:
                break
            elif extrai_valor(x[y - i]) == extrai_valor(x[y]):
                dev.append(i)
                i += 2
            elif extrai_naipe(x[y - i]) == extrai_naipe(x[y]):
                dev.append(i)
                i += 2
            else:
                i += 2
        else:
            i += 2

    return dev

# Coloração
def cor(car):
    if extrai_naipe(car) == '♠':
        car = Azul + car + MC
    elif extrai_naipe(car) == '♥':
        car = Vermelho + car + MC
    elif extrai_naipe(car) == '♦':
        car = Azul + car + MC
    elif extrai_naipe(car) == '♣':
        car = Vermelho + car + MC

    return car

# Empilha cartas
def empilha(b, x, y):
    b[y] = b[x]
    del b[x]

    return b


# Possui movimentos possíveis
def possui_movimentos_possiveis(bar):

    for e in range(len(bar)):     
        mp = lista_movimentos_possiveis(bar, e)
        if mp != []:
            return True

    return False

def g1(bar):
    
    z = 1
    
    print("Situação: ")

    print("------------")
    
    for b in bar:
        print("{}. {}".format(z,b))
        z += 1

def g2(bar):

    while possui_movimentos_possiveis(bar):
        
        c = int(input("Escolha uma carta (digite um número entre 1 e {}): ".format(len(bar))))
        if c < 1 or c > len(bar) or c != " ":
            c = int(input("Inválido, digite um número entre 1 e {}: ".format(len(bar))))
                
        i = c - 1
        mov = lista_movimentos_possiveis(bar, i)
        print(mov)
        
        if len(mov) == 2:

            print("Sobre qual carta você quer empilhar a carta {}? ".format(bar[i]))

            print("1. {}".format(bar[i - 3]))

            print("2. {}".format(bar[i - 1]))

            a = int(input("Escolha (1/2): "))            
            if a == 1:
                bar[i - 3] = bar[i]
                del(bar[i])
                
            elif a == 2:
                bar[i - 1] = bar[i]
                del(bar[i])
        
        else:
            for z in mov:
                if z == 1:
                    bar = empilha(bar, i, i-1)
                    print(len(bar))
                elif i == 3:
                    bar = empilha(bar, i, i-3)
                    print(len(bar))
        
                else:
                    print("A carta {} não pode ser movida. Escolha outra carta (digite um número entre 1 e {}): ".format(bar[i], len(bar)))
    
    return bar

def g3(bar):

    if bar > 1:

        print("YOU LOSE!")

        print("------------")

        novo_jogo = str(input("Quer jogar de novamente? (s/n): "))

        return novo_jogo

    else:

        print("YOU WIN!")

        print("------------")

        novo_jogo = str(input("Quer de jogar de novamente? (s/n): "))

        return novo_jogo



print("Paciência Acordeão")
print("---------------------")
print("Bem-vindo(a) ao jogo 'Paciência Acordeão', o objetivo é simples:")
print('As 52 cartas de um baralho são embaralhadas e distribuídas em sequência. O objetivo do jogo é colocar todas as cartas em uma mesma pilha.')
print("Há apenas dois movimentos possíveis, e são eles:")
print("1. Empilhar a carta sobre uma imediatamente anterior;")
print("2. Empilhar a carta sobre a terceira anterior.")
print("Para que se possa executar um movimento, ao menos uma condição da lista deve ser atendida:")
print("1. Ambas as cartas possuem o mesmo valor;")
print("2. Ambas cartas possuem o mesmo naipe.")
print('---------------------')



com = int(input("Digite 1 para iniciar o jogo  "))

while com != 1:
    com = int(input("Digite 1 para iniciar o jogo "))


f = True
bar = cria_baralho()

while f:
    bar = g2(bar)
    f = g3(bar)
    
    if f == "s":
        f == True
        bar = cria_baralho()
        
    elif f == "n":
        f == False

print("Volte sempre!")