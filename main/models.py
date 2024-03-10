from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=70)
    slug = models.SlugField(max_length=70, unique=True)

    def __str__(self):
        return self.title


class Car(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)
    price = models.DecimalField("Цена", max_digits=10, decimal_places=2)
    description = models.TextField(max_length=300)
    image = models.FileField("Картинка", upload_to="Портер такси")
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, related_name="cars")

    def __str__(self):
        return self.title
