# Generated by Django 3.0.3 on 2020-07-27 00:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0005_cartitem_noted'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartitem',
            old_name='noted',
            new_name='notes',
        ),
    ]
