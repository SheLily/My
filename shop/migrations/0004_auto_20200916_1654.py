# Generated by Django 3.1 on 2020-09-16 16:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20200916_1653'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='tag',
        ),
        migrations.AddField(
            model_name='product',
            name='tag',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='shop.tag'),
        ),
    ]
