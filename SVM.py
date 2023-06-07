import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd
import sklearn

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, confusion_matrix
import joblib

datasets = pd.read_csv('0530/0530_output_6.csv') # '0530/0530_output_6.csv'
datasets.head()  # view dataset

X = datasets.drop(['Lie'], axis=1)

y = datasets['Lie']
# print(y)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=0)

cols = X_train.columns
# print(cols)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

X_train = pd.DataFrame(X_train, columns=[cols])
X_test = pd.DataFrame(X_test, columns=[cols])

X_train.describe()  # show X_train

svc = SVC(kernel='rbf', C=2000)
svc.fit(X_train, y_train)

y_check = svc.predict(X_train)
print(y_check)

print('Train accuracy score: {0:0.4f}'. format(
    accuracy_score(y_train, y_check)))

y_pred = svc.predict(X_test)
print(y_pred)

print('Valid accuracy score: {0:0.4f}'. format(accuracy_score(y_test, y_pred)))

# z = lambda x,y: (-svc.intercept_[0]-svc.coef_[0][0]*x -svc.coef_[0][1]*y) / svc.coef_[0][2]

# tmp = np.linspace(-5,5,30)
# x,y = np.meshgrid(tmp,tmp)

# fig = plt.figure()
# ax  = fig.add_subplot(111, projection='3d')
# # ax.plot3D(X_train[y_train==0,0], X_train[y_train==0,1], X_train[y_train==0,2],'ob')
# # ax.plot3D(X_train[y_train==1,0], X_train[y_train==1,1], X_train[y_train==1,2],'sr')
# ax.plot_surface(x, y, z(x,y))
# ax.view_init(30, 60)
# plt.show()

joblib.dump(svc, 'svc3.pkl')

# cm = confusion_matrix(y_test, y_pred)

# for checking
# clf1 = joblib.load('svc1.pkl')
# clf2 = joblib.load('svc2.pkl')
# clf3 = joblib.load('svc3.pkl')
# clf4 = joblib.load('svc4.pkl')

# y_default1 = clf1.predict(X)
# y_default2 = clf2.predict(X)
# y_default3 = clf3.predict(X)
# y_default4 = clf4.predict(X)
# print(y_default1)
# print(y_default2)
# print(y_default3)
# print(y_default4)

# print('Model accuracy score with default hyperparameters: {0:0.4f}'. format(accuracy_score(y, y_default1)))
# print('Model accuracy score with default hyperparameters: {0:0.4f}'. format(accuracy_score(y, y_default2)))
# print('Model accuracy score with default hyperparameters: {0:0.4f}'. format(accuracy_score(y, y_default3)))
# print('Model accuracy score with default hyperparameters: {0:0.4f}'. format(accuracy_score(y, y_default4)))
