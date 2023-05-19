from django.shortcuts import render
from . import templates
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required


#recebendo a requisicao que o usario fez no servidor usando o request
def pag_inicial(request):
    return render(request,"site/home.html/")

def pag_cadastro(request):
   if request.method =='GET':
    return render(request,"site/cadastro.html/")
   else :
        username = request.POST.get('username')
        email = request.POST.get('email')
        cpf = request.POST.get('cpf')
        senha = request.POST.get('senha')
        user = User.objects.filter(username=username).first()

        if user:
            return render(request,"site/usuariojaexistente.html/")
        user = User.objects.create_user(username=username, email=email, password=senha)
        user.save()
        
        
        return render(request,"site/cadastradocomsucesso.html/")

def pag_login(request):
   if request.method =='GET':
       return render(request,"site/login.html/")
   else :
      username = request.POST.get('username')
      senha = request.POST.get('senha')
      user = authenticate(username=username, password=senha)
   if user: 
        login(request, user)

        return render(request,"site/autenticado.html")
   else:
        return render(request,"site/usuarioenvalido.html")

@login_required(login_url="/home/pag_login/")
def faça_seu_pedido(request):
    return render(request,"site/pedidos.html")

#utilizando [] pois pego apenas usando o metodo get 
def carros(request):
    if request.method=='GET':
       c = request.GET['cor']
       
    if c == "Verde":
        return render(request,"site/carroverde.html")
    
    if c == "Vermelho":
        return render(request,"site/carrovermelho.html")
    
    if c ==  "Amarelo":
        return render(request,"site/carroamarelo.html")
    
    if c == "Laranja":
        return render(request,"site/carrolaranja.html")

def comprafinalizada(request):
    return render(request,"site/comprafinalizada.html")


