# Generated by Django 5.0.6 on 2024-07-14 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pet', '0003_petadopted'),
    ]

    operations = [
        migrations.AddField(
            model_name='pet',
            name='image',
            field=models.ImageField(default=True, upload_to='pets/'),
            preserve_default=False,
        ),
    ]
