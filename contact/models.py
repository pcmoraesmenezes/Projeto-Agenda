from django.db import models
from django.utils import timezone
# Create your models here.
# blank indica a opcionalidade de se registrar aquele campo, quando se está
# true quer dizer que não é obrigatorio registrar o campo


class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50, blank=True)
    email = models.EmailField(max_length=254)
    created_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True)
    show = models.BooleanField(default=True)
    picture = models.ImageField(blank=True, upload_to='pictures/%Y/%m/')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
