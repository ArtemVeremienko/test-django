# Generated by Django 3.2.8 on 2021-10-06 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='created',
            field=models.DateField(auto_created=True),
        ),
    ]
