from django import forms
from django.core.validators import MaxLengthValidator, MinValueValidator


class CompanyForm(forms.ModelForm):
    NUMBER_OF_BUILDING_CHOICES = (
        ('<=10', 'Up to 10'),
        ('1', 'One'),
        ('2', 'Two'),
        ('3', 'Three'),
        ('4', 'Four'),
        ('5', 'Five'),
    )
    SF_UNDER_MGMT_CHOICES = (
        ('<1000000', 'Less than 1 Million'),
        ('<10000', 'Less than 1 Thousand'),
        ('<100', 'Less than 1 Hundred'),
        ('<10', 'Less than Ten'),
    )
    postal_code = forms.IntegerField(max_value=999999, min_value=100000)

    number_of_buildings = forms.ChoiceField(choices=NUMBER_OF_BUILDING_CHOICES)
    sf_under_mgmt = forms.ChoiceField(choices=SF_UNDER_MGMT_CHOICES)

    def clean(self):
        return super().clean()


class SubscriptionForm(forms.ModelForm):
    MODULE_CHOICES = (
        ('tenant', 'Tenant'),
        ('vendor', 'Vendor'),
        ('preventative_maintenance', 'Preventative Maintenance'),
    )

    trial = forms.ChoiceField(
        choices=((False, 'False'), (True, 'True')),
        widget=forms.RadioSelect
    )
    trial_length = forms.IntegerField(max_value=366, min_value=1)
    module = forms.ChoiceField(choices=MODULE_CHOICES)

    def clean(self):
        return super().clean()
