from datetime import date # obtém datas
import os
from tabulate import tabulate # criação de tabelas no console
import time # delay durante a execução do programa
import mysql.connector # conexão com o bd e uso de SQL
import numpy as np # utilização de matrizes 

# dicionário para criptografia
mapeamento = {
    # números
    '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
    # letras maiúsculas
    'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15, 'G': 16, 'H': 17, 'I': 18, 'J': 19,
    'K': 20, 'L': 21, 'M': 22, 'N': 23, 'O': 24, 'P': 25, 'Q': 26, 'R': 27, 'S': 28, 'T': 29,
    'U': 30, 'V': 31, 'W': 32, 'X': 33, 'Y': 34, 'Z': 35,
    # letras minúsculas
    'a': 36, 'b': 37, 'c': 38, 'd': 39, 'e': 40, 'f': 41, 'g': 42, 'h': 43, 'i': 44, 'j': 45,
    'k': 46, 'l': 47, 'm': 48, 'n': 49, 'o': 50, 'p': 51, 'q': 52, 'r': 53, 's': 54, 't': 55,
    'u': 56, 'v': 57, 'w': 58, 'x': 59, 'y': 60, 'z': 61,
    # símbolos especiais
    '-': 62, '.': 63, '%': 64, '$': 65, '/': 66, '+': 67, '!': 68
}

# para decodificação
inverso = {v: k for k, v in mapeamento.items()}

# matriz de criptografia (precisa ser invertível módulo 69)
A = np.array([[2, 3], [1, 4]])

# montar a matriz inversa no mod69
def inversa_modular(matriz, modulo):
    det = int(np.round(np.linalg.det(matriz))) % modulo
    det_inverso = pow(det, -1, modulo)
    matriz_adjunta = np.array([[matriz[1, 1], -matriz[0, 1]],
                               [-matriz[1, 0], matriz[0, 0]]])
    return (det_inverso * matriz_adjunta) % modulo

def criptografar(texto):
    # adiciona '!' se o comprimento do nome for ímpar
    if len(texto) % 2 != 0:
        texto += '!'  # Adiciona '!' apenas internamente
    
    # converte os caracteres para números
    I = [mapeamento[c] for c in texto if c in mapeamento]

    # garante que I tem tamanho par
    if len(I) % 2 != 0:
        I.append(mapeamento['!'])  # Adiciona '!' se necessário
    
    # monta matriz 2xN
    P = np.array([I[i::2] for i in range(2)])

    # codifica
    C = np.dot(A, P) % 69

    # converte de volta para texto codificado
    texto_codificado = ''.join([inverso[num] for num in C.flatten('F')])
    return texto_codificado

def descriptografar(codificado):
    # verifica se é par
    if len(codificado) % 2 != 0:
        raise ValueError("Texto codificado deve ter comprimento par")

    # converte para números
    I = [mapeamento[c] for c in codificado]

    # coloca em em matriz 2xN
    C = np.array([I[i::2] for i in range(2)])

    # decodifica
    A_inv = inversa_modular(A, 69)
    P = np.dot(A_inv, C) % 69

    # converte de volta para texto
    texto_decodificado = ''.join([inverso[int(num)] for num in P.flatten('F')])

    # remove o '!' adicional se existir no final
    if texto_decodificado.endswith('!'):
        texto_decodificado = texto_decodificado[:-1]

    return texto_decodificado

def limpar_tela():
    time.sleep(1) # aguarda por 1 segundos
    os.system('cls' if os.name == 'nt' else 'clear') #limpa o console

conexao = mysql.connector.connect(
    host="localhost", #Usando a rede local
    user="root",
    password="1234", #Trocar ??? quando for testar
    database="pi1"
)

cursor = conexao.cursor()

conexao = mysql.connector.connect(
    host="localhost", #Usando a rede local
    user="root",
    password="???", #Trocar ??? quando for testar
    database="pi1"
)

cursor = conexao.cursor()

limpar_tela()

print('\t\t\t\t\t==========================================================')
print('\t\t\t\t\t|  BEM-VINDO AO SISTEMA DE CÁLCULO DE SUSTENTABILIDADE  |')
print('\t\t\t\t\t==========================================================')

print('\n                                          OBJETIVO:')
print('====================================================================================================')
print('| ATRIBUIR, POR MEIO DE CÁLCULOS E PARÂMETROS PRÉ DEFINIDOS, UMA NOTA DE 1 A 5 DE SUSTENTABILIDADE,|')
print('| ALÉM DE RELATÓRIOS, GRÁFICOS E RECOMENDAÇÕES, COM O FITO DE ESTIMULAR O CRESCIMENTO SUSTENTÁVEL! |')
print('====================================================================================================')
print('| PARA CÁLCULO MAIS PRECISO, CONFIRA A ABA PARÂMETROS PARA REALIZAR AS MEDIÇÕES DE CONSUMO.        |')
print('====================================================================================================')

nota_sus = 0 # média geral do usuário

# ADICIONAR EMAIL P/ RECUPERAÇÃO DE SENHA
def cadastro():
    limpar_tela()
    print('\n                                              CADASTRO                                              ')
    print('====================================================================================================')
    Iusuario = input('* Digite um nome de usuário: ')
    usuario=''
    #verifica se os caracteres estão no mapeamento da criptografia ou não
    for i in Iusuario:
        #caso válido, é adicionado
        if i in mapeamento and i!='!':
            usuario+=i
        #caso inválido, o cadastro não é efetuado
        else:
            print(f"Caracter: {i} não é válido")
            return
    
    #garante que o usuário não é vazio
    if usuario == '':
        return
    
    #verifica os usuarios
    cursor.execute("select u_usuario from usuario") 
    for i in cursor: #percorre o select
        if usuario == descriptografar(i[0]):
            cursor.fetchall() #limpando cursor
            print('* ❌ Erro: Usuário já existe!')
            return

    senha = input('* Digite uma senha: ')
    senha2 = input('* Confirme a senha: ')

    if senha != senha2:
        print('* ❌ Erro: As senhas não coincidem!')
    else:
        #adicionando no banco de dados criptografado
        usuario_cripto = criptografar(usuario)
        senha_cripto = criptografar(senha)
        cursor.execute("insert into usuario (u_usuario,u_senha,u_nota) values (%s,%s,0)", (usuario_cripto,senha_cripto))
        conexao.commit()
        print('* ✅ Cadastro realizado com sucesso!')
    print('====================================================================================================')

# ADICIONAR OPÇÃO P RECUPERAR SENHA
def login():
    limpar_tela()
    print('\n                                           LOGIN')
    print('====================================================================================================')
    usuario = input('* Usuário: ')
    senha = input('* Senha: ')

    # percorre por todos os usuarios
    cursor.execute("SELECT u_usuario, u_senha, u_nota FROM usuario")
    encontrado = False # para caso não ache usuário no bd

    for i in cursor:
        try:
            # descriptografa os dados do banco
            usuario_bd = descriptografar(i[0])
            senha_bd = descriptografar(i[1])

            # Compara com as entradas do usuário
            if usuario == usuario_bd and senha == senha_bd:
                print(f' ✅ Login bem-sucedido! Bem-vindo, {usuario}!')
                print(
                    '====================================================================================================')
                cursor.fetchall()  # limpando cursor
                menu_login(usuario)
                encontrado = True
                break
        except Exception as e:
            print(f"Erro ao descriptografar: {e}")
            continue

    if not encontrado:
        print('* ❌ Erro: Usuário ou senha incorretos!')
        print('====================================================================================================')
        input('Pressione ENTER para continuar...')

def area_login():
    while True:
        limpar_tela()
        print('                                            ÁREA DE LOGIN                                           ')
        print('====================================================================================================')
        print('|             1. Cadastrar         |          2. Login          |          3. Sair                 |')
        print('====================================================================================================')

        opcao = input('Escolha uma opção (1-3): ')

        if opcao == '1':
            cadastro()
        elif opcao == '2':
            login()
        elif opcao == '3':
            print('Saindo do sistema...')
            break
        else:
            print('⚠️ Opção inválida! Tente novamente.')

def parametros(usuario):
    while True:
        limpar_tela()
        tabela_parametros = [
            {
                'titulo': '1. CONSUMO DE ÁGUA',
                'descricao': 'Medido em litros por dia (L/dia) atráves do hidrômetro',
                'dados': [
                    ['Faixa de Consumo', 'Nota', 'Classificação'],
                    ['Mais de 250L', 1, 'Alto consumo'],
                    ['Entre 250 a 200L', 2, 'Consumo elevado'],
                    ['Entre 199 a 150L', 3, 'Consumo moderado'],
                    ['Entre 149 a 100L', 4, 'Baixo consumo'],
                    ['Menos que 100L', 5, 'Consumo excelente']
                ]
            },
            {
                'titulo': '2. CONSUMO DE ENERGIA',
                'descricao': 'Medido em kWh/dia, obtido na conta de luz',
                'dados': [
                    ['Faixa de Consumo', 'Nota', 'Classificação'],
                    ['Mais que 15kW', 1, 'Alto consumo'],
                    ['Entre 15 a 12kW', 2, 'Consumo elevado'],
                    ['Entre 11 a 8kW', 3, 'Consumo moderado'],
                    ['Entre 8 a 5 kW', 4, 'Baixo consumo'],
                    ['Menos que 5kW', 5, 'Consumo excelente']

                ]
            },
            {
                'titulo': '3. USO DE TRANSPORTES',
                'descricao': 'Baseado no tipo de transporte utilizado regularmente',
                'dados': [
                    ['Tipo de transporte', 'Nota', 'Classificação'],
                    ['Transporte privado', 1, 'Alto impacto'],
                    ['Misto (público e privado)', 2, 'Impacto elevado'],
                    ['Transporte público', 3, 'Impacto moderado'],
                    ['Transporte elétrico', 4, 'Baixo impacto'],
                    ['Bicicleta/caminhada', 5, 'Nenhum impacto']
                ]
            },

            {
                'titulo': '4. LIXO RECICLÁVEL',
                'descricao': 'Baseado no percentual em relação ao total de lixo produzido por dia',
                'dados': [
                    ['Percentual', 'Nota', 'Classificação'],
                    ['Menos que 20%', 1, 'Alto impacto'],
                    ['Entre 20 a 30%', 2, 'Impacto elevado'],
                    ['Entre 31 a 40%', 3, 'Impacto moderado'],
                    ['Entre 41 a 50%', 4, 'Baixo impacto'],
                    ['Mais que 50%', 5, 'Impacto irrelevante']
                ]
            }
        ]

        print('\n' + '=' * 60)
        print(f'| Olá, {usuario}!                                          |')
        print('|       PARÂMETROS DE AVALIAÇÃO DE SUSTENTABILIDADE        |')
        print('|' + '-' * 58 + '|')
        print('|   A NOTA FINAL SERÁ OBTIDA A PARTIR DA MÉDIA ARITMÉTICA  |')
        print('=' * 60)

        for i in tabela_parametros:
            print(f'\n{i["titulo"]}')
            print(f'Descrição: {i["descricao"]}')
            print(tabulate(i["dados"], headers='firstrow', tablefmt='grid'))
        opcao = input('\nAperte ENTER para retornar ao menu: ')
        if opcao == '':
            return

def menu_login(usuario):
    while True:
        limpar_tela()
        nota_sus = calcular_sus(usuario)
        print('\n                                                MENU                                                ')
        print('====================================================================================================')
        print(f'| * Usuário: {usuario:<55} Nota: {round(nota_sus,2) if nota_sus is not None else 0:<23} |')
        print('|--------------------------------------------------------------------------------------------------|')
        print('|    1. Cadastro de informações | 2. Lista de gráficos | 3. Ações (recomendações) | 4. Relatório   |')
        print('|                                  5. Parâmetros   |    6. Sair                                    |')
        print('====================================================================================================')

        opcao = input('Escolha uma opção (1-6): ')
        if opcao == '1':  # por as outras opções em cima, em ordem(depois substituir por elif)
            print('Navegando para tela de cadastro...')
            cadastro_tela(usuario)
        elif opcao == '2':
            grafico(usuario)
        elif opcao == '3':
             mostrar_tela_recomendacoes(usuario)
        if opcao=='4':
            Tabela_relatorio(usuario)
        elif opcao == '5':
            parametros(usuario)
        elif opcao == '6':  # por as outras opções em cima, em ordem(depois substituir por elif)
            print('Voltando a área de login...')
            break

def cadastro_tela(usuario): #Tela do cadastro
    while True:
        limpar_tela()
        nota_sus = calcular_sus(usuario)
        print('\n                                       CADASTRO DE INFORMAÇÕES                                      ')
        print('====================================================================================================')
        print(f'| * Usuário: {usuario:<55} Nota: {round(nota_sus,2) if nota_sus is not None else 0:<24}|')
        print('|--------------------------------------------------------------------------------------------------|\n')

        data=date.today() #pegando data atual ejá convertendo para string
        print(f'Data do registro: {data.strftime("%Y-%m-%d")}\n')

        #procurando id do usuário
        cursor.execute("select u_id from usuario where u_usuario = %s", (criptografar(usuario),))
        for i in cursor:
            id_usuario=i[0]
        registro = cadastro_calculo(usuario, data) #chamando a funcao
        
        #fazendo o registro
        cursor.execute("insert into registro (r_usuarioId,r_data,r_energia,r_agua,r_residuo,r_transporte,r_media)" \
        "values (%s,%s,%s,%s,%s,%s,%s)", (id_usuario,registro[0],registro[1],registro[2],registro[3],registro[4],registro[5])) #faço o registro
        conexao.commit()

        nota_sus = calcular_sus(usuario) #calculo da nota geral
        calculo = calcular_nota(registro[1],registro[2],registro[3],registro[4]) #calculo da nota do registro
        print(f'\nNota energia:  {calculo[0]}') #apresento a nota
        print(f'Nota água:       {calculo[1]}')
        print(f'Nota resíduo:    {calculo[2]}')
        print(f'Nota transporte: {calculo[3]}')
        print(f'Nota média:      {calculo[4]}') 

        input("\nPressione qualquer tecla para voltar para o menu: ")
        menu_login(usuario) #voltando para o menu
        return

def cadastro_calculo(usuario, data): #Entrada de dados e cálculo das notas
    try:
        energia=float(input("Informe seu consumo de energia (kW/dia): "))
        agua=float(input("Informe seu consumo de água (L/dia): "))
        residuo=float(input("Informe sua geração de resíduos recicláveis (%): "))
        if(energia<0 or agua<0 or residuo<0):
            raise
        #cabeçalho explicando o último input
        print("\nPV - Privado\nPVU - Público e privado\nPU - Público\nE - Elétrico\nBC - Bicleta e/ou caminhada") 
        transporte=input("Informe o tipo de transporte utilizado (PV/PVU/PU/E/BC): ").upper() #upper() transforma em maiúsculo
            
        #Verificando se a opção do transporte é válida
        if transporte not in ["PV", "PVU", "PU", "E", "BC"]: 
            raise #Leva para o except
    except:
        print("\nValor inválido inserindo, voltando para o menu...")
        menu_login(usuario) #voltando para o menu
        return

    registro = [] #inicializando vetor
    media = []

    media[:] = calcular_nota(energia,agua,residuo,transporte)
    #formato: [data, energia, água, resíduo, transporte, sustentabilidade]
    registro[:] = (data.strftime("%Y-%m-%d"),energia,agua,residuo,transporte,media[4]) #atribui data e os retornos da função no vetor calculo
    return registro

def calcular_sus(usuario):
    nota_sus=0
    #pegando média
    cursor.execute("select avg(registro.r_media) from usuario, registro " \
    "where usuario.u_id = registro.r_usuarioId and usuario.u_usuario= %s", (criptografar(usuario),))
    for i in cursor:
        nota_sus=i[0]

    #atualizando a tabela
    cursor.execute("update usuario set u_nota = %s where u_usuario = %s", (nota_sus,criptografar(usuario)))
    conexao.commit()
    return nota_sus

#Cálculo da nota dos parâmetros
def calcular_nota(energia, agua, residuo, transporte):
    # Cálculo do parâmetro de água
    if (agua > 250):
        n_agua = 1
    elif (agua >= 200 and agua <= 250):
        n_agua = 2
    elif (agua >= 150 and agua <= 199):
        n_agua = 3
    elif (agua >= 100 and agua <= 149):
        n_agua = 4
    else:
        n_agua = 5

    # Cálculo do parâmetro de energia
    if (energia > 15):
        n_energia = 1
    elif (energia >= 12 and energia <= 15):
        n_energia = 2
    elif (energia >= 8 and energia <= 11):
        n_energia = 3
    elif (energia >= 5 and energia <= 8):
        n_energia = 4
    else:
        n_energia = 5

    # Cálculo do parâmetro de resíduos
    if (residuo > 50):
        n_residuo = 5
    elif (residuo >= 41 and residuo <= 50):
        n_residuo = 4
    elif (residuo >= 31 and residuo <= 40):
        n_residuo = 3
    elif (residuo >= 20 and residuo <= 30):
        n_residuo = 2
    else:
        n_residuo = 1

    # Cálculo do parâmetro de transporte
    if (transporte == 'PV'):
        n_transporte = 1
    elif (transporte == 'PVU'):
        n_transporte = 2
    elif (transporte == 'PU'):
        n_transporte = 3
    elif (transporte == 'E'):
        n_transporte = 4
    elif (transporte == 'BC'):
        n_transporte = 5

    # Média geral
    n_sustentabilidade = (n_energia + n_agua + n_residuo + n_transporte) / 4
    return n_energia, n_agua, n_residuo, n_transporte, n_sustentabilidade

def grafico(usuario):
    calcular_sus(usuario)
    limpar_tela()
    print('\n                                          GRÁFICO DE NOTAS                                          ')
    print('====================================================================================================')
    print('|                     GRÁFICO CONSTRUIDO COM BASE NOS ÚLTIMOS 5 REGISTROS                          |')
    print('====================================================================================================')

    #identifica o id do usuário
    cursor.execute("select u_id from usuario where u_usuario = %s", (criptografar(usuario),))
    for i in cursor:
        id_usuario=i[0]

    #verifica se há registros
    cursor.execute("select r_id from registro where r_usuarioId = %s", (id_usuario,))
    select = cursor.fetchone()
    if select is None: #caso não houver
        print("* ❌ Nenhum dado de sustentabilidade encontrado.")
        input("\nPressione ENTER para voltar...")
        return
    cursor.fetchall()

    # pegar os ultimos 5 registros
    cursor.execute("select r_data, r_media from registro " \
    "where r_usuarioId = %s " \
    "order by r_data desc " \
    "limit 5", (id_usuario,))

    datas = []
    notas = []
    for i in cursor:
        datas.append(i[0].strftime('%d/%m'))
        notas.append(i[1])

    # desenho do gráfico
    print(f"\nEvolução da nota de sustentabilidade - {usuario}")
    print(f"Datas: {' | '.join(datas)}\n") #pegar as datas dos registros

    for y in range(5, 0, -1):  # notas de 5 a 1
        linha = f"{y} | "
        for nota in notas:
            linha += "■ " if nota >= y else "  "
        print(linha)

    print("  +" + "―" * (len(notas) * 2))
    print("    " + " ".join(str(i + 1) for i in range(len(notas))))

    opcao = input("\nAperte ENTER para retornar ao menu: ")
    if opcao == '':
        return

def mostrar_tela_recomendacoes(usuario):
    limpar_tela()
    print("\n" + "=" * 80)
    print(f"   ANÁLISE E RECOMENDAÇÕES - {usuario.upper()}")
    print("=" * 80)

    #identifica o id do usuário
    cursor.execute("select u_id from usuario where u_usuario = %s", (criptografar(usuario),))
    for i in cursor:
        id_usuario=i[0]

    #verifica se há registros
    cursor.execute("select r_id from registro where r_usuarioId = %s", (id_usuario,))
    select = cursor.fetchone()
    if select is None: #caso não houver
        print("* ❌ Nenhum dado de sustentabilidade encontrado.")
        input("\nPressione ENTER para voltar...")
        return
    cursor.fetchall()

    # pegar o ultimo registro
    cursor.execute("select r_energia,r_agua,r_residuo,r_transporte from registro " \
    "where r_usuarioId = %s " \
    "order by r_data desc " \
    "limit 1", (id_usuario,))

    for i in cursor:
        dados = i

    notas=calcular_nota(*dados)
    nota_energia = int(notas[0])
    nota_agua = int(notas[1])
    nota_residuo = int(notas[2])
    nota_transporte = int(notas[3])

    classificacoes = { #Classificacoes de consumo
        "energia": {
            1: "Alto consumo",
            2: "Consumo elevado",
            3: "Consumo moderado",
            4: "Baixo consumo",
            5: "Consumo excelente"
        },
        "agua": {
            1: "Alto consumo",
            2: "Consumo elevado",
            3: "Consumo moderado",
            4: "Baixo consumo",
            5: "Consumo excelente"
        },
        "residuo": {
            1: "Alto impacto",
            2: "Impacto elevado",
            3: "Impacto moderado",
            4: "Baixo impacto",
            5: "Impacto irrelevante"
        },
        "transporte": {
            1: "Alto impacto",
            2: "Impacto elevado",
            3: "Impacto moderado",
            4: "Baixo impacto",
            5: "Nenhum impacto"
        }
    }

    dados = { #Nota e possiveis recomendacoes
        "Consumo de energia": {
            "nota": nota_energia,
            "classificacao": classificacoes["energia"][nota_energia],
            "recomendacao": "Trocar lâmpadas por LED, Evite deixar celular carregando a noite toda e Apague as luzes ao sair de um cômodo."
        },
        "Consumo de água": {
            "nota": nota_agua,
            "classificacao": classificacoes["agua"][nota_agua],
            "recomendacao": "Instalar redutores de vazão, consertar vazamentos e reduzir tempo do banho."
        },
        "Geração de resíduos": {
            "nota": nota_residuo,
            "classificacao": classificacoes["residuo"][nota_residuo],
            "recomendacao": "Separar o lixo reciclável, evitar descartáveis e reutilizar embalagens."
        },
        "Uso de transporte": {
            "nota": nota_transporte,
            "classificacao": classificacoes["transporte"][nota_transporte],
            "recomendacao": "Usar bicicleta, transporte público ou incentivar caronas e veículos elétricos."
        }
    }

    for acao, info in dados.items():
        print(f"\n🔹 {acao}")
        print(f"   Nota: {info['nota']} - {info['classificacao']}")
        if info["nota"] < 5:
            print(f"   Recomendações: {info['recomendacao']}")
        else:
            print("   ✅ Excelente! Continue assim!") #caso nao haja recomendacoes

    print("\nPressione ENTER para voltar ao menu.") 
    input()

def relatorio_calculo(nota): # retorna a classificacao de cada nota
    if(nota==5):
        return "ideal, parabéns!"
    elif(nota>=4):
        return "moderado"
    elif(nota>=3):
        return "significativo"
    elif(nota>=2):
        return "elevado"
    elif(nota>=1):
        return "muito elevado"

# Função para criar a tela da tabela
def Tabela_relatorio(usuario):
    limpar_tela()
    nota_sus = calcular_sus(usuario)
    print('=================================================================================================================================')
    print('                                                      RELATÓRIO E HISTÓRICO                                                      ')
    print('=================================================================================================================================')
    print(f"\n{'Registro n°':<15}{'Data':<15}{'Energia':<10}{'Água':<10}{'Resíduo':<10}{'Transporte':<15}{'Média':<10}{'Relatório':<20}")
    print("---------------------------------------------------------------------------------------------------------------------------------")

    #identifica o id do usuário
    cursor.execute("select u_id from usuario where u_usuario = %s", (criptografar(usuario),))
    for i in cursor:
        id_usuario=i[0]
    
    #verifica se há registros
    cursor.execute("select r_id from registro where r_usuarioId = %s", (id_usuario,))
    select = cursor.fetchone()
    if select is None: #caso não houver
        print("* ❌ Nenhum dado de sustentabilidade encontrado.")
        input("\nPressione ENTER para voltar...")
        return
    cursor.fetchall()

    #consultando os registros
    cursor.execute("select r_data,r_energia,r_agua,r_residuo,r_transporte,r_media,r_id " \
    "from registro where r_usuarioId = %s", (id_usuario,))

    j=0
    registro_id = []
    vazio=''
    #:<10 "< indica alinhamento à esquerda, 10 indica o números de espaçoes que irá ocupar"
    for i in cursor:
        notas=calcular_nota(i[1],i[2],i[3],i[4])
        print(f"{j+1:<15}{i[0].strftime('%Y-%m-%d'):<15}{i[1]:<10}{i[2]:<10}{i[3]:<10}{i[4]:<15}{i[5]:<10}", end='')
        print(f'Parâmetro energia:    {notas[0]}, {relatorio_calculo(notas[0])}')
        print(f"{vazio:<85}Parâmetro água:       {notas[1]}, {relatorio_calculo(notas[1])}")
        print(f"{vazio:<85}Parâmetro resíduos:   {notas[2]}, {relatorio_calculo(notas[2])}")
        print(f"{vazio:<85}Parâmetro transporte: {notas[3]}, {relatorio_calculo(notas[3])}")
        print("----------------------------------------------------------------------------------------------------------------------------------")
        registro_id.append(i[6]) #armazena os id dos registros verificados
        j+=1
    print(f"Nota geral: {round(nota_sus,2)}, {relatorio_calculo(nota_sus)}")
    print("-"*130)

    print("\nPara editar ou deletar um registro, digite seu número correspondente")
    print("ou pressione ENTER para voltar ao menu\n")
    opcao = input("Informe sua ação: ")
    if opcao == '':
        return
    else: #edição de registro
        try: 
            opcao = int(opcao) #verifica se o input é numérico
            #verifica se o registro existe
            if(opcao<1 or opcao>len(registro_id)):
                print("* ❌ O valor informado não corresponde a nenhum registro.")
                input("\nPressione ENTER para voltar...")
                return
            
            while(True):
                escolha = input("Pressione E para editar ou D para deletar um registro: ")
                if(escolha.upper() == 'E'):
                    #refaz o calculo
                    print()
                    calculo = cadastro_calculo(usuario, date.today())
                    #altera no bd
                    cursor.execute("update registro set r_energia = %s," \
                    "r_agua = %s," \
                    "r_residuo = %s," \
                    "r_transporte = %s," \
                    "r_media = %s" \
                    "where r_id = %s", (calculo[1],calculo[2],calculo[3],calculo[4],calculo[5],registro_id[opcao-1]))
                    conexao.commit()
                    break
                elif(escolha.upper() == 'D'):
                    cursor.execute("delete from registro where r_id = %s", (registro_id[opcao-1],))
                    conexao.commit()
                    break
                else:
                    print('\n* ❌ Digite uma opção válida')
                    
            nota_sus = calcular_sus(usuario)
            Tabela_relatorio(usuario)
        except:
            return
          
area_login()
