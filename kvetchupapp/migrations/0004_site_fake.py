# Generated by Django 3.0.2 on 2020-04-03 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kvetchupapp', '0003_auto_20200327_0024'),
    ]

    operations = [
        migrations.AddField(
            model_name='site',
            name='fake',
            field=models.CharField(default='hello', max_length=200),
            preserve_default=False,
        ),
    ]
