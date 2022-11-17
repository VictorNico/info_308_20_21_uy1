#import libraries
import pandas
#matplotlib inline
import matplotlib.pyplot as plt
import os

class data_analysis:
    def __init__(self,path="heart.txt"):
        self.path = path if os.path.exists(path) else None
    def get_path(self):
        return self.path
    def set_path(self,new_path):
        self.path = new_path if os.path.exists(path) else None
    def set_row_per_page(self,nb):
        pandas.options.display.max_rows = nb if str(nb).isdigit() else 10
    def load_dataset(self, sep="\t", header=0):
        self.ds = pandas.read_table(self.path,sep,header)
    def get_dimension(self):
        return 'Votre jeu de donnees comporte {} lignes ou individus et {} colonnes ou variables'.format(self.ds.shape()[0],self.ds.shape()[1])
    def get_first_n_people(self,n=5):
        return self.ds.head(n if str(n).isdigit() else 5)
    def get_variable(self):
        return self.ds.colunms
    def get_variable_type(self):
        return self.ds.dtypes
    def get_population_informations(self):
        return self.ds.info()
    def get_population_description_of_all(self):
        self.ds.describe(includes="all")
    def get_variables_population(self,variable):
        return self.ds[variable] if len([b for b in variable  if len([y for y in self.ds.columns if y == b]) != 0]) == len(variable) else self.ds[[p for p in variable if len([x for x in self.ds.columns if x == p]) != 0]]
    def get_variable_population_with_description(self,variable):
        return [self.ds[a].describe() for a in variable] if len([b for b in variable  if len([y for y in self.ds.columns if y == b]) != 0]) == len(variable) else [self.ds[d].describe() for d in [p for p in variable if len([x for x in self.ds.columns if x == p]) != 0]]
    def get_moyen_of_variable(self,variable):
        return self.ds[variable].means() if len([y for y in self.ds.columns if y == variable]) != 0 else 'Is not a variable'
    def get_count_of_variable(self,variable):
        return self.ds[variable].value_counts() if len([y for y in self.ds.columns if y == variable]) != 0 else 'Is not a variable'
    def get_filter_variable(self,variable, begin=0, end=None):
        return self.ds[variable][begin,end] if len([y for y in self.ds.columns if y == variable]) != 0 else 'Is not a variable'
    def get_sort_of_variable_population(self,variable):
        return self.ds[variable].sort_values() if len([y for y in self.ds.columns if y == variable]) != 0 else 'Is not a variable'
    def get_sort_of_variable_population_with_index(self,variable):
        return self.ds[variable].argsort() if len([y for y in self.ds.columns if y == variable]) != 0 else 'Is not a variable'
    def get_population_dataset_sort_by_variable(self,variable):
        return self.ds.sort_values(by=variable) if len([y for y in self.ds.columns if y == variable]) != 0 else 'Is not a variable'
    def get_population_dataset_sort_by_variable_for_n_people(self,variable,n=5):
        return self.ds.sort_values(by=variable).head(n) if (len([y for y in self.ds.columns if y == variable]) != 0 and str(n).isdigit())else 'Is not a variable'
    def draw(self):
        self.ds.hist(column='age')
    
