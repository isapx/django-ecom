from django.contrib import admin
from .models import Category, Customer, Product, Order

#aqui registramos los modelos que queremos que aparezan en la url /admin para que los usemos para probar
#hay que importarlos arriba
admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
