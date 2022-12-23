from django.shortcuts import render
from data_analysis_app.analysis import DataSetAnalysis
from rest_framework import generics
# Create your views here.

class DataSetBarPlotByPassingAttributeAPIView(generics.RetrieveAPIView):

    def get(self, request):
        attr = request.GET.get('attr')
        o = DataSetAnalysis('main/adult.data')
        return o.bar_plot_by_attr(attr)


class GetAvailableValuesInColsAPIView():
    pass

class GetAllColsNameAPIView():
    pass

class PredictIncome():
    pass

class GetTotolAnalysis():
    pass