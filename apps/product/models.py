from django.db import models
from django.utils.safestring import mark_safe
from ckeditor_uploader.fields import RichTextUploadingField
import os


class Category(models.Model):
    STATUS = (
        ('True', 'Activo'),
        ('False', 'Desactivado'),
    )

    parent = models.ForeignKey(
        'self', related_name='children',
        on_delete=models.CASCADE,
        blank=True, null=True,
        verbose_name='padre'
    )
    name = models.CharField(max_length=50, verbose_name='nombre')
    keywords = models.CharField(max_length=255)
    description = models.CharField(max_length=255, verbose_name='descripción')
    status = models.CharField(
        max_length=10, choices=STATUS, verbose_name='estado')
    slug = models.SlugField(null=False, unique=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name='creado')
    updated = models.DateTimeField(auto_now=True, verbose_name='actualizado')

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'

    def __str__(self):
        return self.name


class Product(models.Model):
    STATUS = (
        ('True', 'Activo'),
        ('False', 'Desactivado'),
    )

    VARIANTS = (
        ('None', 'Ninguna'),
        ('Size', 'Talla'),
        ('Color', 'Color'),
        ('Size-Color', 'Talla-Color'),
        ('Landing', 'Landing'),
    )

    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, verbose_name='categoría')
    name = models.CharField(max_length=200, unique=True, verbose_name='nombre')
    keywords = models.CharField(max_length=255, blank=True)
    description = models.TextField(max_length=255, verbose_name='descripción')
    image = models.ImageField(
        upload_to='photos/products', null=False, verbose_name='imagen')
    price = models.IntegerField(default=0, verbose_name='precio')
    compare_price = models.IntegerField(
        default=0, verbose_name='compare precio')
    stock = models.IntegerField(default=0)
    minstock = models.IntegerField(default=3)
    variant = models.CharField(
        max_length=10, choices=VARIANTS, default='None', verbose_name='variante')
    detail = RichTextUploadingField(verbose_name='detalles')
    slug = models.SlugField(null=False, unique=True)
    status = models.CharField(
        max_length=10, choices=STATUS, verbose_name='estado')
    created = models.DateTimeField(auto_now_add=True, verbose_name='creado')
    updated = models.DateTimeField(auto_now=True, verbose_name='actualizado')

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

    def __str__(self):
        return self.name

    def image_tag(self):
        if self.image.url is not None:
            return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
        else:
            return ""


class Images(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, verbose_name='producto')
    name = models.CharField(max_length=50, blank=True, verbose_name='nombre')
    image = models.ImageField(
        blank=True, upload_to='photos/products', verbose_name='imagen')

    class Meta:
        verbose_name = 'Imagen'
        verbose_name_plural = 'Imagenes'

    def __str__(self):
        return self.name


class Color(models.Model):
    name = models.CharField(max_length=20, verbose_name='nombre')
    code = models.CharField(max_length=20, null=False,
                            unique=True, verbose_name='código')

    class Meta:
        verbose_name = 'Color'
        verbose_name_plural = 'Colores'

    def __str__(self):
        return self.name

    def color_tag(self):
        if self.code is not None:
            return mark_safe(
                '<div style="background-color:{}; height: 26px; width: 26px; border-radius: 23px">&emsp;</div>'
                .format(self.code)
            )
        else:
            return ""


class Size(models.Model):
    name = models.CharField(max_length=20, verbose_name='nombre')
    code = models.CharField(max_length=20, null=False,
                            unique=True, verbose_name='código')

    class Meta:
        verbose_name = 'Talla'
        verbose_name_plural = 'Tallas'

    def __str__(self):
        return self.name


class Variants(models.Model):
    name = models.CharField(max_length=100, blank=True,
                            null=True, verbose_name='nombre')
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, verbose_name='producto')
    color = models.ForeignKey(
        Color, on_delete=models.CASCADE, blank=True, null=True)
    size = models.ForeignKey(
        Size, on_delete=models.CASCADE, blank=True, null=True, verbose_name='talla')
    image_id = models.IntegerField(blank=True, null=True, default=0)
    quantity = models.IntegerField(default=1, verbose_name='cantidad')
    price = models.DecimalField(
        max_digits=12, decimal_places=2, default=0, verbose_name='precio')

    class Meta:
        verbose_name = 'Variante'
        verbose_name_plural = 'Variantes'

    def __str__(self):
        return self.name

    def image(self):
        img = Images.objects.get(id=self.image_id)
        if img.id is not None:
            varimage = img.image.url
        else:
            varimage = ""
        return varimage

    def image_tag(self):
        img = Images.objects.get(id=self.image_id)
        if img.id is not None:
            return mark_safe('<img src="{}" height="50"/>'.format(img.image.url))
        else:
            return ""