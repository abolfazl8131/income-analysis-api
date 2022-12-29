
from django.urls import path
from .views import (DataSetBarPlotByPassingAttributeAPIView,
    GetAllColsNameAPIView,
    GetAvailableValuesInColsAPIView ,
    PredictIncome,
    GetDFCorr,
    GetQuartileDeviation,GetVariance,GetStandardDev,GetMean,GetMedian,GetMode)


urlpatterns = [
    path('bar-plot-by-pass-attributes/', DataSetBarPlotByPassingAttributeAPIView.as_view()),
    path('all-attrs/', GetAllColsNameAPIView.as_view()),
    path('col-values/',GetAvailableValuesInColsAPIView.as_view()),
    path('predict/' , PredictIncome.as_view()),
    path('corr/' , GetDFCorr.as_view()),
    path('quartile_dev/' , GetQuartileDeviation.as_view()),
    path('variance/', GetVariance.as_view()),
    path('standard_dev/',GetStandardDev.as_view()),
    path('mode/',GetMode.as_view()),
    path('median/',GetMedian.as_view()),
    path('mean/',GetMean.as_view()),
]