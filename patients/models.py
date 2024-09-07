from django.db import models
from django.contrib.auth.models import AbstractUser
from users.models import User
from django.template.defaultfilters import slugify
from django.urls import reverse


class Voices(models.Model):
    name = models.CharField(max_length=120, unique=True, blank=True, null=True)

    voice = models.FileField(blank=True, verbose_name='voice', upload_to='MedIbow_v2/voices/', null=True)

    class Meta:
        verbose_name = 'Звуки'
        verbose_name_plural = 'Звук'
        db_table = 'Voices'

    def __str__(self):
        return f'Звуки: {self.name}'


class Groups(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='User_groups', null=True, blank=True)
    name = models.CharField(max_length=256)
    slug = models.SlugField(max_length=200, unique=True, db_index=True, verbose_name='URL')

    class Meta:
        verbose_name = 'Группу'
        verbose_name_plural = 'Группа'
        db_table = 'Groups'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):  # new
        self.slug = slugify(self.name)
        super(Groups, self).save(*args, **kwargs)


class Patient(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='patients', null=True)
    groups = models.ForeignKey(Groups, on_delete=models.CASCADE, related_name='patients', null=True)
    first_name = models.CharField(max_length=256)
    username = models.CharField(max_length=256)
    fingerprint = models.PositiveIntegerField()
    portion_of_water = models.CharField(max_length=256)
    number = models.CharField(max_length=256, default="+79000000000")
    voices = models.ForeignKey(Voices, on_delete=models.CASCADE, null=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')
    USERNAME_FIELD = 'username'

    class Meta:
        verbose_name = 'Пациента'
        verbose_name_plural = 'Пациенты'
        db_table = 'Patients'

    def __str__(self):
        return f'{self.username} {self.first_name}'

    def get_absolute_url(self):
        return reverse('patient_detail', kwargs={'slug': self.slug})

    def display_id(self):
        return f'{self.fingerprint:05}'

    def save(self, *args, **kwargs):  # new
        self.slug = slugify(self.fingerprint)
        super(Patient, self).save(*args, **kwargs)


# class Schedule(models.Model):
#
#     # pills = models.ForeignKey(Pills, on_delete=models.CASCADE, blank=True, null=True)
#     patient = models.ForeignKey(Patient, on_delete=models.CASCADE, blank=True, null=True)
#     # first_taking = models.ForeignKey(Time, on_delete=models.CASCADE, blank=True, null=True, related_name="first_taking")
#     # second_taking = models.ForeignKey(Time, on_delete=models.CASCADE, blank=True, null=True, related_name="second_taking")
#     # third_taking = models.ForeignKey(Time, on_delete=models.CASCADE, blank=True, null=True, related_name="third_taking")
#     # quantity = models.ForeignKey(Quantity, on_delete=models.CASCADE, blank=True, null=True)
#     # days = models.ForeignKey(Days, on_delete=models.CASCADE, blank=True, null=True)
#
#     class Meta:
#         verbose_name = 'Расписание'
#         verbose_name_plural = 'Расписание'
#         db_table = 'Shedule'
    # def save(self, *args, **kwargs):  # new
    #     if not self.slug:
    #         self.slug = slugify(self.fingerprint)
    #     return super().save(*args, **kwargs)


class Pills(models.Model):
    name = models.CharField(max_length=256, unique=True, blank=True, null=True)
    # image = models.ImageField()
    container = models.IntegerField(blank=True, null=True)

    class Meta:
        verbose_name = 'Таблетку'
        verbose_name_plural = 'Таблетка'
        db_table = 'Pills'

    def __str__(self):
        return f'{self.name} - {self.container}'


class Taking(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, blank=True, null=True)
    pills = models.ForeignKey(Pills, models.CASCADE, blank=True, null=True)
    time = models.TimeField()
    quantity_pills = models.IntegerField()
    monday = models.BooleanField(default=False)
    tuesday = models.BooleanField(default=False)
    wednesday = models.BooleanField(default=False)
    thursday = models.BooleanField(default=False)
    friday = models.BooleanField(default=False)
    saturday = models.BooleanField(default=False)
    sunday = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'приема'
        verbose_name_plural = 'Прием'
        db_table = 'Taking'

    def __str__(self):
        return f'{self.patient} - Таблетка: {self.pills} Время: {self.time}, Количество: {self.quantity_pills}'