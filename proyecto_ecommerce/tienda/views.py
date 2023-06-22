from django.shortcuts import render,redirect
from django.http import HttpResponse, JsonResponse
from django.template import loader
# from administracion.models import Producto, Varietal

def hola_tienda(request):
    return HttpResponse('Bienvenido a la Tienda')

def index(request):
   template = loader.get_template('tienda/index.html')
   context={'titulo':'Inicio'}
   return HttpResponse(template.render(context,request))

# def indexp(request):
#     template_name="index.html"
#     varietales=Varietal.objects.filter(activo=True)
#     productos=Producto.objects.filter(activo=True)
#     context ={"productos":productos, "varietales":varietales}
#     return render(request,template_name,context)

# def index(request):
#    template = loader.get_template('tienda/index.html')
#    varietales=Varietal.objects.filter(activo=True)
#    productos=Producto.objects.filter(activo=True)
#    context={'titulo':'Inicio','producto':productos,'varietal':varietales}
#    return HttpResponse(template.render(context,request))

# def producto(request):
#    template = loader.get_template('tienda/productos.html')
#    context={'titulo':'Producto'}
#    return HttpResponse(template.render(context,request))

def index(request):
    if(request.method=='GET'):
        titulo = 'Titulo cuando accedo por GET'
    else:
        titulo = 'Titulo cuando accedo por otro método'   
    parametro_uno = request.GET.get('param')     
    
    listado_cursos = [
        {'nombre': 'Diseño UX/UI',
         'descripcion': 'Diseño' ,
         'categoria': 'Diseño',
         },
         {'nombre':'Fullstack Java',
         'descripcion': 'Curso FullStack',
         'categoria': 'Programacion',
         },
         {'nombre': 'Big Data',
         'descripcion': 'test',
         'categoria': 'Analisis de Datos',
         },
         {'nombre': 'Big Data Avanzada',
         'descripcion': 'test',
         'categoria': 'Analisis de Datos',
         },
    ]

    return render(request,'tienda/index.html',
                  {'titulo':titulo,
                   'parametro_uno':parametro_uno,
                   'cursos':listado_cursos
                  })

#Create your views here.

def api_productos(request):
   productos = [{
       'nombre': 'D.V. catena - tinto histórico 2019',
       'varietal': 'Blend',
       'portada': 'https://vinotecaligier.com/media/catalog/product/cache/1/image/500x500/9df78eab33525d08d6e5fb8d27136e95/b/e/be72477.jpg',
       'bodega': 'catena zapata',
       'precio': '3500'
   },{
       'nombre': 'White Bones',
       'varietal': 'Chardonnay',
       'portada': 'https://vinotecaligier.com/media/catalog/product/cache/1/small_image/430x320/9df78eab33525d08d6e5fb8d27136e95/b/e/be76371_base.jpg',
       'bodega': 'catena zapata',
       'precio': '42200'
   },{
       'nombre': 'River',
       'varietal': 'Malbec',
       'portada': 'https://vinotecaligier.com/media/catalog/product/cache/1/image/500x500/9df78eab33525d08d6e5fb8d27136e95/b/e/be72477.jpg',
       'bodega': 'catena zapata',
       'precio': '45600'
    },{
       'nombre': 'Saint Felicien',
       'varietal': 'Rose',
       'portada': 'https://http2.mlstatic.com/D_NQ_NP_601614-MLA52995055033_122022-V.jpg',
       'bodega': 'catena zapata',
       'precio': '9300'
    },{
       'nombre': 'Saint Felicien',
       'varietal': 'Sauvignon Blanc',
       'portada': 'https://cepadevinos.com/wp-content/uploads/2017/07/Saint_Felicien_Sauvignon_Blanc_qbs3es.jpg',
       'bodega': 'catena zapata',
       'precio': '42200'
    },{
       'nombre': 'Nicasia Vineyard Doux',
       'varietal': 'Espumante',
       'portada': 'https://www.espaciovino.com.ar/media/default/0001/65/thumb_64247_default_big.jpeg',
       'bodega': 'catena zapata',
       'precio': '42200'
    },{
       'nombre': 'Paraiso',
       'varietal': 'Blend',
       'portada': 'https://cepadevinos.com/wp-content/uploads/2017/07/Saint_Felicien_Sauvignon_Blanc_qbs3es.jpg',
       'bodega': 'Luigi Bosca',
       'precio': '42200'      
    },{
       'nombre': 'Los Nobles',
       'varietal': 'Chardonnay',
       'portada': 'https://vinotecaligier.com/media/catalog/product/cache/1/image/500x500/9df78eab33525d08d6e5fb8d27136e95/b/e/be72477.jpg',
       'bodega': 'Luigi Bosca',
       'precio': '42200'         
    },]
   response = {'status':'Ok', 'code':200, 'message':'Listado de productos', 'data':productos}
   return JsonResponse(response,safe=False)

def productos(request):    
    return render(request,'tienda/productos.html')
