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
from sklearn_pmml_model.tree import PMMLTreeClassifier

import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler, RobustScaler,LabelEncoder

class PredictIncome(APIView):

    serializer_class = PredictionSerializer
    label_encoder = None

    def post(self, request):

        encoder = LabelEncoder()
      
        encoder.classes_ = np.load('main/saved ml/classes.npy',allow_pickle=True) 

        data = request.data
        
        serializer = self.serializer_class(data = data)

        serializer.is_valid()
     
        v = []

        for k in serializer.data.keys():
            try:
                v.append(int(serializer.data.get(k)))
            except:
                v.append(str(serializer.data.get(k)))

       
        a_v = np.array(v)
                
        a_v = a_v.reshape(1,-1)

        X_encoder = pickle.load(open('main/saved ml/encoder copy.pkl' , 'rb'))

        model = PMMLTreeClassifier(pmml="main/saved ml/dtr copy.pmml")

        df = pd.DataFrame(a_v , columns = ['age',	
                'workclass',	
                'fnlwgt',	
                'education',	
                'education-num',	
                'marital-status',	
                'occupation',	
                'relationship',	
                'race',	
                'sex',	
                'capital-gain',	
                'capital-loss',	
                'hours-per-week',	
                'native-country',
                ])

        # df['age'] = pd.to_numeric(df['age'])
        # df['workclass'] = df['workclass'].astype('|S')
        # df['fnlwgt'] = pd.to_numeric(df['fnlwgt'])
        # df['education'] = df['workclass'].astype('|S')
        # df['education-num'] = pd.to_numeric(df['education-num'])
        # df['marital-status'] = df['marital-status'].astype('|S')
        # df['occupation'] = df['occupation'].astype('|S')
        # df['relationship'] = df['relationship'].astype('|S')
        # df['race'] = df['race'].astype('|S')
        # df['sex'] = df['sex'].astype('|S')
        # df['capital-gain'] = df['capital-gain'].astype('|S')

        for col in df.columns:
            try:
                df[col] = pd.to_numeric(df[col])
            except:
                
                df[col] = df[col].astype(str)
               
        

       

        for i in df.columns:
            
            if type(df[i][0]) == str:
                
                df[i] = X_encoder[i].transform(df[i])

        print(df)

        y_pred = model.predict(df)
        
        real_y = encoder.inverse_transform(y_pred)
        return Response({'prediction':real_y})



class GetTotalAnalysis():
    pass