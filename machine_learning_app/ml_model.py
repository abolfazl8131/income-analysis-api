import pickle
import pandas as pd
import numpy as np
from sklearn_pmml_model.tree import PMMLTreeClassifier
from sklearn.preprocessing import MinMaxScaler, StandardScaler, RobustScaler,LabelEncoder

class TreeClassifier:

    model = PMMLTreeClassifier(pmml="machine_learning_app/saved ml/dtr.pmml")

    X_encoder = pickle.load(open('machine_learning_app/saved ml/encoder.pkl' , 'rb'))
   
    def preprocess(self , v):
        
        a_v = np.array(v)
                
        a_v = a_v.reshape(1,-1)

       
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


        for col in df.columns:
            try:
                df[col] = pd.to_numeric(df[col])
            except:
                
                df[col] = df[col].astype(str)
               
        


        for i in df.columns:
            
            if type(df[i][0]) == str:
              
                df[i] = self.X_encoder[i].transform(df[i])

        return df

        

    def predict(self,v):
        
        X = self.preprocess(v)

        y_pred = self.model.predict(X)
        
        real_y = y_pred

        return real_y

    