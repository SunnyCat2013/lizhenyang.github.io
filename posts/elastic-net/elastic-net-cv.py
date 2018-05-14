from sklearn.linear_model import ElasticNetCV
from sklearn.datasets import make_regression

X, y = make_regression(n_features=2, random_state=0)
regr = ElasticNetCV(cv=5, random_state=0)
regr.fit(X, y)




print(regr.alpha_) 

print(regr.intercept_) 

print(regr.predict([[0, 0]])) 
