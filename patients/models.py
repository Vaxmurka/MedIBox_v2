from django.db import models
from django.contrib.auth.models import AbstractUser
from users.models import User
from django.template.defaultfilters import slugify

from django.urls import reverse


class Voices(models.Model):

    voice1 = models.FileField(blank=True, null=True)
    voice2 = models.FileField(blank=True, null=True)
    voice3 = models.FileField(blank=True, null=True)
    voice4 = models.FileField(blank=True, null=True)
    voice5 = models.FileField(blank=True, null=True)
    voice6 = models.FileField(blank=True, null=True)
    voice7 = models.FileField(blank=True, null=True)
    voice8 = models.FileField(blank=True, null=True)
    voice9 = models.FileField(blank=True, null=True)
    voice10 = models.FileField(blank=True, null=True)

    class Meta:
        verbose_name = 'Звуки'
        verbose_name_plural = 'Звук'
        db_table = 'Voices'


class Groups(models.Model):

    name = models.CharField(max_length=256)
    slug = models.SlugField(max_length=200, unique=True, db_index=True, verbose_name='URL')

    class Meta:
        verbose_name = 'Группу'
        verbose_name_plural = 'Группа'
        db_table = 'Groups'

    def str(self):
        return self.name


class Patient(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='patients')
    groups = models.ForeignKey(Groups, on_delete=models.CASCADE, related_name='patients')

    first_name = models.CharField(max_length=256)
    username = models.CharField(max_length=256)
    fingerprint = models.PositiveIntegerField()
    portion_of_water = models.CharField(max_length=256)
    number = models.CharField(max_length=256, default="+79000000000")
    voices = models.ForeignKey(Voices, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')

    class Meta:
        verbose_name = 'Пациента'
        verbose_name_plural = 'Пациенты'
        db_table = 'Patients'

    def str(self):
        return f'{self.username} {self.first_name}'

    def get_absolute_url(self):
        return reverse('patient_detail', kwargs={'slug': self.slug})

    def display_id(self):
        return f'{self.fingerprint:05}'

    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.fingerprint)
        return super().save(*args, **kwargs)


class Schedule(models.Model):

    # pills = models.ForeignKey(Pills, on_delete=models.CASCADE, blank=True, null=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, blank=True, null=True)
    # first_taking = models.ForeignKey(Time, on_delete=models.CASCADE, blank=True, null=True, related_name="first_taking")
    # second_taking = models.ForeignKey(Time, on_delete=models.CASCADE, blank=True, null=True, related_name="second_taking")
    # third_taking = models.ForeignKey(Time, on_delete=models.CASCADE, blank=True, null=True, related_name="third_taking")
    # quantity = models.ForeignKey(Quantity, on_delete=models.CASCADE, blank=True, null=True)
    # days = models.ForeignKey(Days, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name = 'Расписание'
        verbose_name_plural = 'Расписание'
        db_table = 'Shedule'


class Taking(models.Model):
    shedule = models.ForeignKey(Schedule, models.CASCADE)

    class Meta:
        verbose_name = 'приема'
        verbose_name_plural = 'Прием'
        db_table = 'Taking'


class Pills(models.Model):
    taking = models.ForeignKey(Taking, models.CASCADE, )
    name = models.CharField(max_length=256)
    # image = models.ImageField()
    container = models.IntegerField()

    class Meta:
        verbose_name = 'Таблетку'
        verbose_name_plural = 'Таблетка'
        db_table = 'Pills'

    def str(self):
        return f'{self.name}'


class Quantity(models.Model):
    shedule = models.ForeignKey(Schedule, models.CASCADE)
    quantity_pills = models.IntegerField()

    class Meta:

        verbose_name = 'Прием таблеток'
        verbose_name_plural = 'Прием таблеток'
        db_table = 'TekingPills'


class Time(models.Model):
    taking = models.ForeignKey(Taking, models.CASCADE, )
    time = models.TimeField()

    class Meta:
        verbose_name = 'Время'
        verbose_name_plural = 'Время'
        db_table = 'Time'


class Days(models.Model):
    shedule = models.ForeignKey(Schedule, models.CASCADE)
    quantity_days = models.IntegerField()

    class Meta:
        verbose_name = 'Дней'
        verbose_name_plural = 'Дни'
        db_table = 'Days'


