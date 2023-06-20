from django.db import models
from django.contrib.auth.models import AbstractUser

    # option for user gender
MAN, WOMAN = ('erkak', 'ayol')

    # options for user address
QORAQALPOGISTON, ANDIJON, BUXORO, FARGONA, JIZZAH, NAMANGAN, NAVOIY, QASHQADARYO = ("qoraqalpog'iston", "andijon", "buxoro", "farg'ona", "jizzah", "namangan", "navoiy", "qashqadaryo")
SAMARQAND, SIRDARYO, SURXONDARYO, TOSHKENT, XORAZM, BOSHQA_RESPUBLIKA = ("samarqand", "sirdaryo", "surxondaryo", "toshkent", "xorazm", "boshqa_respublika")



class User(AbstractUser):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=13)
    password = models.CharField(max_length=16)

    def __str__(self):
        return f"{self.name} {self.username}"
    

    # Nomzod modeli
class Condidate(models.Model):

    # choice condidate gender
    GENDER = (
        (MAN, MAN),
        (WOMAN, WOMAN)
    )
    # choice condidate address
    ADDRESS = (
        (QORAQALPOGISTON, QORAQALPOGISTON),
        (ANDIJON, ANDIJON),
        (BUXORO, BUXORO),
        (FARGONA, FARGONA),
        (JIZZAH, JIZZAH),
        (NAMANGAN, NAMANGAN),
        (NAVOIY, NAVOIY),
        (QASHQADARYO, QASHQADARYO),
        (SAMARQAND, SAMARQAND),
        (SIRDARYO, SIRDARYO),
        (SURXONDARYO, SURXONDARYO),
        (TOSHKENT, TOSHKENT),
        (XORAZM, XORAZM),
        (BOSHQA_RESPUBLIKA, BOSHQA_RESPUBLIKA)
    )
    
    condidate_user = models.OneToOneField(User, on_delete=models.CASCADE)       # nomzod foydalanuvchi
    condidate_name = models.CharField(max_length=25)        # nomzod ismi
    condidate_gender = models.CharField(max_length=5, choices=GENDER)       # nomzod jinsi
    condidate_height = models.FloatField()      # nomzod bo'yi
    condidate_age = models.IntegerField()       # nomzod yoshi
    condidate_weight = models.FloatField()      # nomzod vazni
    condidate_address = models.CharField(max_length=25, choices=ADDRESS, default=QORAQALPOGISTON)  # nomzod manzili
    condidate_married = models.CharField(max_length=25)     # nomzod turmush qurganmi?
    condidate_profession = models.CharField(max_length=25)      # nomzod kabi
    condidate_nation = models.CharField(max_length=25)      # nomzod millati
    condidate_health = models.CharField(max_length=50)      # nomzod sog'ligi
    condidate_prayed = models.CharField(max_length=50)      # nomzod ibodatlimi?
    condidate_desires = models.TextField()       # nomzod istaklari

    def __str__(self):
        return self.condidate_name
