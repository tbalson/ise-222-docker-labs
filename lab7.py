from sklearn.datasets import fetch_mldata
from sklearn.datasets import load_digits
import matplotlib
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression

#two ways to get data
#mnistdata = fetch_mldata('MNIST original', data_home='/E222/lab4')
mnistdata2 = load_digits()

#get data shape
print(mnistdata2.data.shape)#(1797, 64)

#plot one image out
plt.gray()
plt.matshow(mnistdata2.images[400])
plt.show()

#get input and output
X = mnistdata2.data
y = mnistdata2.target

#separate to train and test set
X_train, X_test, y_train, y_test = X[:1000],X[1000:],y[:1000],y[1000:]

#get shape
print(X_train.shape, X_test.shape)

#ground truth
y_train_0 = (y_train==0)

#train
log_clf = LogisticRegression()
log_clf.fit(X_train, y_train_0)

#print coefficient
print(log_clf.coef_)

#prediction on one figure
one_digit=X[0]
log_clf.predict([one_digit])
