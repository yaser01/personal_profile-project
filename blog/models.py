from django.db import models
from django.core.validators import ValidationError
from django.utils.translation import gettext_lazy as _


def check_if_valid_score(value):
    if not (0.0 <= value <= 10.0):
        raise ValidationError(
            _('%(value)s is not an valid score'),
            params={'value': value},
        )


class Blog(models.Model):
    def __str__(self):
        return self.title
    title = models.CharField(max_length=150)
    score = models.FloatField(validators=[check_if_valid_score])
    image = models.ImageField(upload_to='blog/images')
    description = models.TextField(blank=True)

