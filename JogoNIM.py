def computador_escolhe_jogada(n, m):
    computador_remove = 1

    while computador_remove != m:
        if (n - computador_remove) % (m + 1) == 0:
            return computador_remove

        else:
            computador_remove += 1

    return computador_remove

def usuario_escolhe_jogada(n, m):
    jogada_valida = False

    while not jogada_valida:
        jogador_remove = int(input("Quantas peças você vai tirar? "))
        if jogador_remove > m or jogador_remove < 1:
            print()
            print("Oops! Jogada inválida! Tente de novo.")
            print()

        else:
            jogada_valida = True

    return jogador_remove

def campeonato():
    numero_rodada = 1
    while numero_rodada <= 3:
        print()
        print("**** Rodada", numero_rodada, "****")
        print()
        partida()
        numero_rodada += 1
    print()
    print("Placar: você 0 x 3 Computador")

def partida():
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))

    vezDoPC = False

    if n % (m+1) == 0:
        print()
        print("Você começa!")
    else:
        print()
        print("Computador começa!")
        vezDoPC = True

    while n > 0:
        if vezDoPC:
            computador_remove = computador_escolhe_jogada(n, m)
            n = n - computador_remove
            if computador_remove == 1:
                print()
                print("O computador tirou uma peça.")
            else:
                print()
                print("O computador tirou", computador_remove, "peças.")
                
            vezDoPC = False
        else:
            jogador_remove = usuario_escolhe_jogada(n, m)
            n = n - jogador_remove
            if jogador_remove == 1:
                print()
                print("Você tirou uma peça.")
            else:
                print()
                print("Você tirou", jogador_remove, "peças.")
            vezDoPC = True
        if n == 1:
            print("Agora resta apenas uma peça no tabuleiro.")
            print()
        else:
            if n != 0:
                print("Agora restam", n, "peças no tabuleiro.")
                print()

    print("Fim do jogo! O computador ganhou!")
    
print("Bem-vindo ao jogo do NIM! Escolha: ")
print()

print("1 -para jogar uma partida isolada")
tipoDePartida = int(input("2 - para jogar um campeonato "))

if tipoDePartida == 2:
    print()
    print("Você escolheu um campeonato!")
    print()
    campeonato()
else:
    if tipoDePartida == 1:
        print()
        partida()