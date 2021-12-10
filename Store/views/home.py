from django.shortcuts import render, redirect, HttpResponseRedirect
from Store.models.category import Category
from Store.models.product import Products
from django.views import View


class Index(View):
    @staticmethod
    def post(request):
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        cart = request.POST.get('cart')

        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity <= 1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity - 1
                else:
                    cart[product] = quantity + 1
            else:
                cart[product] = 1
        else:
            cart = {product: 1}

        request.session['cart'] = cart
        print('cart', request.session['cart'])
        return redirect('home')

    @staticmethod
    def get(request):
        return HttpResponseRedirect(f'/store{request.get_full_path()[1:]}')


def store(request):
    cart = request.session.get('cart')
    if not cart:
        request.session['cart'] = {}
    products = None
    categories = Category.get_all_categories()
    categoryID = request.GET.get('category')

    if categoryID:
        products = Products.get_all_products_by_category(categoryID)

    else:
        products = Products.get_all_products()

    data = {'products': products, 'categories': categories}

    print('are you?:', request.session.get('email'))
    return render(request, 'index.html', data)
