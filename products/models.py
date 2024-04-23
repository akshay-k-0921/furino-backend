from django.db import models

from django.core.validators import MaxValueValidator, MinValueValidator

from decimal import Decimal
from versatileimagefield.fields import VersatileImageField

from main.models import BaseModel,UserBaseModel
from users.models import User

# Create your models here.
class Category(BaseModel):
    name = models.CharField(max_length=128)
    image = VersatileImageField('Image', upload_to="Shop/category")
    description = models.TextField(max_length=250, blank=True, null=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'category'
        verbose_name = ('Category')
        verbose_name_plural = ('Categories')
        ordering = ('auto_id',)

    def __str__(self):
        return str(self.name)
    

class Tags(BaseModel):
    name = models.CharField(max_length=128)

    class Meta:
        db_table = 'tags'
        verbose_name = ('Tag')
        verbose_name_plural = ('Tags')
        ordering = ('auto_id',)

    def __str__(self):
        return str(self.name)


class Product(BaseModel):
    model_no = models.CharField(max_length=128)
    name = models.CharField(max_length=128)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = VersatileImageField('Image', upload_to="Shop/products")
    short_description = models.TextField(max_length=250, blank=True, null=True)
    description = models.TextField(max_length=250, blank=True, null=True)
    additional_information = models.TextField(max_length=250, blank=True, null=True)
    package_items = models.CharField(max_length=50)

    tags = models.ManyToManyField(Tags)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'product'
        verbose_name = ('Product')
        verbose_name_plural = ('Products')
        ordering = ('auto_id',)

    def __str__(self):
        return str(self.name)


class Warranty(BaseModel):
    product = models.ForeignKey(Category, on_delete=models.CASCADE)
    summery = models.TextField(max_length=250, blank=True, null=True)
    service_type = models.TextField(max_length=250, blank=True, null=True)
    covered_in_warranty = models.TextField(max_length=250, blank=True, null=True)
    not_covered_in_warranty = models.TextField(max_length=250, blank=True, null=True)

    class Meta:
        db_table = 'warranty'
        verbose_name = ('Warranty')
        verbose_name_plural = ('Warranties')
        ordering = ('auto_id',)


class ProductGallery(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = VersatileImageField('Image', upload_to="Shop/products")

    class Meta:
        db_table = 'product_gallery'
        verbose_name = ('Product Gallery')
        verbose_name_plural = ('Product Galleries')
        ordering = ('auto_id',)

    def __str__(self):
        return str(self.product)
    

class ProductVariant(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    colour = models.CharField(max_length=128)
    filling_material = models.TextField(max_length=250, blank=True, null=True)
    finish_type = models.TextField(max_length=250, blank=True, null=True)
    secondary_material = models.TextField(max_length=250, blank=True, null=True)
    configuration = models.TextField(max_length=250, blank=True, null=True)
    upholstery_material = models.TextField(max_length=250, blank=True, null=True)
    upholstery_colour = models.TextField(max_length=250, blank=True, null=True)
    adjustable_head_rest = models.BooleanField(default=False)
    is_default = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'product_variant'
        verbose_name = ('Product Variant')
        verbose_name_plural = ('Product Variants')
        ordering = ('auto_id',)

    def __str__(self):
        return str(self.name)


class ProductVariantGallery(BaseModel):
    product_variant = models.ForeignKey(ProductVariant, on_delete=models.CASCADE)
    image = VersatileImageField('Image', upload_to="Shop/products")

    class Meta:
        db_table = 'product_variant_gallery'
        verbose_name = ('Product Variant Gallery')
        verbose_name_plural = ('Product Variant Galleries')
        ordering = ('auto_id',)

    def __str__(self):
        return str(self.product)
    

class Batch(BaseModel):
    product_variant = models.ForeignKey(ProductVariant, on_delete=models.CASCADE)
    product_code = models.CharField(max_length=128)
    size = models.CharField(max_length=128)
    dimensions = models.CharField(max_length=128)
    name = models.CharField(max_length=128)
    price = models.DecimalField(default=0, decimal_places=2, max_digits=15, validators=[MinValueValidator(Decimal('0.00'))])
    stock = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'batch'
        verbose_name = ('Batch')
        verbose_name_plural = ('Batchs')
        ordering = ('auto_id',)

    def __str__(self):
        return str(self.name)
    

class Cart(BaseModel):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    product_variant = models.ForeignKey(ProductVariant, on_delete=models.CASCADE)
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)

    class Meta:
        db_table = 'cart'
        verbose_name = ('Cart')
        verbose_name_plural = ('Carts')
        ordering = ('auto_id',)

    def __str__(self):
        return str(self.customer)
