# Generated by Django 3.0.3 on 2020-08-14 18:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20200814_1837'),
    ]

    operations = [
        migrations.RenameField(
            model_name='emailconfirmed',
            old_name='hashkey',
            new_name='activation_key',
        ),
    ]
