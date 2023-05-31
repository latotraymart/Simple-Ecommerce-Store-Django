from django.contrib import admin
from . import models 



class EccomerceAdmin(admin.AdminSite):
	site_header = 'Beauty Avenue Admin Area'


EcommerceSiteAdmin= EccomerceAdmin(name='EccomerceAdmin')
EcommerceSiteAdmin.register(models.Customer)
EcommerceSiteAdmin.register(models.Product)
EcommerceSiteAdmin.register(models.Category)
EcommerceSiteAdmin.register(models.Order)
EcommerceSiteAdmin.register(models.OrderItem)
EcommerceSiteAdmin.register(models.ShippingAddress)
EcommerceSiteAdmin.register(models.Qrcode_gcash)
EcommerceSiteAdmin.register(models.Qrcode_paymaya)







# Register your models here.
