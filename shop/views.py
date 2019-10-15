from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from django.db.models import Count

def product_list(request, category_id=None):
    category = None
    products = Product.objects.all()
    ccat = Category.objects.annotate(num_products=Count('products'))
    if(category_id):
        category = get_object_or_404(Category, id=category_id)
        products = products.filter(category=category)

    return render(request, 'products.html',
                    {'products': products,
                    'countcat':ccat})

