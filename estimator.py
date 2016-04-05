__author__ = 'bgd'
import sklearn
import pickle
from sklearn import svm
from sklearn.externals import joblib

estimator = joblib.load('traineddata.pkl')

print("Prediction:",estimator.predict([[2,3,3,1,4,8,1,5,2,10]]))