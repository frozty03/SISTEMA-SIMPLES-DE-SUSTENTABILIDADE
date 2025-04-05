import getpass #getpass é para censurar, só que eu nao sei como usar
from datetime import date #para pegar a data atual
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

usuarios = {} #simular bd
registros = {} #guarda valores em matrizes 2D. registros[chave][matriz][valor da matriz] 

#ADICIONAR EMAIL P/ RECUPERAÇÃO DE SENHA
def cadastro():
    print('\n                                       CADASTRO')
    print('====================================================================================================')
    usuario = input('* Digite um nome de usuário: ')

    if usuario in usuarios:
        print('* ❌ Erro: Usuário já existe!')
        return

    senha = input('* Digite uma senha: ')
    senha2 = input('* Confirme a senha: ')

    if senha != senha2:
        print('* ❌ Erro: As senhas não coincidem!')
    else:
        usuarios[usuario] = senha #salvar a senha ao usuario
        registros[usuario] = [] #cria uma chave
        print('* ✅ Cadastro realizado com sucesso!')
    print('====================================================================================================')

#ADICIONAR OPÇÃO P RECUPERAR SENHA
def login():
    print('\n                                           LOGIN')
    print('====================================================================================================')
    usuario = input('* Usuário: ')
    senha = input('* Senha: ')

    if usuario in usuarios and usuarios[usuario] == senha: #se o usuario estiver no dict e a senha corresponder
        print(f' ✅ Login bem-sucedido! Bem-vindo, {usuario}!')
        print('====================================================================================================')
        menu_login(usuario) #iniciar o menu pós login
    else:
        print('* ❌ Erro: Usuário ou senha incorretos!')
        print('====================================================================================================')


def area_login():
    while True:
        print('\n                                       ÁREA DE LOGIN')
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


def menu_login(usuario):
    while True:
        print('\n                                             MENU')
        print('====================================================================================================')
        print(f'| * Usuário: {usuario}                                                                                     |')
        print('|--------------------------------------------------------------------------------------------------|')
        print('|    1. Cadastro de informações | 2. Lista de gráficos | 3. Ações (recomendações) | 4. Relatório   |')
        print('|                   5. Parâmetros   |   6. Histórico de cadastros   |   7. Sair                    |')
        print('====================================================================================================')

        opcao = input('Escolha uma opção (1-7): ')
        if opcao == '1': #por as outras opções em cima, em ordem(depois substituir por elif)
            print('Navegando para tela de cadastro...')
            cadastro_inf(usuario)
        if opcao=='4':
            Tabela_relatorio(usuario)
        if opcao == '7': #por as outras opções em cima, em ordem(depois substituir por elif)
            print('Voltando a área de login...')
            break

def cadastro_inf(usuario):
    while True:
        print('\n                                       CADASTRO DE INFORMAÇÕES')
        print('====================================================================================================')
        print(f'| * Usuário: {usuario}                                                                                     |')
        print('|--------------------------------------------------------------------------------------------------|\n')
        
        data=date.today() #pegando data atual
        print(f'Data do registro: {data}\n')

        try:
            energia=float(input("Informe seu consumo de energia (kW/dia): "))
            agua=float(input("Informe seu consumo de energia (L/dia): "))
            residuo=float(input("Informe sua geração de resíduos recicláveis (%): "))
            
            #cabeçalho explicando o último input
            print("\nPV - Privado\nPVU - Público e privado\nPU - Público\nE - Elétrico\nBC - Bicleta e/ou caminhada") 
            transporte=input("Informe o tipo de transporte utilizado (PV/PVU/PU/E/BC): ").upper() #upper() transforma em maiúsculo
            
            #Verificando se a opção do transporte é válida
            if transporte not in ["PV", "PVU", "PU", "E", "BC"]: 
                raise #Leva para o except
        except:
            print("\nValor inválido inserindo, voltando para o menu...")
            menu_login(usuario) #voltando para o menu
            break

        calculo = [] #inicializando vetor

        #formato: [data, nota_energia, nota_água, nota_resíduo, nota_transporte, nota_sustentabilidade]
        calculo[:] = (data,*calcular_nota(energia,agua,residuo,transporte)) #atribui data e os retornos da função no vetor calculo
        registros[usuario].append(calculo[:]) #faço o registro

        print(f'\nNota eneriga:  {calculo[1]}') #apresento a nota
        print(f'Nota água:       {calculo[2]}')
        print(f'Nota resíduo:    {calculo[3]}')
        print(f'Nota transporte: {calculo[4]}')
        print(f'Nota geral:      {calculo[5]}') 
        
        menu_login(usuario) #voltando para o menu
        break

def input_enter():
    return
    
def calcular_nota(energia,agua,residuo,transporte):

    #Cálculo do parâmetro de água
    if(agua>250):
        n_agua=1
    elif(agua>=200 and agua<=250):
        n_agua=2
    elif(agua>=150 and agua<=199):
        n_agua=3
    elif(agua>=100 and agua<=149):
        n_agua=4
    else:
        n_agua=5

    #Cálculo do parâmetro de energia
    if(energia>15):
        n_energia=1
    elif(energia>=12 and energia<=15):
        n_energia=2
    elif(energia>=8 and energia<=11):
        n_energia=3
    elif(energia>=5 and energia<=8):
        n_energia=4
    else:
        n_energia=5

    #Cálculo do parâmetro de resíduos
    if(residuo>50):
        n_residuo=5
    elif(residuo>=41 and residuo<=50):
        n_residuo=4
    elif(residuo>=31 and residuo<=40):
        n_residuo=3
    elif(residuo>=20 and residuo<=30):
        n_residuo=2
    else:
        n_residuo=1

    #Cálculo do parâmetro de transporte
    if(transporte=='PV'): 
        n_transporte=1
    elif(transporte=='PVU'):
        n_transporte=2
    elif(transporte=='PU'):
        n_transporte=3
    elif(transporte=='E'):
        n_transporte=4
    elif(transporte=='BC'):
        n_transporte=5

    #Média geral
    n_sustentabilidade=(n_energia+n_agua+n_residuo+n_transporte)/4
    return n_energia,n_agua,n_residuo,n_transporte,n_sustentabilidade


# Função para criar a tabela
def Tabela_relatorio(usuario):
    
    print('\t\t\t\t\t======================================')
    print('\t\t\t\t\t              RELATORIO               ')
    print('\t\t\t\t\t======================================')
    print("-------------------------------------------------------------------------------------------------------------------------")
    print("Nome\t\tData\t\tEnergia\tÁgua\tResíduo\tTransporte\tRelatório")
    print("-------------------------------------------------------------------------------------------------------------------------")
    i = 0
    while (i<len(registros[usuario])):
       print(f"{usuario}\t\t{registros[usuario][i][0]}\t{registros[usuario][i][1]}\t{registros[usuario][i][2]}\t{registros[usuario][i][3]}\t{registros[usuario][i][4]}\t{registros[usuario][i][5]}")
       print("\t\t\t\t\t\t\t\t\t\t\tConsumo de água elevado")
       print("\t\t\t\t\t\t\t\t\t\t\tConsumo de energia elevado")
       print("\t\t\t\t\t\t\t\t\t\t\tConsumo de lixo elevado")
       print("\t\t\t\t\t\t\t\t\t\t\tConsumo de transporte razoável")
       print("--------------------------------------------------------------------------------------------------------------------------")
       i=i+1
area_login()

#CADASTRO DE INFORMAÇÕES: abrir parte de inserir as informações de cada parametro, calcular (usar a tabela de parametros que está no figma)
#LISTA DE GRÁFICOS: colocar opções de período (gráficos da semana, do dia e do mês) e criar gráfico com base nos cadastros de informações
#AÇÕES: mostrar as notas do último cadastro e recomendar ações para melhora com base nisso
#RELATÓRIO: mostrar as notas dos 3 ultimos cadastros, simbolizar se melhorou ou se piorou
#PARÂMETROS: colocar a tabela de parâmetros
#HISTÓRICO DE CADASTROS: mostrar todos os outros cadastros e opção de editar informação1
