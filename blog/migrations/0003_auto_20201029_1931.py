# Generated by Django 3.1.1 on 2020-10-29 16:31

import blog.models
from django.db import migrations, models


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
