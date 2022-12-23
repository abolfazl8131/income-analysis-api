
from django.urls import path
from .views import DataSetBarPlotByPassingAttributeAPIView, GetAllColsNameAPIView,GetAvailableValuesInColsAPIView
urlpatterns = [
    path('bar-plot-by-pass-attributes/', DataSetBarPlotByPassingAttributeAPIView.as_view()),
    path('all-attrs/', GetAllColsNameAPIView.as_view()),
    path('col-values/',GetAvailableValuesInColsAPIView.as_view())
]