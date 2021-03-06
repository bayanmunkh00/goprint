# Generated by Django 3.1.12 on 2021-09-23 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_order_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='company',
            field=models.CharField(default=20210923, max_length=60),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='customer',
            field=models.CharField(default=20210923, max_length=60),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='email',
            field=models.CharField(default=20210923, max_length=40),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='phone',
            field=models.IntegerField(default=20210923),
            preserve_default=False,
        ),
    ]
