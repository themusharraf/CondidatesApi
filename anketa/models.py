from django.db import models
from users.models import User


   # Nomzod modeli
class Condidate(models.Model): 

    # choice condidate address
    ADDRESS = (
    ('AND', "Andijon"),
    ('BUX', "Buxoro"),
    ('FAR', "Farg'ona"),
    ('NAM', "Namangan"),
    ('NAV', "Navoiy"),
    ('QASH', "Qashadaryo"),
    ('SAM', "Samarqand"),
    ('SIR', "Sirdaryo"),
    ('SRX', "Surxondaryo"),
    ('JIZ', "Jizzax"),
    ('TOSH', "Toshkent"),
    ('XOR', "Xorazim"),
    ('QSTN', "Qoraqalpog'iston"),
    ('ORES', "Boshqa Respublika"),   # ORES (Other Republic)
    )

    # choice condidate gender
    GENDER = (
    ("MAN", "Erkak"),
    ("WMAN", "Ayol")
    )

    condidate_user = models.OneToOneField(User, on_delete=models.CASCADE)       # nomzod foydalanuvchi
    condidate_name = models.CharField(max_length=25)        # nomzod ismi
    condidate_gender = models.CharField(max_length=5, choices=GENDER)       # nomzod jinsi
    condidate_height = models.FloatField()      # nomzod bo'yi
    condidate_age = models.IntegerField()       # nomzod yoshi
    condidate_weight = models.FloatField()      # nomzod vazni
    condidate_address = models.CharField(max_length=4, choices=ADDRESS)  # nomzod manzili
    condidate_married = models.CharField(max_length=25)     # nomzod turmush qurganmi?
    condidate_profession = models.CharField(max_length=25)      # nomzod kabi
    condidate_nation = models.CharField(max_length=25)      # nomzod millati
    condidate_health = models.CharField(max_length=50)      # nomzod sog'ligi
    condidate_prayed = models.CharField(max_length=50)      # nomzod ibodatlimi?
    condidate_desires = models.TextField()       # nomzod istaklari

    def __str__(self):
        return self.condidate_name


class SavedCondidate(models.Model):
    condidate = models.ForeignKey(Condidate, on_delete=models.CASCADE)
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.condidate)  # if not str() and "TypeError, __str__ returned non-string (type Condidate)"