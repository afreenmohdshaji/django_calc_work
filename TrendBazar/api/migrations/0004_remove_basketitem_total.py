# Generated by Django 4.2.7 on 2024-01-13 09:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_basketitem_total_alter_product_picture'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='basketitem',
            name='total',
        ),
    ]
