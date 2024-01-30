from .cart import Cart

#creamos un context processor para que nuestro carro funcione en todas las paginas
def cart(request):
    #regresamos los datos de nuestro carro por default
    return {'cart': Cart(request)}
