import uuid
from decimal import Decimal
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    auto_id = models.PositiveIntegerField(db_index=True, unique=True)
    creator = models.ForeignKey(
        "auth.User", blank=True, related_name="creator_%(class)s_objects", on_delete=models.CASCADE)
    updater = models.ForeignKey("auth.User", blank=True, null=True,
                                related_name="updater_%(class)s_objects", on_delete=models.CASCADE)
    date_added = models.DateTimeField(db_index=True, auto_now_add=True)
    date_updated = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        abstract = True
        
        
class UserBaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    auto_id = models.PositiveIntegerField(db_index=True, unique=True)
    date_added = models.DateTimeField(db_index=True, auto_now_add=True)
    date_updated = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        abstract = True
        
        
class Location(BaseModel):
    location = models.CharField(max_length=128)
    short_name = models.CharField(max_length=50, blank=True, null=True)
    latitude = models.CharField(max_length=128,blank=True,null=True)
    longitude = models.CharField(max_length=128,blank=True,null=True)

    class Meta:
        db_table = 'location'
        verbose_name = ('Location')
        verbose_name_plural = ('Location')
        ordering = ('auto_id',)

    def __str__(self):
        return str(self.location)
    
    
class Country(models.Model):
    name = models.CharField(max_length=128)
    alpha2code = models.CharField(max_length=128, unique=True)
    alpha3code = models.CharField(max_length=128)
    country_code = models.CharField(max_length=128, blank=True, null=True)
    flag = models.ImageField('Image',upload_to='countries/flags',blank=True, null=True)

    phone_number_length = models.PositiveIntegerField(blank=True, null=True)
    is_active = models.BooleanField(default=False)

    class Meta:
        db_table = 'countries_country'
        verbose_name = ('country')
        verbose_name_plural = ('countries')
        ordering = ('name',)
        default_permissions = ()

    def __str__(self):
        return self.name
    
    
class Commission(BaseModel):
    commission_amount = models.DecimalField(default=0, decimal_places=2, max_digits=15, validators=[MinValueValidator(Decimal('0.00'))])
    delivery_charge = models.DecimalField(default=0, decimal_places=2, max_digits=15, validators=[MinValueValidator(Decimal('0.00'))])
    tax_percentage = models.DecimalField(default=0, decimal_places=2, max_digits=15, validators=[MinValueValidator(Decimal('0.00'))])

    class Meta:
        db_table = 'commission'
        verbose_name = ('commission')
        verbose_name_plural = ('Commission')
        ordering = ('auto_id',)

    def __str__(self):
        return str(self.id)