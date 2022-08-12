from .views import VitalsJSONView
from django.urls import path

urlpatterns = [
    path('', VitalsJSONView.as_view(), name='vitals'),
]
