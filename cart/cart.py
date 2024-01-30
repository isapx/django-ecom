class Cart():
    def __init__(self, request):
        self.session = request.session

        #obtenemos la sesion key si existe
        cart = self.session.get('session_key')

        #si el usuairo es nuevo no hay sesion asi que creamos una
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}

        #nos aseguramos de que el carro este disponible en todas las paginas
        self.cart = cart

    
    def add(self,product):
        product_id = str(product.id)

        #logica
        if product_id in self.cart:
            pass
        else:
            self.cart[product_id] = {'price': str(product.price)}

        self.session.modified = True