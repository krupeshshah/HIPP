from logging import exception
from flask import Flask,render_template,request, url_for, redirect
import numpy as np
import joblib
from dashboard import dashboard

app = Flask(__name__)
app.config["BUNDLE_ERRORS"] = False
app.register_blueprint(dashboard,url_prefix="/Dashboard")

# def init():
#     # load the saved model.
#     global regressor
#     regressor = joblib.load("insurence.pkl")

@app.route('/')
def welcome():
    return render_template('dashboard.html')

@app.route('/submit',methods=['POST','GET'])
def submit():
    total_score=0
    try:
        if request.method == 'POST':
            age = int(request.form['age'])
            sex = request.form['sex']
            if sex == "female":
                sex = "1"
            elif sex == "male":
                sex = "0"
            else:
                return 'Input Error in Sex!' + sex
            bmi = float(request.form['bmi'])
            children = int(request.form['children'])
            smoker = request.form['smoker']
            if smoker == "no":
                smoker = "1"
            elif smoker == "yes":
                smoker = "0"
            else:
                return 'Input Error!'
            region = request.form['region']
            if region == "southeast":
                region = "0"
            elif region == "southwest":
                region = "1"
            elif region == "northeast":
                region = "2"
            elif region == "northwest":
                region = "3"
            else:
                return 'Input Error!'
            # Predict Apparent temperature
            # Same order as the x_train dataframe
            features = [np.array([age, sex,bmi,children,smoker,region])]
            print("1")
            print(features)
            insurence = joblib.load("./insurence.pkl")
            prediction = insurence.predict(features)
            finalprice = np.round(prediction, 2)
            print(finalprice)
            if finalprice < 0:
                print(finalprice)
                finalprice = finalprice * -1
            formatted_float = "${:,.2f}".format(finalprice[0])
            formdata = request.form
            print(formdata)
            return render_template('predictionresult.html', UserDetails = formdata, Price = formatted_float)
    except Exception as e:
        print(e)
        return 'Calculation Error'+str(e), 500
    
@app.route('/Dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/ageDistribution')
def ageDistribution():
    return render_template('ageDistribution.html')

@app.route('/bmiDistribution')
def bmidistribution():
    return render_template('bmiDistribution.html')

@app.route('/sexDistribution')
def sexDistribution():
    return render_template('sexDistribution.html') 

@app.route('/region')
def region():
    return render_template('regionDistribution.html')    
    
@app.route('/children')
def children():
    return render_template('children.html')    

@app.route('/Prediction')
def prediction():
    return render_template('prediction.html')

if __name__=='__main__':
    # init()
    app.run(debug=True)
