from logging import exception
from flask import Flask,render_template,request
import numpy as np
import joblib
app = Flask(__name__)
app.config["BUNDLE_ERRORS"] = False

def init():
    # load the saved model.
    global regressor
    regressor = joblib.load("insurence.pkl")

@app.route('/')
def welcome():
    return render_template('index.html')

# predict?age=31&sex=1&bmi=25.74&children=0&smoker=0&region=0
@app.route('/predict', methods=['GET'])
def predict():
    try:
        # Get parameters for temperature test
        age = float(request.args.get('age'))
        # Get parameters for humidity
        sex = float(request.args.get('sex'))
        # Get parameters for temperature
        bmi = float(request.args.get('bmi'))
        # Get parameters for humidity
        children = float(request.args.get('children'))
        # Get parameters for temperature
        smoker = float(request.args.get('smoker'))
        # Get parameters for humidity
        region = float(request.args.get('region'))

        # Predict Apparent temperature
        # Same order as the x_train dataframe
        features = [np.array([age, sex,bmi,children,smoker,region])]
        prediction = regressor.predict(features)

        return 'apparent_price' +str(prediction)
    except Exception as e:
        print(e)
        return 'Calculation Error'+str(e), 500

@app.route('/submit',methods=['POST','GET'])
def submit():
    total_score=0
    try:
        if request.method == 'POST':
            age = int(request.form['age'])
            sex = int(request.form['sex'])
            bmi = float(request.form['bmi'])
            children = int(request.form['children'])
            smoker = int(request.form['smoker'])
            region = int(request.form['region'])
            # Predict Apparent temperature
            # Same order as the x_train dataframe
            features = [np.array([age, sex,bmi,children,smoker,region])]
            prediction = regressor.predict(features)
            finalprice = np.round(prediction, 2)
            return render_template('index.html',price = finalprice)
    except Exception as e:
        print(e)
        return 'Calculation Error'+str(e), 500
        
if __name__=='__main__':
    init()
    app.run(debug=True)
