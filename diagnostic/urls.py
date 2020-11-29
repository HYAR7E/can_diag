from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from diagnostic import views

urlpatterns = [
    path('enfermedad/', views.SicknessList.as_view()),
    path('enfermedad/<int:pk>/', views.SicknessDetail.as_view()),
    path('sintoma/', views.SymphtomList.as_view()),
    path('sintoma/<int:pk>/', views.SymphtomDetail.as_view()),
    path('paciente/', views.PatientList.as_view()),
    path('paciente/<int:pk>/', views.PatientDetail.as_view()),
    path('diagnostico/', views.DiagnosticList.as_view()),
    path('diagnostico/<int:pk>/', views.DiagnosticDetail.as_view()),
    path('diagnostico/<int:pk>/sintoma/', views.DiagnosticXSymphtomList.as_view()),
    path('diagnostico/<int:diagnostic_pk>/sintoma/<int:pk>/', views.DiagnosticXSymphtomDetail.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)
