from flask import Flask, request, jsonify
import sklearn
import sklearn.datasets 
import numpy as np
import sklearn.model_selection
import sklearn.tree
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn import tree

app = Flask(__name__)
iris = load_iris()

X = iris.data
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

model = tree.DecisionTreeClassifier()

model.fit(X_train, y_train)

@app.route('/', methods=['GET'])
def home():
     return {
        "message": "Hello world!" 
    }

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json['data']
    if len(data) != 4:
        return jsonify({'error': 'Not enough features!'})
    else:
        prediction = model.predict([data])
        return jsonify({'prediction': prediction.tolist()}) 
    
@app.route('/info', methods=['GET'])
def info():
    return {
        "1: model_type": model.__class__.__name__,
        "2: number_of_leaves": int(model.get_n_leaves()),
        "3: depth": model.get_depth(),
        
   }

@app.route('/health', methods=['GET'])
def health():
    return {
        "status": "ok"
   }
if __name__ == '__main__':  
    app.run(host='0.0.0.0', port=5000, debug=True)