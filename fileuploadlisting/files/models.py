from django.db import models

# Create your models here.
class File(models.Model):
    title = models.CharField(max_length=200)
    file = models.FileField(
        upload_to='uploads/',
        verbose_name='File',
    )

    def __str__(self):
        return self.title