from django.shortcuts import render
from data_analysis_app.analysis import DataSetAnalysis
from rest_framework import generics
from django.http import HttpResponse
from rest_framework.response import Response
import base64
# Create your views here.

class DataSetBarPlotByPassingAttributeAPIView(generics.RetrieveAPIView):

    def get(self, request):
        attr = request.GET.get('attr')
        o = DataSetAnalysis('main/adult.data')
        return HttpResponse(base64.decodebytes(o.bar_plot_by_attr(attr)), content_type='image/png')


class GetAvailableValuesInColsAPIView(generics.RetrieveAPIView):

    def get(self, request):
        col = request.GET.get('col')
        o = DataSetAnalysis('main/adult.data')
      
        return Response({'attrs': o.get_col_values(col)})

       


class GetAllColsNameAPIView(generics.RetrieveAPIView):
    def get(self, request):
        
        o = DataSetAnalysis('main/adult.data')
        attrs = o.get_all_attrs()

        return Response({'attrs':attrs})

class PredictIncome():
    pass

class GetTotalAnalysis():
    pass