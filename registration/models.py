from django.db import models

class Register(models.Model):
    full_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(verbose_name="Email")
    password = models.CharField(max_length=100)
    confirm_password = models.CharField(max_length=100)

    def info(self):
        return {
            'full_name': ('charfield', {
                'max_length': 100,
                'is_alpha': True,
                'is_empty': False
            }),
            'last_name': ('charfield', {
                'max_length': 100,
                'null': True,
                'is_alpha': True,
                'is_empty': True
            }),
            'email': ('emailfield', {
                'max_length': 100,
                'unique': True,
                'is_empty': False
            }),
            'password': ('charfield', {
                'max_length': 100,
                'alpha_numeric': True,
                'is_empty': False
            }),
            'confirm_password': ('charfield', {
                'max_length': 100,
                'alpha_numeric': True,
                'is_empty': False
            }),
            
        }



    def __str__(self) -> str:
        return self.full_name

class Login(models.Model):
    email = models.EmailField(verbose_name="Email")
    password = models.CharField(max_length=100)

    def info(self):
        return {
            'email': ('emailfield', {
                'max_length': 100,
                'unique': True,
                'is_empty': False
            }),
            'password': ('charfield', {
                'max_length': 100,
                'alpha_numeric': True,
                'is_empty': False
            })
        }



    def __str__(self) -> str:
        return self.email