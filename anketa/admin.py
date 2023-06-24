from django.contrib import admin

from .models import Condidate
from .models import SavedCondidate

admin.site.register(Condidate)
admin.site.register(SavedCondidate)
