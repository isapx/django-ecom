from django.shortcuts import render, get_object_or_404
from .cart import Cart
from store.models import Product
from django.http import JsonResponse

def cart_summary(request):
    #obtenemos el carrito
    cart = Cart(request)
    cart_products = cart.get_prods
    quantities = cart.get_quants
    return render(request, 'cart_summary.html',{"cart_products": cart_products, "quantities": quantities})


def cart_add(request):
    #obtenemos el carro
    cart = Cart(request)
    
    #probamos el POST
    if request.POST.get('action') == 'post':
        #obtenemos la info
        #product_id = int(request.POST.get('product_id'))
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))

        #buscamos el producto en la base de datos
       #product = get_object_or_404(Product, id=product_id)
        product = get_object_or_404(Product, id=product_id)

        #lo guadramos en la sesion
        cart.add(product=product,quantity=product_qty)

        #obtenemos la cantidad de articulos en el carrito
        cart_quantity = cart.__len__()

        #regresamos un response
        #response = JsonResponse({'Product Name': product.name })
        #response = JsonResponse({'Product Name: ': product.name})
        response = JsonResponse({'qty: ': cart_quantity})
        return response



def cart_delete(request):
    pass

def cart_update(request):
    pass
