from django.forms import ModelForm
from main.models import Product
from django.utils.html import strip_tags

class ProductEntryForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "description", "price", "skin_type"]

    def clean_name(self):
        name = self.cleaned_data["name"]
        return strip_tags(name)
    
    def clean_product(self):
        product = self.cleaned_data["product"]
        return strip_tags(product)

    def clean_skintype(self):
        skin_type = self.cleaned_data["skin_type"]
        return strip_tags(skin_type)  