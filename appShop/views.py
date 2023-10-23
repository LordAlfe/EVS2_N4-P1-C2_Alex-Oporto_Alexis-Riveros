from django.shortcuts import render

# Create your views here.
def renderIndex(request):
    return render(request, 'appShop/index.html')

def electronica(request):
    data={
        "titulo":"Electronica",
        'producto1':"MAC",
        'producto2':"Celular",
        'producto3':"PlayStation",
        'url':"https://portales.inacap.cl/",
        'imagen':'imagenes/espada.PNG',
        'imagen1':'imagenes/espada.PNG',
        'imagen2':'imagenes/espada.PNG'
    }
    return render(request, 'appShop/productos.html',data)

def juguetes(request):
    data={
        "titulo":"Juguetes",
        'producto1':"pelota",
        'producto2':"Figura de accion",
        'producto3':"Juego de Mesa",
        'imagen':'imagenes/fut.PNG',
        'imagen1':'imagenes/fut.PNG',
        'imagen2':'imagenes/fut.PNG'
    }
    return render(request, 'appShop/productos.html',data)

def ropa(request):
    data={
        "titulo":"Ropa",
        'producto1':"Polera",
        'producto2':"Pantalon",
        'producto3':"Chaqueta",
        'imagen':'imagenes/ropa.PNG',
        'imagen1':'imagenes/ropa.PNG',
        'imagen2':'imagenes/ropa.PNG'
    }
    return render(request, 'appShop/productos.html',data)