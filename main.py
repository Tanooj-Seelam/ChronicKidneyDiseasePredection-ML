import numpy as np
import pandas as pd
import numpy as np
import pandas as pd
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.datasets import make_regression
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression
from sklearn.feature_selection import RFE
from matplotlib import pyplot


def pre_process():
    dataset = pd.read_csv("chronic_kidney_disease.csv", header=0, na_values="?")
    dataset.replace("?", np.NaN)
    cleanup = {"Rbc": {"normal": 1, "abnormal": 0},
               "Pc": {"normal": 1, "abnormal": 0},
               "Pcc": {"present": 1, "notpresent": 0},
               "Ba": {"present": 1, "notpresent": 0},
               "Htn": {"yes": 1, "no": 0},
               "Dm": {"yes": 1, "no": 0},
               "Cad": {"yes": 1, "no": 0},
               "Appet": {"good": 1, "poor": 0},
               "pe": {"yes": 1, "no": 0},
               "Ane": {"yes": 1, "no": 0}}
    dataset.replace(cleanup, inplace=True)
    dataset.fillna(round(dataset.mean(), 2), inplace=True)
    dataset.to_csv("ip.csv", sep=',', index=False)


# Function importing Dataset
def importdata():
    balance_data = pd.read_csv('ip.csv', sep=',', header=0)

    # Printing the dataset shape
    print("Dataset Length: ", len(balance_data))
    print("Dataset Shape: ", balance_data.shape)

    # Printing the dataset observations
    return balance_data


# Function to split the dataset
def splitdataset(balance_data):
    # Separating the target variable
    X = balance_data.values[:, 0:24]
    Y = balance_data.values[:, -1]

    # print(X)
    # print(Y)

    # Spliting the dataset into train and test
    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.3, random_state=100)

    return X, Y, X_train, X_test, y_train, y_test


# Function to perform training with giniIndex.
def train_using_gini(X_train, X_test, y_train):
    # Creating the classifier object
    clf_gini = DecisionTreeClassifier(criterion="gini", random_state=100, max_depth=3, min_samples_leaf=5)

    # Performing training
    clf_gini.fit(X_train, y_train)
    return clf_gini


# Function to perform training with entropy.
def tarin_using_entropy(X_train, X_test, y_train):
    # Decision tree with entropy
    clf_entropy = DecisionTreeClassifier(criterion="entropy", random_state=100, max_depth=3, min_samples_leaf=5)

    # Performing training
    clf_entropy.fit(X_train, y_train)
    return clf_entropy


# Function to make predictions
def prediction(X_test, clf_object):
    # Prediction on test with giniIndex
    y_pred = clf_object.predict(X_test)
    return y_pred


# Function to calculate accuracy
def cal_accuracy(y_test, y_pred):
    print("Confusion Matrix: \n",
          confusion_matrix(y_test, y_pred))

    print("Accuracy : ",
          accuracy_score(y_test, y_pred) * 100)

    print("Report : \n",
          classification_report(y_test, y_pred))


# Main code
def main():
    pre_process()
    print('completed');
    # Building Phase
    data = importdata()
    X, Y, X_train, X_test, y_train, y_test = splitdataset(data)

    print(" ")
    #####################################
    from sklearn.feature_selection import SelectFromModel
    from sklearn.feature_selection import SelectKBest
    from sklearn.feature_selection import f_classif
    from numpy import set_printoptions
    X = data.iloc[:, :-1]
    y = data['Class']
    model = LogisticRegression()
    selector = SelectFromModel(estimator=LogisticRegression()).fit(X, y)
    print(selector.estimator_.coef_)
    print(selector.threshold_)
    print(selector.get_support())
    print(selector.transform(X))

    #######################################
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
    #######################
    clf_gini = train_using_gini(X_train, X_test, y_train)
    clf_entropy = tarin_using_entropy(X_train, X_test, y_train)
    print(" ")

    # Operational Phase
    print("#############Results Using Gini Index:##################")
    # Prediction using gini
    y_pred_gini = prediction(X_test, clf_gini)
    cal_accuracy(y_test, y_pred_gini)

    print("#################Results Using DT Entropy:################")
    # Prediction using entropy
    y_pred_entropy = prediction(X_test, clf_entropy)
    cal_accuracy(y_test, y_pred_entropy)

    #####################RFC############################

    print('#######################RFC###########################')
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.metrics import plot_confusion_matrix
    import matplotlib.pyplot as plt
    import seaborn as sns
    from sklearn.metrics import plot_confusion_matrix
    from sklearn.datasets import make_classification
    rmfr = RandomForestClassifier()

    rmfr.fit(X_train, y_train)
    predrmfr = rmfr.predict(X_test)
    print("Confusion Matrix for Random Forest Classifier:")
    cal_accuracy(y_test, predrmfr)
    plot_confusion_matrix(rmfr, X_test, y_test)
    plt.show()

    ##############################################

    print('#####################SVM######################')
    from sklearn.metrics import plot_confusion_matrix
    from sklearn.datasets import make_classification
    from sklearn.svm import SVC
    X, y = make_classification(random_state=0)
    clf = SVC(kernel='linear', C=1.0)
    clf.fit(X_train, y_train)
    SVC(random_state=0)
    plot_confusion_matrix(clf, X_test, y_test)
    plt.show()
    predsvc = clf.predict(X_test)
    print("Confusion Matrix for SVM Classifier:")
    cal_accuracy(y_test, predsvc)


# Calling main function
if __name__ == "__main__":
    main()
