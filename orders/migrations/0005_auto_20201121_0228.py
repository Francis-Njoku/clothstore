# Generated by Django 3.0.3 on 2020-11-21 01:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20201119_0230'),
        ('orders', '0004_auto_20201120_2242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='billing_address',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='billing_address', to='accounts.UserAddress'),
        ),
        migrations.AlterField(
            model_name='order',
            name='shipping_address',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='shipping_address', to='accounts.UserAddress'),
        ),
    ]