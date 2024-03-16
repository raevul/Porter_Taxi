from django.db import models


class Car(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)
    price = models.DecimalField("Цена", max_digits=10, decimal_places=2)
    weight = models.CharField(max_length=40, default="...")
    image = models.ImageField("Картинка", upload_to="services")

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('title', )
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'
