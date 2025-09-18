# KNN (K Nearest Neighbors) in Python - ML From Scratch 01 - Python Engineer

Column: https://www.python-engineer.com/courses/mlfromscratch/01_knn/
Processed: No
created on: September 7, 2023 5:57 PM

![01_knn.png](KNN%20(K%20Nearest%20Neighbors)%20in%20Python%20-%20ML%20From%20Scra%20444e6dc3657e4f9aa68bad408c0709b2/01_knn.png)

**Implement the K Nearest Neighbors (KNN) algorithm, using only built-in Python modules and numpy, and learn about the math behind this popular ML algorithm.**

[Machine Learning](https://www.python-engineer.com/tags/#machine-learning)   [numpy](https://www.python-engineer.com/tags/#numpy)

In this Machine Learning from Scratch Tutorial, we are going to implement the K Nearest Neighbors (KNN) algorithm, using only built-in Python modules and numpy. We will also learn about the concept and the math behind this popular ML algorithm.

All algorithms from this course can be found on [GitHub](https://github.com/patrickloeber/MLfromscratch) together with example tests.

## Implementation

```
import numpy as np
from collections import Counter

def euclidean_distance(x1, x2):
        return np.sqrt(np.sum((x1 - x2)**2))

class KNN:

    def __init__(self, k=3):
        self.k = k

    def fit(self, X, y):
        self.X_train = X
        self.y_train = y

    def predict(self, X):
        y_pred = [self._predict(x) for x in X]
        return np.array(y_pred)

    def _predict(self, x):
        # Compute distances between x and all examples in the training set
        distances = [euclidean_distance(x, x_train) for x_train in self.X_train]
        # Sort by distance and return indices of the first k neighbors
        k_idx = np.argsort(distances)[:self.k]
        # Extract the labels of the k nearest neighbor training samples
        k_neighbor_labels = [self.y_train[i] for i in k_idx]
        # return the most common class label
        most_common = Counter(k_neighbor_labels).most_common(1)
        return most_common[0][0]

```

FREE VS Code / PyCharm Extensions I Use

✅ Write cleaner code with Sourcery, instant refactoring suggestions: [Link*](https://sourcery.ai/?utm_source=youtube&utm_campaign=pythonengineer)

* These are affiliate link. By clicking on it you will not have any additional costs. Instead, you will support my project. Thank you! 🙏