
# Função para criar a tabela
def Tabela_relatorio(usuario ,date ,hora ,agua ,energia ,residuo ,transporte):
    
    print('\t\t\t\t\t======================================')
    print('\t\t\t\t\t              RELATORIO               ')
    print('\t\t\t\t\t======================================')
    print("-------------------------------------------------------------------------------------------------------------------------")
    print("Nome\t\tData\tHora\tÁgua\tEnergia \tResíduo \tTransporte\tRelatório")
    print("-------------------------------------------------------------------------------------------------------------------------")
    
    print(f"{usuario}\t\t{date}\t{hora}\t{agua}\t{energia}\t\t{residuo}\t{transporte}")
    print("\t\t\t\t\t\t\t\t\t\t\tConsumo de água elevado")
    print("\t\t\t\t\t\t\t\t\t\t\tConsumo de energia elevado")
    print("\t\t\t\t\t\t\t\t\t\t\tConsumo de lixo elevado")
    print("\t\t\t\t\t\t\t\t\t\t\tConsumo de transporte razoável")
    print("--------------------------------------------------------------------------------------------------------------------------")



# Chamando a função
Tabela_relatorio(1,2,3,4,5,6,7)


