# Generated by Django 4.1.7 on 2023-03-30 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0009_alter_toy_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='kids',
            name='toys',
            field=models.ManyToManyField(to='main_app.toy'),
        ),
    ]
