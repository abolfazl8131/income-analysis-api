from django.shortcuts import render
from data_analysis_app.analysis import DataSetAnalysis
from rest_framework import generics
from django.http import HttpResponse
import base64
# Create your views here.

class DataSetBarPlotByPassingAttributeAPIView(generics.RetrieveAPIView):

    def get(self, request):
        attr = request.GET.get('attr')
        o = DataSetAnalysis('main/adult.data')
        return HttpResponse(base64.decodebytes(o.bar_plot_by_attr(attr)), content_type='image/png')


class GetAvailableValuesInColsAPIView():
    pass

class GetAllColsNameAPIView():
    pass

class PredictIncome():
    pass

class GetTotolAnalysis():
    pass