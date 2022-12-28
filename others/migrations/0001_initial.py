# Generated by Django 4.1.4 on 2022-12-28 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Workers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('job', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('facebook_profil', models.CharField(max_length=100)),
                ('youtube_profil', models.CharField(max_length=100)),
            ],
        ),
    ]
