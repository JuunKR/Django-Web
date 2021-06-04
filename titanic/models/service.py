from titanic.models.dataset import DataSet
import pandas as pd
import numpy as np
from sklearn.svm import SVC
from sklearn.model_selection import KFold
# K는 카운트를 의미함 n번 접었다라는 뜻 fold 접다
from sklearn.model_selection import cross_val_score


class Service(object):
    dataset = DataSet()

    def new_model(self, payload) -> object: # 리턴이 있으니까 object를 씀
        this = self.dataset
        this.context = './data/'
        this.fname = payload
        return pd.read_csv(this.context + this.fname)

    @staticmethod
    def create_train(this) -> object:
        return this.train.drop('Survived', axis=1)

    @staticmethod
    def create_label(this) -> object:
        return this.train['Survived']

    @staticmethod
    def drop_feature(this, *feature) -> object:
        for i in feature:
            this.train = this.train.drop([i], axis=1)
            this.test = this.test.drop([i], axis=1)
        return this

    @staticmethod
    def embarked_nominal(this) -> object:
        this.train = this.train.fillna({'Embarked': 'S'})
        this.test = this.test.fillna({'Embarked': 'S'})
        this.train['Embarked'] = this.train['Embarked'].map({'S': 1, 'C': 2, 'Q': 3})
        this.test['Embarked'] = this.test['Embarked'].map({'S': 1, 'C': 2, 'Q': 3})
        return this

    @staticmethod
    def fare_ordinal(this) -> object:
        # this.test['Fare'] = this.test['Fare'].fillna(1)
        # print(f'Test 의 null {this.test[this.test.isna().any(axis=1)]}')
        # this.train['FareBand'] = pd.qcut(this.train['Fare'], 4)
        # # qcut 으로 bins 값 설정 {this.train["FareBand.head(10)}
        # # bins = list(pd.qcut(this.train['Fare'],4, retbins=True))
        # # 은 list 구조로 첫번째 인덱스는 str타입의 문자이고 2번재 인덱스가 구간 값이다.
        # # 그래서 [1]을 주고 bins로 처리한다.
        #
        # bins = list(pd.qcut(this.train['Fare'], 4, retbins=True))[1]
        # this.train = this.train.drop(['FareBand'], axis = 1)
        # for these in this.train, this.test:
        #     these['FareBand'] = pd.cut(these['Fare'], bins=bins, labels=[1,2,3,4])
        #
        # return this

        this.test['Fare'] = this.test['Fare'].fillna(1)
        this.train['FareBand'] = pd.qcut(this.train['Fare'], 4)
        # print(f'qcut 으로 bins 값 설정 {this.train["FareBand"].head()}')
        bins = [-1, 8, 15, 31, np.inf]
        this.train = this.train.drop(['FareBand'], axis=1)
        for these in [this.train, this.test]:
            these['FareBand'] = pd.cut(these['Fare'], bins= bins, labels=[1,2,3,4])

        return this
        # this.train['FareBand'] = pd.qcut(this.train['Fare'],4, labels={1, 2, 3, 4})
        # this.test['FareBand'] = pd.qcut(this.train['Fare'],4, labels={1, 2, 3, 4})

    @staticmethod
    def title_norminal(this) -> object:
        combine = [this.train, this.test]
        for dataset in combine:
            dataset['Title'] = dataset.Name.str.extract('([A-Za-z]+)\.', expand=False) #컬럼 추가하는 방법 있으면 가져옴 없으면 만듦
        for dataset in combine:
            dataset['Title'] = dataset['Title'].replace(['Capt', 'Col', 'Don', 'Dr', 'Major', 'Rev', 'Jonkheer', 'Dona'], 'Rare')
            dataset['Title'] = dataset['Title'].replace(['Countess', 'Lady', 'Sir'], 'Royal')
            dataset['Title'] = dataset['Title'].replace('Mlle', 'Mr')
            dataset['Title'] = dataset['Title'].replace('Ms', 'Miss')
            dataset['Title'] = dataset['Title'].replace('Mme', 'Rare')
            title_mapping = {'Mr': 1, 'Miss': 2, 'Mrs': 3, 'Master': 4, 'Royal': 5, 'Rare': 6}
            # fillna(0) # 0은 호칭이 없는 극빈. 노예.
            dataset['Title'] = dataset['Title'].fillna(0)
            dataset['Title'] = dataset['Title'].map(title_mapping)
        return this

    @staticmethod
    def gender_norminal(this) -> object:  #Gender
        combine = [this.train, this.test]
        gender_mapping = {'male': 0, 'female': 1}
        for dataset in combine:
            dataset['Gender'] = dataset['Sex'].map(gender_mapping)
        return this

    @staticmethod
    def age_ordinal(this) -> object:
        train = this.train
        test = this.test
        combine = [train, test]
        bins = [-1, 0, 5, 12, 18, 24, 35, 60, np.inf]  # 미상
        labels = ['Unknown', 'Baby', 'Child', 'Teenager', 'Student', 'Young Adult', 'Adult', 'Senior']
        age_title_mapping = {'Unknown': 0, 'Baby': 1, 'Child': 2, 'Teenager': 3, 'Student': 4, 'Young Adult': 5,
                             'Adult': 6, 'Senior': 7}
        for dataset in combine:
            dataset['Age'] = dataset['Age'].fillna(-0.5)
            dataset['AgeGroup'] = pd.cut(dataset['Age'], bins=bins, labels=labels)
            dataset['AgeGroup'] = dataset['AgeGroup'].map(age_title_mapping)

        return this

    @staticmethod
    def create_k_fold() -> object:
        return KFold(n_splits=10, shuffle=True, random_state=0)

    @staticmethod
    def accuracy_by_svm(this):
        score = cross_val_score(SVC(),
                                this.train,
                                this.label,
                                cv=KFold(n_splits=10,
                                         shuffle=True,
                                         random_state=0,),
                                n_jobs=1,
                                scoring = 'accuracy')
        return round(np.mean(score) * 100, 2)