from titanic.models.dataset import DataSet
import pandas as pd


class Service(object):

    dataset = DataSet()


        def new_model(self, payload):
        this = self.dataset
        this.context = './data/'
        this.fname = payload
        return pd.read_csv(this.context + this.fname)

