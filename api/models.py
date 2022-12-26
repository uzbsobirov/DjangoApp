from django.db import models
from shop.models import Category
from django.core.validators import MinValueValidator, MaxValueValidator
from .managers import AvailableManager
from django.utils.text import slugify


class Post(models.Model):
    STATUS = (
        ('available', 'Available'),
        ('notavailable', 'NotAvailable')
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    slug = models.SlugField(max_length=200)
    image = models.ImageField(upload_to='posts/%Y/%m/%d')
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.CharField(max_length=100, choices=STATUS, default='available')
    rating = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)], null=True, blank=True)
    discount = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], null=True, blank=True)
    objects = models.Manager()
    availabled = AvailableManager()


    def save(self, *args, **kwargs):
        if not self.pk:
            self.slug = slugify(self.name)
        super(Post, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return self.name

