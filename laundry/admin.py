from django.contrib import admin
from .models import Machine, Queue_Entry

admin.site.register(Machine)
admin.site.register(Queue_Entry)