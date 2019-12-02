import pandas as pd

if __name__ == '__main__':
    data = pd.read_csv("iris.data", names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class'])
    iris = pd.DataFrame(data)
    # print(iris)
    # print()

    quantity = pd.DataFrame(iris.mean().round(3), columns=['mean'])
    quantity['standard_deviation'] = iris.std().round(3)
    quantity['median'] = iris.median()
    quantity['minimum'] = iris.min()
    quantity['maximum'] = iris.max()
    print(quantity)
    print()

    setosa = iris[iris['class'] == 'Iris-setosa']
    # print(setosa)
    # print()

    versicolor = iris[iris['class'] == 'Iris-versicolor']
    # print(versicolor)
    # print()

    virginica = iris[iris['class'] == 'Iris-virginica']
    # print(virginica)
    # print()

    quality = pd.DataFrame(setosa.count(), columns=['setosa'])
    quality['versicolor'] = versicolor.count()
    quality['virginica'] = virginica.count()
    quality = quality.drop(['sepal_length'])
    quality = quality.drop(['sepal_width'])
    quality = quality.drop(['petal_length'])
    quality = quality.drop(['petal_width'])
    quality.rename(index={'class': 'amount'}, inplace=True)

    tmp = pd.DataFrame(setosa.count()/iris.count(), columns=['setosa'])
    tmp['versicolor'] = versicolor.count()/iris.count()
    tmp['virginica'] = virginica.count()/iris.count()
    tmp = tmp.drop(['sepal_length'])
    tmp = tmp.drop(['sepal_width'])
    tmp = tmp.drop(['petal_length'])
    tmp = tmp.drop(['petal_width'])
    tmp.rename(index={'class': 'frequency'}, inplace=True)

    quality = quality.append(tmp)
    print(quality)
    print()
