import uuid

from django.contrib.gis.db import models
from django.contrib.auth.models import User
from django.utils import timezone

from versatileimagefield.fields import VersatileImageField

from main.models import UserBaseModel
from main.variables import phone_regex

# Create your models here.
class TempProfile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    auto_id = models.PositiveIntegerField(db_index=True, unique=True)
    name = models.CharField(max_length=128 )
    phone = models.CharField(max_length=15, validators=[phone_regex],unique=True)
    email = models.EmailField(unique=True)
    date_added = models.DateTimeField(db_index=True, auto_now_add=True)

    class Meta:
        db_table = 'temp_profile'
        verbose_name = ('Temporary profile')
        verbose_name_plural = ('Temporary profiles')
        ordering = ('auto_id',)

    def __str__(self):
        return str(self.name)
    
    
class PhoneOtp(models.Model):
    name = models.CharField(max_length=256)
    phone = models.CharField(max_length=15, validators=[phone_regex],null=True,blank=True)
    otp = models.CharField(max_length=6, null=False)
    attempts = models.PositiveIntegerField(default=0)
    date_added = models.DateTimeField(db_index=True, auto_now_add=True)
    is_verified = models.BooleanField(default=False)

    class Meta:
        ordering = ('-date_added', )
        verbose_name = 'Phone OTP'
        verbose_name_plural = 'Phone OTP'

    def __str__(self):
        return f"{self.phone} - {self.otp}"
  
  
class EmailOtp(models.Model):
    name = models.CharField(max_length=256)
    email = models.EmailField(unique=True)
    otp = models.CharField(max_length=6, null=False)
    attempts = models.PositiveIntegerField(default=0)
    date_added = models.DateTimeField(db_index=True, auto_now_add=True)
    is_verified = models.BooleanField(default=False)

    class Meta:
        ordering = ('-date_added', )
        verbose_name = 'Email OTP'
        verbose_name_plural = 'Email OTP'

    def __str__(self):
        return f"{self.email} - {self.otp}" 


class PasswordResetToken(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(default=timezone.now)
    expires_at = models.DateTimeField()
    
    class Meta:
        ordering = ('-created_at', )
        verbose_name = 'Password Reset Token'
        verbose_name_plural = 'Password Reset Token'

    def __str__(self):
        return str(self.user)


class Customer(UserBaseModel):
    user = models.ForeignKey("auth.User", blank=True, related_name="user_%(class)s_objects", on_delete=models.CASCADE)
    name = models.CharField(max_length=128 )
    phone = models.CharField(max_length=15, validators=[phone_regex],unique=True)
    email = models.EmailField()
    image = VersatileImageField('Image', upload_to="Customer/profile", null=True,blank=True)
    password = models.CharField(max_length=256)
    is_terms_agreed = models.BooleanField(default=False)
    
    google_id_token = models.CharField(max_length=500, blank=True, null=True)
    apple_id_token = models.CharField(max_length=500, blank=True, null=True)


    class Meta:
        db_table = 'customer'
        verbose_name = ('customer')
        verbose_name_plural = ('customers')
        ordering = ('-date_added',)

    def __str__(self):
        return f"{self.name} - {self.phone}"