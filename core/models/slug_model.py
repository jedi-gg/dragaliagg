from django.db import models
from django.utils.text import slugify


class SlugModel(models.Model):
    '''
    SlugModel expects a name field or a slug_name property defining the name
    to be used in slug generations
    '''

    slug = models.SlugField(
        default='',
        editable=False,
        max_length=120
    )

    def save(self, *args, **kwargs):
        if getattr(self, 'name', None):
            self.slug = slugify(self.name, allow_unicode=True)
        else:
            self.slug = slugify(self.slug_name(), allow_unicode=True)

        super(SlugModel, self).save(*args, **kwargs)

    class Meta:
        abstract = True
