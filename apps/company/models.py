from django.db import models
from django.utils import timezone


# Create your models here.
class Company(models.Model):
    company_name = models.CharField(max_length=50)
    street_address = models.CharField(max_length=50)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    postal_code = models.CharField(max_length=6)
    number_of_buildings = models.CharField(max_length=30)
    sf_under_mgmt = models.CharField(max_length=30)


class Subscription(models.Model):
    trial = models.BooleanField(default=True)
    trial_length = models.PositiveSmallIntegerField()
    signup_date = models.DateField(auto_now_add=True)
    renewal_date = models.DateField(auto_now=True)
    price_per_sq_feet = models.DecimalField(max_digits=7, decimal_places=6, default=0.000000)
    module = models.CharField(max_length=50, blank=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.signup_date = timezone.now()
        self.renewal_date = timezone.now() + timezone.timedelta(days=1)
        return super().save(*args, **kwargs)


class Contact(models.Model):
    contact_name = models.CharField(max_length=50)
    title = models.CharField(max_length=20)
    work_phone = models.CharField(max_length=20)
    fax = models.CharField(max_length=20, blank=True)
    mobile_phone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(max_length=255)
    referral_option = models.CharField(max_length=30)
    subscribe_to_notices = models.BooleanField(default=True)
