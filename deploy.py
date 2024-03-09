from flask import Flask, render_template, request
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    data = pd.read_csv('Iris.csv')

    X = data.drop('Species', axis=1)
    y = data['Species']

    le = LabelEncoder()
    y = le.fit_transform(y)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = DecisionTreeClassifier()
    model.fit(X_train, y_train)
    sepal_length = request.form['sepal_length']
    sepal_width = request.form['sepal_width']
    petal_length = request.form['petal_length']
    petal_width = request.form['petal_width']
    input_data = pd.DataFrame([[sepal_length, sepal_width, petal_length, petal_width]], columns=X.columns)
    prediction = model.predict(input_data)
    predicted_species = le.inverse_transform(prediction)

    return render_template('result.html', species=predicted_species[0])

if __name__ == '__main__':
    app.run(debug=True)
