
from django.urls import path
from .views import DataSetBarPlotByPassingAttributeAPIView
urlpatterns = [
    path('bar-plot-by-pass-attributes/', DataSetBarPlotByPassingAttributeAPIView.as_view()),
]