# Generated by Django 3.0.3 on 2020-09-20 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketing', '0003_slider_order'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='slider',
            options={'ordering': ['order', '-start_date', '-end_date']},
        ),
        migrations.AddField(
            model_name='slider',
            name='url_link',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]