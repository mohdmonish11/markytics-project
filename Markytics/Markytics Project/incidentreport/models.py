from django.db import models


class Form(models.Model):
    sno = models.AutoField(primary_key=True)
    location = models.CharField(max_length=200)
    incident_description = models.TextField(blank=True)
    incident_date_time = models.DateTimeField(auto_now_add=True)
    incident_location=models.CharField(max_length=350)
    severity = models.CharField(max_length=200)
    suspected_cause = models.TextField(blank=True)
    action_taken = models.TextField(blank=True)
    sub_incident = models.CharField(max_length=250)
    class Meta:
        db_table = "Form_Data"
