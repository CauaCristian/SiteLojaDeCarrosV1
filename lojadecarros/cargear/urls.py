from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
#aqui eu adiciono a urls home para quando ele acessar a home do meu site
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',include('home.urls'))
]
