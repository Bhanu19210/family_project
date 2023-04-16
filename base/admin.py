from django.contrib import admin

# Register your models here.
from .models import Author,Book,Genration_01,Genration_02,Genration_03,Genration_04



admin.site.register(Genration_01)
admin.site.register(Genration_02)
admin.site.register(Genration_03)
admin.site.register(Genration_04)
admin.site.register(Author)
admin.site.register(Book)





