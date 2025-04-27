from django.contrib import admin
from .models import Message, Thread

# Register your models here.
class MessageAdmin(admin.ModelAdmin):
    list_display = ('user', 'content', 'created')

class ThreadAdmin(admin.ModelAdmin):
    list_display = ('id',)

admin.site.register(Message, MessageAdmin)
admin.site.register(Thread)