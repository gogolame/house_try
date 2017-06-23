from django.shortcuts import render
from device.models import Devices
from django.http import HttpResponseServerError


def dev_list(request):
    context = {'devices': Devices.objects.all()}
    if request.method == 'POST':
        form = request.POST
        print(form)
        if 'name' not in form or form['name'] == '':
            return HttpResponseServerError()
        c = Devices(
            room_name=form['name'],
            room_type=form['example'],
            dev_name=form['devname'],
            dev_type=form['devtype'],
            param_1=form['p1'],
            param_2=form['p2'],
            ch_addr=0xff,
            main_dev='220', )
        c.save()
    #devices = Devices.objects.order_by('room_type')
    return render(request, 'device/dev_main.html', context)


def hab_config(request):
    context = {'devices': Devices.objects.all()}
    #devices = Devices.objects.order_by('room_type')
    return render(request, 'device/dev_list.html', context)
