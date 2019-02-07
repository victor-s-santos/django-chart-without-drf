import json
from django.shortcuts import render
from .models import Product, Person

def products(request):
	queryset2 = Person.objects.all()
	names2 = [obj.name for obj in queryset2]
	ages = [int(obj.age) for obj in queryset2]
	queryset = Product.objects.all()
	names = [obj.name for obj in queryset]
	prices = [int(obj.price) for obj in queryset]


	context = {
		'names': json.dumps(names),
		'prices': json.dumps(prices),
		'names2': json.dumps(names2),
		'ages': json.dumps(ages),
	}
	return render(request, 'chart/products.html', context)

# Create your views here.
