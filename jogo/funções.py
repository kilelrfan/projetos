from random import randint


def salvar(ouro, hp, nivel, pontos_de_habilidade, defesa, ataque, nome, xp, xp_precisa):
    with open("meuavatar.txt", "w") as meu_avatar:
        meu_avatar.write(f"{ouro};{hp};{nivel};{pontos_de_habilidade};{defesa};{ataque};{nome};{xp};{xp_precisa}")

    print("Salvo!")


def enter():
    input("PRESSIONE ENTER PARA CONTINUAR")


def verStatus(status_do_personagem):
    print("\n" * 10)
    print("=" * 50)
    for item in status_do_personagem:
        print(f"{item:.<25}", end="")
        print(f"{status_do_personagem[item]:.>25}")
    print("=" * 50)
    enter()


def calculoDano(a, b):
    dano = a["atk"] / (1 + b["def"] / 100)
    return dano


def aleatorio(a=0, b=250):
    return randint(a, b)


def subirNivel(nivel, xp, xp_precisa, hp, ataque, defesa):
    xp -= xp_precisa
    if nivel <= 100:
        xp_precisa = int(xp_precisa * 1.1)
        hp = int(hp * 1.05)
        ataque = int(ataque * 1.05)
        defesa = int(defesa * 1.05)
    elif nivel <= 500:
        xp_precisa = int(xp_precisa * 1.02)
        hp = int(hp * 1.01)
        ataque = int(ataque * 1.01)
        defesa = int(defesa * 1.01)
    else:
        xp_precisa = int(xp_precisa * 1.01)
        hp = int(hp * 1.005)
        ataque = int(ataque * 1.005)
        defesa = int(defesa * 1.005)

    return xp, xp_precisa, hp, ataque, defesa

def numerobonito(numero):
    numero = list(str(numero))

    andou = 0

    for d in range(len(numero) - 1, -1, -1):
        andou += 1
        if andou % 3 == 0:
            numero.insert(d, ".")
            d += 1

    numero = "".join(numero)
    return numero
