# Generated by Django 3.1.7 on 2021-03-04 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='text',
            field=models.TextField(default='none'),
            preserve_default=False,
        ),
    ]
