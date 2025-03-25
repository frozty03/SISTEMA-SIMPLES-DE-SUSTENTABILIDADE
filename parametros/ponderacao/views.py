from django.shortcuts import render

def tabela_parametros(request):
    dados = [
        {
            'categoria': 'Consumo de água (L/dia)',
            'descricao': 'Utilização de hidrômetro',
            'notas': [
                'Nota 1: >250/dia',
                'Nota 2: 250 - 200/dia',
                'Nota 3: 199 - 150/dia',
                'Nota 4: 149 - 100/dia',
                'Nota 5: <100/dia'
            ]
        },
        {
            'categoria': 'Consumo de energia (kW/dia)',
            'descricao': 'Dividir o valor mensal, de kW, obtido na conta de luz, pelos dias do mês',
            'notas': [
                'Nota 1: >15kw/dia',
                'Nota 2: 15 - 12kw/dia',
                'Nota 3: 11 - 8kw/dia',
                'Nota 4: 8 - 5kw/dia',
                'Nota 5: <5kw/dia'
            ]
        },
        {
            'categoria': 'Uso de transportes',
            'descricao': '',
            'notas': [
                'Nota 1: Transporte privado',
                'Nota 2: Transporte público e privado',
                'Nota 3: Transporte público',
                'Nota 4: Transporte elétrico',
                'Nota 5: Bicicleta ou caminhada'
            ]
        },
        {
            'categoria': 'Porcentagem de lixo reciclável',
            'descricao': 'Percentagem de peso da parte reciclável em relação ao total diário',
            'notas': [
                'Nota 1: <20%',
                'Nota 2: 20 - 30%',
                'Nota 3: 31 - 40%',
                'Nota 4: 41 - 50%',
                'Nota 5: >50%'
            ]
        }
    ]
    return render(request, 'tabela_parametros.html', {'dados': dados})