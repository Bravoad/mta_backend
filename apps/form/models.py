from django.db import models


class ContactForm(models.Model):
    name = models.CharField(max_length=100,default='')
    phone = models.CharField(max_length=15,default='')
    consent = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
