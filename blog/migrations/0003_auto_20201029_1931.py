# Generated by Django 3.1.1 on 2020-10-29 16:31

from django.db import migrations, models

import blog.models


class Migration(migrations.Migration):
    dependencies = [
        ('blog', '0002_blog_score'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='score',
            field=models.FloatField(validators=[blog.models.check_if_valid_score]),
        ),
    ]
