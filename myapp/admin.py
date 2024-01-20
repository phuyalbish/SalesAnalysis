from django.contrib import admin
from .models import Client, Client_Product_Bridge, Product, Company, Sales

admin.site.register(Client)
admin.site.register(Product)
admin.site.register(Client_Product_Bridge)
admin.site.register(Company)
admin.site.register(Sales)
