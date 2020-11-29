from django.db import models


class Sickness(models.Model):
	name = models.CharField(max_length=255)
	key = models.CharField(max_length=3, unique=True)

class Symphtom(models.Model):
	name = models.CharField(max_length=255)
	key = models.CharField(max_length=3, unique=True)

class Patient(models.Model):
	name = models.CharField(max_length=255)

class Diagnostic(models.Model):
	patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
	sickness = models.ForeignKey(Sickness, on_delete=models.CASCADE, null=True)
	name = models.CharField(max_length=255)
	created = models.DateTimeField(auto_now_add=True)

class DiagnosticXSymphtom(models.Model):
	diagnostic = models.ForeignKey(Diagnostic, on_delete=models.CASCADE)
	symphtom = models.ForeignKey(Symphtom, on_delete=models.CASCADE)
	detail = models.CharField(max_length=255, null=True)
