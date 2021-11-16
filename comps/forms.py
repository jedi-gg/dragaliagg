from django import forms

from comps.models import Comp
from game_data.models import Adventurer


class CompForm(forms.ModelForm):
    def clean(self):
        cleaned_data = super().clean()

        unit_strings = []
        for x in range(0, 4):
            adv_id = self.data['builds-{}-adventurer'.format(x)]
            if adv_id:
                adventurer = Adventurer.objects.get(id=adv_id)
            
                unit_strings.append(adventurer.slug)

        new_slug = Comp.get_slug_string(
            None,
            cleaned_data['post_date'],
            cleaned_data['difficulty'],
            cleaned_data['creator'],
            cleaned_data['suffix'],
            '-'.join(unit_strings)
        )

        # Check for identical slugs
        same_slugs = Comp.objects.filter(
            slug=new_slug).exclude(pk=self.instance.pk)

        if same_slugs:
            raise forms.ValidationError("Slug (and likely comp) already exist.")
