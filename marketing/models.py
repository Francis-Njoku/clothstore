import datetime
from django.db import models
from django.utils import timezone

# Create your models here.
class MarketingMessageQueryset(models.query.QuerySet):
    def active(self):
        return self.filter(active=True)

    def featured(self):
        current_time = timezone.now()  # change this
        time_threshold = current_time - timedelta(seconds=60)
        return self.filter(featured=False).filter(start_date__lt=timezone.now()).filter(end_date__gte=timezone.now())

class MarketingMessageManager(models.Manager):
    def get_queryset(self):
        return MarketingMessageQueryset(self.model, using=self._db)

    def all(self):
        return self.get_queryset().active()   

    def featured(self):
        return self.get_queryset().active().featured()

    def get_featured_item(self):
        try:
            return self.get_queryset().active().featured()[0]
        except:
            return None

class MarketingMessage(models.Model):
    message = models.CharField(max_length=120)
    active = models.BooleanField(default=False)
    featured = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    start_date = models.DateTimeField(auto_now_add=False, auto_now=False, null=True, blank=True)
    end_date = models.DateTimeField(auto_now_add=False, auto_now=False, null=True, blank=True)

    objects = MarketingMessageManager()
    #messages = MarketingMessageManager()
     
    def __str__(self):
        return str(self.message[:12])

    class Meta:
        ordering = ['-start_date', '-end_date']    