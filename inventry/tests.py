from django.test import TestCase
from .models import Product


class ProductModelTests(TestCase):
    def test_total_value_computation(self):
        p = Product.objects.create(name="Pen", price=10, quantity=3, in_stock=True)
        self.assertEqual(p.total_value, 30)

    def test_in_stock_filter(self):
        Product.objects.create(name="A", price=1, quantity=0, in_stock=False)
        Product.objects.create(name="B", price=1, quantity=5, in_stock=True)
        self.assertEqual(Product.objects.filter(in_stock=True).count(), 1)
        self.assertEqual(Product.objects.filter(in_stock=False).count(), 1)
