from django.urls import path, include
from . import views
from store.admin import EcommerceSiteAdmin
from django.contrib import admin


from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
path('EcommerceSiteAdmin/', EcommerceSiteAdmin.urls),
path('', views.stores, name="stores"),
path('cart', views.cart, name="cart"),
path('checkout', views.checkout, name="checkout"),
path('home', views.home, name="home"),
path('update_item', views.updateItem, name="update_item"),
path('process_order', views.processOrder, name="process_order"),

path('user/', include('django.contrib.auth.urls')),
path('user/', include('user.urls')),


]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)