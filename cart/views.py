from django.shortcuts import render, get_object_or_404
from .cart import Cart
from store.models import Product
from django.http import JsonResponse

def cart_summary(request):
    return render(request, 'cart_summary.html',{})


def cart_add(request):
    #obtenemos el carro
    cart = Cart(request)
    
    #probamos el POST
    if request.POST.get('action') == 'post':
        #obtenemos la info
        #product_id = int(request.POST.get('product_id'))
        product_id = int(request.POST.get('product_id'))

        #buscamos el producto en la base de datos
       #product = get_object_or_404(Product, id=product_id)
        product = get_object_or_404(Product, id=product_id)

        #lo guadramos en la sesion
        cart.add(product=product)

        #regresamos un response
        #response = JsonResponse({'Product Name': product.name })
        response = JsonResponse({'Product Name: ': product.name})
        return response



def cart_delete(request):
    pass

def cart_update(request):
    pass
