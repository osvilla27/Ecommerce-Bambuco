from django.db import models
from apps.user.models import UserAccount
from apps.product.models import Product, Variants


class Cart(models.Model):
    user_id = models.OneToOneField(
        UserAccount, on_delete=models.CASCADE, null=True, verbose_name='usuario')
    created = models.DateTimeField(auto_now_add=True, verbose_name='creado')
    updated = models.DateTimeField(auto_now=True, verbose_name='actualizado')

    def __str__(self):
        return f'{self.id} {self.updated}'

    def get_cart_items_set(self):
        return self.cart_items.all()

    @property
    def count_cart_items_set(self):
        return self.cart_items.count()
    
    @property
    def total_amount(self):
        items = self.cart_items.all()
        total = 0
        for product_variation in items:
            total += product_variation.sub_total
        return total


class CartItem(models.Model):
    STATUS = (
        ('True', 'Activo'),
        ('False', 'Desactivado'),
    )

    product_id = models.ForeignKey(
        Product, on_delete=models.CASCADE, verbose_name='producto')
    cart_id = models.ForeignKey(
        Cart, on_delete=models.CASCADE, verbose_name='cart', related_name="cart_items")
    variant_id = models.ForeignKey(
        Variants, on_delete=models.CASCADE, blank=True, null= True, verbose_name='variante')
    quantity = models.IntegerField(default=1, verbose_name='cantidad')
    status = models.CharField(
        max_length=20, choices=STATUS, verbose_name='estado')
    created = models.DateTimeField(auto_now_add=True, verbose_name='creado')
    updated = models.DateTimeField(auto_now=True, verbose_name='actualizado')

    @property
    def sub_total(self):
        if self.variant_id is not None:
            return self.variant_id.price * self.quantity
        return self.product_id.price * self.quantity

    def __unicode__(self):
        return self.product_id
