import pandas as pd
import numpy as np



class extractData:

    def __init__(self, data_path):
        self.df = pd.read_json(data_path)
        self.x_coordinates = np.array(self.df.columns)

    def normalize_x(x_coordinates):
        pass

    def get_rows(self):
        return self.df.to_numpy()





