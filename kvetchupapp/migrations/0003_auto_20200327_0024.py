# Generated by Django 3.0.2 on 2020-03-27 00:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kvetchupapp', '0002_auto_20200327_0022'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='review',
            options={'ordering': ['-review_date']},
        ),
    ]
