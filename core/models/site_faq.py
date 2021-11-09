from django.db import models


class SiteFAQ(models.Model):
    question = models.TextField(blank=True, null=True)
    answer = models.TextField(blank=True, null=True)
    order_weight = models.PositiveIntegerField(default=0)

    def slug_name(self):
        return self.question

    def __str__(self):
        return self.question
