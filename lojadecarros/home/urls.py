from django.urls import path
from . import views
#adcionando a url o que o usario vai ver ao acessar meu dominio
urlpatterns = [
    path('pag_inicial/',views.pag_inicial,name="pag_inicial"),
    path('pag_cadastro/',views.pag_cadastro,name="pag_cadastro"),
    path('pag_login/',views.pag_login,name="pag_login"),
    path('faça_seu_pedido/',views.faça_seu_pedido,name="faça_seu_pedido"),
    path('carros/',views.carros,name="carros"),
    path('comprafinalizada/',views.comprafinalizada,name="comprafinalizada")
]