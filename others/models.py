from django.db import models

class Workers(models.Model):
    full_name = models.CharField(max_length=100, verbose_name="Full name")
    job = models.CharField(max_length=50, verbose_name="Job")
    email = models.EmailField(verbose_name="Email")
    picture = models.ImageField(upload_to='workers/%Y/%m/%d', verbose_name="Worker picture", blank=True)
    facebook_profil = models.CharField(max_length=100, verbose_name="Account of Facebook")
    youtube_profil = models.CharField(max_length=100, verbose_name="Account of Instagram")

    def __str__(self) -> str:
        return self.full_name
