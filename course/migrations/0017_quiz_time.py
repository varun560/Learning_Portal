# Generated by Django 3.0.6 on 2020-05-19 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0016_question_quiz'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='time',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
    ]