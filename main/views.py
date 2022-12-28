from django.shortcuts import render
from data_analysis_app.analysis import DataSetAnalysis
from rest_framework import generics
from django.http import HttpResponse
from rest_framework.response import Response
import base64
import pickle
from pypmml import Model
import numpy as np
from rest_framework.views import APIView
from .serializers import PredictionSerializer

from machine_learning_app.ml_model import TreeClassifier
# Create your views here.

class DataSetBarPlotByPassingAttributeAPIView(generics.RetrieveAPIView):

    def get(self, request):
        attr = request.GET.get('attr')
        o = DataSetAnalysis('main/adult.data')
        return HttpResponse(base64.decodebytes(o.bar_plot_by_attr(attr)), content_type='image/png')


class GetAvailableValuesInColsAPIView(generics.RetrieveAPIView):

    
    def get(self, request):
       
        o = DataSetAnalysis('main/adult.data')
      
        return Response({'attrs':o.get_col_values()})

       


class GetAllColsNameAPIView(generics.RetrieveAPIView):
    def get(self, request):
        
        o = DataSetAnalysis('main/adult.data')
        attrs = o.get_all_attrs()

        return Response({'attrs':attrs})


class PredictIncome(APIView):

    serializer_class = PredictionSerializer

    label_encoder = None

    def post(self, request):

       
        data = request.data
        
        serializer = self.serializer_class(data = data)

        serializer.is_valid()
     
        v = []

        for k in serializer.data.keys():
            try:
                v.append(int(serializer.data.get(k)))
            except:
                v.append(serializer.data.get(k))
               
        prediction = TreeClassifier().predict(v)

        return Response({"prediction" : prediction})


class GetTotalAnalysis():
    pass