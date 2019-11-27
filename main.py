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

    quality = pd.DataFrame(setosa.count(), columns=['setosa_count'])
    quality['versicolor_count'] = versicolor.count()
    quality['virginica_count'] = virginica.count()
    print(quality)
    print()
