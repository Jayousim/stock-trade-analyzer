import pandas as pd
import numpy as np


class ExtractData:
    time_units = 'ns'

    @staticmethod
    def normalize_times(times):
        scaled = times - times[0]
        #scaled = scaled / scaled[-1]
        return scaled

    def __init__(self, data_path):
        self.df = pd.read_json(data_path, date_unit=ExtractData.time_units)
        self.x_coordinates = self.df.keys()

    def get_iterrows(self):
        return self.df.iterrows()

    def get_df(self):
        return self.df

    def get_rows(self):
        return self.df.to_numpy()

    def get_columns_names(self):
        return ExtractData.np.array(self.x_coordinates)

    def get_columns(self):
        return self.df.columns








