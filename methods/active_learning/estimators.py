from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier


def choose_estimator(choice, n_neighbors):
    if choice == "GaussianNB":
        estimator = GaussianNB()
    elif choice == "kNearestNeighbours":
        estimator = KNeighborsClassifier(n_neighbors=n_neighbors)
    else:
        estimator = DecisionTreeClassifier()

    return estimator
