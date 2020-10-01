from django.db import models
from django.conf import settings


class Product(models.Model):
    name = models.CharField(max_length=256, verbose_name='Название')
    price = models.PositiveIntegerField(verbose_name='Цена')
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(verbose_name='Фотография')
    tag = models.ForeignKey(to='Tag', on_delete=models.CASCADE, related_name='products', null=True, verbose_name='Тег/категория')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class Tag(models.Model):
    name = models.CharField(max_length=256, unique=True, verbose_name='Тег')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'


class Cart(models.Model):
    user = models.OneToOneField(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='cart', verbose_name='Покупатель')
    products = models.ManyToManyField(to='Product', related_name='carts', verbose_name='Товары')

    def __str__(self):
        return self.user

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзина'


class Review(models.Model):
    RATING_CHOICES = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    ]
    product = models.ForeignKey(to='Product', on_delete=models.CASCADE, related_name='reviews', null=True, verbose_name='Товар')
    author = models.CharField(max_length=128, verbose_name='Автор')
    body = models.TextField(verbose_name='Отзыв')
    rating = models.PositiveIntegerField(choices=RATING_CHOICES, verbose_name='Рейтинг')

    def __str__(self):
        return self.author

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'


class Order(models.Model):
    owner = models.OneToOneField(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Покупатель')
    products = models.ManyToManyField(to='Product', related_name='orders', verbose_name='Товары')

    @property
    def price(self):
        return sum([product for product in self.products])

    def __str__(self):
        return self.owner

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
