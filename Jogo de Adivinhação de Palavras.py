'''Jogo de Adivinhação de Palavras'''

# Esse joguinho foi feito com inspiração num projeto do codedex:
# https://github.com/codedex-io
# Nome do projeto original: Build a Word Guessing Game with Python
# https://www.codedex.io/projects/build-a-word-guessing-game-with-python
# Pelo usuário Daniel Li (@realdanielli): https://www.codedex.io/@realdanielli


# Esse joguinho está usando:
# Coleção de dicionários em Portugues (pt-BR)
# https://github.com/fserb/pt-br
# Postado e mantido sobre a licença MIT no GitHub por: @fserb (Fernando Serboncini)
# Copyright 2021 Fernando Serboncini
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files
# (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge,
# publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do
# so, subject to the following conditions:
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
# OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

# Importando 'unicodedata' para padronizar os textos; e usando o '#type: ignore' para ignorar o 'aviso de erro'
import unicodedata #type: ignore
# Importando 're' para filtra o texto padronizado
import re
# Função para padronizar os textos
def textoPadronizado(texto):
    texto = unicodedata.normalize('NFD', texto) # Padrão pra decompor os caracteres (tipo ç -> c)
    texto = texto.encode('ascii', 'ignore').decode('utf-8') # Remove os diacríticos (acento(´), til(~), etc)
    texto = re.sub(r'[^a-zA-Z]', '', texto) # Remove tudo o que não for letra
    return texto.lower() # Coloca tudo em minúsculo

# Importando 'random' para escolher aleatóriamente a palavra
import random

# Importando 'os' para limpar a tela
import os
# Função para limpar a tela
def limparTela():
    os.system('cls' if os.name == 'nt' else 'clear')

# desenhos ASCII que o jogo tem
perdeuFeio = "".join(["\n   _________\n",
                        "  |        |\n",
                        "  | PERDEU |\n",
                        "  |  FEIO! |\n",
                        "  |________|\n",
                        "      |\n",
                        "      |\n",
                        "      |\n",
                        "______|_____\n"])

ganhouBonito = "".join(["\n   ___________\n",
                          "  |          |\n",
                          "  | GANHOU   |\n",
                          "  |  BONITO! |\n",
                          "  |__________|\n",
                          "       |\n",
                          "       |\n",
                          "       |\n",
                          "_______|_____\n"])

homemPalito = ["""               _+______+
                |      |
                |
                |
                |
                |
                |
                |
             ___|_______""",

            """               _+______+
                |      |
                |      O
                |
                |
                |
                |
                |
             ___|_______""",

            """               _+______+
                |      |
                |      O
                |      |
                |      |
                |
                |
                |
             ___|_______""",

            """               _+______+
                |      |
                |      O
                |      |\\
                |      | \\
                |
                |
                |
             ___|_______""",

            """               _+______+
                |      |
                |      O
                |     /|\\
                |    / | \\
                |
                |
                |
             ___|_______""",

            """               _+______+
                |      |
                |      O
                |     /|\\
                |    / | \\
                |      \\ 
                |       \\
                |
             ___|_______""",

            """               _+______+
                |      |
                |      O
                |     /|\\
                |    / | \\
                |     / \\
                |    /   \\
                |
             ___|_______""",]

# Definindo as listas de palavras para o jogo
bancoDePalavras = [] # Lista de palavras
# Ler linha por linha dos arquivos de palavras: 'verbos.txt' ou 'conjugações.txt' e adiciona no banco de palavras;
# Mas se quiser, pode colocar as palavras manualmente no: 'bancoDePalavras = []'
with open('verbos.txt', 'r') as arquivo:
    for linha in arquivo:
        bancoDePalavras.append(linha.strip())
bancoDeErros = []
bancoDasUsadas = []

# Escolhendo uma palavra aleatória do banco de palavras
palavra = random.choice(bancoDePalavras)

# Guardando e padronizando a palavra escolhida
palavraOriginal = palavra
palavra = textoPadronizado(palavra)

#  Colocar um "espaço reservado" para as letras que ainda não foram adivinhadas
palavraAdivinhada = ["_"] * len(palavra)

#  Tentativas do jogador
tentativas = 6

#  Loop do jogo
while tentativas > 0:

# Mostrar a palavra atual com as letras adivinhadas e os espaços reservados
    print("Palavra atual: " + " ".join(palavraAdivinhada))

# Escrever qual a próxima letra a ser adivinhada; Quantas tentativas o jogador ainda tem; Padroniza o que foi digitado;
    print("Você tem: " + str(tentativas) + " tentativas restantes")
    adivinhar = input("Escolha uma letra / palavra: ").lower()
    adivinhar = textoPadronizado(adivinhar)

# Se o jogador escolheu a mesma palavra
    if adivinhar in bancoDasUsadas:
        limparTela()
        print("A Letra / palavra: '" + adivinhar + "', já foi escolhida. Tente outra!")
        continue

# Se o jogador acertou a letra
    if adivinhar in palavra:
        limparTela()
        for i in range(len(palavra)):
            if palavra[i] == adivinhar:
                palavraAdivinhada[i] = adivinhar
        bancoDasUsadas.append(adivinhar)
        print("\n🔥Você acertou!")

# Se o jogador errou a letra
    else:
        limparTela()
        tentativas -= 1
        print("\n💥Errou! Você ainda tem: " + str(tentativas) + " tentativas")
        bancoDeErros.append(adivinhar)
        bancoDasUsadas.append(adivinhar)
        print("Letras / palavras erradas: '" + "', '".join(bancoDeErros))
        contagem = 6 - tentativas
        print(homemPalito[contagem])
    
# Se o jogador adivinhou todas as letras, de uma só vez; Ganhou o jogo
    if adivinhar == palavra:
        limparTela()
        palavraAdivinhada = list(palavra)
        print("\n🏆 Parabéns! Você adivinhou a palavra toda: " + palavraOriginal + " 🏆")
        print(ganhouBonito)
        break

# Se o jogador adivinhou todas as letras, separadamente; Ganhou o jogo
    if "_" not in palavraAdivinhada:
        limparTela()
        print("\n🏆Parabéns! Você adivinhou a palavra: " + palavraOriginal)
        print(ganhouBonito)
        break

# Se o jogador não tiver mais tentativas; Perdeu o jogo
else:
    limparTela()
    print("\n💀Você não tem mais tentativas! A palavra era: " + palavraOriginal)
    print(perdeuFeio)
# # Fim do jogo #                   __
#                                  / /
#                                 /_/
#  ______      ___          ________
# /  __  \     |  \        /   ___  \
# | /  \ |     |  |        |  /   \  |
# | |  | |     |  |        |  \___/  |
# | \__/ |     |  |____    |   ___   |
# \______/     \______/    |__|   |__|
#   _____________       ___   ___       ________      __________        ______
# /   __    __   \     |  |  |  |     /   __   \     |   ____   \      /  __  \
# |  /  \  /  \  |     |  |  |  |     |  /  \  |     |  |    \   \     | /  \ |
# |  |  |  |  |  |     |  |  |  |     |  |  |  |     |  |     |  |     | |  | |
# |  |  |  |  |  |     |  \__/  |     |  |  |  |     |  |_____/  /     | \__/ |
# |__|  |__|  |__|     \________/     |__|  |__|     |__________/      \______/
