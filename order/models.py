from django.db import models

class Food(models.Model):
    name = models.CharField('name', max_length=30)
    description = models.CharField('설명', max_length=100, blank=True,
                                   help_text="간단하게 설명할 문구, 빈칸 가능")
