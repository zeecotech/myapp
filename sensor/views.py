from django.conf import settings

from django.shortcuts import render

import json

import requests

from .models import sensorinputModel

from django.contrib import messages

from .forms import sensorinputForm

from twilio.rest import Client

def sensordisplay(request):
    return render(request, "index.html")

def stsensoralart(request):
    return render(request, "alart.html")

def stsensorinput(request):
    if request.method == "POST" and request.POST.get("stmeta") == "sensor_input":
        form = sensorinputForm(request.POST)
        if form.is_valid():
            form_instance = form.save(commit=False)
            form_instance.stmeta = request.POST.get("stmeta")
            form_instance.save()

            if request.POST.get("stinput") == '1':
                messages.success(request, "Fall detected, send rescue team ASAP!")
                

                account_sid = 'AC6d07168a52acba179613c8abdc7ffd17'
                auth_token = '5726eb72936b2fcd6866f576ab6a66b6'
                client = Client(account_sid, auth_token)

                message = client.messages.create(
                from_='+12295189033',
                body='Fall detected, send rescue team ASAP!',
                to='+2348167116612' 
                )

                return render(request, "alart.html")
            elif request.POST.get("stinput") == '0':
                messages.success(request, "No fall detected, sleeping position mode!")
                account_sid = 'AC6d07168a52acba179613c8abdc7ffd17'
                auth_token = '5726eb72936b2fcd6866f576ab6a66b6'
                client = Client(account_sid, auth_token)

                message = client.messages.create(
                from_='+12295189033',
                body='No fall detected, sleeping position mode!',
                to='+2348167116612'
                )
                return render(request, "alart.html")
            else:
                messages.success(request, "No fall detected, human is safe!")
                account_sid = 'AC6d07168a52acba179613c8abdc7ffd17'
                auth_token = '5726eb72936b2fcd6866f576ab6a66b6'
                client = Client(account_sid, auth_token)

                message = client.messages.create(
                from_='+12295189033',
                body='No fall detected, human is safe!',
                to='+2348167116612'
                )
                return render(request, "alart.html")
        else:
            messages.error(request, "Failed to insert sensor input!")
            return render(request, "index.html")
    else:
        messages.error(request, "Not getting any request at all!")
        return render(request, "index.html")
