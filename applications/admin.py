from django.contrib import admin
from .models import Candidate,Education,Experience,Skills

admin.site.register(Candidate)
admin.site.register(Education)
admin.site.register(Experience)
admin.site.register(Skills)
