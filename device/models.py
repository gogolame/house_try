from django.db import models
#from django.utils import timezone


class Devices(models.Model):
    # author = models.ForeignKey('auth.User')
    # title = models.CharField(max_length=200)
    # text = models.TextField()
    room_name = models.CharField(max_length=200)
    room_type = models.CharField(max_length=200)
    dev_name = models.CharField(max_length=200)
    dev_type = models.CharField(max_length=200)
    main_dev = models.CharField(max_length=200)
    param_1 = models.IntegerField()
    param_2 = models.IntegerField()
    ch_addr = models.IntegerField()

    # created_date = models.DateTimeField(
    #         default=timezone.now)
    # published_date = models.DateTimeField(
    #         blank=True, null=True)

    def publish(self):
       #self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.room_name

class Channel(models.Model):
    channel_type = models.CharField(max_length=200)
    channel_addr = models.IntegerField()

    def publish(self):
        self.save()

    def __str__(self):
        return self.channel_type
