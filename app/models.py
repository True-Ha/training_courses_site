from django.db import models
from django.urls import reverse


class Training(models.Model):
    name = models.CharField(max_length=300)

    description_week = models.TextField(null=True)
    train1 = models.TextField(null=True)
    train2 = models.TextField(null=True)
    train3 = models.TextField(null=True)
    train4 = models.TextField(null=True)
    train5 = models.TextField(null=True)
    train6 = models.TextField(null=True)
    text_after_train = models.TextField(null=True)

    slug = models.SlugField(max_length=130, unique=True, null=True, db_index=True, verbose_name="URL")

    class Day(models.TextChoices):
        Monday = "Понедельник"
        Wednesday = "Среда"
        Friday = "Пятница"

    class Week(models.TextChoices):
        First_week = "1 неделя"
        Second_week = "2 неделя"
        Third_week = "3 неделя"
        Fourth_week = "4 неделя"

    train_week = models.CharField(max_length=300, choices=Week.choices)
    train_day = models.CharField(max_length=300, choices=Day.choices)

    class Meta:
        verbose_name = 'Тренировка'
        verbose_name_plural = 'Тренировки'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('train_detail', kwargs={"slug": self.slug})



