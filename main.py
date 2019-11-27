import pandas as pd

if __name__ == '__main__':
    data = pd.read_csv("iris.data", names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class'])
    iris = pd.DataFrame(data)
    #print(iris)
    print()

    results_quantitative = pd.DataFrame(iris.mean(), columns=['mean'])
    results_quantitative['standard_deviation'] = iris.std()
    results_quantitative['median'] = iris.median()
    results_quantitative['minimum'] = iris.min()
    results_quantitative['maximum'] = iris.max()
    print(results_quantitative)
    print()

    #print(data['class'].describe())
    results_qualitative = pd.DataFrame(iris.mode(), columns=['class'])
    results_qualitative['amount'] = iris['class'].count()
    print(results_qualitative)
    
    # print('Sepal length mean: ' + str(iris['sepal_length'].mean()))
    # print('Sepal width mean: ' + str(iris['sepal_width'].mean()))
    # print('Petal length mean: ' + str(iris['petal_length'].mean()))
    # print('Petal width mean: ' + str(iris['petal_width'].mean()))
    # print()
    #
    # print('Sepal length standard deviation: ' + str(iris['sepal_length'].std()))
    # print('Sepal width standard deviation: ' + str(iris['sepal_width'].std()))
    # print('Petal length standard deviation: ' + str(iris['petal_length'].std()))
    # print('Petal width standard deviation: ' + str(iris['petal_width'].std()))
    # print()
    #
    # print('Sepal length standard deviation: ' + str(iris['sepal_length'].std(ddof=0))) #odchylenie z populacji
    # print('Sepal width standard deviation: ' + str(iris['sepal_width'].std()))
    # print('Petal length standard deviation: ' + str(iris['petal_length'].std()))
    # print('Petal width standard deviation: ' + str(iris['petal_width'].std()))
    # print()
    #
    # print('Sepal length median: ' + str(iris['sepal_length'].median()))
    # print('Sepal width median: ' + str(iris['sepal_width'].median()))
    # print('Petal length median: ' + str(iris['petal_length'].median()))
    # print('Petal width median: ' + str(iris['petal_width'].median()))
    # print()
    #
    # print('Sepal length minimum: ' + str(iris['sepal_length'].min()))
    # print('Sepal width minimum: ' + str(iris['sepal_width'].min()))
    # print('Petal length minimum: ' + str(iris['petal_length'].min()))
    # print('Petal width minimum: ' + str(iris['petal_width'].min()))
    # print()
    #
    # print('Sepal length maximum: ' + str(iris['sepal_length'].max()))
    # print('Sepal width maximum: ' + str(iris['sepal_width'].max()))
    # print('Petal length maximum: ' + str(iris['petal_length'].max()))
    # print('Petal width maximum: ' + str(iris['petal_width'].max()))
    # print()
    #
    # print('Class dominant: ' + str(iris['class'].mode()))
    # print()
