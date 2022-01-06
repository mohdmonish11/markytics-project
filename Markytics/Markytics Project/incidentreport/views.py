from django.shortcuts import render, redirect
from incidentreport.models import *


def homepage(request):
    return render(request,'form.html')
def check_form_inputs(request):
    try:
        uLocation = request.POST["Location"]
        uIncident_description = request.POST["Incident_description"]
        uincident_date_time = request.POST["incident_date_time"]
        uincident_location = request.POST["incident_location"]
        uSeverity = request.POST["Severity"]
        uSuspected_cause = request.POST["Suspected_cause"]
        uAction_taken = request.POST["Action_taken"]
        uSub_incident = request.POST["Sub_incident"]
        if (uLocation=='') or (uIncident_description=='') or (uincident_date_time=='') or (uSeverity==''):
            return render(request,'completeField.html')
        else:
            obj = Form()
            obj.location = uLocation
            obj.incident_description = uIncident_description
            obj.incident_date_time = uincident_date_time
            obj.incident_location = uincident_location
            obj.severity = uSeverity
            obj.suspected_cause = uSuspected_cause
            obj.action_taken = uAction_taken
            obj.sub_incident = uSub_incident
            obj.save()
            return render(request, 'successfull_login.html')
    except Exception as e:
        return redirect('/completeField')
def successfull_login(request):
    return render (request,'successfull_login.html')
def completeField(request):
    return render(request,'completeField.html')
