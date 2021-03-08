from django.db import models
from django.utils.translation import gettext_lazy as _


class Course(models.Model):
    name=models.CharField(max_length=500)
    referral_url=models.URLField()
    description=models.TextField()
    provider=models.ForeignKey('Provider',on_delete=models.CASCADE)
    created=models.DateTimeField(auto_now_add=True)


class Provider(models.Model):
    name=models.CharField(max_length=300)
    website=models.URLField(_("provider website"), max_length=500,blank=True)

