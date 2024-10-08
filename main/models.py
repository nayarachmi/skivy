from django.db import models
import uuid
from django.contrib.auth.models import User

class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.IntegerField()
    skin_type = models.CharField(max_length=20)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    @property
    def is_recommended_for_sensitive_skin(self): #ganti
        return 'sensitive' in self.skin_type.lower()
# Create your models here.

