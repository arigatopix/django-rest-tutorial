# Generated by Django 2.2.2 on 2019-06-13 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='snippet',
            name='code',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
