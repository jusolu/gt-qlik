# Generated by Django 3.0.5 on 2020-06-03 06:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0004_auto_20200603_1325'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='cart_id',
            new_name='user',
        ),
    ]
