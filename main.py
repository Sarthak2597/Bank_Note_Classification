import pickle
import pandas as pd
from flasgger import Swagger
from flask import Flask, request

app = Flask(__name__)
Swagger(app)

pickle_in = open("classifier.pkl", "rb")
classifier = pickle.load(pickle_in)


@app.route('/')
def welcome():
    return "Welcome All"


@app.route('/predict', methods=["Get"])
def predict_note_authentication():
    """Let's Authenticate the Banks Note
    This is using docstrings for specifications.
    ---
    parameters:
      - name: variance
        in: query
        type: number
        required: true
      - name: skewness
        in: query
        type: number
        required: true
      - name: curtosis
        in: query
        type: number
        required: true
      - name: entropy
        in: query
        type: number
        required: true
    responses:
        200:
            description: The output values

    """

    variance = request.args.get("variance")
    skewness = request.args.get("skewness")
    curtosis = request.args.get("curtosis")
    entropy = request.args.get("entropy")
    prediction = classifier.predict([[variance, skewness, curtosis, entropy]])
    return "The predicted value is" + str(prediction)


@app.route('/predict_file', methods=["POST"])
def predict_note_file():
    """Lets' Authenticate the Banks Note
    This is using docstrings for specifications.
    ---

    parameters:
        - name: file
          in: formData
          type: file
          required: true

    responses:
        200:
            description: The output values


    """
    df_test = pd.read_csv(request.files.get("file"))
    print(df_test.head())
    prediction = classifier.predict(df_test)
    return "The predicted values for the csv is" + str(list(prediction))


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)