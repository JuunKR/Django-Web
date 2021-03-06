from titanic.models.dataset import DataSet
from titanic.models.service import Service


class Test(object):

    dataset: object = DataSet()
    service: object = Service()

    def __init__(self, fname):
        self.entity = self.service.new_model(fname)

    def plot(self):
        this = self.entity
        print(f'Train 의 Type 은 {type(this)} 이다')
        print(f'column 의 Type 은 {this.columns} 이다.')
        print(f'column 의 상위 5개 데이터는 {this.head()} 이다.')
        print(f'column 의 하위 5개 데이터는 {this.tail()} 이다.')



