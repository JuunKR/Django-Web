from titanic.models.dataset import DataSet
from titanic.models.service import Service


class Controller(object):

    dataset = DataSet()
    service = Service()

    def modeling(self, train, test) -> object:
        service = self.service

    def preprocessing(self, train) -> object:
        service = self.service
        this = self.dataset
        this.train = service.new_model(train)
        print(f'Train 의 Type 은 {type(this.train)} 이다.')
        print(f'column 의 Type 은 {this.train.columns} 이다.')
        print(f'column 의 상위 5개 데이터는 {this.train.head()} 이다.')
        print(f'column 의 하위 5개 데이터는 {this.train.tail()} 이다.')