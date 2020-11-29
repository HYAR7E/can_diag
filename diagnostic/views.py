# Generic views
from rest_framework import generics
# Custom views
from rest_framework.views import APIView
from rest_framework.response import Response
# Import models and serializers
from .models import Sickness, Symphtom, Patient, DiagnosticXSymphtom, Diagnostic
from .serializers import SicknessSz, SymphtomSz, PatientSz, DiagnosticXSymphtomSz,\
	DiagnosticSz
from .utils import compute_diagnostic


class SicknessList(generics.ListCreateAPIView):
	serializer_class = SicknessSz
	queryset = Sickness.objects.all()

class SicknessDetail(generics.RetrieveUpdateDestroyAPIView):
	serializer_class = SicknessSz
	queryset = Sickness.objects.all()

class SymphtomList(generics.ListCreateAPIView):
	serializer_class = SymphtomSz
	queryset = Symphtom.objects.all()

class SymphtomDetail(generics.RetrieveUpdateDestroyAPIView):
	serializer_class = SymphtomSz
	queryset = Symphtom.objects.all()

class PatientList(generics.ListCreateAPIView):
	serializer_class = PatientSz
	queryset = Patient.objects.all()

class PatientDetail(generics.RetrieveUpdateDestroyAPIView):
	serializer_class = PatientSz
	queryset = Patient.objects.all()

class DiagnosticList(generics.ListCreateAPIView):
	serializer_class = DiagnosticSz
	queryset = Diagnostic.objects.all()

class DiagnosticDetail(generics.RetrieveUpdateDestroyAPIView):
	serializer_class = DiagnosticSz
	queryset = Diagnostic.objects.all()

class DiagnosticXSymphtomList(generics.ListAPIView):
	serializer_class = DiagnosticXSymphtomSz
	queryset = DiagnosticXSymphtom.objects.all()

	def list(self, request, pk):
		# Get queryset
		queryset = self.get_queryset().filter(diagnostic=pk)
		if len(queryset) > 0:
			# Update Diagnostic
			print("DiagnosticXSymphtomList get")
			compute_diagnostic(queryset[0].diagnostic)
		# Serialize queryset
		sz = self.get_serializer_class()
		serializer = sz(queryset, many=True)
		return Response(serializer.data)

class DiagnosticXSymphtomDetail(APIView):
	def post(self, req, *args, **kwargs):
		diagnostic_pk = kwargs.get('diagnostic_pk')
		symphtom_pk = kwargs.get('pk')

		# Get detail from request object (if exist in data)
		detail = None
		if req.data.get('detail'):
			detail = req.data.get('detail')
		# Create Consultation
		dxs_sz = DiagnosticXSymphtomSz(data={
			'diagnostic': diagnostic_pk,
			'symphtom': symphtom_pk,
			'detail': detail})
		if not dxs_sz.is_valid():
			print(dxs_sz.errors)
			return Response(status=500, data={"reason": ", ".join(dxs_sz.errors)})
		# Save consultation object
		dxs_sz.save()
		return Response(status=200, data=dxs_sz.data)

	def delete(self, req, *args, **kwargs):
		diagnostic_pk = kwargs.get('diagnostic_pk')
		symphtom_pk = kwargs.get('pk')
		# Get diagnosticxsymphtom object
		try:
			dxs = DiagnosticXSymphtom.objects.get(diagnostic=diagnostic_pk, symphtom=symphtom_pk)
		except DiagnosticXSymphtom.DoesNotExist:
			return Response(status=404, data={"error": "DiagnosticXSymphtom doesn't exists, please check the url values"})

		diagnostic = dxs.diagnostic
		dxs_pk = dxs.pk
		# Delete instance
		dxs.delete()
		# Update Diagnostic bc of deleted symphtom
		print("AddDiagnosticXSymphtom delete")
		compute_diagnostic(diagnostic)

		return Response(status=200, data={"deleted_instance": dxs_pk})
