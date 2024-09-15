from store.models import Product

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

    
    def add(self,product, quantity):
        product_id = str(product.id)
        product_qty = str(quantity)
        #logica
        if product_id in self.cart:
            pass
        else:
            #self.cart[product_id] = {'price': str(product.price)}
            self.cart[product_id] = int(product_qty)

        self.session.modified = True

    def cart_total(self):
        #obtener ids
        product_ids = self.cart.keys()
        #buscar las claves en el modelo
        products = Product.objects.filter(id__in=product_ids)
        #obtenemos las cantidades
        quantities = self.cart
        #el carrito se tiene asi:indice en string y cantidad en int {'4':3,'2':5}
        total = 0
        for key, value in quantities.items():
            key = int(key)
            for product in products:
                if product.id == key:
                    if product.is_sale:
                        total = total + (product.sale_price * value)
                    else:
                        total = total + (product.price * value)
        return total
        
        


    def __len__(self):
        return len(self.cart)
    
    def get_prods(self):
        #obtenemos los Ids desde el carrito
        product_ids = self.cart.keys()
        #usamos los ids paera buscar los productos en la base de datos
        products = Product.objects.filter(id__in=product_ids)
        return products
    
    def get_quants(self):
        quantities = self.cart
        return quantities
    
    def update(self, product, quantity):
        product_id = str(product)
        product_qty = int(quantity)

        #obtenemos el Carrito
        ourcart = self.cart
        #actualizamos diccionario/carro
        ourcart[product_id] = product_qty

        self.session.modified = True

        thing = self.cart
        return thing

    def delete(self, product):
        product_id = str(product)
        #borramos del diccionario/carrito
        if product_id in self.cart:
            del self.cart[product_id]
        self.session.modified = True