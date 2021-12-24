# Generated by Django 3.2.8 on 2021-12-24 07:27

import backend.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0007_auto_20211222_2334'),
    ]

    operations = [
        migrations.AddField(
            model_name='labelimg',
            name='publish_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_img', to='backend.userinfo'),
        ),
        migrations.AlterField(
            model_name='labelimg',
            name='img',
            field=models.ImageField(max_length=1000, upload_to=backend.models.getURL),
        ),
    ]
