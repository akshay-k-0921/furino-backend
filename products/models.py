from django.db import models

from versatileimagefield.fields import VersatileImageField

from main.models import BaseModel,UserBaseModel

# Create your models here.
class Category(BaseModel):
    name = models.CharField(max_length=128)
    image = VersatileImageField('Image', upload_to="Customer/profile")
    description = models.TextField(max_length=250, blank=True, null=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'category'
        verbose_name = ('Category')
        verbose_name_plural = ('Categories')
        ordering = ('auto_id',)

    def __str__(self):
        return str(self.name)