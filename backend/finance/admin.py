from django.contrib import admin
from .models import UserProfile, Transaction, Goal, SessionLog

admin.site.register(UserProfile)
admin.site.register(Transaction)
admin.site.register(Goal)
admin.site.register(SessionLog)
