from django.db import models
from django.core.validators import MinValueValidator


class Product(models.Model):
    name = models.CharField(max_length=255, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    quantity = models.PositiveIntegerField(default=0)
    in_stock = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']

    def __str__(self) -> str:
        return f"{self.name}"

    @property
    def total_value(self):
        return self.price * self.quantity

    def save(self, *args, **kwargs):
        # Auto-update in_stock based on quantity
        self.in_stock = self.quantity > 0
        super().save(*args, **kwargs)
