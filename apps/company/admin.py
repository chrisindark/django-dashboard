from django.contrib import admin

from .models import Company, Subscription, Contact
from .forms import CompanyForm, SubscriptionForm, ContactForm


class CompanyAdmin(admin.ModelAdmin):
    # fields = ('number_of_buildings', 'sf_under_mgmt',)
    list_display = (
        'company_name', 'street_address', 'city', 'state',
        'postal_code', 'number_of_buildings', 'sf_under_mgmt',)
    form = CompanyForm


class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('trial', 'trial_length', 'signup_date', 'renewal_date',
                    'price_per_sq_feet', 'module')
    form = SubscriptionForm


class ContactAdmin(admin.ModelAdmin):
    list_display = ()
    form = ContactForm

# Register your models here.
admin.site.register(Company, CompanyAdmin)
admin.site.register(Subscription, SubscriptionAdmin)
admin.site.register(Contact, ContactAdmin)
