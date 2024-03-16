from django.db import models


class Car(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)
    price = models.DecimalField("Цена", max_digits=10, decimal_places=2)
    weight = models.CharField(max_length=40, default="...")
    image = models.FileField("Картинка", upload_to="services")

    def __str__(self):
        return self.title
