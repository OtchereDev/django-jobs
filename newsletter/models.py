from django.db import models

CONTENT_TYPE=(
    ('html','html'),
    ('text','text')
)

class Newsletter(models.Model):
    title=models.CharField(max_length=500)
    content_type=models.CharField(choices=CONTENT_TYPE,max_length=30)
    content=models.TextField()
    subscribers=models.ManyToManyField('Subcriber',blank=True)
    created=models.DateTimeField(auto_now_add=True)


class Subcriber(models.Model):
    name=models.CharField(max_length=300)
    email=models.EmailField(max_length=500)

