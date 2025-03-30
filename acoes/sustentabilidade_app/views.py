

from django.shortcuts import render, redirect
from .models import UsuarioSustentavel
from .forms import UsuarioForm
from django.shortcuts import render, get_object_or_404, redirect
import matplotlib.pyplot as plt
import io
import urllib, base64

def calcular_grafico(usuario):
    labels = ['Energia', 'Água', 'Resíduos', 'Transporte']
    valores = [usuario.consumo_energia, usuario.consumo_agua, usuario.residuos, usuario.uso_transporte]

    fig, ax = plt.subplots()
    ax.bar(labels, valores, color=['blue', 'green', 'red', 'orange'])
    ax.set_ylabel('Consumo')
    ax.set_title('Consumo Sustentável')

    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    imagem_png = base64.b64encode(buffer.getvalue()).decode('utf-8')
    buffer.close()
    
    return imagem_png

def calc_nota(self): #Calcula a nota de cada parâmetro
        #Água
        if(self.consumo_agua>250): #Pior nota possível
            self.consumo_agua = 250
        elif(self.consumo_agua<100): #Melhor nota possível
            self.consumo_agua = 100
        na = round(((250-self.consumo_agua)/150) * 5,2) #Calculo uma nota de 0 a 1 e multiplico por 5

        #Energia
        if(self.consumo_energia>15):
            self.consumo_energia = 15
        elif(self.consumo_energia<5):
            self.consumo_energia = 5
        ne = round(((15-self.consumo_energia)/10) * 5,2)

        #Transporte
        if(self.uso_transporte>20):
            self.uso_transporte = 20
        elif(self.uso_transporte<2):
            self.cuso_transporte = 2
        nt = round(((20-self.uso_transporte)/18) * 5,)

        #Resíduos
        if(self.residuos>50):
            self.residuos = 50
        elif(self.residuos<20):
            self.residuos = 20
        nr = round(((50-self.residuos)/30) * 5,2)
        return na,ne,nt,nr

def sugestao(nota): #Determina qual mensagem o usuário irá receber
        if(nota<=1):
            return 'Cuidado! Você possui hábitos muito prejudiciais para o meio ambiente'
        elif(nota<=2):
            return 'Cuidado! Você possui hábitos pouco sustentáveis'
        elif(nota<=3):
            return 'Atenção! Reveja seus hábitos'
        elif(nota<=4):
            return 'Muito bem! Você ainda pode melhorar'
        elif(nota<5):
            return 'Parabéns! Você possui hábitos sustentáveis'
        else:
            return 'Incrível! Você possui altos índices de sustentabilidade'

def cadastro_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_usuarios')
    else:
        form = UsuarioForm()
    return render(request, 'cadastro.html', {'form': form})

def lista_usuarios(request):
    usuarios = UsuarioSustentavel.objects.all() 
    return render(request, 'lista.html', {'usuarios': usuarios})

def detalhes_usuario(request, id):
    usuario = UsuarioSustentavel.objects.get(id=id)
    grafico = calcular_grafico(usuario)
    return render(request, 'detalhes.html', {'usuario': usuario, 'grafico': grafico})
    
def editar_usuario(request, id):
    usuario = get_object_or_404(UsuarioSustentavel, id=id)
    
    if request.method == 'POST':
        form = UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('detalhes_usuario', id=usuario.id)
    else:
        form = UsuarioForm(instance=usuario)

    return render(request, 'editar_usuario.html', {'form': form, 'usuario': usuario})

def acoes_usuario(request, id): #Tela de ações
    usuario = UsuarioSustentavel.objects.get(id=id)
    nota = [0,0,0,0]
    s_acao = [0,0,0,0]
    nota[0],nota[1],nota[2],nota[3] = calc_nota(usuario) #Notas em cada parâmetro
    i=0
    while(i<4):
        s_acao[i] = sugestao(nota[i]) #Mensagem de sugestão
        i+=1
    return render(request, 'acoes.html',{'usuario': usuario, 'nota': nota, 'acao' : s_acao})