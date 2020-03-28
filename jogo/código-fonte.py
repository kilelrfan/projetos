from random import randint
import time
import os
from jogo import funções

def tempo():
    time.sleep(2)


inimigos = {1 : {"hp" : 500, "ataque" : 50}, 2 : {"hp" : 400, "ataque" : 70}, 3 : {"hp" : 700, "ataque" : 30}}

#       Menu do jogo

if os.path.exists("meuavatar.txt"):# retorna verdadeiro se existir
    print("1 - Novo jogo".center(90))
    print("2 - Continuar".center(90))
    escolha = int(input())
#if os.path.isfile("meuavatar.txt") só retorna verdadeiro se for um arquivo

else:
    escolha = 1



while escolha == 1:
    nome = input("Qual o seu nome? ")

    status_do_personagem = {
    "ouro" : 0,
    "hp" : 500,
    "nivel" : 1,
    "pontos_habilidade" : 10,
    "defesa" : 100,
    "ataque" : 100,
    "nome" : nome,
    "xp" : 0,
    "xp_precisa" : 300
    }

    print("\n"*10)
    print("Tudo ok!".center(90))
    funções.enter()
    print("Agora vamos nessa!". center(90))
    tempo()
    print("\n"*20)
    escolha = 2

    with open("meuavatar.txt", "w") as meu_avatar:
        for item in status_do_personagem:
            meu_avatar.write(f"{status_do_personagem[item]};")
    escolha = 2


    '''
        for i in personagens:
            if personagens[i] == escolhido:
                meu_avatar.write(f"{i}")
                break
'''


while escolha == 2:
    with open("meuavatar.txt", "r") as meu_avatar:
        linha = meu_avatar.readline().split(";")
        ouro = int(linha[0])
        hp = int(linha[1])
        nivel = int(linha[2])
        pontos_de_habilidade = int(linha[3])
        defesa = int(linha[4])
        #ataques = [int(a) for a in linha[2].strip("[]").split(", ")] # ou list(map(int, linha[2].strip("[]").split(", "))
        ataque = int(linha[5])
        nome = linha[6]
        xp = int(linha[7])
        xp_precisa = int(linha[8])

    print(f"Bem vindo {nome}!".center(90))
    print("\n"*4)
    tempo()
    print("\n"*20)

    status_do_personagem = {
    "Ouro" : ouro,
    "Hp" : hp,
    "Nivel" : nivel,
    "Pontos_de_habilidade" : pontos_de_habilidade,
    "Defesa" : defesa,
    "Ataque" : ataque,
    "Nome" : nome,
    "Xp que precisa" : funções.numerobonito(xp_precisa - xp)
    }


    while True:
        while xp_precisa - xp <= 0:
            nivel += 1
            xp, xp_precisa, hp, ataque, defesa = funções.subirNivel(nivel, xp, xp_precisa, hp, ataque, defesa)
            print(f"PARABÉNS POR CHEGAR AO NÍVEL {nivel}")
            pontos_de_habilidade += 3


        status_do_personagem = {
            "Ouro": ouro,
            "Hp": hp,
            "Nivel": nivel,
            "Pontos_de_habilidade": pontos_de_habilidade,
            "Defesa": defesa,
            "Ataque": ataque,
            "Nome": nome,
            "Xp que precisa": funções.numerobonito(xp_precisa - xp)
        }
        
        print("O que deseja fazer?\n".center(100))
        print(f"1 - Batalhar".center(20), f"2 - Salvar".center(20), f"3 - Sair".center(20), f"4 - Status".center(20), f"5 - Loja".center(20))
        print("\n"*4)
        n = int(input("Sua escolha: "))

        if n == 1:
            xp += 300
            ouro += 15
            
        if n == 2:
            print("SALVANDO...")
            tempo()
            print("\n"*10)
            funções.salvar(ouro,hp,nivel,pontos_de_habilidade,defesa,ataque,nome, xp, xp_precisa)
            funções.enter()
            print("\n"*10)
        
        elif n == 3:
            escolha = 3
            print("SAINDO...")
            break
        elif n == 4:
            funções.verStatus(status_do_personagem)
            print("\n"*10)

if escolha == 3:
    tempo()
    print("\n"*10)
    print("Até mais!".center(90))
