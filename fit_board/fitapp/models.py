from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.core.validators import RegexValidator


class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('client', 'Client'),
        ('trainer', 'Trainer'),
        ('admin', 'Admin'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    groups = models.ManyToManyField(
        Group,
        verbose_name='groups',
        blank=True,
        related_name='custom_users',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='user permissions',
        blank=True,
        related_name='custom_users',
    )

    class Meta:
        verbose_name_plural = "Тип пользователя"


class Gym_name(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Залы'


class Trainer(models.Model):
    GENDER_CHOICES = (
        ('мужской', 'Муж'),
        ('женский', 'Жен'),
    )
    PHONE_REGEX = r'^\+?1?\d{9,15}$'

    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    # photo = models.ImageField(upload_to='photos/')
    birth_date = models.DateField()
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES)
    gym = models.ForeignKey(Gym_name, on_delete=models.CASCADE)
    sport = models.CharField(max_length=100)
    phone_number = models.CharField(validators=[RegexValidator(regex=PHONE_REGEX)], max_length=15, unique=True)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name_plural = 'Тренера'


class Client(models.Model):
    PHONE_REGEX = r'^\+?1?\d{9,15}$'
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    client_name = models.CharField(max_length=100)
    phone_num = models.CharField(validators=[RegexValidator(regex=PHONE_REGEX)], max_length=15, unique=True)
    trainer_name = models.ForeignKey(Trainer, on_delete=models.CASCADE)

    def __str__(self):
        return self.client_name

    class Meta:
        verbose_name_plural = 'Клиенты'


class Schedule(models.Model):
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    gym = models.ForeignKey(Gym_name, on_delete=models.CASCADE)
    day = models.DateField(verbose_name='Дата тренировки')
    start_time = models.TimeField()
    finish_time = models.TimeField()

    def __str__(self):
        return f"Тренер {self.trainer.full_name} проводит занятия - {self.day} с {self.start_time} до {self.finish_time}, в зале {self.gym}"

    class Meta:
        verbose_name_plural = 'Расписания тренера'


class Booking(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.client} записан по следующим параметрам: {self.schedule}"

    class Meta:
        verbose_name_plural = 'Записи на тренировки'