from django.contrib import admin
from .models import CONTACT, SKILL, EXPERIENCE, PROJECT, EDUCATION

# Register your models here.


admin.site.register(CONTACT)
admin.site.register(SKILL)
admin.site.register(EXPERIENCE)
admin.site.register(PROJECT)
admin.site.register(EDUCATION)