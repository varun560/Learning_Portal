# Generated by Django 3.0.6 on 2020-05-18 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0004_lecture'),
    ]

    operations = [
        migrations.AddField(
            model_name='lecture',
            name='src',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
    ]
