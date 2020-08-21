from predict import routes
from flask import Flask
import pickle
import os


app = Flask(__name__)
model_uts = pickle.load(open('model_rfUTS.pkl', 'rb'))
model_ys = pickle.load(open('model_rfYS.pkl', 'rb'))
app.config['SECRET_KEY'] = 'c15483cb0c7aa3d48defca3ba2bd3c21'
