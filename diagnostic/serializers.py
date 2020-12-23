from rest_framework import serializers
from .models import Sickness, Symphtom, Patient, DiagnosticXSymphtom, Diagnostic
from .utils import compute_diagnostic

class SicknessSz(serializers.ModelSerializer):
	pk = serializers.ReadOnlyField()
	class Meta:
		model = Sickness
		fields = ['pk', 'name', 'key']

class SymphtomSz(serializers.ModelSerializer):
	pk = serializers.ReadOnlyField()
	class Meta:
		model = Symphtom
		fields = ['pk', 'name', 'key']

class PatientSz(serializers.ModelSerializer):
	pk = serializers.ReadOnlyField()
	class Meta:
		model = Patient
		fields = ['pk', 'name']

class DiagnosticSz(serializers.ModelSerializer):
	pk = serializers.ReadOnlyField()
	sickness_obj = SicknessSz(source="sickness", read_only=True)
	patient_obj = PatientSz(source="patient", read_only=True)
	created = serializers.DateTimeField(format='%d/%m/%Y', read_only=True)
	class Meta:
		model = Diagnostic
		fields = ['pk', 'patient', 'sickness', 'name', 'created', 'sickness_obj', 'patient_obj']

class DiagnosticXSymphtomSz(serializers.ModelSerializer):
	pk = serializers.ReadOnlyField()
	class Meta:
		model = DiagnosticXSymphtom
		fields = ['pk', 'diagnostic', 'symphtom', 'detail']

	def create(self, data):
		dxs = DiagnosticXSymphtom.objects.create(**data)
		# Update Diagnostic with new symphtom
		print("DiagnosticXSymphtom create")
		compute_diagnostic(dxs.diagnostic)
		return dxs
