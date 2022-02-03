from django.db import models
from django.utils.translation import gettext as _

# Create your models here.

class Blue(models.Model):
    title = models.CharField(_("title"),max_length=255)
    contenet = models.CharField(_("content"),max_length=255)
    app_name =  models.CharField(_("app_name"),max_length=255)


    def __str__(self):
        return self.title
    
