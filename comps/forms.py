from django import forms

from comps.models import Comp


class CompForm(forms.ModelForm):
    def clean(self):
        cleaned_data = super().clean()

        new_slug = Comp.get_slug_string(
            None,
            cleaned_data['post_date'],
            cleaned_data['difficulty'],
            cleaned_data['creator'],
            cleaned_data['suffix'],
        )

        # Check for identical slugs
        same_slugs = Comp.objects.filter(
            slug=new_slug).exclude(pk=self.instance.pk)

        if same_slugs:
            raise forms.ValidationError("Slug (and likely comp) already exist.")
