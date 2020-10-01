from typing import Dict, Any
from django.views import View
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from shop.models import Product, Tag, Cart, Review, Order
from shop.forms import ReviewForm


class HomePageView(View):
    context: Dict[str, Any] = {}

    def get(self, request):
        self.context['tags'] = Tag.objects.all()

        return render(request, 'shop/home.html', context=self.context)


class CatalogView(View):
    context: Dict[str, Any] = {}

    def get(self, request, tag: str):
        self.context['products'] = Product.objects.filter(tag__name=tag)
        self.context['tags'] = Tag.objects.all()
        request.session['tag'] = tag

        return render(request, 'shop/catalog.html', context=self.context)


class ProductView(View):
    context: Dict[str, Any] = {}

    def get(self, request, product_id: int):

        self._set_context_data(product_id)

        return render(request, 'shop/product.html', context=self.context)

    def post(self, request, product_id):
        self._set_context_data(product_id, data=request.POST)
        form = self.context['review_form']

        if form.is_valid():
            form.save()

        return render(request, 'shop/product.html', context=self.context)

    def _set_context_data(self, product_id: int, data=None):
        self.context['tags'] = Tag.objects.all()
        self.context['product'] = get_object_or_404(Product, id=product_id)
        self.context['reviews'] = Review.objects.filter(product__id=product_id)
        self.context['review_form'] = ReviewForm(data=data)
        self.context['cart'], created = Cart.objects.get_or_create(user=self.request.user)


class CartView(LoginRequiredMixin, View):
    context: Dict[str, Any] = {}

    def get(self, request):
        self._set_context_data()

        return render(request, 'shop/cart.html', context=self.context)

    def post(self, request):
        self._set_context_data()

        tag = request.session.get('tag')
        product_id = request.POST['product_id']
        action = request.POST['action']

        if action.upper() == 'ADD':
            self.context['cart'].products.add(get_object_or_404(Product, id=product_id))
            return redirect('catalog', tag=tag) if tag else redirect('home_page')

        if action.upper() == 'REMOVE':
            self.context['cart'].products.remove(get_object_or_404(Product, id=product_id))
            return render(request, 'shop/cart.html', context=self.context)

    def _set_context_data(self):
        self.context['cart'], created = Cart.objects.get_or_create(user=self.request.user)
        self.context['tags'] = Tag.objects.all()


class OrderView(LoginRequiredMixin, View):
    context: Dict[str, Any] = {}

    def post(self, request):
        self.context['tags'] = Tag.objects.all()
        cart = Cart.objects.get(user=self.request.user)
        order = Order.objects.create(owner=self.request.user)
        for product in cart.products.all():
            order.products.add(product)

        order.save()
        cart.products.remove()

        return render(request, 'shop/order.html', context=self.context)
