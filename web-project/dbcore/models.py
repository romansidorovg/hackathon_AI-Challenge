from django.db import models


class InputFormModel(models.Model):
    file = models.FileField(upload_to='model/')

    class Meta:
        verbose_name = 'Модель'
        verbose_name_plural = 'Модель'


class ResultModelFile(models.Model):
    file = models.FileField(upload_to='result/')

    class Meta:
        verbose_name = 'Результат предсказания'
        verbose_name_plural = 'Результат предсказания'