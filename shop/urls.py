from django.urls import path
from shop import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home_page'),
    path('catalog/<str:tag>', views.CatalogView.as_view(), name='catalog'),
    path('cart/', views.CartView.as_view(), name='cart'),
    path('product/<int:product_id>', views.ProductView.as_view(), name='product'),
    path('order/', views.OrderView.as_view(), name='order'),
]
