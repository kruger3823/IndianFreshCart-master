# Generated by Django 4.0.5 on 2022-07-26 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Portal', '0007_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.CharField(default='', max_length=100),
        ),
    ]