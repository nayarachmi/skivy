from django.test import TestCase, Client
from django.utils import timezone
from .models import Product

class mainTest(TestCase):
    def test_main_url_is_exist(self):
        response = Client().get('')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get('')
        self.assertTemplateUsed(response, 'main.html')

    def test_nonexistent_page(self):
        response = Client().get('/skibidi/')
        self.assertEqual(response.status_code, 404)

    def test_recommended_for_sensitive_skin(self):
        # Membuat entri produk untuk pengujian
        product = Product.objects.create(
            name="Sensitive Skin Cream",
            description="A soothing cream for sensitive skin.",
            price=20000,
            skin_type="sensitive, dry"
        )
        # Pengujian properti is_recommended_for_sensitive_skin
        self.assertTrue(product.is_recommended_for_sensitive_skin)

    def test_not_recommended_for_sensitive_skin(self):
        # Membuat entri produk yang tidak direkomendasikan untuk kulit sensitif
        product = Product.objects.create(
            name="Oily Skin Gel",
            description="A gel for oily skin types.",
            price=15000,
            skin_type="oily, combination"
        )
        # Pengujian properti is_recommended_for_sensitive_skin
        self.assertFalse(product.is_recommended_for_sensitive_skin)
