from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(User)
admin.site.register(Event_Type)
admin.site.register(Event_Class)
admin.site.register(Event_Type_To_Class)
admin.site.register(Event_Class_To_Experience_Level)
admin.site.register(Workout_Event)
admin.site.register(Event_To_User)
