import pandas as pd

if __name__ == '__main__':
    data = pd.read_csv("iris.data", names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class'])
    iris = pd.DataFrame(data)
    print(iris)
    print('Sepal length mean: ' + str(iris['sepal_length'].mean()))
