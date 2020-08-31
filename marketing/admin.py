from django.contrib import admin

# Register your models here.
from .models import MarketingMessage

# TO customize the model directly here
class MarketingMessageAdmin(admin.ModelAdmin):
    class Meta:
        model = MarketingMessage

admin.site.register(MarketingMessage, MarketingMessageAdmin)