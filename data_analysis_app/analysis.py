import pandas as pd

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

        if attr not in self.df.columns()[:-1] and self.df[attr][0] != str:
            raise ('please enter the dataset attrs and the attr values must be str, not int neither float!') 
               

        plt = self.df[attr].value_counts().plot(kind='bar')

        return plt