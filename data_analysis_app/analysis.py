import pandas as pd
import io, base64

class DataSetAnalysis:

    def __init__(self, path) -> None:
        self.df = pd.read_csv(path , sep=',' , names = ['age',
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
                'native-country','income'] )

    def bar_plot_by_attr(self, attr):

        if attr not in self.df.columns[:-1] and type(self.df[attr][0]) != str:
            raise ('please enter the dataset attrs and the attr values must be str, not int neither float!') 
               
        
        plt = self.df[attr].value_counts().plot(kind='bar')
        buffer = io.BytesIO()
        plt.figure.savefig(buffer, format='png')
        b64 = base64.b64encode(buffer.getvalue())
        
        return b64

    def get_all_attrs(self):
        cols = self.df.columns[:-1]
        return cols

    def get_col_values(self):

        values = []

        for col in self.df.columns[:-1]:

            if type(self.df[col][0]) == str:
                values.append({col :self.df[col].unique()})

        return values
    
