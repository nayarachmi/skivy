from django.db import models

class ProductEntry(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.IntegerField()
    skin_type = models.CharField(max_length=20)

    @property
    def is_recommended_for_sensitive_skin(self): #ganti
        return 'sensitive' in self.skin_type.lower()
# Create your models here.
