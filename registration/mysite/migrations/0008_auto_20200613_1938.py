# Generated by Django 3.0.6 on 2020-06-13 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0007_auto_20200613_1738'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cour',
            options={},
        ),
        migrations.AlterField(
            model_name='courimage',
            name='image',
            field=models.FileField(upload_to='images/'),
        ),
    ]
