from django.contrib import admin
from .models import Volunteer, City, Duty, Gender, Experience, Independence, Senior
# Register your models here.
class VolunteerAdmin(admin.ModelAdmin):
    list_display=["first_name", "last_name", "gender", "experience"]
class SeniorAdmin(admin.ModelAdmin):
    list_display=["first_name", "last_name", "gender", "independence"]
admin.site.register(Duty)
admin.site.register(City)
admin.site.register(Volunteer)
admin.site.register(Gender)
admin.site.register(Experience)
admin.site.register(Independence)
admin.site.register(Senior)