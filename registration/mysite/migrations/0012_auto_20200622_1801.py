# Generated by Django 3.0.6 on 2020-06-22 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0011_remove_cour_created_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cour',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
