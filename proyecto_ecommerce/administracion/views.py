from django.shortcuts import render

# from administracion.forms import VarietalForm, ProductoForm

# from administracion.models import Varietal, Producto

# Create your views here.
def index_administracion(request):
    variable='test variable'
    return render (request, 'administracion/index_administracion.html',{'variable':variable})

# def varietales_index(request):
#     #queryset
#     varietales = Varietal.objects.filter(baja=False)
#     return render(request,'administracion/varietales/index.html',{'varietales':varietales})