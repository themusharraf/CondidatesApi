from django.db import models
from users.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ...


class Candidate(models.Model):
    class Type(models.TextChoices):
        TOSHKENT = 'toshkent', 'Toshkent'
        ANDIJON = 'andijon', 'Andijon'
        BUXORO = 'boxoro', 'Buxoro'
        FARGONA = 'fargona', 'Fargona'
        JIZZAH = 'jizzah', 'Jizzah'
        NAMANGAN = 'namangan', 'Namangan'
        NAVOIY = 'navoiy', 'Navoiy'
        QASHQADARYO = 'qashqadaryo', 'Qashqadaryo'
        SAMARQAND = 'samarqand', 'Samarqand'
        SIRDARYO = 'sirdaryo', 'Sirdaryo'
        SURXONDARYO = 'surxondaryo', 'Surxondaryo'
        XORAZM = 'xorazm', 'Xorazm'
        QORAQALPOGISTON = 'qoraqalpogiston', 'Qoraqalpogiston'
        BOSHQA_RESPUBLIKA = 'boshqa_respublika', 'Boshqa_respublika'

    class Gender(models.TextChoices):
        ERKAK = 'erkak', 'Erkak'
        AYOL = 'ayol', 'Ayol'

    author = models.OneToOneField(User, on_delete=models.CASCADE)  # nomzod foydalanuvchi
    status = models.BooleanField(default=False)
    gender = models.CharField(max_length=5, choices=Gender.choices)  # nomzod jinsi
    address = models.CharField(max_length=25, choices=Type.choices)  # nomzod manzili
    full_name = models.CharField(max_length=25)  # nomzod ismi
    height = models.FloatField()  # nomzod bo'yi
    age = models.PositiveIntegerField()  # nomzod yoshi
    weight = models.FloatField()  # nomzod vazni
    married = models.CharField(max_length=25)  # nomzod turmush qurganmi?
    profession = models.CharField(max_length=50)  # nomzod kasbi
    nation = models.CharField(max_length=25)  # nomzod millati
    health = models.CharField(max_length=50)  # nomzod sog'ligi
    prayed = models.CharField(max_length=50)  # nomzod ibodatlimi?
    desires = models.TextField()  # nomzod istaklari
    view_count = models.PositiveIntegerField(default=0)  # nomzod necha marta kurilgan


@receiver(post_save, sender=User)
def create_candidate(sender, instance, created, **kwargs):
    if created:
        Candidate.objects.create(user=instance)


@receiver(post_save, sender=Candidate)
def update_user_status(sender, instance, created, **kwargs):
    if created:
        instance.user.is_active = instance.status
        instance.user.save()
