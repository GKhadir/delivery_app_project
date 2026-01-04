from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, phone, password=None, **extra_fields):
        if not email:
            raise ValueError("Users must have an email address")
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, phone=phone, **extra_fields)
        user.set_password(password)  # hashes the password
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, phone, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, username, phone, password, **extra_fields)


class UsersData(AbstractBaseUser, PermissionsMixin):
    Roles = (
        ('admin', 'ADMIN'),
        ('customer', 'CUSTOMER'),
        ('delivery', 'DELIVERY'),
    )

    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.BigIntegerField()
    role = models.CharField(max_length=20, choices=Roles, default='customer')
    is_active = models.BooleanField(default=True)
    is_verified = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)  # required for admin
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'phone']

    objects = CustomUserManager()

    def __str__(self):
        return self.email

class user_profiles(models.Model):
    id=models.AutoField(primary_key=True)
    user_id=models.OneToOneField(UsersData,on_delete=models.CASCADE)
    full_name=models.CharField(max_length=100)
    date_of_birth=models.DateField()

class addresses(models.Model):
    id=models.AutoField(primary_key=True)
    user_id=models.ForeignKey(UsersData,on_delete=models.CASCADE)
    address_line1=models.CharField(max_length=100)
    address_line2=models.CharField(max_length=100)
    city=models.CharField(max_length=20)
    state=models.CharField(max_length=20)
    pincode=models.CharField(max_length=20)
    latitude=models.DecimalField(max_digits=20,decimal_places=10)
    longitude=models.DecimalField(max_digits=20,decimal_places=10)
    is_defualt=models.BooleanField(default=False)

class delivary_partner_details(models.Model):
    id=models.AutoField(primary_key=True)
    user_id=models.OneToOneField(UsersData,on_delete=models.CASCADE)
    vehical_no=models.CharField(max_length=20)
    vehocal_type=models.CharField(max_length=20)
    license_no=models.CharField(max_length=20)
    is_available=models.BooleanField(default=False)
