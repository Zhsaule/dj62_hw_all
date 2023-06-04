from django.db import models
from django.template.defaultfilters import slugify


class Phone(models.Model):
    # TODO: Добавьте требуемые поля
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=11, decimal_places=2)
    image = models.URLField(max_length=200)
    release_date = models.DateField(default='null')
    lte_exists = models.BooleanField(default='True')
    slug = models.SlugField(max_length=200)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Phone, self).save(*args, **kwargs)

