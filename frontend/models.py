from django.db import models
from django.urls import reverse

CATEGORY_CHOICES = (
    ("C", "Computer"),
    ("M", "Mobile"),
    ("T", "Tablet"),
)

LABEL_CHOICES = (
    ("N", "New"),
    ("U", "Used"),
    ("R", "Refurbished"),
)


class Item(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    discount_price = models.FloatField(blank=True, null=True)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=5)
    label = models.CharField(choices=LABEL_CHOICES, max_length=5)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField()
    image = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.title

    def get_discount_percent(self):
        return 100 - (self.discount_price * 100 / self.price)

    def get_item_url(self):
        return reverse("frontend:item-detail", kwargs={"slug": self.slug})
