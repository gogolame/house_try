from django.shortcuts import render
from device.models import Devices

def dev_list(request):
    context = {
    'devices' : Devices.objects.all()


    }
    #devices = Devices.objects.order_by('room_type')
    return render(request, 'device/dev_list.html', context)