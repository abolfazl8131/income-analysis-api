from django.shortcuts import render
from data_analysis_app.analysis import DataSetAnalysis
from rest_framework import generics
from django.http import HttpResponse
from rest_framework.response import Response
import base64
import pickle
from pypmml import Model
import numpy as np
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

from rest_framework.views import APIView
from .serializers import PredictionSerializer
import os

class PredictIncome(APIView):

    serializer_class = PredictionSerializer
    label_encoder = None

    def post(self, request):

        
        if os.path.getsize('main/saved ml/Departure_encoder copy.pkl') > 0:
            with open('main/saved ml/Departure_encoder copy.pkl', 'rb') as f:
                
                self.label_encoder = pickle.load(f) 

        data = request.data

        serializer = self.serializer_class(data = data)
        serializer.is_valid()
       
        v = []

        
        for k in serializer.data.keys():
            try:
                v.append(int(serializer.data.get(k)))
            except:
                v.append(serializer.data.get(k))

        print(v[1:])
        
        a_v = np.array(v[1:])
        print(a_v)
        for i in range (1 , len(a_v)):
            if type(v[i]) == str:
                
                v[i] = self.label_encoder.transform(v[i])
                
            v[i] = self.label_encoder.transform(v[i])
               

        
        model = Model.fromFile('main/saved ml/dtr.pmml')

        y_pred = model.predict(v)

        y_pred = self.label_encoder.inverse_transform(y_pred)

        return Response({'prediction':y_pred})



class GetTotalAnalysis():
    pass