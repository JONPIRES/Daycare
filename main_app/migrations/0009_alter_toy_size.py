# Generated by Django 4.1.7 on 2023-03-30 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0008_alter_toy_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='toy',
            name='size',
            field=models.CharField(choices=[('S', 'Small'), ('M', 'Medium'), ('L', 'Large')], default='S', max_length=1),
        ),
    ]
