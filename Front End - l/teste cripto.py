import numpy as np

# dicionário
mapeamento = {
    # números
    '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
    # letras maiúsculas
    'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15, 'G': 16, 'H': 17, 'I': 18, 'J': 19,
    'K': 20, 'L': 21, 'M': 22, 'N': 23, 'O': 24, 'P': 25, 'Q': 26, 'R': 27, 'S': 28, 'T': 29,
    'U': 30, 'V': 31, 'W': 32, 'X': 33, 'Y': 34, 'Z': 35,
    # símbolos especiais
    '-': 36, '.': 37, ' ': 38, '$': 39, '/': 40, '+': 41, '%': 42
}

# para decodificação
inverso = {v: k for k, v in mapeamento.items()}

# matriz de criptografia
A = np.array([[5, 4], [3, 3]])


# função para calcular a matriz inversa modular
def matriz_inversa_modular(matriz, modulo):
    det = int(np.round(np.linalg.det(matriz))) % modulo
    det_inverso = pow(det, -1, modulo)
    matriz_adjunta = np.array([[matriz[1, 1], -matriz[0, 1]], [-matriz[1, 0], matriz[0, 0]]])
    return (det_inverso * matriz_adjunta) % modulo


# calcula a matriz inversa
AI = matriz_inversa_modular(A, 43)


def codificar(mensagem):
    mensagem = mensagem.upper()
    caracteres_validos = set(mapeamento.keys())

    # verifica caracteres inválidos
    for c in mensagem:
        if c not in caracteres_validos:
            raise ValueError(f"Caractere inválido: '{c}'")

    # se quantidade não for par, repete o último caractere
    if len(mensagem) % 2 != 0:
        mensagem += mensagem[-1]

    # converter para números
    I = [mapeamento[c] for c in mensagem]

    # criar matriz de pares
    P = []
    for i in range(len(I) // 2):
        k = 2 * i
        P.append([I[k], I[k + 1]])
    P = np.array(P).T

    # codificar
    C = np.dot(A, P) % 43

    # converter para texto
    C = C.T
    TC = []
    for i in range(len(I) // 2):
        TC.extend(C[i, :])
    codificado = [inverso[int(i)] for i in TC]

    return ''.join(codificado)


def decodificar(codificado):
    # verifica comprimento par
    if len(codificado) % 2 != 0:
        raise ValueError("Mensagem codificada deve ter comprimento par")

    # converter para números
    I = [mapeamento[c] for c in codificado]

    # criar matriz de pares
    C = []
    for i in range(len(I) // 2):
        k = 2 * i
        C.append([I[k], I[k + 1]])
    C = np.array(C).T

    # decodificar
    P = np.dot(AI, C) % 43

    # converter para texto
    P = P.T
    TC = []
    for i in range(len(I) // 2):
        TC.extend(P[i, :])
    decodificado = [inverso[int(i)] for i in TC]

    # Verifica se o último caractere foi repetido (padding)
    if len(decodificado) > 1 and decodificado[-1] == decodificado[-2]:
        decodificado = decodificado[:-1]

    return ''.join(decodificado)


# exemplo específico p bom dia 12
if __name__ == "__main__":
    mensagem_original = 'BOM DIA 12'
    print(f"Mensagem original: {mensagem_original}")

    # Codificação
    try:
        # tem 9 caracteres (será repetido o ultimo caracter)
        mensagem_codificada = codificar(mensagem_original)
        print(f"Mensagem codificada: {mensagem_codificada}")

        # decodificação
        mensagem_decodificada = decodificar(mensagem_codificada)
        print(f"Mensagem decodificada: {mensagem_decodificada}")

    except ValueError as e:
        print(f"Erro: {e}")