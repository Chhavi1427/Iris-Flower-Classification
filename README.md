
# Iris Flower Classification 

[![Iris Flower Classification ](https://github.com/Chhavi1427/Iris-Flower-Classification/blob/master/main.png)](https://irisflowerclassification-z7j1.onrender.com)

This is a simple Flask web application for predicting the species of Iris flowers based on their sepal and petal measurements.

## Table of Contents
- [Prerequisites](#Prerequisites)
- [Usage](#usage)
- [Deployment-on-Render](#Deployment-on-Render)
- [Features](#features)
- [File-Structure](#File-Structure)
- [Dataset](#Dataset)
- [Model](#Model)
- [References](#References)
- [Contact-Information-and-Project-Details](#Contact-Information-and-Project-Details)

## Prerequisites


Before running this application, ensure you have the following dependencies installed:
- Python 3.x
- Flask
- pandas
- scikit-learn

You can install the required Python packages using pip:

```bash

## Running the Application

To run the Flask application, execute the following command in your terminal:

python deploy.py 

```

This command will start a local server, and you can access the application in your web browser at [http://localhost:5000](https://irisflowerclassification-z7j1.onrender.com).

## Usage

1. Open your web browser and go to https://irisflowerclassification-z7j1.onrender.com.
2. Enter the sepal and petal measurements in the provided input fields.
3. Click the "Predict" button.
4. The predicted species of the Iris flower will be displayed on the screen.

## Deployment-on-Render

This application can be deployed on Render. Ensure that you have the necessary configuration set up for deployment, including specifying the correct environment variables, dependencies, and deployment commands.

## File-Structure

- `app.py`: Flask application script containing route definitions and model prediction logic.
- `templates/`: Directory containing HTML templates for rendering web pages.
- `index.html`: HTML template for the home page.
- `result.html`: HTML template for displaying the prediction result.

## Dataset

The application uses the Iris dataset (`Iris.csv`) to train the model. This dataset contains 150 samples of iris flowers, with measurements for sepal length, sepal width, petal length, petal width, and the corresponding species.

## Model

The model used for prediction is a Decision Tree Classifier trained on the Iris dataset. It predicts the species of iris flowers based on their features.


## References

- [Flask Documentation](https://flask.palletsprojects.com/)
- [scikit-learn Documentation](https://scikit-learn.org/stable/)
- [Oasis Infobyte](https://www.oasisinfobyte.com/)


## Contact-Information-and-Project-Details

**Project Name:** Iris Flower Classification

**Author:** [Chhavi Modi ](https://github.com/Chhavi1427)

**Project Link:** https://github.com/Chhavi1427/Iris-Flower-Classification

**Email:** modichavi1427@gmail.com


