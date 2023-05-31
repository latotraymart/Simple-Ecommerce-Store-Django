from django.shortcuts import render
from django.http import JsonResponse
import json
import datetime

from .models import *
from .utils import cookieCart, cartData, guestOrder

# Create your views here.

def stores(request):
	data = cartData(request)
	cartItems = data['cartItems']
			
	products = None
	categories = Category.objects.all()
	categoryID = request.GET.get('category')
	if categoryID:
		products = Product.get_all_products_by_categoryid(categoryID)
	else:
		products = Product.get_all_products();

	context ={'products':products, 'cartItems':cartItems, 'categories':categories}
	return render(request, 'stores.html',context)

def cart(request):

	data = cartData(request)
	cartItems = data['cartItems']
	order = data['order']
	items = data['items']

	context = {'items':items, 'order':order, 'cartItems':cartItems}
	
	return render(request, 'cart.html',context)




def checkout(request):
	
	data = cartData(request)
	cartItems = data['cartItems']
	order = data['order']
	items = data['items']
	qrname = Qrcode_gcash.objects.all()
	qrname2 = Qrcode_paymaya.objects.all()
		
	context = {'items':items, 'order':order, 'cartItems':cartItems, 'qrname':qrname, 'qrname2':qrname2}
	return render(request, 'checkout.html',context)

def home(request):
	
	return render(request, 'homepage.html',{})


def updateItem(request):
	data = json.loads(request.body)
	productId = data['productId']
	action = data['action']
	print('Action:', action)
	print('Product:', productId)


	customer = request.user.customer
	product = Product.objects.get(id=productId)
	order, created = Order.objects.get_or_create(customer=customer, complete=False)

	orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)


	if action == 'add':
		orderItem.quantity = (orderItem.quantity + 1)
	elif action == 'remove':
		orderItem.quantity = (orderItem.quantity - 1)

	orderItem.save()

	if orderItem.quantity <= 0:
		orderItem.delete()

	return JsonResponse('Item was added', safe=False)

from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def processOrder(request):
	transaction_id = datetime.datetime.now().timestamp()
	data = json.loads(request.body)

	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
		
		
	else:
		customer, order = guestOrder(request, data)

	total = float(data['form']['total'])
	order.transaction_id = transaction_id

	if total == order.get_cart_total:
		order.complete = True
	order.save()

	if order.shipping == True:
		ShippingAddress.objects.create(
				customer=customer,
				order=order,
				address=data['shipping']['address'],
				city=data['shipping']['city'],
				baranggay=data['shipping']['baranggay'],
				country=data['shipping']['country'],
				zipcode=data['shipping']['zipcode'],


			)

	return JsonResponse('Payment complete', safe=False)
	
	


