from django.shortcuts import render

from django.shortcuts import render

def mostrar_parametros(request):
    parametros = [
        {
            'nome': 'Consumo de Água (L/dia)',
            'descricao': 'Utilização do hidrômetro',
            'notas': [
                {'valor': 1, 'descricao': '>250L/dia'},
                {'valor': 2, 'descricao': '250-200L/dia'},
                {'valor': 3, 'descricao': '199-150L/dia'},
                {'valor': 4, 'descricao': '149-100L/dia'},
                {'valor': 5, 'descricao': '<100L/dia'},
            ]
        },
        {
            'nome': 'Consumo de Energia (kW/dia)',
            'descricao': 'Nível obtido na conta de luz',
            'notas': [
                {'valor': 1, 'descricao': '>15kW/dia'},
                {'valor': 2, 'descricao': '15-12kW/dia'},
                {'valor': 3, 'descricao': '11-8kW/dia'},
                {'valor': 4, 'descricao': '6-5kW/dia'},
                {'valor': 5, 'descricao': '<5kW/dia'},
            ]
        },
        {
            'nome': 'Uso de Transportes',
            'descricao': 'Meio de transporte utilizado',
            'notas': [
                {'valor': 1, 'descricao': 'Transporte privado'},
                {'valor': 2, 'descricao': 'Transporte público e privado'},
                {'valor': 3, 'descricao': 'Transporte público'},
                {'valor': 4, 'descricao': 'Transporte elétrico'},
                {'valor': 5, 'descricao': 'Bicicleta ou caminhada'},
            ]
        },
        {
            'nome': 'Porcentagem de lixo reciclável',
            'descricao': 'Peso da parte reciclável em relação ao total',
            'notas': [
                {'valor': 1, 'descricao': '>20%'},
                {'valor': 2, 'descricao': '20-30%'},
                {'valor': 3, 'descricao': '31-40%'},
                {'valor': 4, 'descricao': '41-50%'},
                {'valor': 5, 'descricao': '>50%'},
            ]
        }
    ]

    return render(request, 'mostrar_parametros.html', {'parametros': parametros})
