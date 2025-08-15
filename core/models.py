<<<<<<< HEAD
import uuid
from django.db import models
from django.db.models.functions import Lower, Upper, Length, Concat
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.db.models import Sum, Prefetch, Count, Avg, Max, Min, StdDev, Variance, CharField, Value
from django.db import connection


# Create your models here.
class Restaurant(models.Model):
    
    # enumeration type
    class Restaurant_Type(models.TextChoices):
        ITALY = "IT", _("Italy")
        CHINESE = "CH", _("Chinese")
        JAPAN = "JP", _("Japan")
        NIGERIA = "NG", _("Nigeria")

    # table fields
    name = models.CharField(max_length=100, validators=[])
    email = models.EmailField(_("Email"), max_length=254, unique=True)
    type = models.CharField(max_length=5, choices=Restaurant_Type, default=Restaurant_Type.NIGERIA) # enum applied
    created_at = models.DateTimeField(auto_now_add=True, default=timezone.now(), db_comment="the date that restaurant was created")
    updated_at = models.DateTimeField(auto_now=True, default=timezone.now(), help_text="Please use the following format: <em>YYYY-MM-DD</em>.")
    deleted_at = models.DateTimeField(auto_now_add=True, default=timezone.now())

    # table default settings
    class Meta:
        db_table = 'restaurant'
        ordering = [Lower('created_at')]
        get_latest_by = 'created_at'
        managed = True
        verbose_name = 'Restaurant'
        verbose_name_plural = 'Restaurants'

    # format return values
    def __str__(self):
        return f"{self.name} {self.type}"
    
    # set default save method
    def save(self, *args, **kwargs):
        if self._state.adding:
            print(self._state.adding)

        return super().save(*args, **kwargs)


class Order(models.Model):
    order_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
=======
from django.db import models

# Create your models here.

class Core(models.Model):
    pass
>>>>>>> 37c8de4e6d889e676bff40b3af33b47307371d3d
