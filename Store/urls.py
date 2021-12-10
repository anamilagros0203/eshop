from django.urls import path
from .views.cart import Cart
from .views.home import Index, store
from .views.orders import OrderView

urlpatterns = [
    path('', Index.as_view(), name='homepage'),
    path('store', store, name='store'),
    path('cart', Cart.as_view, name='cart'),
    path('orders', OrderView.as_view(), name='orders'),
]
