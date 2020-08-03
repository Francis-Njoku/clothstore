# Generated by Django 3.0.3 on 2020-07-27 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_variation'),
    ]

    operations = [
        migrations.AddField(
            model_name='variation',
            name='category',
            field=models.CharField(choices=[('size', 'size'), ('color', 'color'), ('package', 'package')], default='size', max_length=120),
        ),
    ]