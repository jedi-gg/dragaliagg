from django.core.management.base import BaseCommand
from django.utils.text import slugify

from game_data.models import PortraitAbility


class Command(BaseCommand):
    def handle(self, *args, **options):
        portrait_abilites = {
            # Strength
            'Strength +10%': 'Increases strength by 10%.',
            '(Element) Strength +18%': 'If the user is attuned to the specified element: increases strength by 18%.',
            '(Element & Weapon) Strength +20%': 'If the user is attuned to the specified element & wields the specified weapon type: increases strength by 20%.',

            # Skill Damage
            'Skill Damage +20%': 'Increases attack skill damage by 20%.',
            '(Element) Skill Damage +35%': 'If the user is attuned to the specified element: increases attack skill damage by 35%.',
            '(Element & Weapon) Skill Damage +40%': 'If the user is attuned to the specified element & wields the specified weapon type: increases attack skill damage by 40%.',

            # Critical Rate
            'Critical Rate +8%': 'Increases critical rate by 8%.',
            '(Element) Critical Rate +13%': 'If the user is attuned to the specified element: increases critical rate by 13%.',
            '(Element & Weapon) Critical Rate +15%': 'If the user is attuned to the specified element & wields the specified weapon type: increases critical rate by 15%.',

            # Force Strike
            'Force Strike +30%': 'Increases force strike damage by 30%.',
            '(Element) Force Strike +45%': 'If the user is attuned to the specified element: increases force strike damage by 45%.',
            '(Element & Weapon) Force Strike +50%': 'If the user is attuned to the specified element & wields the specified weapon type: increases force strike damage by 50%.',

            # HP
            'HP +8%': 'Increases HP by 8%.',
            '(Element) HP +13%': 'If the user is attuned to the specified element: increases HP by 13%.',
            '(Element & Weapon) HP +15%': 'If the user is attuned to the specified element & wields the specified weapon type: increases HP by 15%.',

            # Dragon Damage
            'Dragon Damage +10%': 'Adds 10% to the modifier applied to damage when in dragon form.',
            '(Element) Dragon Damage +15%': 'If the user is attuned to the specified element: adds 15% to the modifier applied to damage when in dragon form.',
            '(Element & Weapon) Dragon Damage +18%': 'If the user is attuned to the specified element & wields the specified weapon type: adds 18% to the modifier applied to damage when in dragon form.',

            # Dragon Haste
            'Dragon Haste +8%': 'Increases dragon gauge fill rate by 8%.',
            '(Element) Dragon Haste +13%': 'If the user is attuned to the specified element: increases dragon gauge fill rate by 13%.',
            '(Element & Weapon) Dragon Haste +15%': 'If the user is attuned to the specified element & wields the specified weapon type: increases dragon gauge fill rate by 15%.',

            # Skill Haste
            'Skill Haste +5%': 'Increases skill gauge fill rate by 5%.',
            '(Element) Skill Haste +7%': 'If the user is attuned to the specified element: increases skill gauge fill rate by 7%.',
            '(Element & Weapon) Skill Haste +8%': 'If the user is attuned to the specified element & wields the specified weapon type: increases skill gauge fill rate by 8%.',

            # Skill Prep
            'Skill Prep +30%': 'Fills 30% of skill gauges at the start of quests.',
            '(Element) Skill Prep +45%': 'If the user is attuned to the specified element: fills 45% of skill gauges at the start of quests.',
            '(Element & Weapon) Skill Prep +50%': 'If the user is attuned to the specified element & wields the specified weapon type: fills 50% of skill gauges at the start of quests.',

            # Defense
            'Defense +6%': 'Increases defense by 6%.',
            '(Element) Defense +8%': 'If the user is attuned to the specified element: increases defense by 8%.',
            '(Element & Weapon) Defense +10%': 'If the user is attuned to the specified element & wields the specified weapon type: increases defense by 10%.',
            
            # Critical Damage
            'Critical Damage +9%': 'Adds 9% to the modifier applied to critical damage.',
            '(Element) Critical Damage +13%': 'If the user is attuned to the specified element: adds 13% to the modifier applied to critical damage.',
            '(Element & Weapon) Critical Damage +15%': 'If the user is attuned to the specified element & wields the specified weapon type: adds 15% to the modifier applied to critical damage.',

            # Recovery Potency
            'Recovery Potency +10%': 'Increases the potency of recovery skills by 10%.',
            '(Element) Recovery Potency +18%': 'If the user is attuned to the specified element: increases the potency of recovery skills by 18%.',
            '(Element & Weapon) Recovery Potency +20%': 'If the user is attuned to the specified element & wields the specified weapon type: increases the potency of recovery skills by 20%.',

            # Dragon Time
            'Dragon Time +10%': 'Extends shapeshift time by 10%.',
            '(Element) Dragon Time +18%': 'If the user is attuned to the specified element: extends shapeshift time by 18%.',
            '(Element & Weapon) Dragon Time +20%': 'If the user is attuned to the specified element & wields the specified weapon type: extends shapeshift time by 20%.',

            # Tradeoffs
            '(Element & Weapon) Steady Hitter I': 'If the user is attuned to the specified element & wields the specified weapon type: increases attack skill damage by 40%, but lowers the modifier applied to critical damage by 25%.',
            '(Element & Weapon) Easy Hitter I': 'If the user is attuned to the specified element & wields the specified weapon type: increases strength by 20%, but reduces force strike damage by 50%.',
            '(Element & Weapon) Lucky Hitter I': 'If the user is attuned to the specified element & wields the specified weapon type: increases critical rate by 15%, but lowers the modifier applied to damage when in dragon form by 18%.',
            '(Element & Weapon) Hasty Hitter I': 'If the user is attuned to the specified element & wields the specified weapon type: increases skill gauge fill rate by 15%, but reduces attack skill damage by 20%.',
        }

        for name, desc in portrait_abilites.items():
            pa_id = slugify(name)

            PortraitAbility.objects.update_or_create(
                id=pa_id,
                defaults={
                    'ability_name': name,
                    'ability_description': desc
                }
            )