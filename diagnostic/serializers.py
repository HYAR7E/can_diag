from rest_framework import serializers
from .models import Sickness, Symphtom, Patient, DiagnosticXSymphtom, Diagnostic
from .utils import compute_diagnostic

class SicknessSz(serializers.ModelSerializer):
	class Meta:
		model = Sickness
		fields = ['name', 'key']

class SymphtomSz(serializers.ModelSerializer):
	class Meta:
		model = Symphtom
		fields = ['name', 'key']

class PatientSz(serializers.ModelSerializer):
	class Meta:
		model = Patient
		fields = ['name']

class DiagnosticSz(serializers.ModelSerializer):
	sickness_obj = SicknessSz(source="sickness", read_only=True)
	patient_obj = PatientSz(source="patient", read_only=True)
	created = serializers.DateTimeField(format='%d/%m/%Y')
	class Meta:
		model = Diagnostic
		fields = ['patient', 'sickness', 'name', 'created', 'sickness_obj', 'patient_obj']

class DiagnosticXSymphtomSz(serializers.ModelSerializer):
	class Meta:
		model = DiagnosticXSymphtom
		fields = ['diagnostic', 'symphtom', 'detail']

	def create(self, data):
		dxs = DiagnosticXSymphtom.objects.create(**data)
		# Update Diagnostic with new symphtom
		print("DiagnosticXSymphtom create")
		compute_diagnostic(dxs.diagnostic)
		return dxs
